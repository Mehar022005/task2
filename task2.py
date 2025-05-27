import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
sns.set(style="whitegrid")
df = pd.read_csv("Titanic.csv")
print(df.info())
print(df.head())

# Summary Statistics
print("\n Mean Values")
print(df.mean(numeric_only=True))
print("\n Median Values")
print(df.median(numeric_only=True))
print("\n Standard Deviation")
print(df.std(numeric_only=True))
print("\n Descriptive Statistics ")
print(df.describe(include='all'))

 #Histograms and Boxplots

# Histograms
df.hist(figsize=(12, 10), bins=20, edgecolor='black')
plt.suptitle("Histograms for Numeric Features", fontsize=16)
plt.tight_layout()
plt.show()

# Boxplot - Age
plt.figure(figsize=(8, 5))
sns.boxplot(x=df["Age"], color="orange")
plt.title("Boxplot of Age")
plt.show()

# Boxplot - Fare
plt.figure(figsize=(8, 5))
sns.boxplot(x=df["Fare"], color="green")
plt.title("Boxplot of Fare")
plt.show()

#  Correlation Matrix & Pairplot

# Correlation matrix
plt.figure(figsize=(10, 6))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Matrix")
plt.show()

# Pairplot with selected features
sns.pairplot(df.dropna(), vars=["Age", "Fare", "Pclass"], hue="Survived", palette="husl")
plt.suptitle("Pairplot of Selected Features", y=1.02)
plt.show()

# Identify Patterns, Trends, or Anomalies

# Survival by Sex
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Survived', hue='Sex')
plt.title("Survival by Gender")
plt.show()

# Survival by Pclass
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Pclass', hue='Survived')
plt.title("Survival by Passenger Class")
plt.show()

# Age distribution by survival
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="Age", hue="Survived", kde=True, bins=30)
plt.title("Age Distribution by Survival")
plt.show()

# Feature-Level Inference from Visuals

# Interactive histogram using Plotly (optional)
fig = px.histogram(df, x="Age", color="Survived", nbins=30, title="Age vs Survival (Interactive)")
fig.show()

# Bar plot - Embarked vs Survival
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Embarked', hue='Survived')
plt.title("Survival by Embarkation Port")
plt.show()

# Bar plot - SibSp (siblings/spouses aboard) vs Survival
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='SibSp', hue='Survived')
plt.title("Survival by Number of Siblings/Spouses Aboard")
plt.show()

# BONUS: Missing Values Visualization
plt.figure(figsize=(10, 4))
sns.heatmap(df.isnull(), cbar=False, cmap="YlGnBu", yticklabels=False)
plt.title("Missing Values in Dataset")
plt.show()

# Print missing value count
print("\n=== Missing Values per Column ===")
print(df.isnull().sum())
