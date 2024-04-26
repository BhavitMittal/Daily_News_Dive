from django.http import HttpResponse
from django.shortcuts import render,redirect
import requests
from newsdataapi import NewsDataApiClient
def index(request):
    return HttpResponse("This is the second page")
def defining_content(articles):
    d={}
    l=[]
    for i in range(8):
        l.append({
            f"title":f"{articles[i]['title']}",
            f"url":f"{articles[i]['url']}",
            f"urlToImage":f"{articles[i]['urlToImage']}"
                  })
        
    

    # d={'Title0':f"{articles[0]['title']}",
    #     'Source0':f"Source: {articles[0]['source']['name']}",
    #     'Description0':f"Description: {articles[0]['description']}",
    #     'URL0':f"{articles[0]['url']}",
    #     'Content0':f"Content: {articles[0]['content']}",
    #     'urlToImage0':f"{articles[0]['urlToImage']}",

    #     'Title1':f"{articles[1]['title']}",
    #     'Source1':f"Source: {articles[1]['source']['name']}",
    #     'Description1':f"Description: {articles[1]['description']}",
    #     'URL1':f"{articles[1]['url']}",
    #     'Content1':f"Content: {articles[1]['content']}",
    #     'urlToImage1':f"{articles[1]['urlToImage']}",

    #     'Title2':f"{articles[2]['title']}",
    #     'Source2':f"Source: {articles[2]['source']['name']}",
    #     'Description2':f"Description: {articles[2]['description']}",
    #     'URL2':f"{articles[2]['url']}",
    #     'Content2':f"Content: {articles[2]['content']}",
    #     'urlToImage2':f"{articles[2]['urlToImage']}",

    #     'Title3':f"{articles[3]['title']}",
    #     'Source3':f"Source: {articles[3]['source']['name']}",
    #     'Description3':f"Description: {articles[3]['description']}",
    #     'URL3':f"{articles[3]['url']}",
    #     'Content3':f"Content: {articles[3]['content']}",
    #     'urlToImage3':f"{articles[3]['urlToImage']}",

    #     'Title4':f"{articles[4]['title']}",
    #     'Source4':f"Source: {articles[4]['source']['name']}",
    #     'Description4':f"Description: {articles[4]['description']}",
    #     'URL4':f"{articles[4]['url']}",
    #     'Content4':f"Content: {articles[4]['content']}",
    #     'urlToImage4':f"{articles[4]['urlToImage']}",

    #     'Title5':f"{articles[5]['title']}",
    #     'Source5':f"Source: {articles[5]['source']['name']}",
    #     'Description5':f"Description: {articles[5]['description']}",
    #     'URL5':f"{articles[5]['url']}",
    #     'Content5':f"Content: {articles[5]['content']}",
    #     'urlToImage5':f"{articles[5]['urlToImage']}",

    #     'Title6':f"{articles[6]['title']}",
    #     'Source6':f"Source: {articles[6]['source']['name']}",
    #     'Description6':f"Description: {articles[6]['description']}",
    #     'URL6':f"{articles[6]['url']}",
    #     'Content6':f"Content: {articles[6]['content']}",
    #     'urlToImage6':f"{articles[6]['urlToImage']}",

    #     'Title7':f"{articles[7]['title']}",
    #     'Source7':f"Source: {articles[7]['source']['name']}",
    #     'Description7':f"Description: {articles[7]['description']}",
    #     'URL7':f"{articles[7]['url']}",
    #     'Content7':f"Content: {articles[7]['content']}",
    #     'urlToImage7':f"{articles[7]['urlToImage']}"
    #     }
    # return d
    return l
def defining_category(category):
    base_url = 'https://newsapi.org/v2/top-headlines'
    api_key = '01de3fa5d332484ebebf88d15c797288'  # Replace with your actual News API key
    language = 'en'   # Language of the news articles
    sort_by = 'top'  # Sort articles by published date
    page_size = 1     # Number of articles to fetch

    # Define the request parameters
    params = {
        'country':'in',
        'apiKey': api_key,
        'category':category
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

    d=defining_content(articles)
    return d
def home(request):
    global d1
    if request.method=="POST":
        query = request.POST.get('query')
        base_url = 'https://newsapi.org/v2/everything'
        api_key = '2999889420de4fe8b30dcf0abec97f5e'  # Replace with your actual News API key
        language = 'en'   # Language of the news articles
        sort_by = 'publishedAt'  # Sort articles by published date
        page_size = 10    # Number of articles to fetch

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
            l=defining_content(articles)
            return render(request,"index.html",{'l':l})
    l=defining_category("general")
    context={
        'l':l,
    }
    return render(request,"index.html",context)
    # except:
    #     return render(request,"index.html")
# print(query)
# Define the base URL and parameters for the News API
def news(request):
        return render(request,"news.html",d1)

def entertainment(request):
    d=defining_category("entertainment")
    return render(request,"entertainment.html",{'l':d})


base_url = 'https://newsapi.org/v2/top-headlines'
api_key = '01de3fa5d332484ebebf88d15c797288'  # Replace with your actual News API key
language = 'en'   # Language of the news articles
sort_by = 'top'  # Sort articles by published date
page_size = 1     # Number of articles to fetch

# Define the request parameters
params = {
    'country':'in',
    'apiKey': api_key,
    'category':"general"
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

defining_content(articles)