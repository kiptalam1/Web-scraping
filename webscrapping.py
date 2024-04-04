import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, features='html.parser')
table = soup.find('table')
world_titles = table.find_all('th')[1:10]
#print(world_titles)
world_table_titles = [title.text.strip() for title in world_titles]
#print(world_table_titles)


import pandas as pd
df = pd.DataFrame(columns = world_table_titles)
print(df)
column_data = table.find_all('tr')

for row in column_data[2:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    #print(individual_row_data)
    length = len(df)
    df.loc[length] = individual_row_data

df.drop(columns= ['State-owned', 'Ref.'], inplace=True)    
df.rename(columns={'Headquarters[note 1]':'Headquarters'}, inplace=True)
print(df)

df.to_csv(r'C:\Users\q1\Documents\webscraping\Companies.csv')