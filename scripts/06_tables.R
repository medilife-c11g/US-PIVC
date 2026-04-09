#!/usr/bin/env Rscript
# Generate Table 1 and Table 2 as PDF and CSV

library(readr)

# ============================================================
# TABLE 1: Characteristics of Included Studies
# ============================================================

t1 <- data.frame(
  Study = c("Kleidon TM", "Bridey C", "Feinsmith SE", "Dachepally R",
            "Shokoohi H", "Favot M", "Varghese S", "Leroux S",
            "Paladini A", "Saltarelli NA", "Cottrell JT", "Refosco M",
            "Nishizawa T", "Desai K"),
  Year = c(2025, 2018, 2021, 2023, 2019, 2019, 2025, 2023, 2018, 2015,
           2021, 2024, 2020, 2018),
  Country = c("Australia", "France", "USA", "USA", "USA", "USA", "India", "USA", "Italy", "USA",
              "USA", "Brazil", "Japan", "USA"),
  Design = c("RCT", "RCT", "Retro cohort", "Retro cohort", "Prosp cohort",
             "Retro cohort", "RCT", "RCT", "Prosp cohort", "Retro cohort",
             "Retro cohort", "Prosp cohort", "RCT", "Retro cohort"),
  Setting = c("Children's hospital", "Tertiary ICU", "Academic centre",
              "Paediatric ICU", "Tertiary ED", "Tertiary ED",
              "Paediatric ED", "Tertiary ED", "Paediatric ED", "Tertiary ED",
              "Children's hospital", "Paediatric ED", "Mixed ICU", "Paediatric ED"),
  Population = c("Paediatric 0-18y", "Adult ICU (DIVA)", "Adult (DIVA)",
                 "Paediatric ICU (DIVA)", "Adult ED (all)", "Adult ED (CT contrast)",
                 "Paediatric 1mo-17y", "Adult ED", "Paediatric ED (DIVA) >10y",
                 "Adult ED (DIVA)", "Paediatric (mixed)", "Paediatric ED (mixed)",
                 "Adult ICU (DIVA)", "Paediatric ED (mixed)"),
  N_USG = c(84, 57, 7972, 99, 182, 291, 45, 106, 20, 885,
            256, 135, 30, 160),
  N_LM = c(80, 57, 35498, 88, 148, 29217, 45, 116, 20, 1803,
           287, 135, 30, 363),
  DIVA = c("No", "Yes", "Yes", "Yes", "No", "No", "Mixed", "No", "Yes", "Yes",
           "Mixed", "Mixed", "Yes", "Mixed"),
  Cath_Confounded = c("No", "No", "No", "Yes*", "No", "No", "No", "No", "Yes*", "No",
                      "No", "Yes*", "No", "Yes*"),
  Follow_up = c("Until removal", "Max 3 days", "30 days", "Until removal",
                "72 hours", "33 months", "2 hours", "48-96h", "Until removal", "Hospital stay",
                "Until removal", "Until removal", "Up to 1 week", "Until removal"),
  Key_Finding = c("Failure 23.8% vs 25.0% (NS); Dwell 47.1 vs 47.7h (NS)",
                  "Lifespan 3 vs 3 days (NS); Extravasation 34% vs 18% (p=0.094)",
                  "Adjusted HR 0.91 (0.87-0.95) favoring USG",
                  "Median dwell 219 vs 108h; HR 2.20 (1.45-3.34)",
                  "Premature removal 27% vs 21% (RR 1.26, NS)",
                  "Contrast extrav 4.1% vs 0.21% (RR 19.4)",
                  "2hr patency 97.78% vs 84.44% (p=0.03)",
                  "Failure 11.3% vs 9.5% (NS); Utility 23.5 vs 24.7h (NS)",
                  "Dwell 9.2+/-6.0 vs 3.2+/-2.1 days (p<0.0001)",
                  "Infiltration 7.6% vs 5.9% (OR 1.31, NS)",
                  "Dwell 96 vs 59h (p<0.001); USG +36.7h longer",
                  "Dwell 127 vs 60h; USG used 64mm vs blind 19-32mm",
                  "1st-attempt success 70% vs 40% (p<0.05); Extravasation 13.6% vs 28.5% (NS)",
                  "K-M dwell 143 vs 89h (p<0.001); Failure 34% vs 32% (NS)"),
  stringsAsFactors = FALSE
)

