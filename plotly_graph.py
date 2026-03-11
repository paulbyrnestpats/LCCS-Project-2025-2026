# plotly_graph.py
# This script uses Plotly to create a graph from CSV data.

import pandas as pd
import plotly.express as px

# Load CSV data
df = pd.read_csv("data.csv")

# Example: create a line graph
# Change the column names depending on your dataset
fig = px.line(
    df,
    x="Time",
    y="Temperature",
    title="Temperature Over Time"
)

# Display the graph
fig.show()
