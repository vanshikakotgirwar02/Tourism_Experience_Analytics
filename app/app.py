# Import required libraries

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configure the Streamlit page

st.set_page_config(
    page_title="Tourism Experience Analytics",
    page_icon="🌍",
    layout="wide"
)

# Main application title

st.title("🌍 Tourism Experience Analytics")

st.write(
    "Explore tourism trends, attraction ratings, "
    "popular destinations, and personalized attraction recommendations."
)

# Load the datasets

@st.cache_data
def load_data():
    
    features = pd.read_csv(
        "data/tourism_experience_features.csv"
    )
    
    recommendations = pd.read_csv(
        "data/attraction_recommendations.csv"
    )
    
    return features, recommendations


df, attraction_df = load_data()

st.success("Datasets loaded successfully!")

# Create sidebar navigation

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select a section:",
    [
        "Dashboard",
        "Rating Analysis",
        "Attraction Analysis",
        "Recommendations"
    ]
)

# Dashboard page

if page == "Dashboard":

    st.header("📊 Tourism Dashboard")

    # Calculate key metrics
    
    total_visits = len(df)
    
    total_attractions = df["Attraction"].nunique()
    
    total_cities = df["CityName"].nunique()
    
    average_rating = df["Rating"].mean()

    # Display metrics
    
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Visits",
        f"{total_visits:,}"
    )

    col2.metric(
        "Attractions",
        total_attractions
    )

    col3.metric(
        "Cities",
        total_cities
    )

    col4.metric(
        "Average Rating",
        f"{average_rating:.2f}"
    )

    st.subheader("📈 Visits Over Time")

    yearly_visits = (
        df.groupby("VisitYear")["TransactionId"]
        .count()
        .sort_index()
    )

    st.line_chart(yearly_visits)

    # Rating Analysis page

elif page == "Rating Analysis":

    st.header("⭐ Rating Analysis")

    rating_counts = (
        df["Rating"]
        .value_counts()
        .sort_index()
    )

    st.subheader("Rating Distribution")

    st.bar_chart(rating_counts)

    st.subheader("Average Rating")

    st.write(
        f"Overall average rating: "
        f"**{df['Rating'].mean():.2f}**"
    )

    # Rating category distribution
    
    if "RatingCategory" in df.columns:

        category_counts = (
            df["RatingCategory"]
            .value_counts()
        )

        st.subheader("Rating Categories")

        st.bar_chart(category_counts)

        # Attraction Analysis page

elif page == "Attraction Analysis":

    st.header("🏛️ Attraction Analysis")

    # Top attractions
    
    top_attractions = (
        df.groupby("Attraction")["TransactionId"]
        .count()
        .sort_values(ascending=False)
        .head(10)
    )

    st.subheader("Top 10 Most Visited Attractions")

    st.bar_chart(top_attractions)

    # Top cities
    
    top_cities = (
        df.groupby("CityName")["TransactionId"]
        .count()
        .sort_values(ascending=False)
        .head(10)
    )

    st.subheader("🌆 Top 10 Cities")

    st.bar_chart(top_cities)

    # Visit modes
    
    visit_modes = (
        df["VisitMode"]
        .value_counts()
    )

    st.subheader("👥 Visit Modes")

    st.bar_chart(visit_modes)

    # Recommendation page

elif page == "Recommendations":

    st.header("🧭 Attraction Recommendations")

    st.write(
        "Select a city to discover recommended attractions."
    )

    # Get available cities
    
    cities = sorted(
        attraction_df["CityName"]
        .dropna()
        .unique()
    )

    selected_city = st.selectbox(
        "Select a City",
        cities
    )

    # Number of recommendations
    
    top_n = st.slider(
        "Number of Recommendations",
        min_value=1,
        max_value=10,
        value=5
    )

    # Filter recommendations
    
    city_recommendations = attraction_df[
        attraction_df["CityName"] == selected_city
    ].head(top_n)

    st.subheader(
        f"Recommended Attractions in {selected_city}"
    )

    if len(city_recommendations) > 0:

        display_columns = [
            "Attraction",
            "Country",
            "AttractionType",
            "VisitCount",
            "AverageRating",
            "RecommendationScore"
        ]

        st.dataframe(
            city_recommendations[display_columns],
            use_container_width=True
        )

    else:

        st.warning(
            "No recommendations available for this city."
        )

        # Footer

st.sidebar.markdown("---")

st.sidebar.info(
    "Tourism Experience Analytics\n\n"
    "Built using Python, Pandas, "
    "Matplotlib, Seaborn and Streamlit."
)