write_csv(t1, "output/table1_study_characteristics.csv")
cat("Table 1 CSV saved: output/table1_study_characteristics.csv\n")

# ============================================================
# TABLE 2A: RoB 2 for RCTs
# ============================================================

t2a <- data.frame(
  Study = c("Kleidon 2025", "Bridey 2018", "Varghese 2025", "Leroux 2023", "Nishizawa 2020"),
  D1_Randomisation = c("Low", "Low", "Low", "Low", "Low"),
  D2_Deviations = c("Some concerns", "Some concerns", "Low", "Some concerns", "Some concerns"),
  D3_Missing_Data = c("Low", "Low", "Low", "High", "Low"),
  D4_Measurement = c("Low", "Some concerns", "Some concerns", "Some concerns", "Some concerns"),
  D5_Reporting = c("Low", "Low", "Some concerns", "Low", "Low"),
  Overall = c("Some concerns", "Some concerns", "Some concerns", "High risk", "Some concerns"),
  stringsAsFactors = FALSE
)

write_csv(t2a, "output/table2a_rob2_rcts.csv")
cat("Table 2A CSV saved: output/table2a_rob2_rcts.csv\n")

# ============================================================
# TABLE 2B: NOS for Cohort Studies
# ============================================================

t2b <- data.frame(
  Study = c("Feinsmith 2021", "Dachepally 2023", "Shokoohi 2019",
            "Favot 2019", "Paladini 2018", "Saltarelli 2015",
            "Cottrell 2021", "Refosco 2024", "Desai 2018"),
  Selection_max4 = c(3, 3, 4, 2, 3, 3, 3, 2, 2),
  Comparability_max2 = c(1, 1, 2, 1, 1, 1, 1, 1, 1),
  Outcome_max3 = c(2, 2, 3, 2, 2, 1, 2, 2, 2),
  Total = c("6/9", "6/9", "9/9", "5/9", "6/9", "5/9", "6/9", "5/9", "5/9"),
  Key_Concern = c("Selection bias (DIVA), missing IFR data",
                  "Catheter length confounding",
                  "(Highest quality)",
                  "Ecological comparison, different data sources",
                  "Catheter type confounding",
                  "Conference abstract only",
                  "Same catheter type; USG more difficult cases",
                  "Catheter length confounding (64mm vs 19-32mm)",
                  "USG group 55% DIVA hx vs TPIV 7.2%; longer catheters"),
  stringsAsFactors = FALSE
)

write_csv(t2b, "output/table2b_nos_cohorts.csv")
cat("Table 2B CSV saved: output/table2b_nos_cohorts.csv\n")

# ============================================================
# PDF GENERATION
# ============================================================

# --- Table 1 PDF ---
pdf("output/table1_study_characteristics.pdf", width = 17, height = 10)
par(mar = c(1, 1, 3, 1))
plot.new()
title(main = "Table 1. Characteristics of Included Studies", cex.main = 1.3, font.main = 2)

# Prepare display matrix
col_names <- c("Study", "Year", "Country", "Design", "Setting", "Population",
               "N (USG)", "N (LM)", "DIVA", "Cath.\nConf.", "Follow-up", "Key Finding")
mat <- cbind(t1$Study, t1$Year, t1$Country, t1$Design, t1$Setting, t1$Population,
             t1$N_USG, t1$N_LM, t1$DIVA, t1$Cath_Confounded, t1$Follow_up, t1$Key_Finding)

nc <- ncol(mat)
nr <- nrow(mat)

# Column widths (proportional)
cw <- c(0.07, 0.03, 0.05, 0.06, 0.08, 0.10, 0.04, 0.04, 0.03, 0.03, 0.07, 0.22)
cw <- cw / sum(cw)
cx <- c(0, cumsum(cw))
cx <- cx[1:nc] + cw/2  # center positions
x_start <- 0.01
x_end <- 0.99
cx <- x_start + cx * (x_end - x_start)

