import requests
import pandas as pd
import re # regular expression
import csv
import streamlit as st

from bs4 import BeautifulSoup

# HARDCODED VARIABLES
keyword = 'electrician' ## drop down that will review list
zipcode = '07657' ## text box / also need to validate it is a valid zip code
radius = '5' ## drop down that will review list

# Streamlit Section 

st.title('Super Pages Web Scraper')
st.write('This is a web scraper that will scrape the Super Pages website for electricians in your area.')
st.write('Please enter the following information:')

df = pd.read_csv('trades.csv')



Super_Pages_URL = f"https://www.superpages.com/search?search_terms={keyword}&geo_location_terms={zipcode}&page={radius}"
page = requests.get(Super_Pages_URL)



# Define the pattern you want to search for
#pattern = r'href="http://.*?"'
pattern = r'href="(http://.*?)"'

# Search for the pattern in the page text
matches = re.findall(pattern, page.text)

# Print the found matches

# now take this list of urls and insert them into a text file
# now we need to loop through the text file and scrape the data from each url
#print(webList[0]) # href="http://www.bvhelectric.com"

for match in matches:
    webList = []
    cleaned_url = match.replace('href="', '')
    #cleaned_url.rstrip('"')
    webList.append(cleaned_url)



webList

'''
def extract_urls(html):
   if html is None:
       return []
   soup = BeautifulSoup(html, 'html.parser')
   # Use a regular expression to match URLs
   url_pattern = re.compile(r'https?://\S+')
   urls = []
   
   for a_tag in soup.find_all('a', href=True):
       href = a_tag.get('href')
       # Filter out non-HTTP URLs and remove any fragments (#)
       if href and re.match(url_pattern, href) and not href.endswith('#'):
           urls.append(href)
   return urls


def extract_urls_with_class(html, class_name):
    if html is None:
        return []

    soup = BeautifulSoup(html, 'html.parser')
    # Use a regular expression to match URLs
    url_pattern = re.compile(r'https?://\S+')
    urls = []
    
    for a_tag in soup.find_all('a', href=True, class_=class_name):
        href = a_tag.get('href')
        # Filter out non-HTTP URLs and remove any fragments (#)
        if href and re.match(url_pattern, href) and not href.endswith('#'):
            urls.append(href)
    print(urls)
    return urls

'''