#!/usr/bin/env Rscript
# ============================================================
# 04_meta_analysis.R
# USG-PIVC Post-Insertion Outcomes Meta-Analysis
# ============================================================
# Title: Post-insertion outcomes of ultrasound-guided versus
#        landmark peripheral intravenous catheters
# Date: 2026-04-03
# ============================================================

suppressPackageStartupMessages({
  library(meta)
  library(metafor)
  library(readr)
  library(dplyr)
})

cat("=", rep("=", 59), "\n", sep = "")
cat("USG-PIVC Post-Insertion Outcomes Meta-Analysis\n")
cat("=", rep("=", 59), "\n\n", sep = "")

output_dir <- "output"
dir.create(output_dir, showWarnings = FALSE)

# ============================================================
# 1. LOAD DATA
# ============================================================
df <- read_csv("data/meta_input.csv", show_col_types = FALSE)
cat("Loaded", nrow(df), "studies\n\n")
df$catheter_confounded <- ifelse(is.na(df$catheter_confounded), FALSE,
                                 df$catheter_confounded %in% c(TRUE, "Yes", "yes", "TRUE"))
labels <- paste0(df$first_author, " (", df$year, ")")

# ============================================================
# HELPER: Wan et al. 2014 — Median/IQR → Mean/SD
# ============================================================
wan_mean <- function(median, q1, q3, n) (q1 + median + q3) / 3
wan_sd   <- function(median, q1, q3, n) (q3 - q1) / (2 * qnorm((0.75 * n - 0.125) / (n + 0.25)))

# Convert median/IQR to mean/SD for dwell time
for (i in 1:nrow(df)) {
  if (is.na(df$dwell_mean_usg[i]) && !is.na(df$dwell_median_usg[i])) {
    df$dwell_mean_usg[i] <- wan_mean(df$dwell_median_usg[i], df$dwell_q1_usg[i], df$dwell_q3_usg[i], df$n_usg[i])
    df$dwell_sd_usg[i]   <- wan_sd(df$dwell_median_usg[i], df$dwell_q1_usg[i], df$dwell_q3_usg[i], df$n_usg[i])
  }
  if (is.na(df$dwell_mean_lm[i]) && !is.na(df$dwell_median_lm[i])) {
    df$dwell_mean_lm[i] <- wan_mean(df$dwell_median_lm[i], df$dwell_q1_lm[i], df$dwell_q3_lm[i], df$n_lm[i])
    df$dwell_sd_lm[i]   <- wan_sd(df$dwell_median_lm[i], df$dwell_q1_lm[i], df$dwell_q3_lm[i], df$n_lm[i])
  }
}

# ============================================================
# 2. PRIMARY OUTCOME: Catheter Failure / Premature Removal
# ============================================================
cat("\n", rep("=", 60), "\n")
cat("PRIMARY: Catheter Failure (all-cause)\n")
cat(rep("=", 60), "\n")

# Studies with dichotomous failure data (excluding confounded)
fail_idx <- !is.na(df$failure_usg) & !is.na(df$failure_lm) & !df$catheter_confounded
cat("Studies with failure data (unconfounded):", sum(fail_idx), "\n")

if (sum(fail_idx) >= 2) {
  m_fail <- metabin(
    event.e = df$failure_usg[fail_idx],
    n.e     = df$n_usg[fail_idx],
    event.c = df$failure_lm[fail_idx],
    n.c     = df$n_lm[fail_idx],
    studlab = labels[fail_idx],
    sm = "RR",
    method = "MH",
    method.tau = "DL",
    random = TRUE, fixed = TRUE,
    prediction = TRUE,
    title = "Catheter Failure (all-cause)"
  )

  i2 <- round(m_fail$I2 * 100, 1)
  cat("\nI² =", i2, "%\n")
  if (i2 > 75) cat("SUBSTANTIAL HETEROGENEITY — narrative synthesis recommended\n")
  print(summary(m_fail))

  pdf(paste0(output_dir, "/forest_catheter_failure.pdf"), width = 12, height = 5)
  forest(m_fail,
         prediction = TRUE,
         print.tau2 = TRUE, print.I2 = TRUE,
         leftcols = c("studlab", "event.e", "n.e", "event.c", "n.c"),
         leftlabs = c("Study", "Events\n(USG)", "Total\n(USG)", "Events\n(LM)", "Total\n(LM)"),
         smlab = "Catheter Failure\nRisk Ratio",
         col.diamond = ifelse(i2 > 75, "red", "blue"))
  dev.off()
  cat("Forest plot saved: output/forest_catheter_failure.pdf\n")

  # Leave-one-out
  if (m_fail$k >= 3) {
    cat("\n--- Leave-One-Out Sensitivity ---\n")
    loo <- metainf(m_fail, pooled = "random")
    print(loo)
  }

  # Sensitivity: REML estimator + Hartung-Knapp-Sidik-Jonkman (HKSJ) CI adjustment
  cat("\n--- Sensitivity: REML + HKSJ adjustment ---\n")
  m_fail_reml <- metabin(
    event.e = df$failure_usg[fail_idx],
    n.e     = df$n_usg[fail_idx],
    event.c = df$failure_lm[fail_idx],
    n.c     = df$n_lm[fail_idx],
    studlab = labels[fail_idx],
    sm = "RR", method = "MH",
    method.tau = "REML",
    hakn = TRUE,        # Hartung-Knapp adjustment
    random = TRUE, fixed = FALSE,
    title = "Catheter Failure — REML+HKSJ sensitivity"
  )
  cat("REML+HKSJ: RR =", round(exp(m_fail_reml$TE.random), 3),
      "(95% CI", round(exp(m_fail_reml$lower.random), 3), "to",
      round(exp(m_fail_reml$upper.random), 3), "), p =",
      round(m_fail_reml$pval.random, 4), "\n")
} else {
  cat("Fewer than 2 studies — skipping pooled analysis.\n")
  m_fail <- NULL
}

