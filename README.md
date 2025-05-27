# task2
# Titanic Dataset - Exploratory Data Analysis (EDA)

This project is part of the **Elevate Labs Internship - Task 2**, where the goal is to perform an in-depth Exploratory Data Analysis (EDA) on the Titanic dataset.

---

## **Dataset Information**

* **Source**: [Titanic dataset](https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv)
* **Description**: This dataset provides information on passengers aboard the Titanic, including whether they survived or not, along with details such as age, sex, ticket fare, class, etc.

---

## **Objectives**

* Generate summary statistics (mean, median, standard deviation)
* Visualize distributions using histograms and boxplots
* Analyze correlations and feature relationships
* Identify patterns and anomalies
* Make basic inferences from the visualized data

---

## **Libraries Used**

* `pandas`
* `matplotlib`
* `seaborn`
* `plotly` (optional, for interactive visualizations)

---

## **Key Steps and Results**

### 1. **Summary Statistics**

* Calculated mean, median, and standard deviation for numeric features.
* Used `describe()` to view complete statistical info.

### 2. **Visualizations**

* **Histograms**: Showed distributions of age, fare, etc.
* **Boxplots**: Detected outliers in age and fare.
* **Correlation Matrix**: Revealed weak correlations between features.
* **Pairplots**: Explored relationships between multiple numeric features.
* **Countplots**: Compared survival rates across different genders, classes, and embarked ports.

### 3. **Insights**

* **Women had higher survival rates** than men.
* **1st class passengers** were more likely to survive.
* Infants and young children had higher survival chances.
* Age distribution is slightly right-skewed.
* The 'Cabin' column has many missing values and may not be useful without cleaning.

### 4. **Missing Data**

* Displayed a heatmap of missing values.
* 'Age', 'Cabin', and 'Embarked' had missing values needing preprocessing.

---

## **Conclusion**

This EDA helped understand the Titanic dataset better by visualizing and analyzing key features. These insights are crucial for building accurate predictive models in later stages.



