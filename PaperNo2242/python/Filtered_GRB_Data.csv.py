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
import pandas as pd

# Create the dataset
filtered_grb_data = {
    "GRB Event": ["GRB 221009A", "GRB 221009A", "GRB 060614", "GRB 060614"],
    "Raw Data": [
        "GRB 221009A Fluence: 1.2E-4 Peak Flux: 3.5E-6",
        "GRB 221009A Fluence: 1.4E-4 Peak Flux: 4.1E-6",
        "GRB 060614 Fluence: 9.8E-5 Peak Flux: 2.7E-6",
        "GRB 060614 Fluence: 8.5E-5 Peak Flux: 2.5E-6"
    ]
}

# Convert to DataFrame
df_filtered = pd.DataFrame(filtered_grb_data)

# Save the file
filtered_csv_path = "Filtered_GRB_Data.csv"
df_filtered.to_csv(filtered_csv_path, index=False)

# Provide download link
from google.colab import files
files.download(filtered_csv_path)

print("✅ File created. Click the download link above to save the file.")
