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

# Define cosmic structures and their entanglement metrics
cosmic_structures = ["Quipu", "Shapley", "Ser-CorBor", "Hercules", "Scu-Peg"]
quantum_coherence = [4.99, 3.21, 2.88, 2.35, 1.92]
topological_entanglement = [2.77, 2.10, 1.85, 1.42, 1.15]
holographic_entropy = [15.33, 12.45, 10.78, 8.92, 7.11]

# Set up figure
plt.figure(figsize=(10, 6))

# Plot each entanglement metric
plt.plot(cosmic_structures, quantum_coherence, marker='o', linestyle='-', label="Quantum Coherence")
plt.plot(cosmic_structures, topological_entanglement, marker='s', linestyle='--', label="Topological Entanglement")
plt.plot(cosmic_structures, holographic_entropy, marker='D', linestyle='-.', label="Holographic Entropy")

# Enhance visualization
plt.xlabel("Cosmic Structure", fontsize=12)
plt.ylabel("Entanglement Metric Value", fontsize=12)
plt.title("Entanglement Metrics Across Cosmic Scales", fontsize=14)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)

# Show plot
plt.show()