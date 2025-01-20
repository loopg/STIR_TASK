

# -----------------Without Proxy------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from pymongo import MongoClient
from datetime import datetime
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client['trending_topics']
collection = db['topics']

# Selenium setup
chrome_options = webdriver.ChromeOptions()

def fetch_trending_topics():
    # Use webdriver-manager to automatically download and manage the correct version of ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get("https://twitter.com/login")
        
        # Wait for the username field to appear (adjusted wait time)
        username_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "session[username_or_email]"))
        )
        username_field.send_keys("your_username")  # Replace with your Twitter username
        username_field.send_keys(Keys.RETURN)
        
        # Wait for the password field to appear (adjusted wait time)
        password_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "session[password]"))
        )
        password_field.send_keys("your_password")  # Replace with your Twitter password
        password_field.send_keys(Keys.RETURN)
        
        # Wait for some time for login to process
        time.sleep(30)  # Wait for 30 seconds for the login to complete, can be adjusted based on your network speed

        # Fetch trending topics
        trends = driver.find_elements(By.XPATH, "//span[contains(text(), 'Trending')]/../../..//span")[:5]
        trending_topics = [trend.text for trend in trends if trend.text.strip()]

        # Metadata
        unique_id = str(datetime.now().timestamp())
        ip_address = "No Proxy Used"  # Since proxy is disabled
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        record = {
            "_id": unique_id,
            "trend1": trending_topics[0],
            "trend2": trending_topics[1],
            "trend3": trending_topics[2],
            "trend4": trending_topics[3],
            "trend5": trending_topics[4],
            "timestamp": timestamp,
            "ip_address": ip_address,
        }
        collection.insert_one(record)
        return record

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()  # Ensure driver is properly closed


# -------------------------------------------using selenium with proxy-1--------------------------------------------

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from pymongo import MongoClient
# from datetime import datetime
# import time
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # MongoDB setup
# client = MongoClient("mongodb://localhost:27017/")
# db = client['trending_topics']
# collection = db['topics']

# # Proxy setup (replace with your ProxyMesh credentials)
# PROXY = "username:password@us-ca.proxymesh.com:31280"  # Replace with actual ProxyMesh credentials
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(f"--proxy-server=http://{PROXY}")  # Use the proxy server

# def fetch_trending_topics():
#     # Use webdriver-manager to automatically download and manage the correct version of ChromeDriver
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=chrome_options)

#     try:
#         driver.get("https://twitter.com/login")
        
#         # Wait for the username field to appear
#         username_field = WebDriverWait(driver, 20).until(
#             EC.visibility_of_element_located((By.NAME, "session[username_or_email]"))
#         )
#         username_field.send_keys("your_username")  # Replace with your Twitter username
#         username_field.send_keys(Keys.RETURN)
        
#         # Wait for the password field to appear
#         password_field = WebDriverWait(driver, 20).until(
#             EC.visibility_of_element_located((By.NAME, "session[password]"))
#         )
#         password_field.send_keys("your_password")  # Replace with your Twitter password
#         password_field.send_keys(Keys.RETURN)
        
#         # Wait for login to complete
#         time.sleep(5)  # Wait for 5 seconds after login to allow page to load

#         # Fetch trending topics
#         trends = driver.find_elements(By.XPATH, "//span[contains(text(), 'Trending')]/../../..//span")[:5]
#         trending_topics = [trend.text for trend in trends if trend.text.strip()]

#         # Metadata
#         unique_id = str(datetime.now().timestamp())
#         ip_address = PROXY.split('@')[1].split(':')[0]  # Extract the IP address from Proxy string
#         timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#         # Save to MongoDB
#         record = {
#             "_id": unique_id,
#             "trend1": trending_topics[0],
#             "trend2": trending_topics[1],
#             "trend3": trending_topics[2],
#             "trend4": trending_topics[3],
#             "trend5": trending_topics[4],
#             "timestamp": timestamp,
#             "ip_address": ip_address,
#         }
#         collection.insert_one(record)
#         return record

#     except Exception as e:
#         print(f"Error: {e}")
#     finally:
#         driver.quit()  # Ensure driver is properly closed



# -------------------------------------------using selenium with proxy -2--------------------------------------------

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from pymongo import MongoClient
# from datetime import datetime
# import time
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import random
# import logging
# from urllib.parse import quote

# # Setup logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # MongoDB setup
# client = MongoClient("mongodb://localhost:27017/")
# db = client['trending_topics']
# collection = db['topics']

# # Proxy setup (replace with your ProxyMesh credentials)
# proxy_username = "lol******"
# proxy_password = "********"
# proxy_host = "us-ca.proxymesh.com:31280"
# PROXY = f"{quote(proxy_username)}:{quote(proxy_password)}@{proxy_host}"  # Properly encode credentials

# # Selenium Chrome options
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(f"--proxy-server=http://{PROXY}")  # Use ProxyMesh server

