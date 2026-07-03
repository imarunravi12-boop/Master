from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
from collections import Counter

# 1.You are automating a test where clicking a "Download" button opens a new window. How would you handle pop-up windows in Selenium?
driver = webdriver.Chrome()
driver.get("https://example.com")

# Step 1: Store main window handle
main_window = driver.current_window_handle

# Step 2: Click on the "Download" button
driver.find_element(By.ID, "downloadBtn").click()

# Step 3: Wait and switch to new window
for handle in driver.window_handles:
    if handle != main_window:
        driver.switch_to.window(handle)
        break

# Step 4: Do actions in pop-up window
print("Pop-up window title:", driver.title)

# Step 5: Close pop-up and return to main window
driver.close()
driver.switch_to.window(main_window)
driver.quit()

# 2.Simple Google Search Using Selenium
# Step 1: Launch browser
driver = webdriver.Chrome()

# Step 2: Open Google
driver.get("https://www.google.com")

# Step 3: Find the search box and enter text
driver.find_element(By.NAME, "q").send_keys("Selenium Python")

# Step 4: Submit the search form
driver.find_element(By.NAME, "q").submit()

# Step 5: Wait and close
time.sleep(5)
driver.quit()

# 3.Basic Login Example (dummy site)
driver = webdriver.Chrome()
driver.get("https://example.com/login")  # Replace with real login URL

# Fill username and password fields
driver.find_element(By.ID, "username").send_keys("your_username")
driver.find_element(By.ID, "password").send_keys("your_password")

# Click login button
driver.find_element(By.ID, "loginButton").click()

# Wait and close
time.sleep(5)
driver.quit()

# 4.Ecommerce website - search - cake
# list of product on webpage -- cake

driver = webdriver. Chrome()
driver.get("https://amazon.com")

# check if specific text present
if "Example cake " in driver.page_source:
    print("text found")
else:
    print("text not found")

driver.quit()

# 1.What are the different types of waits in Selenium? Explain with examples
# 1.Implicit Wait:

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear

driver.get("https://example.com")
driver.find_element("id", "username").send_keys("admin")

# 2.Explicit Wait:
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "username")))
element.send_keys("admin")

# 2.What is the difference between find_element() and find_elements() in Selenium?
# find_element()
element = driver.find_element(By.ID, "username")
element.send_keys("admin")

# find_elements()
elements = driver.find_elements(By.TAG_NAME, "input")
print(f"Total inputs: {len(elements)}")

# 3.You have an Excel sheet that contains more than 100 sets of login credentials — each row has a Username and Password.
# You need to read all data from the Excel file and perform login testing in a web application using Python Selenium?

# Step 1: Load the Excel file

workbook = load_workbook("credentials.xlsx")
sheet = workbook.active  # or workbook['Sheet1'] if named

# Step 2: Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Step 3: Loop through Excel rows
for row in range(2, sheet.max_row + 1):  # skipping header row
    username = sheet.cell(row=row, column=1).value
    password = sheet.cell(row=row, column=2).value
    print(f"Testing with Username: {username}, Password: {password}")

    # Step 4: Navigate to login page
    driver.get("https://example.com/login")  # <-- Replace with your app URL
    time.sleep(1)

    # Step 5: Enter username & password
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)

    # Step 6: Click login button
    driver.find_element(By.ID, "loginBtn").click()
    time.sleep(2)

    # Step 7: Validation (simple example)
    if "dashboard" in driver.current_url.lower():
        print(f"✅ Login success for user: {username}")
    else:
        print(f"❌ Login failed for user: {username}")

    # Step 8: Logout if necessary (optional)
    # driver.find_element(By.ID, "logoutBtn").click()

# Step 9: Close the browser
driver.quit()

# 4. How do you handle dropdowns in Selenium? Provide a code example using Python.

# Step 1: Launch browser
driver = webdriver.Chrome()
driver.get("https://example.com/dropdown")

# Step 2: Locate dropdown and create Select object
dropdown = Select(driver.find_element(By.ID,"country"))

# Step 3: Select option by visible text
dropdown.select_by_visible_text("India")

time.sleep(5)
driver.quit()

# 5. How can you take a screenshot of a webpage using Selenium in Python? Provide a code example.
# Step 1: Launch browser
driver = webdriver.Chrome()
driver.get("https://example.com")
# Step 2: Take screenshot
driver.save_screenshot("screenshot.png")  # Saves screenshot in current directory
# Step 3: Close browser
driver.quit()

# 6.How do you handle multiple windows?

# Step 1: Launch browser
driver = webdriver.Chrome()
driver.get("https://google.com")

# step 2: Store main window handle
parent = driver.current_window_handle

for handle in driver.window_handles:
    if handle != parent:
        driver.switch_to.window(handle)

driver.close()
driver.switch_to.window(parent)

# 7.How do handle iframes in Selenium? Provide a code example using Python.

# Step 1: Launch Browser
driver = webdriver.Chrome()
driver.get("https://example.com/iframepage")

# Step 2: Switch to iframe by ID or Name
iframe = driver.find_element(By.XPATH,"//iframe=[@id='iframe']")
driver.switch_to.frame(iframe)

