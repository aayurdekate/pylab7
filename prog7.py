import pandas as pd
import numpy as np

# Sample data
data = {
    'Photographer': ['Alice', 'Bob', 'Alice', 'Carol', 'Alice', 'Dave', 'Bob', 'Carol'],
    'Media_Type': ['Photo', 'Video', 'Photo', 'Photo', 'Video', 'Photo', 'Video', 'Photo'],
    'Views': [120, np.nan, 80, 90, 100, np.nan, 50, 70],
    'Likes': [10, 20, 5, np.nan, 8, 15, np.nan, 12],
    'Upload_Date': ['2024-09-01', '2024-09-02', '2024-09-01', '2024-09-03', '2024-09-02', '2024-09-01', '2024-09-02', '2024-09-03']
}

df = pd.DataFrame(data)

print("Initial Dataset:")
print(df)

df['Views'].fillna(df['Views'].mean(), inplace=True)
df['Likes'].fillna(df['Likes'].mean(), inplace=True)

print("\nDataset after handling missing data:")
print(df)

df.set_index(['Photographer', 'Media_Type'], inplace=True)

print("\nDataset with hierarchical indexing:")
print(df)

aggregation = df.groupby('Photographer').agg({'Views': 'sum', 'Likes': 'sum'})

print("\nAggregated data (total views and likes per photographer):")
print(aggregation)
