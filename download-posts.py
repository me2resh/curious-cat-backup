import requests
import json
import time

# API URL for inbox
API_URL = 'https://curiouscat.live/api/v2/inbox'
HEADERS = {
    'accept': '*/*',
    'accept-language': 'en_US',
    'authorization': 'Basic YOUR_TOKEN_HERE',  # Replace with your actual token
    'cookie': 'YOUR_COOKIE_HERE',
    'referer': 'https://curiouscat.live/inbox',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-arch': '"arm"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"128.0.6613.162"',
    'sec-ch-ua-full-version-list': '"Chromium";v="128.0.6613.162", "Not;A=Brand";v="24.0.0.0", "Google Chrome";v="128.0.6613.162"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-ch-ua-platform-version': '"14.7.0"',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

# Function to fetch inbox data
def fetch_inbox(max_timestamp=None):
    params = {
        '_ob': 'registerOrSignin2'
    }
    if max_timestamp:
        params['max_timestamp'] = max_timestamp
    
    print(f"Fetching inbox data with max_timestamp: {max_timestamp}")
    
    try:
        response = requests.get(API_URL, headers=HEADERS, params=params, timeout=10)
        response.raise_for_status()
        print(f"Received response with status code: {response.status_code}")
        return response.json()
    except requests.Timeout:
        print("Request timed out. Trying again...")
        return None
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Function to download all inbox messages
def download_inbox():
    all_messages = []
    max_timestamp = None
    has_more = True

    while has_more:
        print(f"Starting new iteration with max_timestamp: {max_timestamp}")
        data = fetch_inbox(max_timestamp)
        
        if data and 'posts' in data:
            posts = data['posts']
            print(f"Fetched {len(posts)} posts.")
            
            if not posts:
                print("No more posts found.")
                has_more = False
            else:
                all_messages.extend(posts)
                # Update max_timestamp for the next request
                max_timestamp = posts[-1]['timestamp']
                print(f"Updated max_timestamp to {max_timestamp}")
        else:
            print("No data received or no posts field in the response.")
            has_more = False
        # Add a small sleep to prevent rate-limiting issues
        time.sleep(1)

    return all_messages

# Download inbox messages and save to a file
print("Starting inbox download...")
inbox_messages = download_inbox()

with open('curiouscat_inbox.json', 'w') as f:
    json.dump(inbox_messages, f)

print(f"Downloaded {len(inbox_messages)} inbox messages.")
