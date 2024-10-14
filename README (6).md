# Flipkart Live Data Product Recommendation System With Sentimental Analysis

## Overview

This project focuses on scraping product reviews from Flipkart, analyzing customer sentiment, and providing data-driven product recommendations. By utilizing natural language processing (NLP) techniques such as sentiment analysis, the project helps enhance the product recommendation engine based on customer reviews.


## Features

**Web Scraping:** Automated extraction of product reviews and ratings from Flipkart using Selenium and Beautiful Soup.

**Sentiment Analysis:** Utilizes TextBlob for analyzing the sentiment of reviews to gauge customer opinions.

**Product Recommendations:** Provides personalized product recommendations based on user input and sentiment analysis results.

**User-Friendly Interface:** Interactive Streamlit app for users to input their preferences and receive recommendations.

**Data Visualization:** Presents results in a visually appealing format with structured data display.



## Technologies Used

**List of libraries and tools used, including:**
- Python
- Selenium
- Beautiful Soup
- TextBlob
- LangChain
- Streamlit
- Pandas
## Screenshots

![Distribution of Ratings](https://github.com/user-attachments/assets/d446d7fb-64a6-4dfa-972e-5ae6444aa9ba)

![Price Distribution of Products](https://github.com/user-attachments/assets/a49e2b06-2c8d-4778-b4f2-a7e898557998)

![Top 10 Products by Avg Rating](https://github.com/user-attachments/assets/3a352530-2ba3-423e-ae81-8a490b2f049c)

![TextBlob Sentiment Score Distribution](https://github.com/user-attachments/assets/452af2f8-8d6b-4cf6-b2ee-3ea5d79b4be0)

![TextBlob Sentiment Distribution](https://github.com/user-attachments/assets/4d1de4e4-d9f0-46ef-89ce-07238ddabf63)

![1st](https://github.com/user-attachments/assets/db1989d5-a3cd-40fb-840a-338c48763fb6)

![2nd](https://github.com/user-attachments/assets/f248652c-bc96-4852-90ec-e810eca941c9)

![3rd](https://github.com/user-attachments/assets/75da12d2-34be-4513-94d4-962de2058e02)

![4th](https://github.com/user-attachments/assets/cb38b8b0-bf69-41b2-bd12-ff537ffaf24f)


## Future Improvements

**Enhanced Sentiment Analysis:**

- Implement more advanced sentiment analysis techniques using machine learning models (e.g., fine-tuning BERT or other transformer models) for improved accuracy.
- Incorporate emotion detection (e.g., joy, anger, sadness) to provide deeper insights into customer sentiments.

**Multi-Language Support:**

- Expand the project to support reviews in multiple languages, enhancing accessibility for users from different regions.
- Use translation APIs (e.g., Google Translate) to analyze sentiment across various languages.

**User Profile and Customization:**

- Create user profiles that save preferences and previous interactions to provide tailored recommendations over time.
- Allow users to specify parameters such as price range, brand preferences, and feature requirements.

**Data Visualization Enhancements:**

- Introduce interactive visualizations using libraries like Plotly or Matplotlib to showcase sentiment trends over time or compare different products visually.
- Provide dashboards summarizing user interactions, product ratings, and overall sentiment.

**Product Comparison Feature:**

- Implement a feature allowing users to compare multiple products side-by-side, including ratings, reviews, and sentiment scores.
- Enhance the UI to make it more user-friendly and visually appealing.

**Integration with Other E-Commerce Platforms:**

- Extend scraping capabilities to include other e-commerce platforms like Amazon or eBay for a broader product selection and recommendation base.
- Standardize the scraping process to accommodate varying HTML structures of different websites.

 **Feedback Loop for Recommendations:**

- Introduce a feedback mechanism where users can rate the accuracy of recommendations, allowing the model to learn and adapt over time.
- Utilize reinforcement learning techniques to continuously improve the recommendation algorithm based on user interactions.

**Performance Optimization:**

- Optimize the scraping process to reduce loading times and increase efficiency, such as implementing headless browsing or asynchronous scraping.
- Introduce error handling and retries for network issues to improve reliability during scraping.

**Deployment and Scaling:**

- Deploy the application on cloud platforms (e.g., AWS, Heroku) to make it accessible to a wider audience.
- Consider using containerization (e.g., Docker) for easier deployment and management of the application.

**Documentation and Tutorials:**

- Provide comprehensive documentation and tutorials for users on how to set up and use the application effectively.
- Include examples of different use cases to help users understand the full potential of the application.