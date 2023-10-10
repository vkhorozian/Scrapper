# import requests
# import re
# import streamlit as st
# from bs4 import BeautifulSoup
# 
# st.title('Email Collector')
# st.write('This app scrapes the web for email addresses')
# st.write('Enter a URL and click Go to begin')
# 
# # Regular expression pattern to capture email addresses within HTML content
# email_pattern = re.compile(r'\b[A-Za-z0-9.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b')
# 
# # Create a text box
# url = st.text_input('Enter a URL', key='url')
# 
# # Function to scrape the email addresses
# def scrape():
#     if url:
#         # Get the HTML from the URL
#         html_content = requests.get(url).text
#         
#         # Use BeautifulSoup to parse the HTML
#         soup = BeautifulSoup(html_content, 'html.parser')
#         
#         # Find specific elements that may contain email addresses
#         # You may need to adjust this based on the HTML structure of the webpage
#         elements_to_search = soup.find_all(['p', 'div', 'span', 'a'])
# 
#         found_emails = []
# 
#         # Find email addresses in each element
#         for element in elements_to_search:
#             element_text = element.get_text()
#             email_addresses = re.findall(email_pattern, element_text)
#             if email_addresses:
#                 found_emails.extend(email_addresses)
# 
#         # Display found email addresses in the app
#         if found_emails:
#             st.write("Found Email Addresses:")
#             for email in found_emails:
#                 st.write(email)
#         else:
#             st.write("No email addresses found on the webpage.")
# 
# # Create a button to trigger the scraping function
# if st.button('Go'):
#     scrape()



import csv
import requests
import re
import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup

st.title('Email Collector')
st.write('This app scrapes the web for email addresses')
st.write('Upload a CSV file with URLs and click Go to begin')

# Regular expression pattern to capture email addresses within HTML content
email_pattern = re.compile(r'\b[A-Za-z0-9.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b')

# Create a file input widget
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

# Function to scrape the email addresses
def scrape():
    if uploaded_file:
        # Open the CSV file in text mode
        csv_text = uploaded_file.read().decode("utf-8")
        csv_lines = csv_text.splitlines()

        found_emails = []

        # Iterate over each row in the CSV file
        csv_file = csv.reader(csv_lines)
        for row in csv_file:
            url = row[0]

            # Check if the URL is missing the scheme and prepend "https://" if needed
            if not re.match(r'http[s]?://', url):
                url = 'https://' + url

            try:
                # Get the HTML from the URL
                html_content = requests.get(url).text

                # Use BeautifulSoup to parse the HTML
                soup = BeautifulSoup(html_content, 'html.parser')

                # Find specific elements that may contain email addresses
                # You may need to adjust this based on the HTML structure of the webpage
                elements_to_search = soup.find_all(['p', 'div', 'span', 'a'])

                # Find email addresses in each element
                for element in elements_to_search:
                    element_text = element.get_text()
                    email_addresses = re.findall(email_pattern, element_text)
                    if email_addresses:
                        found_emails.extend(email_addresses)
            except Exception as e:
                st.write(f"Error scraping {url}: {str(e)}")

        # Create a dataframe from the found email addresses list
        df = pd.DataFrame(found_emails, columns=['Email'])

        # Drop duplicate email addresses
        df.drop_duplicates(inplace=True)

        # Print the dataframe
        st.dataframe(df)


# Create a button to trigger the scraping function
if st.button('Go'):
    scrape()

