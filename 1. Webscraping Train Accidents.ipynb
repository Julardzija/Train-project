"""
Project 5: Railway Accidents
Part 1: webscraping

Objective for this part:
    "Data Gathering: Crawl all Wikipedia articles on railway accidents,
    use the corresponding page for 1815 as a starting point: 
    https://en.wikipedia.org/wiki/Category:Railway_accidents_in_1815
    Find a strategy to exclude articles that do not directly refer to accidents.

    Data Storage: Store the retrieved information in a CSV file. For each railway accident 
    store the following information in columns: 
    date, location, coordinates (if available), cause, and number of deaths
"""

# Importing necessary libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
from tqdm import tqdm

# Setting the URL and start year for data collection
URL = 'https://en.wikipedia.org/wiki/Category:Railway_accidents_in_'
START_YEAR = 1815


# Function to get a list of accident page URL´s for all years
def get_accidents(soup):
       # Finding all hyperlinks in the content area
    # This class (HTML) represents the section of wikipedia that deals with all the articles.
    # By finding all the "href" we find each URL for the articles.
    links = soup.find("div", {"class": "mw-content-ltr", 'dir':"ltr"}).find_all(href=True)
    hrefs = [l.get('href') for l in links]
    #Create empty list where we will save all the information
    filtered = []
    
# In this loop we make sure to exclude all unwanted links    
    for href in hrefs:
        if href.startswith('/wiki/Category') or href.startswith('/wiki/Wikipedia:FAQ'):
            pass
        
# Here we ensure to append the URLS we are interested in 
        elif href.startswith('/wiki/'):
            filtered.append(href)
            
# If there are no articles found, we call the pages for "no accidents"    
    if filtered[0] == '/wiki/Wikipedia:Categorization':
        return "No Accidents"
#We return the list of all the articles we are interested in
    return filtered


# This is a function to get the infobox data from a specific accident page.
# (Almost) all train accident pages have an infobx with all the relevant information we need.
def get_infobox(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'lxml')
    
# Here we create a simple filter by looking at the first paragraph of each article.
# If it does not include these words, we expect it to not be a page about a train accident.    
    num = 0
    text = ""
    for paragraph in soup.find_all('p', limit=2):
        text += paragraph.text
      
    if text.find("train") >= 0 or text.find("locomotive") >= 0 or text.find("rail") >= 0 or text.find("tram") >= 0:
        num += 1
    if text.find("accident") >= 0 or text.find("crash") >= 0 or text.find("wreck") >= 0 or text.find("derail") >= 0 or text.find("colli") >= 0 or text.find("disaster") >= 0 or text.find("injur") >= 0:
        num += 1

        
# Here we find the infobox and get the information if there is an infobox. 
# If there are no infobox we will get the output "no infobox"        
    if num == 2:
        table = soup.select_one('.infobox.vcard')
        title = soup.find("h1", {"id": "firstHeading"}).get_text()
      
        try:
            rows = table.find_all('tr')
            output = {}
            for row in rows:
                if len(row.select('th, td')) == 2:
                    key = row.select_one('th').text
                    value = row.select_one('td').text
                    output[key]=value
                    output["Accident title"] = title
        except:
            output = ("No infobox")
    else:
        output = ("not a train accident")
    
    return output


#Here we make a list of all the URL´s and webscrape them from 1815 until 2021
data = []
YEAR = START_YEAR
while YEAR <= 2021:
    r = requests.get(URL + str(YEAR))
    soup = BeautifulSoup(r.content, "html.parser")
    ACCIDENTS = get_accidents(soup)
    data.append([YEAR, ACCIDENTS])
    YEAR += 1



# Storing the data in a Pandas DataFrame

# Frist load data into dataframe
df = pd.DataFrame(data, columns = ['year', 'accident'])

# Then transforming each element of a list-like object to a row
# By using this function it makes several rows, one for each accident within the same year. 
df = df.explode('accident')

# Remove rows without accidents
df = df[df.accident != 'No Accidents']

# Add https://en.wikipedia.org/ to accident URL
df['accident_url'] = 'https://en.wikipedia.org/' + df.accident

# Reset index as we have removed the rows we labeled as "no accident"
df = df.reset_index()





# Adding progress bar for infobox extraction

tqdm.pandas()

# Applying the get_infobox function to each accident URL
# Allows us to retrieve the relevant data from each article by calling the infobox function
df['infobox'] = df.accident_url.progress_apply(get_infobox)




# Extracting specific infobox data into separate columns
df['Accident title'] = df.infobox.str['Accident title']
df['Date'] = df.infobox.str['Date']
df['Location'] = df.infobox.str['Location']
df['Coordinates'] = df.infobox.str['Coordinates'].str.split("/").str[-1]
df['Cause'] = df.infobox.str['Cause']
df['Deaths'] = df.infobox.str['Deaths']


# Saving the DataFrame to a CSV file
df.to_csv('WebscrapedTrainAccidents.csv', index=False, encoding='utf-8')


