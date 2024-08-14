import requests

def number_of_subscribers(subreddit):
    # Define the Reddit API URL for the subreddit's about page
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Define custom headers with a User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            data = response.json()
            # Return the number of subscribers
            return data.get('data', {}).get('subscribers', 0)
        else:
            # If the subreddit is invalid, return 0
            return 0
    except requests.RequestException:
        # If there is an exception in the request, return 0
        return 0