from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
import time

# Setup WebDriver 
driver = webdriver.Chrome()

# Open the Cookie Clicker game
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Wait for the game to load (to be adjusted)
time.sleep(10)

# Locate the giant cookie element
cookie = driver.find_element(By.ID, "bigCookie")

# Main game loop
try:
    while True:
        # Click the giant cookie
        cookie.click()

        # Purchase upgrades if available
        items = driver.find_elements(By.CSS_SELECTOR, "#products .enabled")
        if items:
            items[-1].click()  # Purchase the most expensive affordable item

        # Purchase upgrades if available
        upgrades = driver.find_elements(By.CSS_SELECTOR, "#upgrades .enabled")
        if upgrades:
            upgrades[0].click()  # Purchase the first available upgrade

        # Adjust sleep time if necessary, this will slow down the loop
        time.sleep(0.1)

except KeyboardInterrupt:
    # Stop the script gracefully with CTRL+C
    print("Script stopped by user")

finally:
    driver.quit()