# Row positions
y_header <- 0.94
y_start <- 0.88
y_step <- 0.060
row_fills <- rep(c("#F8F8F8", "#FFFFFF"), length.out = nr)

# Draw header background
rect(x_start, y_header - 0.03, x_end, y_header + 0.03, col = "#2171B5", border = NA)

# Header text
for (j in 1:nc) {
  text(cx[j], y_header, col_names[j], cex = 0.55, font = 2, col = "white")
}

# Data rows
for (i in 1:nr) {
  y <- y_start - (i - 1) * y_step
  rect(x_start, y - 0.03, x_end, y + 0.03, col = row_fills[i], border = NA)
  for (j in 1:nc) {
    text_cex <- if (j == 12) 0.42 else if (j %in% c(5,6)) 0.45 else 0.5
    text(cx[j], y, mat[i, j], cex = text_cex)
  }
}

# Bottom line
segments(x_start, y_start - nr * y_step + 0.04, x_end, y_start - nr * y_step + 0.04, lwd = 1)

# Footnote
text(x_start, y_start - nr * y_step,
     "*USG group used systematically longer catheters than landmark group; results confounded by catheter length/type.",
     adj = 0, cex = 0.45, font = 3)

dev.off()
cat("Table 1 PDF saved: output/table1_study_characteristics.pdf\n")

# --- Table 2A PDF (RoB 2) ---
pdf("output/table2_risk_of_bias.pdf", width = 14, height = 9)

# Page 1: RoB 2
par(mar = c(1, 1, 3, 1))
plot.new()
title(main = "Table 2. Risk of Bias Assessment", cex.main = 1.3, font.main = 2)
text(0.5, 0.95, "Part A: Cochrane RoB 2 for Randomised Controlled Trials", cex = 1.0, font = 2)

rob_cols <- c("Study", "D1:\nRandomisation", "D2:\nDeviations", "D3:\nMissing Data",
              "D4:\nMeasurement", "D5:\nReporting", "Overall")
rob_mat <- cbind(t2a$Study, t2a$D1_Randomisation, t2a$D2_Deviations,
                 t2a$D3_Missing_Data, t2a$D4_Measurement, t2a$D5_Reporting, t2a$Overall)

nc2 <- ncol(rob_mat)
nr2 <- nrow(rob_mat)
cw2 <- c(0.15, rep(0.12, 5), 0.15)
cw2 <- cw2 / sum(cw2)
cx2 <- c(0, cumsum(cw2))
cx2 <- cx2[1:nc2] + cw2/2
cx2 <- 0.05 + cx2 * 0.90

y_h2 <- 0.88
y_s2 <- 0.78
y_st2 <- 0.12

# Color coding function
rob_color <- function(val) {
  if (grepl("Low", val)) return("#C7E9C0")
  if (grepl("High", val)) return("#FDB9B9")
  if (grepl("Some", val)) return("#FFF3CD")
  return("#FFFFFF")
}

# Header
rect(0.05, y_h2 - 0.04, 0.95, y_h2 + 0.04, col = "#2171B5", border = NA)
for (j in 1:nc2) {
  text(cx2[j], y_h2, rob_cols[j], cex = 0.7, font = 2, col = "white")
}

# Data
for (i in 1:nr2) {
  y <- y_s2 - (i - 1) * y_st2
  for (j in 1:nc2) {
    fill_col <- if (j == 1) "#F8F8F8" else rob_color(rob_mat[i, j])
    x_left <- 0.05 + c(0, cumsum(cw2))[j] * 0.90
    x_right <- 0.05 + cumsum(cw2)[j] * 0.90
    rect(x_left, y - 0.04, x_right, y + 0.04, col = fill_col, border = "#CCCCCC")
    text(cx2[j], y, rob_mat[i, j], cex = 0.65)
  }
}