# Step 3: Perform actions inside iframe
driver.find_element(By.ID, "insideIframeElement").click()

# Step 4: Switch back to main content
driver.switch_to.default_content()

# Step 5:Close browser
driver.quit()


# 8.How to handle alerts and pop-ups in Selenium? Provide a code example using Python.

# Step 1: Launch Browser
driver = webdriver.Chrome()
driver.get("https://example.com/alertpage")

# Step 2: Trigger alert
driver.find_element(By.ID,"alertButton").click()

# Step 3: Switch to alert
alert = driver.switch_to.alert
print(alert.text)  # Print alert text
alert.accept()  # To accept the alert

# Step 4: Close browser
driver.quit()

# 9.How do you switch between multiple browser windows in Selenium?

# Step 1: Launch Browser window 1
driver = webdriver.Chrome()
driver.get("https://www.google.com/")

# Step 2: Open new window using JavaScript
driver.execute_script("window.open('https://www.google.com/');")
driver.execute_script("window.open('https://www.google.com/');")

# Step 3: Current window handles
window = driver.current_window_handle

# Step 4: Switch to second window
driver.switch_to_window(window[2])
driver.set_window_position(1000,0)

# Step 5: Switch to frist window
driver.switch_to_window(window[1])
driver.set_window_position(800,0)

# Step 5: Switch to current window
driver.switch_to_window(window[0])
driver.set_window_position(0,0)

driver.quit()

# 10.Dynamic Highest Number

# Step1 : Launch Browser
driver = webdriver.Chrome()
driver.get("https://example.com/numbers")

# Step 2: Find all number elements
elements = driver.find_elements(By.XPATH, "//td[text()='cc']/following-sibling::td[1]")

numbers = []
# Extract and convert to int
for val in elements:
    num = int(val.text)
    numbers.append(num)

# Find highest value
max_value = max(numbers)
print("Highest value:", max_value)



# 11 Calculate the frequency of URLs on a webpage and identify the most frequently occurring URL.
# Step 1: Setup Selenium WebDriver
driver = webdriver.Chrome()

# Step 2: Navigate to target page
try:
    target_url = "https://example.com/targetpage"
    driver.get(target_url)
# Step 3: Find all links on the page
    links = driver.find_elements(By.TAG_NAME, "a")[:100]  # Get first 100 links

# Extract the href attribute from each link and store in a list
    url_list = []
    for link in links:
        url = link.get_attribute("href")
        if url:
            url_list.append("href")

# step 4: Calculate the Frequency of each URL
    if url_list:
        counts = Counter(url_list)

        # Get the most common URL and its count
        most_common_url, frequency = counts.most_common(1)[0]

        print("-" * 30)
        print(f"Total URLs processed: {len(url_list)}")
        print(f"Most Frequent URL: {most_common_url}")
        print(f"Appearance Count: {frequency}")
        print("-" * 30)
    else:
        print("No URLs found on the page.")

finally:
    # 5. Close the browser
    driver.quit()


# 13. Scrape the first 200 book entries from a webpage, extracting the URL, author name, and page count for each book. Store this data in a structured format (e.g., a list of dictionaries) and analyze the frequency of URLs to identify the most common one.

# Setup Selenium WebDriver
driver = webdriver.Chrome()

try:
    # 1. Navigate to the target page
    driver.get("https://your-target-website.com")

    # 2. Find all book/link containers
    # We target the 'wrapper' for each entry to keep metadata linked correctly
    items = driver.find_elements(By.CSS_SELECTOR, ".book-entry")[:200]

    scraped_data = []

    for index, item in enumerate(items, start=1):
        try:
            # Extracting specific fields based on your requirements
            url = item.find_element(By.TAG_NAME, "a").get_attribute("href")
            author = item.find_element(By.CSS_SELECTOR, ".author-name").text
            page_count = item.find_element(By.CSS_SELECTOR, ".page-num").text

            # Storing data in a structured dictionary
            scraped_data.append({
                "unique_index": index,
                "url": url,
                "author": author,
                "pages": page_count,
                "line_index": index  # Assuming line index refers to the row position
            })
        except Exception as e:
            continue  # Skip if an element is missing for a specific item

    # 3. Analyze Frequency of URLs
    url_list = [data['url'] for data in scraped_data]
    url_counts = Counter(url_list)
    most_common_url, freq = url_counts.most_common(1)[0]

    # 4. Summary Output
    print(f"{'=' * 40}")
    print(f"Extraction Summary")
    print(f"{'=' * 40}")
    print(f"Total Items Processed: {len(scraped_data)}")
    print(f"Unique Index Range: 1 - {len(scraped_data)}")
    print(f"Most Frequent URL: {most_common_url}")
    print(f"URL Appearance Count: {freq}")
    print(f"{'=' * 40}\n")

    # 5. Displaying formatted data (Top 5 rows as example)
    df = pd.DataFrame(scraped_data)
    print("Data Preview (First 5 entries):")
    print(df[['unique_index', 'author', 'pages', 'url']].head())

finally:
    driver.quit()