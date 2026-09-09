# 🌍 Tourism Experience Analytics

## 📌 Project Overview

Tourism Experience Analytics is a data analytics and recommendation project that analyzes tourism visit data to understand visitor behavior, attraction popularity, ratings, visit patterns, and popular destinations.

The project combines data exploration, preprocessing, feature engineering, visualization, and a recommendation system into an interactive Streamlit dashboard.

---

## 🎯 Objectives

The main objectives of this project are:

- Analyze tourism visit patterns
- Identify the most popular attractions
- Identify popular cities and countries
- Analyze tourist ratings
- Understand different visit modes
- Analyze tourism trends over time
- Compare attraction popularity with ratings
- Recommend popular attractions based on popularity and ratings
- Provide an interactive dashboard for tourism analysis

---

## 📊 Datasets

The project uses multiple related tourism datasets containing information about:

- Users
- Attractions
- Attraction types
- Cities
- Countries
- Regions
- Continents
- Visit modes
- Transactions and ratings

The datasets were combined during the preprocessing stage to create a unified tourism dataset.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- SciPy
- OpenPyXL
- Streamlit
- Jupyter Notebook

---

## 🔄 Project Workflow

The project was developed through the following stages:

### 1. Data Exploration

Explored the individual datasets and examined:

- Dataset dimensions
- Columns and data types
- Missing values
- Duplicate records
- Categorical variables
- Ratings
- Attractions
- User activity
- Tourism trends

### 2. Data Preprocessing

The datasets were cleaned and combined using common IDs.

Major preprocessing tasks included:

- Handling missing values
- Standardizing ID data types
- Validating IDs
- Merging related datasets
- Removing unnecessary columns
- Renaming columns
- Creating useful date and rating-related columns

### 3. Feature Engineering

Additional features were created to improve tourism analysis and recommendations, including:

- User Visit Count
- Attraction Visit Count
- Attraction Average Rating
- Attraction Popularity
- Rating Score
- Visit Year Group
- User Average Rating
- City Visit Count

### 4. Analysis & Visualization

The project analyzes:

- Rating distribution
- Top attractions
- Top cities
- Top countries
- Visit modes
- Tourism visits over time
- Attraction popularity versus average rating

### 5. Recommendation System

A popularity-based recommendation system was developed.

The recommendation score combines:

- Attraction popularity
- Attraction average rating

The system can provide:

- General attraction recommendations
- City-based attraction recommendations

### 6. Streamlit Dashboard

An interactive Streamlit application was developed with four main sections:

- 📊 Dashboard
- ⭐ Rating Analysis
- 🏛️ Attraction Analysis
- 🧭 Recommendations

---

## 📁 Project Structure

```text
Tourism_Experience_Analytics/
│
├── app/
│   └── app.py
│
├── data/
│   ├── tourism_experience_processed.csv
│   ├── tourism_experience_features.csv
│   └── attraction_recommendations.csv
│
├── models/
│
├── notebooks/
│   ├── 01_Data_Exploration.ipynb
│   ├── 02_Data_Preprocessing.ipynb
│   ├── 03_Feature_Engineering.ipynb
│   ├── 04_Analysis_and_Visualization.ipynb
│   └── 05_Recommendation_System.ipynb
│
├── reports/
│
├── src/
│
├── .gitignore
├── README.md
└── requirements.txt