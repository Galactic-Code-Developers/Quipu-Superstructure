#
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
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

# Cluster Data: [Name, RA (deg), DEC (deg)]
cluster_data = [
    ["RXCJ0150.7+3305", 27.6789, 33.0851],
    ["RXCJ0214.2+5144", 33.5702, 51.7473],
    ["RXCJ0228.1+2811", 37.0413, 28.1940],
    ["RXCJ0229.0+3805", 37.2543, 38.0964],
    ["RXCJ0229.9+2307", 37.4793, 23.1172],
    ["RXCJ0246.0+3653", 41.5149, 36.8865],
    ["RXCJ0251.1+4513", 42.7979, 45.2237],
    ["RXCJ0254.0+3625", 43.5042, 36.4294],
    ["RXCJ0257.6+1605", 44.4088, 16.0932],
    ["RXCJ0301.8+3549", 45.4632, 35.8268]
]

# Define adjacency matrix (manually designed for network visualization)
adj_matrix = np.array([
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 1, 0, 0],
    [1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 0]
])

# Create graph from adjacency matrix
G = nx.from_numpy_array(adj_matrix)  # FIXED FUNCTION

# Assign cluster names as labels
labels = {i: cluster_data[i][0] for i in range(len(cluster_data))}

# Compute network metrics
clustering_coeffs = nx.clustering(G)  # Clustering coefficients
eigenvector_centrality = nx.eigenvector_centrality(G)  # Eigenvector centrality
betweenness_centrality = nx.betweenness_centrality(G)  # Betweenness centrality

# Normalize values for color mapping
node_colors = list(clustering_coeffs.values())

# Create figure
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)  # Position nodes using force-directed layout

# Draw network graph
nodes = nx.draw_networkx_nodes(G, pos, node_color=node_colors, cmap=plt.cm.viridis, node_size=800)
nx.draw_networkx_edges(G, pos, edge_color='gray')
nx.draw_networkx_labels(G, pos, labels, font_size=8)

# Add colorbar for clustering coefficient values
cbar = plt.colorbar(nodes)
cbar.set_label("Clustering Coefficient", fontsize=12)

plt.title("Adjacency Matrix-Based Cosmic Connectivity\n(Color-coded by Clustering Coefficient)")
plt.show()

# Compare to ΛCDM model expectations (mock comparison)
lcdm_matrix = np.random.choice([0, 1], size=(10, 10), p=[0.7, 0.3])
np.fill_diagonal(lcdm_matrix, 0)
lcdm_G = nx.from_numpy_array(lcdm_matrix)  # FIXED FUNCTION

lcdm_clustering = nx.average_clustering(lcdm_G)
quipu_clustering = nx.average_clustering(G)

print(f"Average Clustering Coefficient (Quipu): {quipu_clustering:.3f}")
print(f"Average Clustering Coefficient (ΛCDM Model): {lcdm_clustering:.3f}")

# Output statistical metrics
print("\nAdditional Network Statistics:")
print(f"Eigenvector Centrality: {eigenvector_centrality}")
print(f"Betweenness Centrality: {betweenness_centrality}")