# Fetching Trending Topics with Selenium

This project demonstrates how to fetch the top 5 trending topics from Twitter using Selenium. There are three different methods provided to achieve this:

1. **Without Proxy**
2. **Using Proxy**
3. **Using Residential Proxy**

## Prerequisites

- Python 3.x
- MongoDB
- ChromeDriver
- Required Python packages (install using `pip install -r requirements.txt`)

## Method 1: Without Proxy

This method uses Selenium to log in to Twitter and fetch the trending topics without using any proxy.

### Steps:

1. **Setup MongoDB**: Ensure MongoDB is running on `localhost:27017`.
2. **Configure Selenium**: Use `webdriver-manager` to manage ChromeDriver.
3. **Fetch Trending Topics**: Log in to Twitter and scrape the trending topics.

### Code:

```python
# filepath: /C:/Users/sahil pandey/OneDrive/Desktop/task/selenium_script.py
# ...existing code...
def fetch_trending_topics():
    # ...existing code...
    ip_address = "No Proxy Used"  # Since proxy is disabled
    # ...existing code...
```

## Method 2: Using Proxy

This method uses a proxy server to fetch the trending topics, which can help in avoiding IP bans.

### Steps:

1. **Setup Proxy**: Configure the proxy server with your credentials.
2. **Configure Selenium**: Use `webdriver-manager` to manage ChromeDriver and set up the proxy.
3. **Fetch Trending Topics**: Log in to Twitter and scrape the trending topics using the proxy.

### Code:

```python
# filepath: /C:/Users/sahil pandey/OneDrive/Desktop/task/selenium_script.py
# ...existing code...
PROXY = "your_proxy_username:your_proxy_password@proxy_address:port"  # Replace with actual Proxy credentials
chrome_options.add_argument(f"--proxy-server=http://{PROXY}")  # Use the proxy server
# ...existing code...
```

## Method 3: Using Residential Proxy

This method uses a residential proxy to fetch the trending topics, which can provide better anonymity and reduce the chances of being blocked.

### Steps:

1. **Setup Residential Proxy**: Configure the residential proxy with your credentials.
2. **Configure Selenium**: Use `webdriver-manager` to manage ChromeDriver and set up the residential proxy.
3. **Fetch Trending Topics**: Log in to Twitter and scrape the trending topics using the residential proxy.

### Code:

```python
# filepath: /C:/Users/sahil pandey/OneDrive/Desktop/task/selenium_script.py
# ...existing code...
proxy_username = "your_proxy_username"
proxy_password = "your_proxy_password"
proxy_address = "your_proxy_address:port"
PROXY = f"{quote(proxy_username)}:{quote(proxy_password)}@{proxy_address}"  # Encode credentials properly
chrome_options.add_argument(f"--proxy-server=http://{PROXY}")  # Use the residential proxy
# ...existing code...
```

## Running the Flask Application

The Flask application provides a web interface to trigger the Selenium script and display the trending topics.

### Steps:

1. **Run Flask Application**: Start the Flask server.
2. **Access Web Interface**: Open the browser and navigate to `http://localhost:5000`.
3. **Fetch Trending Topics**: Click the button to run the script and display the trending topics.

### Code:

```python
# filepath: /c:/Users/sahil pandey/OneDrive/Desktop/task/app.py
# ...existing code...
@app.route('/run-script')
def run_script():
    record = fetch_trending_topics()
    return jsonify(record)
# ...existing code...
```

## Conclusion

This project demonstrates three different methods to fetch trending topics from Twitter using Selenium. Each method has its own advantages and can be chosen based on the requirements and constraints.
