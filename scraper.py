import requests
import pandas as pd
import re # regular expression
import csv
import streamlit as st
from bs4 import BeautifulSoup
from streamlit.components.v1 import html


# HARDCODED VARIABLES
# keyword = 'electrician' ## drop down that will review list
# zipcode = '07657' ## text box / also need to validate it is a valid zip code
# radius = '5' ## drop down that will review list

# Streamlit Section 
st.title('Super Pages Web Scraper')
st.write('This is a web scraper that will scrape the Super Pages website for electricians in your area.')
st.write('Please enter the following information:')


# Read the CSV file into a DataFrame
df = pd.read_csv('./resources/trades.csv')  # Replace 'names.csv' with your actual CSV file name
# Get the list of names from the DataFrame
df = df['Link Text'].tolist()
# Create a Streamlit dropdown with the names
selected_catagory = st.selectbox('Select a category.', df)


# Display the selected name
st.write('Selected name:', selected_catagory)


# ZIP CODE SECTION
st.write('Please enter your zip code:')
# LOGIC FOR ZIPCODE
def validate_zip_code(zip_code):
    if len(zip_code) != 5 or not zip_code.isdigit():
        return False
    else:
        return True
# ZIP CODE TEXT BOX
zip_code = st.text_input("Enter a 5-digit number", max_chars=5)
if validate_zip_code(zip_code):
    st.write("The zip code you entered is:", zip_code)
else:
    st.write("Please enter a valid 5-digit number")


# RADIUS SECTION (Radio Buttons)

st.write('Please select a radius:')
radius = ['1 Mile', '5 Miles', '10 Miles', '15 Miles', '20 Miles']
selected_radius = st.radio('Select an option', radius)

if(selected_radius == '1 Mile'):
    pages = 1
elif(selected_radius == '5 Miles'):
    pages = 5
elif(selected_radius == '10 Miles'):
    pages = 10
elif(selected_radius == '15 Miles'):
    pages = 15
else:
    pages = 20

st.write('You selected:', selected_radius)
st.write('You selected:', pages)


# def embed_google_maps():
#     html_string = '''
#     <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d38785.70341915034!2d-74.00661089999999!3d40.7127753!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c2596b09e6cb75%3A0x62ed6fdb1164e0a7!2sNew%20York%2C%20NY%2C%20USA!5e0!3m2!1sen!2sus!4v1628525763669!5m2!1sen!2sus" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
#     '''
#     return html_string
# 
# def main():
#     st.title("My Streamlit App with Google Maps")
#     st.markdown("Here's a map of New York City:")
#     html_code = embed_google_maps()
#     html(html_code, width=700, height=500)
# 
# if __name__ == "__main__":
#     main()

if pages == 1:

# Read the CSV file into a DataFrame
    Super_Pages_URL = f"https://www.superpages.com/search?search_terms={selected_catagory}&geo_location_terms={zip_code}&page={pages}"
    
    page = requests.get(Super_Pages_URL)

    # Define the pattern you want to search for
    #pattern = r'href="http://.*?"'
    pattern = r'href="(http://.*?)"'
    
    # Search for the pattern in the page text
    matches = re.findall(pattern, page.text)

else:
    
    # Create a loop that will go through the pages and scrape the data just like the previous example
    

    all_matches = []

    for i in range(1, pages + 1):
        Super_Pages_URL = f"https://www.superpages.com/search?search_terms={selected_catagory}&geo_location_terms={zip_code}&page={i}"
        page = requests.get(Super_Pages_URL)
        pattern = r'href="(http://.*?)"'
        matches = re.findall(pattern, page.text)
        all_matches.extend(matches)

    df = pd.DataFrame({'Matches': all_matches})
    selected_catagory_no_space = selected_catagory.replace(' ', '_')
    df.to_csv(f'{selected_catagory_no_space}.csv', index=False)

        
    
    # use the super pages url and take the number givien by pages and iterate through the pages and scrape the data 
    # store all the data into a data frame 
    # print the data frame using stream lit
    
    
    

# now take this list of urls and insert them into a text file
# now we need to loop through the text file and scrape the data from each url
# Print the found matches
# print(webList[0]) # href="http://www.bvhelectric.com"

# Create a button
if st.button('Go'):
    for match in matches:
        webList = []
        cleaned_url = match.replace('href="', '')
        #cleaned_url.rstrip('"')
        webList.append(cleaned_url)
        st.write(webList)
    





# def extract_urls(html):
#    if html is None:
#        return []
#    soup = BeautifulSoup(html, 'html.parser')
#    # Use a regular expression to match URLs
#    url_pattern = re.compile(r'https?://\S+')
#    urls = []
#    
#    for a_tag in soup.find_all('a', href=True):
#        href = a_tag.get('href')
#        # Filter out non-HTTP URLs and remove any fragments (#)
#        if href and re.match(url_pattern, href) and not href.endswith('#'):
#            urls.append(href)
#    return urls


# def extract_urls_with_class(html, class_name):
#     if html is None:
#         return []
# 
#     soup = BeautifulSoup(html, 'html.parser')
#     # Use a regular expression to match URLs
#     url_pattern = re.compile(r'https?://\S+')
#     urls = []
#     
#     for a_tag in soup.find_all('a', href=True, class_=class_name):
#         href = a_tag.get('href')
#         # Filter out non-HTTP URLs and remove any fragments (#)
#         if href and re.match(url_pattern, href) and not href.endswith('#'):
#             urls.append(href)
#     print(urls)
#     return urls



# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# 
# # URL of the webpage to scrape
# url = 'https://www.superpages.com/categories/'
# 
# # Send an HTTP GET request to the URL
# response = requests.get(url)
# 
# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the HTML content using BeautifulSoup
#     soup = BeautifulSoup(response.text, 'html.parser')
# 
#     # Find all <a> tags
#     all_a_tags = soup.find_all('a')
# 
#     # Extract link text and store it in a list
#     link_texts = [a_tag.text for a_tag in all_a_tags]
# 
#     # Create a DataFrame from the list of link texts
#     df = pd.DataFrame({'Link Text': link_texts})
# 
#     # Save the DataFrame to a CSV file
#     df.to_csv('links.csv', index=False)
# 
#     print('Data has been saved to links.csv')
# else:
#     print(f"Failed to fetch the webpage. Status code: {response.status_code}")
    
