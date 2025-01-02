# Selenium-Playground

# Selenium Table Search Automation

This script automates the process of testing a table search functionality on the Selenium Playground website. It verifies that searching for "New York" returns the expected result.

## Features
- Navigates to the Selenium Playground Table Search Demo.
- Interacts with the search box to search for "New York."
- Validates that the search results display "5 entries out of 24 total entries."

---

## Setup Instructions

### Prerequisites
1. Python 3.x installed on your system.
2. Selenium WebDriver library installed. Install it via pip:
3. Chrome browser installed.
4. ChromeDriver compatible with your Chrome version. Download from [ChromeDriver](https://chromedriver.chromium.org/downloads).

---

### How to Run the Script

1. Clone or download this repository.
2. Open the terminal/command prompt and navigate to the script's directory.
3. Replace the placeholder `"path/to/chromedriver"` in the script with the absolute path to your `chromedriver` executable.
4. Run the script:

   
---

### Notes
- Ensure your ChromeDriver matches your installed Chrome browser version.
- If running on a headless server, you can configure the script to use headless mode by adding the following:
```python
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(driver_path, options=options)


