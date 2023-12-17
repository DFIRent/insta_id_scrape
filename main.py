import requests
from bs4 import BeautifulSoup
import json
import re


def get_instagram_user_id(username):
    url = f'https://www.instagram.com/{username}'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        script_tags = soup.find_all('script')

        pattern = re.compile(r'"profile_id":"(\d+)"')

        for script_tag in script_tags:
            if script_tag.string is not None:
                match = pattern.search(script_tag.string)
                if match:
                    user_id = match.group(1)
                    return user_id
        else:
            print("User data not found.")
            return None
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None


# Main script
if __name__ == '__main__':
    username = input("Enter the Instagram username: ")
    user_id = get_instagram_user_id(username)

    if user_id:
        print(f"User ID for {username}: {user_id}")
    else:
        print("Failed to fetch user ID.")
