from django.http import HttpResponse
from django.shortcuts import render
import requests
def index(request):
    return HttpResponse("This is the second page")
def home(request):
    global query
    if request.method=="POST":
        query = request.POST.get('topic')
    return render(request,"home.html")
# print(query)
# Define the base URL and parameters for the News API
def news(request):
    base_url = 'https://newsapi.org/v2/everything'
    api_key = '01de3fa5d332484ebebf88d15c797288'  # Replace with your actual News API key
    language = 'en'   # Language of the news articles
    sort_by = 'publishedAt'  # Sort articles by published date
    page_size = 5     # Number of articles to fetch

    # Define the request parameters
    params = {
        'q': query,
        'language': language,
        'sortBy': sort_by,
        'pageSize': page_size,
        'apiKey': api_key
    }

    # Send a GET request to the News API
    response = requests.get(base_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        articles = data['articles']
    else:
        print("Failed to fetch news articles. Status code:", response.status_code)

    d={'Title':f"{articles[0]['title']}",
    'Source':f"Source: {articles[0]['source']['name']}",
    'Published at':f"Published At: {articles[0]['publishedAt']}",
    'Description':f"Description: {articles[0]['description']}",
    'URL':f"{articles[0]['url']}",
    'Content':f"Content: {articles[0]['content']}"
    }
    return render(request,"news.html",d)