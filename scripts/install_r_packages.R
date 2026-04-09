#!/usr/bin/env Rscript
# install_r_packages.R
# Install all required R packages for meta-analysis

packages <- c(
  "meta",        # Core meta-analysis functions
  "metafor",     # Advanced meta-analysis (rma, forest, funnel)
  "dmetar",      # Influence analysis, GOSH, find.outliers
  "readxl",      # Read Excel files
  "readr",       # Read CSV files
  "dplyr",       # Data manipulation
  "ggplot2",     # Plotting
  "gridExtra"    # Arrange multiple plots
)

cat("Installing R packages for meta-analysis...\n\n")

for (pkg in packages) {
  if (!requireNamespace(pkg, quietly = TRUE)) {
    cat("Installing:", pkg, "...\n")
    install.packages(pkg, repos = "https://cran.r-project.org", quiet = TRUE)
  } else {
    cat("Already installed:", pkg, "\n")
  }
}

# dmetar may need special installation
if (!requireNamespace("dmetar", quietly = TRUE)) {
  cat("\nInstalling dmetar from GitHub...\n")
  if (!requireNamespace("remotes", quietly = TRUE)) {
    install.packages("remotes", repos = "https://cran.r-project.org")
  }
  remotes::install_github("MathiasHarrer/dmetar", quiet = TRUE)
}

cat("\n✅ All packages installed!\n")