# Legend
legend_y <- 0.22
text(0.05, legend_y, "Legend:", font = 2, cex = 0.7, adj = 0)
rect(0.15, legend_y - 0.015, 0.19, legend_y + 0.015, col = "#C7E9C0", border = "#999")
text(0.20, legend_y, "Low risk", cex = 0.6, adj = 0)
rect(0.33, legend_y - 0.015, 0.37, legend_y + 0.015, col = "#FFF3CD", border = "#999")
text(0.38, legend_y, "Some concerns", cex = 0.6, adj = 0)
rect(0.55, legend_y - 0.015, 0.59, legend_y + 0.015, col = "#FDB9B9", border = "#999")
text(0.60, legend_y, "High risk", cex = 0.6, adj = 0)

# --- Page 2: NOS ---
plot.new()
par(mar = c(1, 1, 3, 1))
title(main = "Table 2. Risk of Bias Assessment (continued)", cex.main = 1.3, font.main = 2)
text(0.5, 0.95, "Part B: Newcastle-Ottawa Scale for Cohort Studies", cex = 1.0, font = 2)

nos_cols <- c("Study", "Selection\n(max 4)", "Comparability\n(max 2)", "Outcome\n(max 3)",
              "Total", "Key Concern")
nos_mat <- cbind(t2b$Study, t2b$Selection_max4, t2b$Comparability_max2,
                 t2b$Outcome_max3, t2b$Total, t2b$Key_Concern)

nc3 <- ncol(nos_mat)
nr3 <- nrow(nos_mat)
cw3 <- c(0.14, 0.10, 0.12, 0.10, 0.08, 0.30)
cw3 <- cw3 / sum(cw3)
cx3 <- c(0, cumsum(cw3))
cx3 <- cx3[1:nc3] + cw3/2
cx3 <- 0.05 + cx3 * 0.90

y_h3 <- 0.88
y_s3 <- 0.78
y_st3 <- 0.10

# NOS color
nos_color <- function(total_str) {
  val <- as.numeric(sub("/9", "", total_str))
  if (is.na(val)) return("#FFFFFF")
  if (val >= 8) return("#C7E9C0")
  if (val >= 6) return("#FFF3CD")
  return("#FDB9B9")
}

# Header
rect(0.05, y_h3 - 0.04, 0.95, y_h3 + 0.04, col = "#2171B5", border = NA)
for (j in 1:nc3) {
  text(cx3[j], y_h3, nos_cols[j], cex = 0.7, font = 2, col = "white")
}

# Data
for (i in 1:nr3) {
  y <- y_s3 - (i - 1) * y_st3
  for (j in 1:nc3) {
    fill_col <- if (j == 5) nos_color(nos_mat[i, j]) else if (j == 1) "#F8F8F8" else "#FFFFFF"
    x_left <- 0.05 + c(0, cumsum(cw3))[j] * 0.90
    x_right <- 0.05 + cumsum(cw3)[j] * 0.90
    rect(x_left, y - 0.04, x_right, y + 0.04, col = fill_col, border = "#CCCCCC")
    text_cex <- if (j == 6) 0.55 else 0.65
    text(cx3[j], y, nos_mat[i, j], cex = text_cex)
  }
}

# Legend
legend_y2 <- 0.12
text(0.05, legend_y2, "NOS Total:", font = 2, cex = 0.7, adj = 0)
rect(0.18, legend_y2 - 0.015, 0.22, legend_y2 + 0.015, col = "#C7E9C0", border = "#999")
text(0.23, legend_y2, "8-9 (Good)", cex = 0.6, adj = 0)
rect(0.38, legend_y2 - 0.015, 0.42, legend_y2 + 0.015, col = "#FFF3CD", border = "#999")
text(0.43, legend_y2, "6-7 (Fair)", cex = 0.6, adj = 0)
rect(0.58, legend_y2 - 0.015, 0.62, legend_y2 + 0.015, col = "#FDB9B9", border = "#999")
text(0.63, legend_y2, "0-5 (Poor)", cex = 0.6, adj = 0)

dev.off()
cat("Table 2 PDF saved: output/table2_risk_of_bias.pdf\n")

cat("\nAll tables generated.\n")
