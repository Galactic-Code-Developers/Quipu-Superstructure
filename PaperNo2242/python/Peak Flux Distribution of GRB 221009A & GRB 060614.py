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
# Install necessary packages
!pip install pandas matplotlib --quiet

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the extracted GRB dataset (replace with your extracted CSV file)
file_path = "Filtered_GRB_Data.csv"

# Read the dataset
df = pd.read_csv(file_path)

# Display the first few rows of the filtered data
print("✅ Loaded GRB 221009A and GRB 060614 Data:")
print(df.head())

# 🔹 **Step 1: Extract Fluences and Peak Fluxes**
# Assuming the raw dataset contains fluence (erg/cm^2) and peak flux (ph/cm^2/s)
df["Fluence"] = df["Raw Data"].str.extract(r'(\d+\.\d+E[+-]\d+)').astype(float)
df["Peak Flux"] = df["Raw Data"].str.extract(r'(\d+\.\d+E[+-]\d+)$').astype(float)

# 🔹 **Step 2: Plot Fluence and Peak Flux Distributions**
plt.figure(figsize=(12, 5))

# Plot Fluence
plt.subplot(1, 2, 1)
plt.hist(df["Fluence"], bins=15, color='blue', alpha=0.7)
plt.xlabel("Fluence (erg/cm²)")
plt.ylabel("Count")
plt.title("Fluence Distribution of GRB 221009A & GRB 060614")

# Plot Peak Flux
plt.subplot(1, 2, 2)
plt.hist(df["Peak Flux"], bins=15, color='red', alpha=0.7)
plt.xlabel("Peak Flux (ph/cm²/s)")
plt.ylabel("Count")
plt.title("Peak Flux Distribution of GRB 221009A & GRB 060614")

# Show plots
plt.tight_layout()
plt.show()

# Save the figures
fluence_plot_path = "GRB_Fluence_Distribution.png"
peak_flux_plot_path = "GRB_PeakFlux_Distribution.png"

plt.savefig(fluence_plot_path, dpi=300)
plt.savefig(peak_flux_plot_path, dpi=300)

print(f"✅ Fluence and Peak Flux histograms saved as '{fluence_plot_path}' and '{peak_flux_plot_path}'.")

# Provide a download link for the saved figures
from google.colab import files
files.download(fluence_plot_path)
files.download(peak_flux_plot_path)