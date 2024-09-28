# CuriousCat Downloader

This project contains scripts to download your posts and inbox messages from CuriousCat using their internal API. 

## Overview

This repository provides two Python scripts:
1. `download-posts.py`: Downloads your public CuriousCat posts.
2. `download-inbox.py`: Downloads your CuriousCat inbox messages.

These scripts use the CuriousCat API and require your **token**, **cookie**, and **username** from your logged-in session to access your data.

## Features

- Fetch all posts and inbox messages from CuriousCat.
- Stores the downloaded data as JSON files.
- Simple setup using Python and `requests`.

## Setup

### Requirements

- Python 3.x
- `requests` library (Install via `pip install requests`)

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/me2resh/curious-cat-backup.git
    cd curious-cat-backup
    ```

2. Set up a virtual environment (optional, but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Before running the scripts, you'll need to provide your **token**, **cookie**, and **username** from your CuriousCat account. Follow the steps below to obtain them.

### Steps to Get Token, Cookie, and Username Using Google Chrome

1. **Open Developer Tools in Chrome:**
   - Go to the CuriousCat website and log in to your account.
   - Right-click anywhere on the page and click **Inspect** or press `Cmd + Option + I` (on Mac) or `Ctrl + Shift + I` (on Windows/Linux).
   - This will open the Developer Tools console.

2. **Go to the Network Tab:**
   - Once the Developer Tools are open, navigate to the **Network** tab.
   - Make sure the console is open while you interact with CuriousCat (such as checking your inbox or making a request). This will capture all network requests.

3. **Filter API Requests:**
   - In the **Network** tab, you’ll see a list of requests. To filter out unnecessary requests, you can type `inbox` or `api` in the search bar within the Network tab. This will show you the API requests related to fetching your inbox or posts.
   - You’re looking for a request to `https://curiouscat.live/api/v2/inbox` or a similar endpoint.

4. **Inspect the Request Details:**
   - Click on one of the requests to the `/api/v2/inbox` endpoint.
   - In the **Headers** tab, under **Request Headers**, you will find:
     - **Authorization:** This header contains your **token**. Copy everything after `Basic `.
     - **Cookie:** This contains your **cookie**. Copy everything in this field.
     - **Referer:** This will show the URL of your profile (e.g., `https://curiouscat.live/yourusername`). Your **username** is the last part of this URL. Copy your username.

5. **Add Token, Cookie, and Username to Your Script:**
   - Open `download-inbox.py` or `download-posts.py`.
   - Replace the placeholder `YOUR_TOKEN_HERE` with the token you copied from the `Authorization` header.
   - Replace the placeholder `YOUR_COOKIE_HERE` with the cookie you copied from the `Cookie` header.
   - Replace `YOUR_USERNAME_HERE` with your actual CuriousCat username.

### Example of where to place the values in your script:

```python
# Inside the script, update the headers with your values

USERNAME = 'YOUR_USERNAME_HERE'  # Replace with your actual CuriousCat username
HEADERS = {
    'accept': '*/*',
    'accept-language': 'en_US',
    'authorization': 'Basic YOUR_TOKEN_HERE',  # Replace with your actual token
    'cookie': 'YOUR_COOKIE_HERE',  # Replace with your actual cookie
    'referer': f'https://curiouscat.live/{USERNAME}',  # Replace with your actual username
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-arch': '"arm"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"128.0.6613.162"',
    'sec-ch-ua-full-version-list': '"Chromium";v="128.0.6613.162", "Not;A=Brand";v="24.0.0.0", "Google Chrome";v="128.0.6613.162"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"macOS"',
    'sec-ch-ua-platform-version': '"14.7.0"',
}
```

### Important Notes:
- **Keep your token, cookie, and username confidential.** Do not share them publicly or include them in any publicly accessible scripts or repositories. These values are unique to your session and account.

### Running the Scripts

#### Download Inbox
To download your CuriousCat inbox messages:

```bash
python download-inbox.py
```

The messages will be saved in `curiouscat_inbox.json`.

#### Download Posts
To download your public CuriousCat posts:

```bash
python download-posts.py
```

The posts will be saved in `curiouscat_posts.json`.

## Troubleshooting

### 1. **No output or script hanging:**
   - Ensure your **token**, **cookie**, and **username** are up to date. If they expire, you will need to get new ones following the steps above.
   - Add `print()` statements to debug where the script might be hanging.

### 2. **Invalid credentials error:**
   - Ensure the **token**, **cookie**, and **username** were copied correctly from the Developer Tools and are not expired.

### 3. **Rate-limiting:**
   - If you receive too many requests error, it's recommended to add a small delay between API calls by using `time.sleep(seconds)`.

## Contributing

Feel free to fork this repository, add features, or fix bugs! If you'd like to contribute, please open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