# ============================================================
# 3. PRIMARY OUTCOME: Dwell Time
# ============================================================
cat("\n", rep("=", 60), "\n")
cat("PRIMARY: Dwell Time (hours)\n")
cat(rep("=", 60), "\n")

dwell_idx <- !is.na(df$dwell_mean_usg) & !is.na(df$dwell_mean_lm) & !df$catheter_confounded
cat("Studies with dwell time data (unconfounded):", sum(dwell_idx), "\n")

if (sum(dwell_idx) >= 2) {
  m_dwell <- metacont(
    n.e    = df$n_usg[dwell_idx],
    mean.e = df$dwell_mean_usg[dwell_idx],
    sd.e   = df$dwell_sd_usg[dwell_idx],
    n.c    = df$n_lm[dwell_idx],
    mean.c = df$dwell_mean_lm[dwell_idx],
    sd.c   = df$dwell_sd_lm[dwell_idx],
    studlab = labels[dwell_idx],
    sm = "MD",
    method.tau = "DL",
    random = TRUE, fixed = TRUE,
    prediction = TRUE,
    title = "Catheter Dwell Time (hours)"
  )

  i2 <- round(m_dwell$I2 * 100, 1)
  cat("\nI² =", i2, "%\n")
  if (i2 > 75) cat("SUBSTANTIAL HETEROGENEITY — pooled estimate suppressed per pre-specified I²>75% rule\n")
  print(summary(m_dwell))

  # H1 fix (2026-04-28, post Codex audit): when I²>75%, suppress pooled diamond
  # to enforce the methods-stated rule. Keep individual study estimates visible.
  pdf(paste0(output_dir, "/forest_dwell_time.pdf"), width = 12, height = 5)
  forest(m_dwell,
         prediction = (i2 <= 75),
         random = (i2 <= 75), fixed = FALSE,
         print.tau2 = TRUE, print.I2 = TRUE,
         smlab = ifelse(i2 > 75,
                        "Dwell Time\nMean Difference (hours) — NOT POOLED (I²>75%)",
                        "Dwell Time\nMean Difference (hours)"),
         col.diamond = "blue")
  dev.off()
  cat("Forest plot saved: output/forest_dwell_time.pdf\n")
} else {
  cat("Fewer than 2 studies — skipping pooled analysis.\n")
  m_dwell <- NULL
}

# ============================================================
# 4. SECONDARY: Infiltration
# ============================================================
cat("\n", rep("=", 60), "\n")
cat("SECONDARY: Infiltration\n")
cat(rep("=", 60), "\n")

infil_idx <- !is.na(df$infiltration_usg) & !is.na(df$infiltration_lm) & !df$catheter_confounded
cat("Studies with infiltration data:", sum(infil_idx), "\n")

