# -*- coding: utf-8 -*-
"""Student_Performance_Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15Tm7B9PA0zG2LEf2RKHqJdjSmrVDSeWr
"""

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Create the DataFrame
data = {
    'Student': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'Study Hours': [1, 2, 3, 4, 5, 6, 7],
    'Sleep Hours': [8, 7, 6, 2, 3, 4, 1],
    'Score': [45, 50, 55, 70, 60, 80, 85]
}

df = pd.DataFrame(data)

# Display the DataFrame
print("📊 Student Performance Data:\n")
print(df)

# Step 2: Visualizations
sns.set(style="whitegrid")

# Study Hours vs Score
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='Study Hours', y='Score', color='blue', s=100)
plt.title('Study Hours vs Score')
plt.xlabel('Study Hours')
plt.ylabel('Score')
plt.tight_layout()
plt.show()

# Sleep Hours vs Score
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='Sleep Hours', y='Score', color='green', s=100)
plt.title('Sleep Hours vs Score')
plt.xlabel('Sleep Hours')
plt.ylabel('Score')
plt.tight_layout()
plt.show()

# Step 3: Correlation Matric
print("\n📈 Correlation Matrix:\n")
correlation = df[['Study Hours', 'Sleep Hours', 'Score']].corr()
print(correlation)

# Step 4: Insights
print("\n📌 Insights:")
if correlation.loc['Score', 'Study Hours'] > 0:
    print("🔹 Students who study more tend to score higher.")
if correlation.loc['Score', 'Sleep Hours'] < 0:
    print("🔹 More sleep is associated with slightly lower scores in this dataset.")
