from django.http import HttpResponse
from django.shortcuts import render,redirect
import requests
from newsdataapi import NewsDataApiClient
from service import  models
def defining_content(articles):
    d={}
    l=[]
    for i in range(16):
        l.append({
            f"title":f"{articles[i]['title']}",
            f"url":f"{articles[i]['url']}",
            f"urlToImage":f"{articles[i]['urlToImage']}"
                  })
    return l
def defining_category(category):
    base_url = 'https://newsapi.org/v2/top-headlines'
    api_key = '01de3fa5d332484ebebf88d15c797288'  # Replace with your actual News API key
    language = 'en'   # Language of the news articles
    sort_by = 'top'  # Sort articles by published date
    page_size = 20    # Number of articles to fetch

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
def defining_query(query):
    base_url = 'https://newsapi.org/v2/everything'
    api_key = '01de3fa5d332484ebebf88d15c797288'  # Replace with your actual News API key
    language = 'en'   # Language of the news articles
    sort_by = 'publishedAt'  # Sort articles by published date
    page_size = 20    # Number of articles to fetch

    # Define the request parameters
    params = {
        'q': query,
        'language': language,
        'sortBy': sort_by,
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
        return l
def home(request):
    interests=models.interest.objects.get(user=request.user)
    t=[]
    s=""
    if interests.science==True:
        t.append("science")
    if interests.technology==True:
        t.append("technology")
    if interests.sports==True:
        t.append("sports")
    if interests.finance==True:
        t.append("finance")
    if interests.education==True:
        t.append("education")
    if interests.entertainment==True:
        t.append("entertainment")
    if len(t)==0:
        m=defining_category("general")
        context={
            'l':m,
        }
        return render(request,"home.html",context)
    elif len(t)==1:
        s=t[0]
    elif len(t)==2:
        s=t[0]+" AND "+t[1]
    else:
        s=t[0]
        for i in range(1,len(t)):
            s=s+" AND "+t[i]
    # print(interests.user.username)
    if request.method=="POST":
        query = request.POST.get('query')
        base_url = 'https://newsapi.org/v2/everything'
        api_key = '01de3fa5d332484ebebf88d15c797288'  # Replace with your actual News API key
        language = 'en'   # Language of the news articles
        sort_by = 'publishedAt'  # Sort articles by published date
        page_size = 20   # Number of articles to fetch

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
            return render(request,"home.html",{'l':l,})
    l=defining_query(s)
    context={
        'l':l,
    }
    return render(request,"home.html",context)  

def index(request):
    global d1
    if request.method=="POST":
        query = request.POST.get('query')
        base_url = 'https://newsapi.org/v2/everything'
        api_key = '01de3fa5d332484ebebf88d15c797288'  # Replace with your actual News API key
        language = 'en'   # Language of the news articles
        sort_by = 'publishedAt'  # Sort articles by published date
        page_size = 20    # Number of articles to fetch

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

def save_interests(request):
    try:
        interests=models.interest.objects.get(user=request.user)
        if interests.checking==True:
            return redirect('home')
        else:
            if request.method=="POST":
                if (request.POST.get('science'))=="on":
                    science =True
                else:
                    science=False
                if request.POST.get('technology')=="on":
                    technology =True
                else:
                    technology=False
                if (request.POST.get('sports'))=="on":
                    sports =True
                else:
                    sports=False            
                if (request.POST.get('finance'))=="on":
                    finance =True
                else:
                    finance=False
                if (request.POST.get('education'))=="on":
                    education =True
                else:
                    education=False
                if (request.POST.get('entertainment'))=="on":
                    entertainment=True
                else:
                    entertainment=False
                interests=models.interest.objects.create(science=science,technology=technology,sports=sports,education=education,entertainment=entertainment,checking=True,user=request.user)
                return redirect('home')
    except:
        if request.method=="POST":
            if (request.POST.get('science'))=="on":
                science =True
            else:
                science=False
            if request.POST.get('technology')=="on":
                technology =True
            else:
                technology=False
            if (request.POST.get('sports'))=="on":
                sports =True
            else:
                sports=False            
            if (request.POST.get('finance'))=="on":
                finance =True
            else:
                finance=False
            if (request.POST.get('education'))=="on":
                education =True
            else:
                education=False
            if (request.POST.get('entertainment'))=="on":
                entertainment=True
            else:
                entertainment=False
            interests=models.interest.objects.create(science=science,technology=technology,sports=sports,education=education,entertainment=entertainment,checking=True,user=request.user)
            return redirect('home')
    return render(request,"interests.html")

def science(request):
    d=defining_category("science")
    return render(request,"science.html",{'l':d})

def technology(request):
    d=defining_category("technology")
    return render(request,"technology.html",{'l':d})

def sports(request):
    d=defining_category("sports")
    return render(request,"sports.html",{'l':d})

def finance(request):
    d=defining_category("business")
    return render(request,"finance.html",{'l':d})
def health(request):
    d=defining_category("health")
    return render(request,"health.html",{'l':d})

def entertainment(request):
    d=defining_category("entertainment")
    return render(request,"entertainment.html",{'l':d})