if (sum(infil_idx) >= 2) {
  m_infil <- metabin(
    event.e = df$infiltration_usg[infil_idx],
    n.e     = df$n_usg[infil_idx],
    event.c = df$infiltration_lm[infil_idx],
    n.c     = df$n_lm[infil_idx],
    studlab = labels[infil_idx],
    sm = "RR", method = "MH", method.tau = "DL",
    random = TRUE, fixed = TRUE, prediction = TRUE,
    title = "Infiltration"
  )
  print(summary(m_infil))

  pdf(paste0(output_dir, "/forest_infiltration.pdf"), width = 12, height = 5)
  forest(m_infil, prediction = TRUE, print.I2 = TRUE,
         smlab = "Infiltration\nRisk Ratio")
  dev.off()
  cat("Forest plot saved: output/forest_infiltration.pdf\n")
} else {
  cat("Fewer than 2 studies — skipping.\n")
  m_infil <- NULL
}

# ============================================================
# 5. SECONDARY: Extravasation (contrast)
# ============================================================
cat("\n", rep("=", 60), "\n")
cat("SECONDARY: Extravasation\n")
cat(rep("=", 60), "\n")

extrav_idx <- !is.na(df$extravasation_usg) & !is.na(df$extravasation_lm)
cat("Studies with extravasation data:", sum(extrav_idx), "\n")

if (sum(extrav_idx) >= 2) {
  m_extrav <- metabin(
    event.e = df$extravasation_usg[extrav_idx],
    n.e     = df$n_extravasation_usg[extrav_idx],
    event.c = df$extravasation_lm[extrav_idx],
    n.c     = df$n_extravasation_lm[extrav_idx],
    studlab = labels[extrav_idx],
    sm = "RR", method = "MH", method.tau = "DL",
    random = TRUE, fixed = TRUE,
    title = "Extravasation"
  )
  i2_extrav <- round(m_extrav$I2 * 100, 1)
  cat("\nExtravasation I² =", i2_extrav, "%\n")
  if (i2_extrav > 75) cat("SUBSTANTIAL HETEROGENEITY — pooled estimate suppressed per pre-specified I²>75% rule\n")
  print(summary(m_extrav))

  # H1 fix: same suppression rule as dwell time
  pdf(paste0(output_dir, "/forest_extravasation.pdf"), width = 12, height = 5)
  forest(m_extrav,
         random = (i2_extrav <= 75), fixed = FALSE,
         print.I2 = TRUE,
         smlab = ifelse(i2_extrav > 75,
                        "Extravasation\nRisk Ratio — NOT POOLED (I²>75%)",
                        "Extravasation\nRisk Ratio"))
  dev.off()
  cat("Forest plot saved: output/forest_extravasation.pdf\n")
} else {
  cat("Fewer than 2 studies — narrative synthesis only.\n")
  m_extrav <- NULL
}

# ============================================================
# 6. SENSITIVITY ANALYSIS: Including confounded studies
# ============================================================
cat("\n", rep("=", 60), "\n")
cat("SENSITIVITY: Effect of including catheter-confounded studies\n")
cat(rep("=", 60), "\n")

# Dwell time with ALL studies (including Dachepally, Paladini)
dwell_all_idx <- !is.na(df$dwell_mean_usg) & !is.na(df$dwell_mean_lm)
if (sum(dwell_all_idx) > sum(dwell_idx)) {
  cat("\nDwell time with confounded studies included:\n")
  m_dwell_all <- metacont(
    n.e    = df$n_usg[dwell_all_idx],
    mean.e = df$dwell_mean_usg[dwell_all_idx],
    sd.e   = df$dwell_sd_usg[dwell_all_idx],
    n.c    = df$n_lm[dwell_all_idx],
    mean.c = df$dwell_mean_lm[dwell_all_idx],
    sd.c   = df$dwell_sd_lm[dwell_all_idx],
    studlab = labels[dwell_all_idx],
    sm = "MD", method.tau = "DL",
    random = TRUE, fixed = TRUE
  )
  print(summary(m_dwell_all))
}

# ============================================================
# 7. SENSITIVITY: RCTs only
# ============================================================
cat("\n", rep("=", 60), "\n")
cat("SENSITIVITY: RCTs Only — Catheter Failure\n")
cat(rep("=", 60), "\n")

rct_fail_idx <- fail_idx & df$design == "RCT"
if (sum(rct_fail_idx) >= 2) {
  m_rct <- metabin(
    event.e = df$failure_usg[rct_fail_idx],
    n.e     = df$n_usg[rct_fail_idx],
    event.c = df$failure_lm[rct_fail_idx],
    n.c     = df$n_lm[rct_fail_idx],
    studlab = labels[rct_fail_idx],
    sm = "RR", method = "MH", method.tau = "DL",
    random = TRUE, fixed = TRUE
  )
  cat("RCTs only (k =", m_rct$k, "):\n")
  print(summary(m_rct))
} else {
  cat("Fewer than 2 RCTs with failure data — skipping.\n")
}

