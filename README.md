# TellCo Analysis Project

## Project Overview

This project involves a detailed analysis of TellCo, a mobile service provider in the Republic of Pefkakia. The goal is to assess its suitability for acquisition by a wealthy investor by focusing on user behavior, engagement, experience, and satisfaction to identify opportunities for growth and profitability.

## Project Objectives

1. **User Overview Analysis**
2. **User Engagement Analysis**
3. **User Experience Analysis**
4. **Satisfaction Analysis**

## Detailed Tasks

### Task 1: User Overview Analysis

**1.1 Aggregate user data**
- Aggregate xDR sessions, session duration, download (DL) and upload (UL) data, and total data volume per user.

**1.2 Exploratory Data Analysis**
- **Variable Descriptions**: Describe all relevant variables and their data types.
- **Variable Transformations**: Segment users into decile classes based on session duration and compute total data per decile class.
- **Univariate Analysis**: Compute dispersion parameters (mean, median, etc.) and perform graphical analysis.
- **Bivariate Analysis**: Explore relationships between applications and total DL+UL data.
- **Correlation Analysis**: Compute and interpret a correlation matrix for various data types (e.g., Social Media, Google, Email, YouTube, Netflix, Gaming, and Others).
- **Principal Component Analysis (PCA)**: Reduce data dimensions and interpret results.

### Task 2: User Engagement Analysis

**2.1 Aggregate and Normalize Engagement Metrics**
- Aggregate session frequency, session duration, and total traffic per customer ID.
- Normalize metrics and perform k-means clustering (k=3) to classify customers.
- Compute non-normalized metrics per cluster and visualize results.

**2.2 Analyze Top Users and Applications**
- Derive the top 10 most engaged users and the top 3 most used applications.
- Optimize k for clustering using the elbow method and interpret findings.

### Task 3: Experience Analytics

**3.1 Aggregate Experience Metrics**
- Aggregate average TCP retransmission, RTT, handset type, and throughput per customer.

**3.2 Analyze Network Parameters**
- List and analyze top, bottom, and most frequent TCP, RTT, and throughput values.

**3.3 Analyze Experience by Handset Type**
- Analyze the distribution of throughput and TCP retransmission by handset type.

**3.4 Experience Clustering**
- Perform k-means clustering (k=3) on experience metrics and provide a description for each cluster.

### Task 4: Satisfaction Analysis

**4.1 Compute Scores**
- Calculate engagement and experience scores using Euclidean distance.
  
**4.2 Calculate Satisfaction Scores**
- Compute the average of engagement and experience scores to determine satisfaction scores. Report the top 10 satisfied customers.

**4.3 Regression Model**
- Build and evaluate a regression model to predict satisfaction scores.

**4.4 Satisfaction Clustering**
- Perform k-means clustering (k=2) on satisfaction scores.

**4.5 Aggregate Scores per Cluster**
- Aggregate average satisfaction and experience scores per cluster.

**4.6 Export to MySQL**
- Export final user data including IDs, engagement, experience, and satisfaction scores to a MySQL database. Provide a screenshot of a select query output.

**4.7 Model Deployment and Monitoring**
- Deploy the model using Docker or MLFlow. Track model changes including code version, start and end times, source, parameters, metrics, and artifacts. Provide a report with code version, metrics, and artifacts.

### Task 5: Dashboard Development

**Design and Develop Dashboard**
- Create a web-based dashboard using Streamlit.
- Separate each page by task title (e.g., User Overview Analysis, User Engagement Analysis, Experience Analysis, Satisfaction Analysis).
- Add relevant plots for each page to visualize data insights.

