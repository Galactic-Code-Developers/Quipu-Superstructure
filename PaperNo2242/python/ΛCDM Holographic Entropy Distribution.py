# Copyright (c) 2025 Antonios Valamontes
# ORCID: https://orcid.org/0009-0008-5616-7746
#
# Licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) License.
# You may use, share, modify, and distribute this code, provided that proper attribution
# is given to the original author.
#
# Full license details: https://creativecommons.org/licenses/by/4.0/
#
# DISCLAIMER: This code is provided "as is," without warranty of any kind. The author is
# not responsible for any damages or unintended consequences arising from its use.
#
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare

# Define cosmic structures
cosmic_structures = ["Quipu", "Shapley", "Ser-CorBor", "Hercules", "Scu-Peg"]

# Define entanglement entropy values
holographic_entropy_qte = np.array([15.33, 12.45, 10.78, 8.92, 7.11])
holographic_entropy_lcdm = np.array([14.00, 11.80, 10.50, 8.50, 6.90])

# Normalize both distributions to ensure equal total sum
qte_sum = np.sum(holographic_entropy_qte)
lcdm_sum = np.sum(holographic_entropy_lcdm)

holographic_entropy_qte_normalized = holographic_entropy_qte * (lcdm_sum / qte_sum)

# Define observational uncertainty (error bars)
holographic_entropy_err = np.array([0.50, 0.45, 0.40, 0.35, 0.30])

# Perform Chi-Square test with normalized values
chi_stat, p_value = chisquare(holographic_entropy_qte_normalized, holographic_entropy_lcdm)

# Set up figure
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# QTE Entropy Distribution
axes[0].bar(cosmic_structures, holographic_entropy_qte, color='blue', alpha=0.6,
            label="QTE Holographic Entropy", yerr=holographic_entropy_err, capsize=5)
axes[0].set_title("QTE Holographic Entropy Distribution")
axes[0].set_xlabel("Cosmic Structure")
axes[0].set_ylabel("Entropy Value")
axes[0].grid(True, linestyle="--", alpha=0.6)
axes[0].legend()

# LCDM Entropy Distribution
axes[1].bar(cosmic_structures, holographic_entropy_lcdm, color='red', alpha=0.6,
            label="ΛCDM Entropy Prediction")
axes[1].set_title("ΛCDM Holographic Entropy Distribution")
axes[1].set_xlabel("Cosmic Structure")
axes[1].grid(True, linestyle="--", alpha=0.6)
axes[1].legend()

# Display Chi-Square test results
plt.figtext(0.5, -0.02, f"Chi-Square Test: χ² = {chi_stat:.2f}, p-value = {p_value:.4f}", fontsize=12, ha="center")

# Show plot
plt.tight_layout()
plt.show()

# Display Chi-Square results
print(f"Chi-Square Test Statistic: {chi_stat:.2f}")
print(f"p-value: {p_value:.4f}")