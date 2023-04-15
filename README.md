# Webscraping train accidents from Wikipedia

The aim for this project was to webscrape all train accident articles from Wikipedia, and then create visualisation and a user interface with Dash and Plotly. 
This project is divided into 4 parts in four notebooks.

## Objective for each notebook

[![Open in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Julardzija/Train-project/blob/main/Notebooks/1WebscrapingTrainAccidents.ipynb)
**Notebook 1: Webscraping** 


* Data Gathering: Crawl all Wikipedia articles on railway accidents, using the corresponding page for 1815 as a starting point: 
     https://en.wikipedia.org/wiki/Category:Railway_accidents_in_1815
     
* Find a strategy to exclude articles that do not directly refer to accidents.

* Data Storage: Store the retrieved information in a CSV file. For each railway accident I store the following information in columns: 
     - Date
     - Location
     - Coordinates (if available)
     - Cause
     - Number of deaths
       
       
[![Open in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Julardzija/Train-project/blob/main/Notebooks/2CleaningData.ipynb)       
**Notebook 2: Cleaning data**

* Cleaning all the data scraped from the first notebook. Every column is handled one by one to ensure the data is ready for the visualisation

[![Open in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Julardzija/Train-project/blob/main/Notebooks/3EnrichData.ipynb)
**Notebook 3: Enriching data**

* Add coordinates to train accidents that has location information but is missing coordinates 

[![Open in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Julardzija/Train-project/blob/main/Notebooks/4VisualisingTrainAccidents.ipynb)
**Notebook 4: Visualising data** 


* Data Analysis and User Interface: Create a graphical user interface with Dash/Plotly that supports the following functionalities:
     - plot all accidents on a map with one dot per incident and a color that indicates the instrument category
     - count the numbers of deaths through railway accidents per decade and 
     - generate a time-based line chart that shows the temporal development
     - display a summary of all accident causes in a word cloud




This was an exam project in the course "Programming for Data Science" where we had to show and present the final results in an oral exam.


You can open my code by clicking on the URL: 




