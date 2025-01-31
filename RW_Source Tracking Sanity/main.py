import csv
from playwright.sync_api import sync_playwright

CSV_FILE = "form_data.csv"  # Update with your actual CSV file path

def fill_form(page, data):
    """Open LP URL, fill, and submit the form using Playwright"""
    lp_url = data["lp_url"]  # Read LP URL from CSV
    page.goto(lp_url)  # Open the landing page

    # Fill the form fields
    page.fill("input[name='Email']", data["email"])
    page.fill("input[name='FirstName']", data["firstName"])
    page.fill("input[name='LastName']", data["lastName"])
    page.fill("input[name='Company']", data["company"])
    page.fill("input[name='Title']", data["jobTitle"])
    page.select_option("select[name='Country']", data["country"])  # Dropdown example

    # Submit the form
    page.click("button[type='submit']")  # Adjust the selector if needed
    page.wait_for_timeout(2000)  # Wait for form submission

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set headless=True for silent execution
        page = browser.new_page()

        # Read the CSV file and process each row
        with open(CSV_FILE, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                fill_form(page, row)  # Submit form for each LP URL

        browser.close()

if __name__ == "__main__":
    main()
