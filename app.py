import streamlit as st
import pandas as pd
from langchain_community.llms import Cohere
import cohere
import os

# Set page config (must be the first Streamlit command)
st.set_page_config(page_title="Product Recommendation", layout="centered")

# Load sentiment data
sentiment_data = pd.read_csv("D:/Bala DS/Data science Class materials/Projects/P6_Final_Project/Project_Final/FlipKart_Dataset_with_Sentiment_Analysis.csv")

# Initialize Cohere (Replace with your Cohere API Key)
cohere_api_key = 'LGqaNW3Tfcdb3A1rhmd3NOZI5jMsbpLJlnjS4ZsW'
co = cohere.Client(cohere_api_key)

# Function to recommend products based on user query
def recommend_products(query, sentiment_data):
    try:
        # Analyze the user's input using Cohere
        response = co.generate(prompt=query, model='command-xlarge-nightly')

        # Process response (you can also use a custom NLP method if needed)
        search_keywords = response.generations[0].text.strip().split()

        # Filter sentiment data based on query analysis (e.g., find related product names or positive reviews)
        recommendations = sentiment_data[sentiment_data['Cleaned_Review'].str.contains('|'.join(search_keywords), case=False)]

        # Sort products by sentiment score
        recommendations = recommendations.sort_values(by='TextBlob_Sentiment_Score', ascending=False)

        # Return top 5 products (Name and Price only)
        return recommendations[['Product Name', 'Price']].head(5)
    except Exception as e:
        st.error(f"An error occurred while processing your request: {e}")
        return pd.DataFrame()

# Streamlit App Interface
st.markdown("<h1 style='text-align: center; color: #800080;'>📱AI-Powered-Product-Recommendations-with-Sentiment-Analysis-for-Flipkart📱</h1>", unsafe_allow_html=True)

# Add a relevant phone banner image for better UI
st.image("https://i0.wp.com/www.smartprix.com/bytes/wp-content/uploads/2020/03/wallpapers-e1585151078813.jpg", use_column_width=True)
# User input section with styled markdown
st.markdown("<h4 style='color: #800000;'>📝To receive the top phone recommendations, please input your preferences:📝</h4>", unsafe_allow_html=True)  # Maroon color
st.markdown("<p style='color: #FF4500;'>For example: <b>best camera phone</b>, <b>lightweight</b>, <b>long battery life</b>, etc.</p>", unsafe_allow_html=True)  # Linen color

# Create a container for input elements
with st.container():
    query = st.text_area("Describe what you want:", height=100)
    recommend_button = st.button("🔍 Suggestion")

# Validate input and show recommendations when the button is clicked
if recommend_button:
    if len(query.strip()) == 0:
        st.warning("Please enter a valid query.")
    else:
        with st.spinner("Fetching recommendations..."):
            recommended_products = recommend_products(query, sentiment_data)
        
        if not recommended_products.empty:
            st.markdown("<h3 style='color: #32CD32;'>🎊🎁Here are the top 5 phones that we Suggested:🎊🎁</h3>", unsafe_allow_html=True)

            # Display product name and price with colored text in a structured format
            for idx, row in recommended_products.iterrows():
                st.markdown(f"<div style='border: 1px solid #00BFFF; border-radius: 10px; padding: 10px; margin: 10px 0; background-color: #1E1E1E;'><p style='font-size:18px; color:#FFFFFF;'><b>{row['Product Name']}</b> - <span style='color:#FF4500;'>₹{row['Price']}</span></p></div>", unsafe_allow_html=True)
        else:
            st.warning("No matching products found. Please try a different query.")

# Add the new footer with your name
st.markdown("<p style='text-align: center; font-size:14px; color:gray;'>System Created by <b>Balamurugan Arunachalam</b></p>", unsafe_allow_html=True)