#!/usr/bin/env Rscript
# PRISMA 2020 Flow Diagram — base R graphics

draw_box <- function(x, y, w, h, label, fill = "#E8F4FD", border = "#2171B5", cex = 0.7) {
  rect(x - w/2, y - h/2, x + w/2, y + h/2, col = fill, border = border, lwd = 1.5)
  text(x, y, label, cex = cex)
}

draw_arrow <- function(x1, y1, x2, y2) {
  arrows(x1, y1, x2, y2, length = 0.08, lwd = 1.5, col = "#333333")
}

pdf("output/prisma_flowchart.pdf", width = 11, height = 14)

par(mar = c(0.5, 0.5, 1.5, 0.5))
plot(NULL, xlim = c(0, 100), ylim = c(0, 100), axes = FALSE, xlab = "", ylab = "",
     main = "Figure 1. PRISMA 2020 Flow Diagram", cex.main = 1.2, font.main = 2)

# ===== IDENTIFICATION =====
text(5, 97, "IDENTIFICATION", adj = 0, font = 2, cex = 0.9, col = "#555555")

draw_box(40, 93, 45, 8,
         "Records identified from databases\n(n = 1,632)\n\nPubMed (n = 530)  |  Embase (n = 984)\nCochrane CENTRAL (n = 68)  |  CINAHL (n = 50)",
         fill = "#E8F4FD", cex = 0.65)

# ===== DUPLICATES =====
draw_arrow(40, 89, 40, 84)

draw_box(40, 81, 30, 5,
         "Duplicates removed\n(n = 273)",
         fill = "#FDE8E8", border = "#CB181D", cex = 0.7)

# ===== SCREENING =====
draw_arrow(40, 78.5, 40, 74)

text(5, 75, "SCREENING", adj = 0, font = 2, cex = 0.9, col = "#555555")

draw_box(40, 71, 30, 6,
         "Records screened\n(title & abstract)\n(n = 1,359)",
         fill = "#E8F4FD", cex = 0.7)

draw_arrow(55, 71, 68, 71)

draw_box(80, 71, 22, 5,
         "Records excluded\n(n = 1,342)",
         fill = "#FDE8E8", border = "#CB181D", cex = 0.7)

# ===== FULL-TEXT RETRIEVAL =====
draw_arrow(40, 68, 40, 63)

text(5, 64, "ELIGIBILITY", adj = 0, font = 2, cex = 0.9, col = "#555555")

draw_box(40, 60, 30, 5,
         "Reports sought for retrieval\n(n = 17)",
         fill = "#E8F4FD", cex = 0.7)

draw_arrow(55, 60, 68, 60)

draw_box(80, 60, 22, 7,
         "Reports not retrieved\n(n = 0)",
         fill = "#FDE8E8", border = "#CB181D", cex = 0.6)

# ===== FULL-TEXT ASSESSMENT =====
draw_arrow(40, 57.5, 40, 52)

draw_box(40, 48, 32, 7,
         "Reports assessed for\neligibility\n(n = 17)",
         fill = "#E8F4FD", cex = 0.65)

draw_arrow(56, 48, 66, 48)

draw_box(80, 48, 26, 14,
         "Reports excluded (n = 5)\n\nSingle-arm, no comparator:\n  1 (Malik)\nPortuguese language:\n  1 (Avelar)\nNot published:\n  2 (oncology nurses,\n     ICU nurses DIVA)\nProtocol only, same trial:\n  1 (Kleidon BJN)\n\nDuplicate report noted:\n  1 (Kleidon JVA)",
         fill = "#FDE8E8", border = "#CB181D", cex = 0.52)

# ===== INCLUDED =====
draw_arrow(40, 44.5, 40, 38)

text(5, 39, "INCLUDED", adj = 0, font = 2, cex = 0.9, col = "#555555")

draw_box(40, 34, 35, 7,
         "Studies included in\nqualitative synthesis\n(n = 14)\n5 RCTs, 9 cohort studies\n(78,329 participants)",
         fill = "#C7E9C0", border = "#238B45", cex = 0.65)

draw_arrow(40, 30.5, 40, 26)

draw_box(40, 23, 35, 5,
         "Studies included in\nmeta-analysis\n(varies by outcome, max k = 4)",
         fill = "#C7E9C0", border = "#238B45", cex = 0.65)

# ===== DETAIL BOX =====
draw_box(40, 14, 55, 10,
         "Meta-analysis outcomes:\n\nCatheter failure: k = 4 (RR 1.23, 95% CI 1.00-1.51)\nDwell time: k = 3 (I\u00b2 = 91.9%, not pooled)\nInfiltration: k = 2 (RR 0.68, 95% CI 0.12-3.83)\nExtravasation: k = 3 (I\u00b2 = 95.7%, not pooled)\nHR-based failure: k = 2 (HR 1.02, 95% CI 0.75-1.38)",
         fill = "#F5F5F5", border = "#999999", cex = 0.58)

dev.off()

cat("PRISMA flow diagram saved: output/prisma_flowchart.pdf\n")
