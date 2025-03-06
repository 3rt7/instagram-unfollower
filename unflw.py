from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, sys, pprint


def take_users(driver :webdriver, popup, total_count :int):
    while True:
        users_elements = popup.find_elements(By.CSS_SELECTOR, "a.notranslate")
        if users_elements:
            driver.execute_script("arguments[0].scrollIntoView()", users_elements[-1]) # scroll into last user visible
            time.sleep(2)

        if len(users_elements) >= total_count:
            break
        
    # convert to set for: 1. have unique usernames 2. use difference operator
    users = {user.text.strip() for user in users_elements}
    return users
    
try:
    username = sys.argv[1]
except:
    print("Please provide your username when running the script")
    sys.exit(1)

browser = webdriver.Chrome()
browser.get("https://instagram.com")
browser.find_element(By.NAME, "username").send_keys(username)

print("Waiting for the user to log-in...")

# wait 5 minutes for the presence of an element that indicates a successfull log-in, in this case 'profile'
WebDriverWait(browser, 300).until(EC.presence_of_element_located((By.XPATH, f"//a[contains(@href, '/{username}')]")))

browser.get(f"https://instagram.com/{username}")
time.sleep(2) # avoid being blocked

followers_elem = browser.find_element(By.XPATH, "//a[contains(@href, '/followers')]")
followers_count = int(followers_elem.text.split()[0])
print(f"Total followers: {followers_count}")
following_elem = browser.find_element(By.XPATH, "//a[contains(@href, '/following')]")
following_count = int(following_elem.text.split()[0])
print(f"Total following: {following_count}")

# make the followers pop up appear
followers_elem.click()
# wait for the popup to load
time.sleep(2)
pop_up = browser.find_element(By.CSS_SELECTOR, "div[role='dialog']")
print("Getting followers list...")
followers = take_users(browser, pop_up, followers_count)
# close pop up
pop_up.find_element(By.TAG_NAME, "button").click()
time.sleep(2)

# make the following pop up appear
following_elem.click()
time.sleep(2)
pop_up = browser.find_element(By.CSS_SELECTOR, "div[role='dialog']")
print("Getting following count...")
following = take_users(browser, pop_up, following_count)
# close pop up
pop_up.find_element(By.TAG_NAME, "button").click()

print("Everything done, closing browser")
browser.quit()

not_following_back = following - followers
print(f"{len(not_following_back)} not following you back!")
pprint.pprint(not_following_back)
