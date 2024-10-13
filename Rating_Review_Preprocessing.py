import pandas as pd
import re
import spacy
import nltk
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.corpus import stopwords  # Import stopwords here

# Download NLTK resources if necessary
try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords')

# Load the spaCy English model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    import os
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Load the dataset
file_path = r'D:/Bala DS/Data science Class materials/Projects/P6_Final_Project/Project_Final/Dataset/Mobile_Phone_Data.csv'
try:
    df = pd.read_csv(file_path)
    print(f"Loaded dataset with {df.shape[0]} reviews.")
except Exception as e:
    print(f"Error loading the dataset: {e}")
    exit()  # Exit if dataset fails to load

# Assign 'product_id' as Product Name
df['product_id'] = df['Product Name']

# Remove rows with missing values in 'Review', 'Rating', and 'Price'
df.dropna(subset=['Review', 'Rating', 'Price'], inplace=True)

# Cleaning the Review Text
def clean_review(text):
    """Remove HTML tags, special characters, emojis, and convert to lowercase."""
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    # Remove emojis using regex
    text = re.sub(r'[^\x00-\x7F]+', '', text)  # Removes non-ASCII characters (including emojis)
    # Remove special characters, numbers (only keep alphabets)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Apply cleaning function to reviews
df['Cleaned_Review'] = df['Review'].apply(clean_review)

# Tokenization, stopword removal, and lemmatization
stop_words = set(stopwords.words('english'))

def tokenize_and_normalize(text):
    """Tokenize, remove stopwords, and apply lemmatization."""
    doc = nlp(text)  # Tokenize and lemmatize using spaCy
    # Remove stopwords, punctuation, and retain only alphabetic tokens
    words = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return ' '.join(words)

# Apply tokenization and normalization
df['Tokenized_Review'] = df['Cleaned_Review'].apply(tokenize_and_normalize)

# Convert 'Rating' to numeric and filter out invalid entries
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
df = df[df['Rating'].notnull()]

# Convert 'Price' to numeric (remove currency symbols and commas)
df['Price'] = df['Price'].apply(lambda x: re.sub(r'[^\d]', '', str(x)))  # Remove non-numeric characters
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')  # Convert to numeric

# Filter rows where the price is between ₹20,000 and ₹40,000
df = df[(df['Price'] >= 20000) & (df['Price'] <= 40000)]

# Drop duplicates if necessary
df.drop_duplicates(inplace=True)

# Remove the 'Product Link' column
df.drop(columns=['Product Link'], inplace=True)

# Save the cleaned and processed data to a new CSV file
output_path = 'D:/Bala DS/Data science Class materials/Projects/P6_Final_Project/Project_Final/Processed_Mobile_Phone_Data.csv'
df.to_csv(output_path, index=False)
print(f"Processed data saved to {output_path}.")

# Display the first few rows of the cleaned data
print(df.head())

# Plot Rating Distribution
plt.figure(figsize=(10, 6))
sns.countplot(x='Rating', data=df, palette='viridis')
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Number of Reviews')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Plot Price Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Price'], bins=30, kde=True, color='skyblue')
plt.title('Price Distribution of Products')
plt.xlabel('Price (₹)')
plt.ylabel('Number of Products')
plt.grid(axis='y')
plt.show()

# Calculate average rating for each product
avg_rating = df.groupby('product_id').agg(Avg_Rating=('Rating', 'mean')).reset_index()

# Get the top 10 products by average rating
top_n = avg_rating.sort_values(by='Avg_Rating', ascending=False).head(10)

# Horizontal Bar Plot for Top N Products
plt.figure(figsize=(10, 6))
sns.barplot(x='Avg_Rating', y='product_id', data=top_n, palette='coolwarm')
plt.title('Top 10 Products by Average Rating')
plt.xlabel('Average Rating')
plt.ylabel('Product ID')
plt.grid(axis='x')
plt.show()
