import pandas as pd

# Load the dataset
file_path = "D:/Bala DS/Data science Class materials/Projects/P6_Final_Project/Project_Final/phone_links.csv"
df = pd.read_csv(file_path)

# Display original data shape
print(f"Original dataset size: {df.shape}")

# Remove duplicates
df = df.drop_duplicates()

# Clean the 'Price' column by removing currency symbol '₹' and commas, and then convert to float
df['Price'] = df['Price'].str.replace('₹', '').str.replace(',', '').str.strip().astype(float)

# Remove rows with price greater than 40000
df = df[(df['Price'] >= 20000) & (df['Price'] <= 40000)]

# Remove rows where the 'Product Link' contains the word 'refurbished'
df = df[~df['Product Link'].str.contains("refurbished", case=False)]

# Display cleaned data shape
print(f"Cleaned dataset size: {df.shape}")

# Save the cleaned dataset to a new CSV file
output_file_path = "D:/Bala DS/Data science Class materials/Projects/P6_Final_Project/Project_Final/Cleaned_Phone_Links.csv"
df.to_csv(output_file_path, index=False)

print(f"Cleaned dataset saved to {output_file_path}")
