#!/usr/bin/env Rscript
# =============================================================================
# 07_rob_visualization.R
# Figure 7 — Risk-of-bias visual summary (RoB 2 + NOS) for US-PIVC SR/MA
# Produces: POMIN_v2_2026-05-05/figures/Figure7_RoB_Summary.pdf
#
# Data source: output/risk_of_bias.md (authoritative ratings, audited 2026-04-28)
# =============================================================================

suppressPackageStartupMessages({
  library(robvis)
  library(ggplot2)
  library(patchwork)
  library(dplyr)
  library(tidyr)
})

out_pdf <- "/Users/chencc/Research/US-PIVC/POMIN_v2_2026-05-05/figures/Figure7_RoB_Summary.pdf"
out_png <- "/Users/chencc/Research/US-PIVC/POMIN_v2_2026-05-05/figures/Figure7_RoB_Summary.png"
dir.create(dirname(out_pdf), recursive = TRUE, showWarnings = FALSE)

# ---- RoB 2 for the 5 RCTs (per output/risk_of_bias.md) ---------------------
rob2 <- tibble::tribble(
  ~Study,            ~D1,            ~D2,             ~D3,            ~D4,             ~D5,             ~Overall,
  "Kleidon 2025",    "Low",          "Some concerns", "Low",          "Low",           "Low",           "Some concerns",
  "Bridey 2018",     "Low",          "Some concerns", "Low",          "Some concerns", "Low",           "Some concerns",
  "Varghese 2025",   "Low",          "Low",           "Low",          "Some concerns", "Some concerns", "Some concerns",
  "Leroux 2023",     "Low",          "Some concerns", "High",         "Some concerns", "Low",           "High",
  "Nishizawa 2020",  "Low",          "Some concerns", "Low",          "Some concerns", "Low",           "Some concerns"
)

# robvis expects column header "Study"/"D1"/.../"Overall" for tool="ROB2"
rob2_traffic <- rob_traffic_light(
  data    = rob2,
  tool    = "ROB2",
  psize   = 7,
  colour  = "cochrane"
)
rob2_summary <- rob_summary(
  data    = rob2,
  tool    = "ROB2",
  overall = TRUE,
  weighted = FALSE,
  colour  = "cochrane"
)

# ---- NOS for the 9 cohort studies (custom ggplot — robvis has no native NOS) ----
nos <- tibble::tribble(
  ~Study,             ~Selection, ~Comparability, ~Outcome, ~Total, ~KeyConcern,
  "Feinsmith 2021",   3, 1, 2, 6, "Selection bias (DIVA), missing IFR",
  "Dachepally 2023",  3, 1, 2, 6, "Catheter length confounding",
  "Shokoohi 2019",    4, 2, 3, 9, "Highest quality (nested in RCT)",
  "Favot 2019",       2, 1, 2, 5, "Ecological comparison",
  "Paladini 2018",    3, 1, 2, 6, "Catheter type confounding",
  "Saltarelli 2015",  3, 1, 1, 5, "Conference abstract only",
  "Cottrell 2021",    3, 1, 2, 6, "Difficulty-class imbalance",
  "Refosco 2024",     2, 1, 2, 5, "Catheter length confounding (64 mm vs 19–32 mm)",
  "Desai 2018",       2, 1, 2, 5, "DIVA history + catheter length"
)

# Star-fraction cell colour: green = max, amber = ≥half, red = <half
nos_long <- nos %>%
  select(Study, Selection, Comparability, Outcome) %>%
  mutate(Study = factor(Study, levels = rev(Study))) %>%
  pivot_longer(-Study, names_to = "Domain", values_to = "Stars") %>%
  mutate(
    Max     = case_when(Domain == "Selection" ~ 4,
                        Domain == "Comparability" ~ 2,
                        Domain == "Outcome" ~ 3),
    Frac    = Stars / Max,
    Rating  = case_when(Frac == 1   ~ "Low",
                        Frac >= 0.5 ~ "Some concerns",
                        TRUE        ~ "High"),
    Label   = paste0(Stars, "/", Max),
    Domain  = factor(Domain, levels = c("Selection", "Comparability", "Outcome"))
  )

