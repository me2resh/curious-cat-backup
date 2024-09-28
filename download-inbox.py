import requests
import json

# Define the API endpoint and headers
API_URL = 'https://curiouscat.live/api/v2.1/profile'
USERNAME = 'YOUR_USERNAME_HERE'
HEADERS = {
    'accept': '*/*',
    'accept-language': 'en_US',
    'authorization': 'Basic YOUR_TOKEN_HERE',  # Replace with your actual token
    'cookie': 'YOUR_COOKIE_HERE',
    'referer': f'https://curiouscat.live/{USERNAME}',
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

# Function to make API request
def fetch_posts(max_timestamp=None):
    params = {
        'username': USERNAME,
        '_ob': 'registerOrSignin2'
    }
    if max_timestamp:
        params['max_timestamp'] = max_timestamp

    try:
        response = requests.get(API_URL, headers=HEADERS, params=params, timeout=10)
        response.raise_for_status()  # Raises an HTTPError if the response status is 4xx or 5xx
        return response.json()
    except requests.Timeout:
        print("Request timed out. Trying again...")
        return None
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Function to download posts until no more are available
def download_all_posts():
    all_posts = []
    max_timestamp = None
    has_more_posts = True

    while has_more_posts:
        data = fetch_posts(max_timestamp)
        if data and 'posts' in data:
            posts = data['posts']
            if not posts:
                has_more_posts = False
            else:
                all_posts.extend(posts)
                # Get the timestamp of the last post to use for the next request
                max_timestamp = posts[-1]['post']['timestamp']
        else:
            has_more_posts = False

    return all_posts

# Download posts and save to a file
all_posts = download_all_posts()

with open('curiouscat_posts.json', 'w') as f:
    json.dump(all_posts, f)

print(f"Downloaded {len(all_posts)} posts.")