# ============================================================
# 7b. SENSITIVITY: Cohort-only & Design Subgroup (Codex audit B2 fix, 2026-04-28)
# ============================================================
cat("\n", rep("=", 60), "\n")
cat("SENSITIVITY: Cohort-only / Design Subgroup — Catheter Failure\n")
cat(rep("=", 60), "\n")

cohort_fail_idx <- fail_idx & df$design == "Cohort"
if (sum(cohort_fail_idx) >= 2) {
  m_cohort <- metabin(
    event.e = df$failure_usg[cohort_fail_idx],
    n.e     = df$n_usg[cohort_fail_idx],
    event.c = df$failure_lm[cohort_fail_idx],
    n.c     = df$n_lm[cohort_fail_idx],
    studlab = labels[cohort_fail_idx],
    sm = "RR", method = "MH", method.tau = "DL",
    random = TRUE, fixed = TRUE
  )
  cat("Cohorts only (k =", m_cohort$k, "):\n")
  print(summary(m_cohort))
} else {
  cat("Fewer than 2 cohorts with failure data — skipping.\n")
}

# Design subgroup interaction (test for design effect)
if (!is.null(m_fail) && m_fail$k >= 3) {
  design_sub <- df$design[fail_idx]
  if (length(unique(design_sub)) > 1) {
    cat("\nDesign subgroup interaction (RCT vs Cohort):\n")
    m_design <- update(m_fail, subgroup = design_sub)
    print(summary(m_design))
  } else {
    cat("Only one design type — design subgroup not testable.\n")
  }
}

# ============================================================
# 7c. SENSITIVITY: Leave-one-out + largest-study influence (Codex audit H5, 2026-04-28)
# ============================================================
cat("\n", rep("=", 60), "\n")
cat("SENSITIVITY: Leave-one-out — Catheter Failure\n")
cat(rep("=", 60), "\n")

if (!is.null(m_fail) && m_fail$k >= 3) {
  m_loo <- metainf(m_fail, pooled = "random")
  cat("Leave-one-out (random-effects) for catheter failure:\n")
  print(m_loo)

  # Identify the largest-weight study (Saltarelli per audit; verify dynamically)
  weights_random <- m_fail$w.random / sum(m_fail$w.random) * 100
  largest_idx <- which.max(weights_random)
  cat(sprintf("\nLargest-weight study: %s (%.1f%% weight)\n",
              m_fail$studlab[largest_idx], weights_random[largest_idx]))
  cat(sprintf("After excluding %s: pooled RR = %s\n",
              m_fail$studlab[largest_idx],
              gsub(" ", "", m_loo$studlab[largest_idx])))

  # Save LOO results to CSV by reconstructing manually (metainf accessors vary by version)
  loo_df <- data.frame(
    study_excluded = m_fail$studlab,
    weight_in_full_model = sprintf("%.1f%%", weights_random),
    pooled_RR_95CI = NA_character_,
    p_value = NA_character_,
    I2 = NA_character_,
    stringsAsFactors = FALSE
  )
  for (k in seq_along(m_fail$studlab)) {
    keep <- seq_along(m_fail$studlab) != k
    m_k <- metabin(
      event.e = m_fail$event.e[keep], n.e = m_fail$n.e[keep],
      event.c = m_fail$event.c[keep], n.c = m_fail$n.c[keep],
      studlab = m_fail$studlab[keep],
      sm = "RR", method = "MH", method.tau = "DL",
      random = TRUE, fixed = TRUE
    )
    loo_df$pooled_RR_95CI[k] <- sprintf("%.2f [%.2f, %.2f]",
                                        exp(m_k$TE.random),
                                        exp(m_k$lower.random),
                                        exp(m_k$upper.random))
    loo_df$p_value[k] <- format.pval(m_k$pval.random, digits = 3)
    loo_df$I2[k] <- sprintf("%.1f%%", m_k$I2 * 100)
  }
  write_csv(loo_df, paste0(output_dir, "/SupTable_LOO_catheter_failure.csv"))
  cat("\nLOO table saved: output/SupTable_LOO_catheter_failure.csv\n")
} else {
  cat("Fewer than 3 studies — LOO not informative.\n")
}

# ============================================================
# 8. SUBGROUP: Adult vs Paediatric
# ============================================================
cat("\n", rep("=", 60), "\n")
cat("SUBGROUP: Adult vs Paediatric — Catheter Failure\n")
cat(rep("=", 60), "\n")