cochrane_pal <- c("Low" = "#02C100", "Some concerns" = "#E2DF07", "High" = "#BF0000", "No information" = "#4EA1F7")

nos_plot <- ggplot(nos_long, aes(Domain, Study, fill = Rating)) +
  geom_tile(colour = "grey20", linewidth = 0.4) +
  geom_text(aes(label = Label), size = 3.6, colour = "black") +
  scale_fill_manual(values = cochrane_pal, name = "RoB rating") +
  labs(title = "B. Newcastle-Ottawa Scale (cohort studies, n = 9)",
       subtitle = "Stars by NOS domain (Selection /4, Comparability /2, Outcome /3); colour = derived risk band",
       x = NULL, y = NULL) +
  theme_minimal(base_size = 10) +
  theme(
    panel.grid    = element_blank(),
    axis.text.y   = element_text(face = "italic"),
    plot.title    = element_text(face = "bold"),
    plot.subtitle = element_text(size = 8, colour = "grey30"),
    legend.position = "bottom"
  )

# ---- Overall RoB-summary bar (combined RCT + cohort overall ratings) -------
overall_combined <- bind_rows(
  tibble(Study = rob2$Study, Tool = "RoB 2 (RCT)", Overall = rob2$Overall),
  tibble(Study = nos$Study,
         Tool  = "NOS (cohort)",
         Overall = case_when(nos$Total >= 8 ~ "Low",
                             nos$Total >= 6 ~ "Some concerns",
                             TRUE           ~ "High"))
) %>%
  mutate(Overall = factor(Overall, levels = c("Low", "Some concerns", "High")))

overall_bar <- ggplot(overall_combined, aes(x = Tool, fill = Overall)) +
  geom_bar(position = "fill", colour = "grey30", linewidth = 0.3) +
  scale_fill_manual(values = cochrane_pal, name = "Overall risk") +
  scale_y_continuous(labels = scales::percent, expand = c(0, 0)) +
  coord_flip() +
  labs(title = "C. Overall risk distribution by assessment tool",
       x = NULL, y = "% of studies") +
  theme_minimal(base_size = 10) +
  theme(
    panel.grid.major.y = element_blank(),
    plot.title         = element_text(face = "bold"),
    legend.position    = "bottom"
  )

# ---- Compose 3-panel figure (A: RoB2 traffic, B: NOS heatmap, C: combined bar) ----
top <- rob2_traffic + ggtitle("A. Cochrane RoB 2 traffic-light plot (RCTs, n = 5)") +
  theme(plot.title = element_text(face = "bold", size = 11))

combined <- (top / (nos_plot | overall_bar)) +
  plot_layout(heights = c(1.2, 1.0)) +
  plot_annotation(
    title    = "Figure 7. Risk-of-bias and methodological-quality summary across all 14 included studies",
    subtitle = "Cochrane Risk of Bias 2 (5 RCTs) and Newcastle-Ottawa Scale (9 cohort studies); see Table 2 for details",
    caption  = "Authoritative ratings: output/risk_of_bias.md (audited 2026-04-28). Cochrane RoB colour palette.",
    theme    = theme(plot.title = element_text(face = "bold", size = 13),
                     plot.subtitle = element_text(size = 10, colour = "grey25"),
                     plot.caption = element_text(size = 8, colour = "grey40", hjust = 0))
  )

ggsave(out_pdf, combined, width = 11, height = 12, units = "in", device = cairo_pdf)
ggsave(out_png, combined, width = 11, height = 12, units = "in", dpi = 200)

cat("Saved:\n  ", out_pdf, "\n  ", out_png, "\n", sep = "")
