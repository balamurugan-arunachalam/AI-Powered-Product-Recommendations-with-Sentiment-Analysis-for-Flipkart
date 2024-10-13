import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

# Load the preprocessed dataset
file_path = 'D:/Bala DS/Data science Class materials/Projects/P6_Final_Project/Project_Final/Processed_Mobile_Phone_Data01.csv'
df = pd.read_csv(file_path)

# TextBlob Sentiment Analysis Function
def get_textblob_sentiment(text):
    """Determine sentiment polarity using TextBlob."""
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity  # Polarity score (-1 to 1)

    # Categorize based on polarity thresholds
    if polarity > 0.5:
        sentiment = 'Strongly Positive'
    elif 0 < polarity <= 0.5:
        sentiment = 'Positive'
    elif polarity == 0:
        sentiment = 'Neutral'
    elif -0.5 <= polarity < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Strongly Negative'

    return polarity, sentiment

# Apply TextBlob sentiment analysis
df['TextBlob_Sentiment_Score'], df['TextBlob_Sentiment'] = zip(*df['Cleaned_Review'].apply(get_textblob_sentiment))

# Save the updated DataFrame with TextBlob sentiment analysis
output_path = 'D:/Bala DS/Data science Class materials/Projects/P6_Final_Project/Project_Final/FlipKart_Dataset_with_Sentiment_Analysis.csv'
df.to_csv(output_path, index=False)
print(f"Sentiment analysis results with TextBlob saved to {output_path}.")

# Display the first few rows with sentiment analysis
print(df[['Product Name', 'Cleaned_Review', 'TextBlob_Sentiment', 'TextBlob_Sentiment_Score']].head())

# Visualization: TextBlob Sentiment Distribution
plt.figure(figsize=(10, 5))
sns.countplot(x='TextBlob_Sentiment', data=df, palette='pastel',
              order=['Strongly Positive', 'Positive', 'Neutral', 'Negative', 'Strongly Negative'])
plt.title('TextBlob Sentiment Distribution')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Histogram of TextBlob Sentiment Scores
plt.figure(figsize=(10, 5))
sns.histplot(df['TextBlob_Sentiment_Score'], bins=30, kde=True, color='blue')
plt.title('TextBlob Sentiment Score Distribution')
plt.xlabel('Sentiment Score (Polarity)')
plt.ylabel('Number of Reviews')
plt.grid(axis='y')
plt.show()

# Aggregation: Average Sentiment Score by Product
product_sentiment_summary = df.groupby('Product Name').agg(
    avg_textblob_sentiment_score=('TextBlob_Sentiment_Score', 'mean'),
    total_textblob_positive_reviews=('TextBlob_Sentiment', lambda x: (x == 'Positive').sum()),
    total_reviews=('TextBlob_Sentiment', 'count')  # Using TextBlob_Sentiment for review count
).sort_values(by='avg_textblob_sentiment_score', ascending=False)

# Show the top 5 products based on TextBlob average sentiment score
print("Top 5 Products Based on TextBlob Sentiment Analysis:")
print(product_sentiment_summary.head())

# Save the product sentiment summary for future use in recommendation systems
summary_output_path = 'D:/Bala DS/Data science Class materials/Projects/P6_Final_Project/Project_Final/Product_Sentiment_Summary_TextBlob.csv'
product_sentiment_summary.to_csv(summary_output_path)
print(f"Product sentiment summary saved to {summary_output_path}.")