# # User-Agent rotation to minimize detection
# user_agents = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
# ]
# chrome_options.add_argument(f"user-agent={random.choice(user_agents)}")

# # Enable headless mode (optional)
# # chrome_options.add_argument("--headless")
# # chrome_options.add_argument("--disable-gpu")

# def fetch_trending_topics():
#     logger.info("Starting Selenium with Proxy...")
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=chrome_options)

#     try:
#         logger.info("Opening Twitter login page...")
#         driver.get("https://twitter.com/login")

#         # Wait for the username field
#         username_field = WebDriverWait(driver, 30).until(
#             EC.visibility_of_element_located((By.NAME, "session[username_or_email]"))
#         )
#         username_field.send_keys("your_username")  # Replace with your Twitter username
#         username_field.send_keys(Keys.RETURN)

#         # Wait for the password field
#         password_field = WebDriverWait(driver, 30).until(
#             EC.visibility_of_element_located((By.NAME, "session[password]"))
#         )
#         password_field.send_keys("your_password")  # Replace with your Twitter password
#         password_field.send_keys(Keys.RETURN)

#         # Wait for the home page to load fully
#         time.sleep(10)  # Give enough time for dynamic content to load

#         # Fetch trending topics
#         logger.info("Fetching trending topics...")
#         trends = driver.find_elements(By.XPATH, "//span[contains(text(), 'Trending')]/../../..//span")[:5]
#         trending_topics = [trend.text for trend in trends if trend.text.strip()]
        
#         if not trending_topics:
#             logger.warning("No trending topics found. The page structure might have changed.")

#         # Metadata
#         unique_id = str(datetime.now().timestamp())
#         ip_address = PROXY.split('@')[1].split(':')[0]  # Extract IP address from Proxy string
#         timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#         # Save to MongoDB
#         record = {
#             "_id": unique_id,
#             "trend1": trending_topics[0] if len(trending_topics) > 0 else "N/A",
#             "trend2": trending_topics[1] if len(trending_topics) > 1 else "N/A",
#             "trend3": trending_topics[2] if len(trending_topics) > 2 else "N/A",
#             "trend4": trending_topics[3] if len(trending_topics) > 3 else "N/A",
#             "trend5": trending_topics[4] if len(trending_topics) > 4 else "N/A",
#             "timestamp": timestamp,
#             "ip_address": ip_address,
#         }
#         collection.insert_one(record)
#         logger.info(f"Record saved to MongoDB: {record}")
#         return record

#     except Exception as e:
#         logger.error(f"An error occurred: {e}")
#     finally:
#         driver.quit()
#         logger.info("Driver closed successfully.")

# # Run the function
# if __name__ == "__main__":
#     fetch_trending_topics()






# ------------using stealth selenium-------------------------------------------------------------------

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium_stealth import stealth
# from pymongo import MongoClient
# from datetime import datetime
# import random
# import logging
# from urllib.parse import quote
# import time
# from webdriver_manager.chrome import ChromeDriverManager

# # Setup logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # MongoDB setup
# client = MongoClient("mongodb://localhost:27017/")
# db = client['trending_topics']
# collection = db['topics']

# # Proxy setup (replace with your ProxyMesh credentials)
# proxy_username = "*******"
# proxy_password = "*******"
# proxy_host = "us-ca.proxymesh.com:31280"
# PROXY = f"{quote(proxy_username)}:{quote(proxy_password)}@{proxy_host}"  # Properly encode credentials

# # Selenium Chrome options
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(f"--proxy-server=http://{PROXY}")  # Use ProxyMesh server

# # User-Agent rotation to minimize detection
# user_agents = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
# ]
# chrome_options.add_argument(f"user-agent={random.choice(user_agents)}")

# # Disable headless mode for debugging
# # chrome_options.add_argument("--headless")
# # chrome_options.add_argument("--disable-gpu")

# def fetch_trending_topics():
#     logger.info("Starting Selenium with Proxy and Stealth...")
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=chrome_options)

#     # Apply Selenium Stealth
#     stealth(
#         driver,
#         languages=["en-US", "en"],
#         vendor="Google Inc.",
#         platform="Win32",
#         webgl_vendor="Intel Inc.",
#         renderer="Intel Iris OpenGL Engine",
#         fix_hairline=True,
#     )

#     try:
#         logger.info("Opening Twitter login page...")
#         driver.get("https://twitter.com/login")

#         # Wait for the username field
#         username_field = WebDriverWait(driver, 30).until(
#             EC.visibility_of_element_located((By.NAME, "session[username_or_email]"))
#         )
#         username_field.send_keys("your_username")  # Replace with your Twitter username
#         username_field.send_keys(Keys.RETURN)

#         # Wait for the password field
#         password_field = WebDriverWait(driver, 30).until(
#             EC.visibility_of_element_located((By.NAME, "session[password]"))
#         )
#         password_field.send_keys("your_password")  # Replace with your Twitter password
#         password_field.send_keys(Keys.RETURN)