if (!is.null(m_fail) && m_fail$k >= 3) {
  age_sub <- df$age_group[fail_idx]
  if (length(unique(age_sub)) > 1) {
    m_sub <- update(m_fail, subgroup = age_sub)
    print(summary(m_sub))

    pdf(paste0(output_dir, "/forest_failure_by_age.pdf"), width = 13, height = 7)
    forest(m_sub, print.I2.ci = TRUE, smlab = "Catheter Failure\nRisk Ratio")
    dev.off()
    cat("Subgroup forest plot saved.\n")
  } else {
    cat("Only one age group — skipping.\n")
  }
}

# ============================================================
# 9. GENERIC HR FOREST PLOT (for studies reporting HRs)
# ============================================================
cat("\n", rep("=", 60), "\n")
cat("HR-BASED ANALYSIS: Studies reporting Hazard Ratios\n")
cat(rep("=", 60), "\n")

# Studies with HR data (log-transform for meta-analysis)
# Feinsmith: HR 0.91 (0.87-0.95) — USG vs PIV (USG protective)
# Dachepally: HR 0.50 (0.30-0.69) — inverted from traditional vs USG HR 2.20 (confounded)
# Shokoohi: RR 1.26 (0.88-1.80) — USG vs LM for premature removal

hr_studies <- c("Feinsmith (2021)", "Shokoohi (2019)")
hr_loghr   <- c(log(0.91), log(1.26))
hr_logse   <- c((log(0.95) - log(0.87)) / (2 * 1.96),
                (log(1.80) - log(0.88)) / (2 * 1.96))

if (length(hr_studies) >= 2) {
  m_hr <- metagen(
    TE    = hr_loghr,
    seTE  = hr_logse,
    studlab = hr_studies,
    sm    = "HR",
    method.tau = "DL",
    random = TRUE, fixed = TRUE,
    title = "Catheter Failure/Premature Removal (HR)"
  )
  print(summary(m_hr))

  pdf(paste0(output_dir, "/forest_HR_failure.pdf"), width = 12, height = 4)
  forest(m_hr, print.I2 = TRUE,
         smlab = "Catheter Failure\nHazard Ratio (USG vs LM)",
         xlim = c(0.5, 2.0))
  dev.off()
  cat("HR forest plot saved: output/forest_HR_failure.pdf\n")
}

# ============================================================
# 10. SUMMARY TABLE
# ============================================================
cat("\n", rep("=", 60), "\n")
cat("SUMMARY OF ALL POOLED OUTCOMES\n")
cat(rep("=", 60), "\n\n")

results_list <- list(
  "Catheter Failure (RR)" = m_fail,
  "Dwell Time (MD)" = m_dwell,
  "Infiltration (RR)" = m_infil,
  "Extravasation (RR)" = m_extrav
)

summary_rows <- list()
for (name in names(results_list)) {
  m <- results_list[[name]]
  if (is.null(m)) next

  i2_pct <- round(m$I2 * 100, 1)
  poolable <- ifelse(i2_pct > 75, "No", "Yes")

  # H1 fix (2026-04-28, post Codex audit): for non-poolable outcomes, do not
  # report a pooled estimate or p-value to avoid contradicting the methods-stated
  # I²>75% no-pooling rule. The exploratory random-effects values are still
  # visible in the R console output but are deliberately omitted from the
  # submission summary CSV.
  if (poolable == "No") {
    est <- "Not pooled (exploratory only)"
    pval_disp <- "—"
  } else if (inherits(m, "metabin")) {
    est <- sprintf("%.2f [%.2f, %.2f]",
                   exp(m$TE.random), exp(m$lower.random), exp(m$upper.random))
    pval_disp <- format.pval(m$pval.random, digits = 3)
  } else {
    est <- sprintf("%.1f [%.1f, %.1f]",
                   m$TE.random, m$lower.random, m$upper.random)
    pval_disp <- format.pval(m$pval.random, digits = 3)
  }

  summary_rows[[length(summary_rows) + 1]] <- data.frame(
    Outcome = name, k = m$k,
    Estimate_95CI = est,
    I2 = paste0(i2_pct, "%"),
    p_value = pval_disp,
    Poolable = poolable,
    stringsAsFactors = FALSE
  )
}

if (length(summary_rows) > 0) {
  summary_df <- do.call(rbind, summary_rows)
  print(summary_df, row.names = FALSE)
  write_csv(summary_df, paste0(output_dir, "/meta_analysis_summary.csv"))
  cat("\nSummary saved:", paste0(output_dir, "/meta_analysis_summary.csv"), "\n")
}

cat("\nMeta-analysis complete.\n")
cat("Check output/ folder for forest plots and summary tables.\n")
