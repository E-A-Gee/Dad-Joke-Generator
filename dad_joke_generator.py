from pyfiglet import figlet_format
from requests import get
from random import choice

# print header
print(figlet_format('Dad Joke 3000'))

# get topic from user
topic = input("Let me tell you a joke! Give me a topic: ")

# get request
url = "https://icanhazdadjoke.com/search"
response = get(
    url,
    headers={"Accept": "application/json"},
    params={"term": topic}
).json()
# turn the received data into python from json

jokes_list = [x['joke'] for x in response["results"]]

if response["total_jokes"] == 1:
    print(f"I've got one joke about {topic}. Here it is:")
    print(choice(jokes_list))

elif response["total_jokes"] > 1:
    print(f"I've for {len(jokes_list)} jokes about {topic}. Here's one of them:")
    print(choice(jokes_list))

else:
    print("Sorry! No jokes found!")