#         # Wait for the home page to load fully
#         time.sleep(10)  # Give enough time for dynamic content to load

#         # Fetch trending topics
#         logger.info("Fetching trending topics...")
#         trends = driver.find_elements(By.XPATH, "//span[contains(text(), 'Trending')]/../../..//span")[:5]
#         trending_topics = [trend.text for trend in trends if trend.text.strip()]

#         if not trending_topics:
#             logger.warning("No trending topics found. The page structure might have changed.")

#         # Metadata
#         unique_id = str(datetime.now().timestamp())
#         ip_address = PROXY.split('@')[1].split(':')[0]  # Extract IP address from Proxy string
#         timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#         # Save to MongoDB
#         record = {
#             "_id": unique_id,
#             "trend1": trending_topics[0] if len(trending_topics) > 0 else "N/A",
#             "trend2": trending_topics[1] if len(trending_topics) > 1 else "N/A",
#             "trend3": trending_topics[2] if len(trending_topics) > 2 else "N/A",
#             "trend4": trending_topics[3] if len(trending_topics) > 3 else "N/A",
#             "trend5": trending_topics[4] if len(trending_topics) > 4 else "N/A",
#             "timestamp": timestamp,
#             "ip_address": ip_address,
#         }
#         collection.insert_one(record)
#         logger.info(f"Record saved to MongoDB: {record}")
#         return record

#     except Exception as e:
#         logger.error(f"An error occurred: {e}")
#     finally:
#         driver.quit()
#         logger.info("Driver closed successfully.")

# # Run the function
# if __name__ == "__main__":
#     fetch_trending_topics()




# ------------------------------------------------using resedencial proxy--------------------------------------------

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from pymongo import MongoClient
# from datetime import datetime
# import random
# import logging
# from urllib.parse import quote
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# # Setup logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # MongoDB setup
# client = MongoClient("mongodb://localhost:27017/")
# db = client['trending_topics']
# collection = db['topics']

# # Residential Proxy setup (replace with your credentials)
# proxy_username = "your_proxy_username"
# proxy_password = "your_proxy_password"
# proxy_address = "your_proxy_address:port"
# PROXY = f"{quote(proxy_username)}:{quote(proxy_password)}@{proxy_address}"  # Encode credentials properly

# # Selenium Chrome options
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(f"--proxy-server=http://{PROXY}")  # Use the residential proxy

# # User-Agent rotation to minimize detection
# user_agents = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
# ]
# chrome_options.add_argument(f"user-agent={random.choice(user_agents)}")

# def fetch_trending_topics():
#     logger.info("Starting Selenium with Residential Proxy...")
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=chrome_options)

#     try:
#         logger.info("Opening Twitter login page...")
#         driver.get("https://twitter.com/login")

#         # Wait for the username field
#         username_field = WebDriverWait(driver, 30).until(
#             EC.visibility_of_element_located((By.NAME, "session[username_or_email]"))
#         )
#         username_field.send_keys("your_username")  # Replace with your Twitter username
#         username_field.send_keys(Keys.RETURN)

#         # Wait for the password field
#         password_field = WebDriverWait(driver, 30).until(
#             EC.visibility_of_element_located((By.NAME, "session[password]"))
#         )
#         password_field.send_keys("your_password")  # Replace with your Twitter password
#         password_field.send_keys(Keys.RETURN)

#         # Wait for the home page to load fully
#         time.sleep(10)  # Give enough time for dynamic content to load

#         # Fetch trending topics
#         logger.info("Fetching trending topics...")
#         trends = driver.find_elements(By.XPATH, "//span[contains(text(), 'Trending')]/../../..//span")[:5]
#         trending_topics = [trend.text for trend in trends if trend.text.strip()]

#         if not trending_topics:
#             logger.warning("No trending topics found. The page structure might have changed.")

#         # Metadata
#         unique_id = str(datetime.now().timestamp())
#         ip_address = proxy_address.split(":")[0]  # Extract the proxy IP
#         timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#         # Save to MongoDB
#         record = {
#             "_id": unique_id,
#             "trend1": trending_topics[0] if len(trending_topics) > 0 else "N/A",
#             "trend2": trending_topics[1] if len(trending_topics) > 1 else "N/A",
#             "trend3": trending_topics[2] if len(trending_topics) > 2 else "N/A",
#             "trend4": trending_topics[3] if len(trending_topics) > 3 else "N/A",
#             "trend5": trending_topics[4] if len(trending_topics) > 4 else "N/A",
#             "timestamp": timestamp,
#             "ip_address": ip_address,
#         }
#         collection.insert_one(record)
#         logger.info(f"Record saved to MongoDB: {record}")
#         return record

#     except Exception as e:
#         logger.error(f"An error occurred: {e}")
#     finally:
#         driver.quit()
#         logger.info("Driver closed successfully.")

# # Run the function
# if __name__ == "__main__":
#     fetch_trending_topics()
