import requests
from config import NEWS_API_KEY





api_key = NEWS_API_KEY

def techcrunch():
    title_list = []
    api_address = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={api_key}" #startup and technology news
    json_data = requests.get(api_address).json()

    articles = json_data["articles"]
    num_articles = min(3, len(articles)) # Fetch up to 3 titles or the number of articles available if less than 3

    for i in range(num_articles):
        title = json_data["articles"][i]["title"]
        title_list.append(f"article {i+1}:  {title}.")
    return title_list

def business():
    title_list = []
    api_address = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={api_key}" #Top business headlines in the US right now
    json_data = requests.get(api_address).json()
    articles = json_data["articles"]
    num_articles = min(3, len(articles))

    #fatch the first 3 titles
    for i in range(num_articles):
        title = json_data["articles"][i]["title"]
        title_list.append(f"article {i+1}:  {title}.")
    return title_list

def wsj():
    title_list = []
    api_address = f"https://newsapi.org/v2/everything?domains=wsj.com&apiKey={api_key}" #All articles published by the Wall Street Journal
    json_data = requests.get(api_address).json()
    articles = json_data["articles"]
    num_articles = min(3, len(articles))

    #fatch the first 3 titles
    for i in range(num_articles):
        title = json_data["articles"][i]["title"]
        title_list.append(f"article {i+1}:  {title}.")
    return title_list





