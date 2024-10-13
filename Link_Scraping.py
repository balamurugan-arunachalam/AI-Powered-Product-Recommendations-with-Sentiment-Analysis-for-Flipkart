import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to scrape reviews for a given mobile brand and item
def scrape_reviews(brand_xpath):
    # Open Flipkart URL
    driver.get(url)

    # Close the login popup if it appears
    try:
        close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'✕')]"))
        )
        close_button.click()
    except Exception:
        pass  # Login popup not found or already closed.

    # Locate the filter section
    try:
        filter_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[1]'))
        )
    except Exception:
        pass  # Filter section not found.

    # Click on the mobile brand
    try:
        # Wait for the mobile brand element to be located
        mobile_brand = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, brand_xpath))
        )
        mobile_brand.click()
        time.sleep(10)  # Wait for the page to reload if the click is successful
    except Exception:
        return  # Exit the function if we cannot click the brand

    # Click the minimum price dropdown
    try:
        min_price = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[2]/div[4]/div[1]'))
        )
        min_price.click()

        # Select the 20,000 option from the dropdown
        min_price_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div/div[3]/div/div[1]/div/div[1]/div/section[2]/div[4]/div[1]/select/option[4]'))
        )
        min_price_option.click()
        time.sleep(1)  # Allow time for the selection to process
    except Exception:
        pass  # Could not select minimum price.

    # Scroll down to make sure the brand element is visible
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)  # Allow time for the page to load

    # Scroll back up to the top
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)  # Allow time for the scroll action to complete

    # Initialize an empty list to store product details
    product_details = []

    # Scrape product links, names, and prices from the current page and iterate through pagination
    while True:
        time.sleep(3)  # Allow time for page to load

        # Scrape phone links, names, and prices
        try:
            # Locate the div elements that contain product links
            product_divs = driver.find_elements(By.CSS_SELECTOR, "div._75nlfW")
            product_names = driver.find_elements(By.CSS_SELECTOR, "div.KzDlHZ")
            product_prices = driver.find_elements(By.CSS_SELECTOR, "div.Nx9bqj._4b5DiR")

            # Iterate over product divs and scrape details
            for i in range(len(product_divs)):
                try:
                    # Get the product link
                    link = product_divs[i].find_element(By.TAG_NAME, "a").get_attribute('href')

                    # Get the product name
                    name = product_names[i].text if i < len(product_names) else "N/A"

                    # Get the product price
                    price = product_prices[i].text if i < len(product_prices) else "N/A"

                    # Print scraped details
                    print(f'Product Link: {link}, Product Name: {name}, Price: {price}')

                    # Append the details to the product list
                    product_details.append([link, name, price])

                except Exception:
                    pass  # Error extracting product details, skip this product

            # Click the 'Next' button to go to the next page, if available
            try:
                next_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Next')]"))
                )
                driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
                time.sleep(1)
                next_button.click()
                time.sleep(3)  # Wait for the next page to load
            except Exception:
                break  # No more pages or an error occurred

        except Exception:
            break  # Could not find phones or scrape links

    return product_details  # Return the scraped product details


# Initialize Chrome driver
driver = webdriver.Chrome()

# Open Flipkart URL
url = "https://www.flipkart.com/search?q=mobile+phones+&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY"
driver.get(url)

# List of mobile brands and their respective XPaths
brands = {
    "Samsung": {
        "brand_xpath": '//*[@id="container"]/div/div[3]/div/div[1]/div/div[1]/div/section[3]/div[2]/div[1]/div[3]',
    },

    "Google": {
        "brand_xpath": '//*[@id="container"]/div/div[3]/div/div[1]/div/div[1]/div/section[3]/div[2]/div[1]/div[4]',
    },

    "Motorola": {
        "brand_xpath": '//*[@id="container"]/div/div[3]/div/div[1]/div/div[1]/div/section[3]/div[2]/div[1]/div[5]',
    },

    "Vivo": {
        "brand_xpath": '//*[@id="container"]/div/div[3]/div/div[1]/div/div[1]/div/section[3]/div[2]/div[1]/div[6]',
    },

    "Oppo": {
        "brand_xpath": '//*[@id="container"]/div/div[3]/div/div[1]/div/div[1]/div/section[3]/div[2]/div[1]/div[7]',
    }
}

# Prepare the CSV file for writing data
csv_file_path = "D:/Bala DS/Data science Class materials/Projects/P6_Final_Project/Project_Final/phone_links.csv"
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Product Link", "Product Name", "Price"])  # Write headers

    # Iterate over each brand and scrape reviews
    for brand, xpaths in brands.items():
        print(f"Scraping reviews for {brand}...")
        product_details = scrape_reviews(xpaths["brand_xpath"])
        writer.writerows(product_details)  # Write all product details to the CSV after scraping each brand

# Close the browser
driver.quit()
