from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException

options = Options()
# options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

website = "https://www.booking.com/searchresults.en-gb.html?ss=Ho+Chi+Minh+City&ssne=Ho+Chi+Minh+City&ssne_untouched=Ho+Chi+Minh+City&efdco=1&label=gen173nr-1FCAQoggJCF3NlYXJjaF9obyBjaGkgbWluaCBjaXR5SAlYBGj0AYgBAZgBCbgBB8gBDdgBAegBAfgBA4gCAagCA7gC2Nn5wQbAAgHSAiRmNGViNjBhMy0wZjA3LTQzMjMtYjU3YS04ZTFhNTFjODNlYTXYAgXgAgE&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=-3730078&dest_type=city&checkin=2025-07-01&checkout=2025-07-10&group_adults=2&no_rooms=1&group_children=0"
driver.get(website)

wait = WebDriverWait(driver, 15)
names = []
prices = []
ratings = []
cancellation = []
prepaid = []
breakfast = []
distances = []

for i in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

for i in range(1000): 
    try:
        load_more = driver.find_element(By.XPATH, './/button/span[contains(text(), "Load more results")]')
        actions = ActionChains(driver)
        actions.scroll_to_element(load_more)
        actions.pause(3)
        actions.perform()
        load_more.click()
        time.sleep(3) 
    except:
        break
    

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="property-card"]')))
items = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')

for item in items:
    try:
        name = item.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]').text
    except:
        name = "None"
    names.append(name)
    
    try:
        price = item.find_element(By.XPATH, './/span[contains(@data-testid, "price-and-discounted-price")]').text
    except:
        price = "None"
    prices.append(price)
     
    try:
        rating = item.find_element(By.CSS_SELECTOR, 'div[data-testid="review-score"] div:nth-child(2)').text
    except:
        rating = "None"
    ratings.append(rating)
     
    try:
        distance = item.find_element(By.XPATH, './/span[contains(@data-testid , "distance")]').text
    except:
        distance = "None"
    distances.append(distance)
      
    try:
        item.find_element(By.XPATH, './/span[contains(@data-testid, "cancellation-policy-icon")]')
        cancellation.append("Yes")
    except NoSuchElementException:
        cancellation.append("No")
        
    try:
        item.find_element(By.XPATH, './/span[contains(@data-testid, "prepayment-policy-icon")]')
        prepaid.append("No")
    except NoSuchElementException:
        prepaid.append("Yes")
    
    try:
        item.find_element(By.XPATH, './/span[contains(@class, "d651523034")]')
        breakfast.append("Yes")
    except NoSuchElementException:
        breakfast.append("No")
   


df = pd.DataFrame({
    "Name": names,
    "Price": prices,
    "Rating": ratings,
    "Distance from the centre": distances,
    "Free Cancellation": cancellation,
    "Prepayment needed": prepaid,
    "Breakfast included": breakfast
})
df.to_csv('hotels.csv', index=False)

driver.quit()