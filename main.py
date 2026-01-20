import requests
from send_email import send_email

topic=input("enter the topic you want to search: ")
url=f"https://newsapi.org/v2/everything?q={topic}&from=2025-12-18&sortBy=publishedAt&apiKey=4ada824a177e4945b2c7c81a3414ad24&language=en"

# make request using the requests module
request=requests.get(url)

# get the request in the json format
content=request.json()
print(content)

# Access the articles title and description
def news_fetch():
    message = ""
    for article in content["articles"]:
        if article["title"] is not None:
            title=article["title"]
            description=article["description"]
            message_url=article["url"]
            message += f"title:{title}\ndescription:{description}\nlink:{message_url}"
            message += "\n" + ("-" * 60) + "\n"
    send_email(message)

news_fetch()