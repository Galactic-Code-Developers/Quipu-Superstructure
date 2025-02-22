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

# Define cosmic structures
cosmic_structures = ["Quipu", "Shapley", "Ser-CorBor", "Hercules", "Scu-Peg"]

# Define entanglement metrics
quantum_coherence = np.array([4.99, 3.21, 2.88, 2.35, 1.92])
topological_entanglement = np.array([2.77, 2.10, 1.85, 1.42, 1.15])
holographic_entropy = np.array([15.33, 12.45, 10.78, 8.92, 7.11])

# Define ΛCDM predictions for entanglement entropy
lcdm_entropy = np.array([14.00, 11.80, 10.50, 8.50, 6.90])
entropy_deviation = holographic_entropy - lcdm_entropy  # Difference from ΛCDM

# Define observational uncertainty (error bars)
quantum_coherence_err = np.array([0.25, 0.20, 0.18, 0.15, 0.12])
topological_entanglement_err = np.array([0.15, 0.12, 0.10, 0.08, 0.06])
holographic_entropy_err = np.array([0.50, 0.45, 0.40, 0.35, 0.30])

# Set up figure
plt.figure(figsize=(10, 6))

# Plot entanglement metrics with error bars
plt.errorbar(cosmic_structures, quantum_coherence, yerr=quantum_coherence_err, fmt='o-', label="Quantum Coherence")
plt.errorbar(cosmic_structures, topological_entanglement, yerr=topological_entanglement_err, fmt='s--', label="Topological Entanglement")
plt.errorbar(cosmic_structures, holographic_entropy, yerr=holographic_entropy_err, fmt='D-.', label="Holographic Entropy")

# Plot ΛCDM entropy predictions for comparison
plt.plot(cosmic_structures, lcdm_entropy, 'r--', label="ΛCDM Entropy Prediction")

# Add entropy deviation as text annotations
for i, val in enumerate(entropy_deviation):
    plt.text(i, holographic_entropy[i] + 0.5, f"Δ={val:.2f}", fontsize=10, ha='center', color='black')

# Enhance visualization
plt.xlabel("Cosmic Structure", fontsize=12)
plt.ylabel("Entanglement Metric Value", fontsize=12)
plt.title("Entanglement Metrics Across Cosmic Scales\n(Comparison with ΛCDM Predictions)", fontsize=14)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)

# Show plot
plt.show()