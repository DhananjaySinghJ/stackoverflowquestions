import requests
import json

# Send a GET request to the Stack Exchange API
response = requests.get('http://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

# Check if the request was successful
if response.status_code == 200:
    questions = response.json()['items']

    # Loop through each question in the response
    for question in questions:
        if question['answer_count'] == 0:  # Modify this to retrieve answered questions if needed
            print(f"Title: {question['title']}")
            print(f"Link: {question['link']}")
        else:
            print("Skipped")
        print()  # Print a newline for better readability
else:
    print(f"Failed to retrieve questions. Status code: {response.status_code}")
