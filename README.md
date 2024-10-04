# ApacheBeam-Data-Engineering

## Assignment 1: World Happiness Report 2019 - Advanced EDA with D3.js Visualizations

### Overview

This project explores the **World Happiness Report 2019** dataset from Kaggle. It involves performing an advanced **Exploratory Data Analysis (EDA)**, utilizing both traditional Python libraries such as **Pandas**, **Matplotlib**, and **Seaborn**, as well as advanced **D3.js** visualizations for interactive insights. 

The aim is to push the limits of interactive data visualization by integrating **D3.js** into Colab to create dynamic visualizations, such as bar charts, scatter plot matrices, and a world map that visualizes the distribution of happiness scores across countries.

### Key Features
- **Descriptive Statistics**: Summarizing key statistics of the dataset.
- **Boxplot**, **Distribution Plot**, and **KDE Plot** for Happiness Score and GDP per Capita.
- **Scatter Plot** for Happiness Score vs. GDP per Capita with interactive elements.
- **Interactive Bar Chart** showing Happiness Score vs. Overall Rank.
- **World Happiness Map** with D3.js, showing the global distribution of happiness.
- **Interactive Bubble Chart** to highlight relationships between Happiness Score, GDP, and Population size.

### EDA Steps
- **Loading and Inspecting the Dataset**: Load the dataset, inspect the structure, data types, and summary statistics.
- **Data Cleaning**: Handle missing values and outliers using the IQR method.
- **Feature Engineering**: Create a new feature categorizing happiness into `Very Happy`, `Happy`, and `Unhappy`.
- **Data Visualization with Python**: Use Boxplot, KDE, and Heatmap to explore key features.
- **Advanced D3.js Visualizations**: Implement interactive bar charts, scatter plots, world maps, and bubble charts to visualize key relationships.

### Installation and Setup
Install the necessary Python packages:
   ```bash
   pip install kaggle matplotlib seaborn

   !mkdir ~/.kaggle
   !cp kaggle.json ~/.kaggle/
   !chmod 600 ~/.kaggle/kaggle.json
  ```
## Project Files

- **`world_happiness_eda.ipynb`**: The Jupyter notebook containing the full EDA and D3.js visualizations.
- **`kaggle.json`**: Kaggle API token for accessing the dataset (ensure it’s kept private).
- **`data/world-happiness/2019.csv`**: The cleaned dataset used for the analysis.
- **`README.md`**: This file.

---

## About the Dataset

The **World Happiness Report** ranks 156 countries by how happy their citizens perceive themselves to be. The ranking is based on six key factors that contribute to well-being:

- **GDP per Capita**
- **Social Support**
- **Healthy Life Expectancy**
- **Freedom to Make Life Choices**
- **Generosity**
- **Perceptions of Corruption**

---

## Conclusion

This project demonstrates how advanced **D3.js** visualizations can enhance the exploratory data analysis process, providing interactive and visually appealing insights into the happiness levels of countries worldwide. It bridges the gap between traditional static plots and modern, dynamic data visualization techniques.


## Assignment 2: NYC Airbnb Open Data - Auto EDA with Sweetviz

### Overview

This project explores the **New York City Airbnb Open Data** using the **Sweetviz** library for an automated Exploratory Data Analysis (AutoEDA). Sweetviz provides a highly visual and detailed report, making it easy to understand the dataset at a glance.

The goal of this project is to create an appealing and comprehensive AutoEDA that gives viewers quick insights into the dataset, covering descriptive statistics, feature correlations, and visual representations of the data distribution.

### Key Features
- **AutoEDA**: Automatically generated analysis using **Sweetviz**, providing a complete overview of the dataset.
- **Visual Summary**: The Sweetviz report includes visual summaries of all the dataset features, showing key statistics, missing data, and correlations.
- **Interactive Report**: The Sweetviz report is interactive, allowing viewers to explore the data visually with ease.

### AutoEDA Steps
- **Dataset Selection**: The dataset chosen for this analysis is the New York City Airbnb Open Data from Kaggle.
- **AutoEDA with Sweetviz**: Sweetviz automatically generates a detailed report, which includes:
  - Descriptive statistics for each column (mean, median, standard deviation, etc.).
  - Distribution plots for numerical features.
  - Correlations between features.
  - Identification of missing values.

### Installation and Setup

To run the AutoEDA using Sweetviz, follow the steps below:

1. Install the necessary Python packages:
   ```bash
   pip install sweetviz kaggle

## Project Files

- **`NYC_Airbnb_AutoEDA.html`**: The auto-generated Sweetviz report (to be pushed to the repository).
- **`kaggle.json`**: The Kaggle API key (not included in the repository for privacy reasons).
- **`AB_NYC_2019.csv`**: The dataset used for the analysis.
- **`README.md`**: This file.

## About the Dataset

The **New York City Airbnb Open Data** dataset includes information about Airbnb listings in New York City, including location, price, number of reviews, and availability. It provides valuable insights into the Airbnb market in one of the most popular cities in the world.

### Key columns in the dataset include:
- **Price**: The price of the Airbnb listing.
- **Neighborhood Group**: The borough of New York City where the listing is located.
- **Minimum Nights**: The minimum number of nights required for booking.
- **Availability**: The availability of the listing for booking over the next year.

---

## Conclusion

This project demonstrates how **Sweetviz** can automate the process of data exploration, providing detailed and visually appealing reports. It allows viewers to quickly understand the distribution, relationships, and missing values in the data, making it a powerful tool for exploratory data analysis.

