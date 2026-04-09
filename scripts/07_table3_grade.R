#!/usr/bin/env Rscript
# Table 3: GRADE Summary of Findings — PDF

pdf("output/table3_grade_sof.pdf", width = 16, height = 8)
par(mar = c(1, 1, 3, 1))
plot.new()
title(main = "Table 3. GRADE Summary of Findings", cex.main = 1.4, font.main = 2)
text(0.5, 0.94, "USG-guided vs Landmark PIVC Insertion: Post-insertion Outcomes", cex = 0.9, font = 3)

# Data
outcomes <- c("Catheter failure", "Dwell time", "Infiltration", "Extravasation", "HR-based failure")
studies  <- c("4 (2 RCTs, 2 cohorts)", "3 (2 RCTs, 1 cohort)", "2 (1 RCT, 1 cohort)", "2 (1 RCT, 1 cohort)", "2 (2 cohorts)")
pts      <- c("3,404", "929", "2,778", "29,612", "43,800")
effects  <- c("RR 1.23\n(1.00-1.51)", "Not pooled\n(I\u00b2=91.9%)", "RR 0.68\n(0.12-3.83)", "Not pooled\n(I\u00b2=96.7%)", "HR 1.02\n(0.75-1.38)")
grades   <- c("Low", "Very low", "Very low", "Very low", "Very low")
symbols  <- c("\u2295\u2295\u2296\u2296", "\u2295\u2295\u2296\u2296", "\u2295\u2296\u2296\u2296", "\u2295\u2296\u2296\u2296", "\u2295\u2296\u2296\u2296")
reasons  <- c("Serious risk of bias\n(1 high-risk RCT, 2 cohorts);\nSerious imprecision\n(CI crosses unity)",
              "Very serious inconsistency\n(I\u00b2=91.9%; Cottrell favors\nUSG, Kleidon/Leroux null);\nSerious risk of bias",
              "Serious risk of bias\n(abstract only);\nSerious inconsistency\n(I\u00b2=65.9%);\nVery serious imprecision",
              "Very serious inconsistency\n(I\u00b2=96.7%);\nSerious indirectness\n(different definitions);\nSerious risk of bias",
              "Serious risk of bias\n(observational);\nSerious inconsistency\n(I\u00b2=68.1%);\nSerious imprecision")

nr <- length(outcomes)
nc <- 6

# Column positions
col_labels <- c("Outcome", "Studies (k)", "Participants", "Effect Estimate\n(95% CI)", "Certainty\n(GRADE)", "Downgrade Reasons")
cw <- c(0.10, 0.11, 0.07, 0.12, 0.10, 0.28)
cw <- cw / sum(cw)
x_left <- 0.03
x_right <- 0.97
total_w <- x_right - x_left
cx <- x_left + (c(0, cumsum(cw))[1:nc] + cw/2) * total_w
x_borders <- x_left + c(0, cumsum(cw)) * total_w

# Row positions
y_header <- 0.86
row_h <- 0.13
y_rows <- y_header - (1:nr) * row_h - 0.02

# Grade colors
grade_col <- function(g) {
  if (g == "High") return("#C7E9C0")
  if (g == "Moderate") return("#D4E8F7")
  if (g == "Low") return("#FFF3CD")
  return("#FDB9B9")
}

# Header
rect(x_left, y_header - 0.04, x_right, y_header + 0.04, col = "#2171B5", border = NA)
for (j in 1:nc) {
  text(cx[j], y_header, col_labels[j], cex = 0.65, font = 2, col = "white")
}

# Data rows
for (i in 1:nr) {
  y <- y_rows[i]

  for (j in 1:nc) {
    fill <- if (j == 5) grade_col(grades[i]) else if (i %% 2 == 0) "#FFFFFF" else "#F5F7FA"
    rect(x_borders[j], y - row_h/2 + 0.01, x_borders[j+1], y + row_h/2 - 0.01,
         col = fill, border = "#CCCCCC", lwd = 0.5)
  }

  # Content
  text(cx[1], y, outcomes[i], cex = 0.6, font = 2)
  text(cx[2], y, studies[i], cex = 0.55)
  text(cx[3], y, pts[i], cex = 0.6)
  text(cx[4], y, effects[i], cex = 0.55)
  text(cx[5], y, paste0(grades[i]), cex = 0.6, font = 2)
  text(cx[6], y, reasons[i], cex = 0.45, adj = c(0.5, 0.5))
}

# Footer
foot_y <- y_rows[nr] - row_h/2 - 0.02
segments(x_left, foot_y, x_right, foot_y, lwd = 1.5, col = "#2171B5")

text(x_left, foot_y - 0.03,
     "GRADE certainty ratings: High = further research very unlikely to change confidence; Moderate = further research likely to have an important impact;",
     adj = 0, cex = 0.45, font = 3)
text(x_left, foot_y - 0.055,
     "Low = further research very likely to have an important impact; Very low = any estimate of effect is very uncertain.",
     adj = 0, cex = 0.45, font = 3)
text(x_left, foot_y - 0.08,
     "CI = confidence interval; HR = hazard ratio; MD = mean difference; RCT = randomised controlled trial; RR = risk ratio.",
     adj = 0, cex = 0.45)

dev.off()
cat("Table 3 GRADE PDF saved: output/table3_grade_sof.pdf\n")
