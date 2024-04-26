from newsdataapi import NewsDataApiClient
api=NewsDataApiClient('pub_409074342cf7f578fddcd193b070dc6282da5')
response=api.news_api(q="cricket",language="en",size=1,country="in")
data=response['results']
d={'Title':f"{data[0]['title']}",
'Description':f"Description: {data[0]['description']}",
'URL':f"{data[0]['link']}",
'Content':f"Content: {data[0]['content']}",
'urlToImage':f"{data[0]['image_url']}"
}
for i in d.keys():
    print(d.get(i))





# from urllib.request import urlopen
# import requests
# from bs4 import BeautifulSoup
# import urllib.parse
# from openai import OpenAI
# from newsdataapi import NewsDataApiClient

# # headers={
# #     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0',

# # }

# api_key = '01de3fa5d332484ebebf88d15c797288'  # Replace with your actual News API key
# api=NewsDataApiClient(apikey='pub_409074342cf7f578fddcd193b070dc6282da5')
# language = 'en'   # Language of the news articles
# sort_by = 'publishedAt'  # Sort articles by published date
# page_size = 1    # Number of articles to fetch

# # Define the request parameters
# params = {
#     'q': "cricket",
#     'language': language,
#     'sortBy': sort_by,
#     'pageSize': page_size,
#     'apiKey': api_key
# }
# base_url = f'https://newsdata.io/api/1/news?apikey=pub_409074342cf7f578fddcd193b070dc6282da5&q=finance&language=en'
# # Send a GET request to the News API
# response = api.news_api(q='cricket',scroll=True,max_result=1)
# print(response)
# Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the JSON response
#     data = response.json()
#     articles = data['results']
# else:
#     print("Failed to fetch news articles. Status code:", response.status_code)
# print(articles[0]['title'])
# l=articles[0]['link']
# print(l)
# response=requests.get(l,headers=headers)
# content=response.content
# soup=BeautifulSoup(response.content,"html.parser")
# text=soup.find_all('p')
# print(text)



