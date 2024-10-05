# ApacheBeam-Data-Engineering

## Assignment 1: World Happiness Report 2019 - Advanced EDA with D3.js Visualizations

a) Assignment 1 is to do a complete dataset EDA in colab (preferably using D3.js visualizations)
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
<img width="899" alt="Screenshot 2024-10-04 at 2 35 54 PM" src="https://github.com/user-attachments/assets/d433ce7a-f2d4-4082-bc57-35825af3957f">
<img width="899" alt="Screenshot 2024-10-04 at 2 36 09 PM" src="https://github.com/user-attachments/assets/67d3ad85-be2b-4705-935a-b4ba07702949">
<img width="899" alt="Screenshot 2024-10-04 at 2 36 24 PM" src="https://github.com/user-attachments/assets/a7e2a825-2c16-4842-ad7b-8cee046bd4c7">
<img width="676" alt="Screenshot 2024-10-04 at 2 36 48 PM" src="https://github.com/user-attachments/assets/2d9772e6-6c46-4238-a868-460b570171ed">
<img width="411" alt="Screenshot 2024-10-04 at 2 37 51 PM" src="https://github.com/user-attachments/assets/2fbc467d-b87b-47e0-8a46-749154f564e8">
<img width="411" alt="Screenshot 2024-10-04 at 2 38 08 PM" src="https://github.com/user-attachments/assets/9afc8b86-a8f8-4c7b-808b-1c823765fde3">
<img width="410" alt="Screenshot 2024-10-04 at 2 38 37 PM" src="https://github.com/user-attachments/assets/4e3e802b-a246-44fc-a171-6be1d9c28d50">
<img width="601" alt="Screenshot 2024-10-04 at 2 38 51 PM" src="https://github.com/user-attachments/assets/9b682a37-9850-4396-8194-8ff50654e3ad">


---

## Conclusion

This project demonstrates how advanced **D3.js** visualizations can enhance the exploratory data analysis process, providing interactive and visually appealing insights into the happiness levels of countries worldwide. It bridges the gap between traditional static plots and modern, dynamic data visualization techniques.


## Assignment 2: NYC Airbnb Open Data - Auto EDA with Sweetviz
b) Assignment 2 - Auto EDA with your favorite tool
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

<img width="938" alt="Screenshot 2024-10-04 at 2 35 00 PM" src="https://github.com/user-attachments/assets/52476563-71fb-4f33-97c7-cbdeecf7eee7">
<img width="938" alt="Screenshot 2024-10-04 at 2 35 13 PM" src="https://github.com/user-attachments/assets/77163220-fb94-4e60-9a6f-e7bdcaee09dd">

---
## Conclusion

This project demonstrates how **Sweetviz** can automate the process of data exploration, providing detailed and visually appealing reports. It allows viewers to quickly understand the distribution, relationships, and missing values in the data, making it a powerful tool for exploratory data analysis.



## Assignment 3: Apache Beam Kafka Streaming Pipeline: Data Engineering Assignment

c) Assignment 3 - Apache beam features - demonstrate apache beam in a colab including composite transform, pipeline io, triggers, windowing ,pardo and streaming

## Prerequisites
Before getting started, ensure that you have the following installed:
- [Java JDK 8+](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html)
- [Apache Kafka](https://kafka.apache.org/downloads) (Kafka 2.12 or later)
- Python 3.7+
- [Apache Beam](https://beam.apache.org/get-started/quickstart-py/)

## Setting Up Kafka
1. **Download and Extract Kafka**:
   - Download Kafka from the [official site](https://kafka.apache.org/downloads).
   - Extract the Kafka archive.
2. **Start Zookeeper**:
   Zookeeper is required for managing Kafka brokers. Run the following command in the Kafka installation directory:

   ```bash
   bin/zookeeper-server-start.sh config/zookeeper.properties
   ```
## Code Summary

This pipeline reads messages from a Kafka input topic, processes each message by decoding the byte arrays into UTF-8 strings, and writes the processed messages to a Kafka output topic. It utilizes Apache Beam’s streaming mode for continuous data processing and Kafka for message ingestion and output. The pipeline is configured to run in real-time and handles both message consumption and production.

colab code -> 


## Key Concepts

- **Composite Transform**: A combination of multiple transforms bundled together to perform complex data processing tasks in a modular way.
- **Pipeline IO**: Input and output operations in a pipeline, allowing data to be read from or written to external systems like Kafka, databases, or file systems.
- **Triggers**: Mechanisms that control when windowed results are emitted, based on event time, processing time, or data completeness.
- **Windowing**: Organizes data into logical windows for aggregation in streaming pipelines, allowing efficient processing of unbounded data.
- **ParDo**: A parallel processing transform that applies a user-defined function (DoFn) to each element in a PCollection.
- **Streaming**: Continuous processing of unbounded data streams in real-time, rather than processing a finite dataset.

## Conclusion

This project demonstrates the use of Apache Beam with Kafka for real-time data streaming and processing. By leveraging key features such as composite transforms, windowing, and triggers, the pipeline efficiently handles unbounded data streams in a scalable and fault-tolerant manner. This setup provides a solid foundation for building advanced streaming applications capable of processing data in real-time, making it ideal for scenarios like log processing, IoT data ingestion, or event-driven architectures.
