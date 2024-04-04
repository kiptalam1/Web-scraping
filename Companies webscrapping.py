import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, features='html.parser')

# finding the required table from the page
table = soup.find('table')
world_titles = table.find_all('th')[1:10]
#print(world_titles)
world_table_titles = [title.text.strip() for title in world_titles]
#print(world_table_titles)

# Create a dataframe for the dataset
# df stands for dataframe
import pandas as pd
df = pd.DataFrame(columns = world_table_titles)
print(df)

# finding the required columns from the table and adding to the df
column_data = table.find_all('tr')

# populating rows of the table to the dataframe
for row in column_data[2:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    #print(individual_row_data)
    length = len(df)
    df.loc[length] = individual_row_data
    
# dropping unwanted columns from the created dataframe
df.drop(columns= ['State-owned', 'Ref.'], inplace=True)    

# renaming column 
df.rename(columns={'Headquarters[note 1]':'Headquarters'}, inplace=True)
print(df)

# saving the dataset to the local storage
df.to_csv(r'C:\Users\q1\Documents\webscraping\Companies.csv')
