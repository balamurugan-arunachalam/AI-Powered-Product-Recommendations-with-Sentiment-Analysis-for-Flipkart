import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Function to scrape product details
def scrape_product_details(product_link):
    # Load the product link in the current tab
    driver.get(product_link)  # Load the product link in the current tab
    driver.refresh()  # Refresh the page to ensure it loads properly

    # Get page source and parse with Beautiful Soup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Scrape the product name
    try:
        product_name = soup.select_one("h1._6EBuvT").get_text(strip=True)
        print(f'Product Name: {product_name}')
    except Exception as e:
        print("Could not find the product name.")
        product_name = "N/A"

    # Scrape the product price
    try:
        price = soup.select_one("div.Nx9bqj.CxhGGd").get_text(strip=True)
        print(f'Product Price: {price}')
    except Exception as e:
        print("Could not find the product price.")
        price = "N/A"

    # Click the 'All Reviews' section
    try:
        all_reviews_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div._23J90q.RcXBOT"))
        )
        all_reviews_button.click()
    except Exception as e:
        print("Could not find or click on the 'All Reviews' button.")
        return []

    # Wait for reviews to load
    time.sleep(5)  # Adjust this time if needed

    # List to store scraped review data
    review_data = []

    # Scrape ratings and reviews across multiple pages
    page_count = 0
    max_pages = 25  # Set a maximum number of pages to prevent infinite loops

    while page_count < max_pages:
        time.sleep(5)  # Allow time for reviews to load

        # Scrape ratings and reviews
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        ratings = soup.select("div.XQDdHH.Ga3i8K")
        reviews = driver.find_elements(By.CSS_SELECTOR, "div.ZmyHeo")

        if not ratings or not reviews:
            print("No ratings or reviews found. Exiting...")
            break

        # Iterate over each review and handle the 'Read More' button
        for rating, review in zip(ratings, reviews):
            try:
                # Check for the 'Read More' button
                read_more_button = review.find_element(By.CSS_SELECTOR, "span.b4x-fr")
                if read_more_button:
                    driver.execute_script("arguments[0].click();", read_more_button)
                    time.sleep(1)  # Allow time for the review to expand

                # Scrape the full review text and format it
                full_review_text = review.text.replace('\n', ' ').replace('\r', '').strip()
            except Exception:
                # If no 'Read More' button is found, just get the text directly and format it
                full_review_text = review.text.replace('\n', ' ').replace('\r', '').strip()

            print(f'Rating: {rating.text}, Review: {full_review_text}')
            review_data.append([product_link, product_name, price, rating.text, full_review_text])

        # Check for the next button and move to the next page if available
        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Next')]"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
            time.sleep(1)  # Allow some time for scrolling
            driver.execute_script("arguments[0].click();", next_button)
            time.sleep(5)  # Wait for the next page to load
            page_count += 1  # Increment the page count
        except Exception as e:
            print("No more pages or an error occurred:", e)
            break

    return review_data  # Return the collected review data

# Initialize Chrome driver
driver = webdriver.Chrome()

# Read product links from the CSV file
input_csv_file_path = "D:/Bala DS/Data science Class materials/Projects/P6_Final_Project/Project_Final/Cleaned_Phone_Links.csv"
product_links = []

with open(input_csv_file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        product_links.append(row['Product Link'])  # Extracting the 'Product Link' column

# Prepare to save data into a new CSV file
output_csv_file_path = "D:/Bala DS/Data science Class materials/Projects/P6_Final_Project/Project_Final/Mobile_Phone_Data.csv"
with open(output_csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write headers to the output CSV file
    writer.writerow(["Product Link", "Product Name", "Price", "Rating", "Review"])

# Loop through each product link and scrape details
for link in product_links:
    review_data = scrape_product_details(link)  # Call the scrape function
    if review_data:  # Only save if there's data to save
        # Save scraped data into the CSV file
        with open(output_csv_file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(review_data)  # Write all review data for this product

    # Reuse the same tab for the next product
    driver.get("about:blank")  # Clear the page before loading the next URL

# Quit the browser after all reviews have been scraped
driver.quit()
