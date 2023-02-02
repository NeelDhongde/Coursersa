#import html5lib as html5lib
#import mamba
#import pip
#import requests
from bs4 import BeautifulSoup # to help in web scarpping
import  requests # to down a web page

html="<!DOCTYPE html><html><head><title>Coursera</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
soup = BeautifulSoup(html, "html.parser")

print(soup.prettify()) # to display the code in nested structure

#tag_object = soup.title
#print("tag object:", tag_object)
#print("tag object type:", type(tag_object))

tag_object = soup.h3
print(tag_object)
tag_child = tag_object.b
print(tag_child)
tag_object.parent
print(tag_object.parent)

sibling_1=tag_object.next_sibling
print(sibling_1)

sibling_2 = sibling_1.next_sibling
print(sibling_2)

sal = sibling_2.next_sibling
print(sal)

#child = tag_child['id']
#print(child)

#saw = tag_child.attrs
#print(saw)

#value = tag_child.get('id')
#print(value)

#tag_string=tag_child.string
#print(tag_string)

#qwe = type(tag_string)
#print(qwe)

#unicode_string = str(tag_string)
#print(unicode_string)

table = "<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table_bs = BeautifulSoup(table, "html.parser")

table_rows = table_bs.find_all('tr')
print(table_rows)

first_row = table_rows[0]
print(first_row)
print(type(first_row))
rwo = first_row.td
print(rwo)

#for i, row in enumerate(table_rows):
 #   print("row", i, "is", row)


  #  for i, row in enumerate(table_rows):
   #     print("row", i)
    #    cells=row.find_all('td')
     #   for j, cell in enumerate(cells):
      #      print('column', j, "cell", cell)

#list = table_bs.find_all(["tr", 'td'])
#print(list)

#save = table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
#print(save)
#red = table_bs.find_all(href=True)
#print(red)

black = table_bs.find_all(href=False)
print(black)

yellow = soup.find_all(id = "boldest")
print(yellow)


blue = table_bs.find_all(string="Florida")
print(blue)

two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"
two_tables_bs = BeautifulSoup(two_tables, "html.parser")

two_tables_bs.find_all("table")
print(two_tables_bs)

green = two_tables_bs.find("table",class_='pizza')
print(green)

url = "http://www.ibm.com"
data = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")  # create a soup object using the variable 'data
for link in soup.find_all('a', href=True):
    print(link.get('href'))

    for link in soup.find_all('img'):
        print(link)
        print(link.get('src'))

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
data = requests.get(url).text
soup = BeautifulSoup(data, "html.parser")
print(soup)
table = soup.find('table')
print(table)

#for row in table.find_all('tr'):
 #   cols = row.find_all('td')
  #  color_name = cols[2].string
   # color_code = cols[3].string
   # print("{}.......{}".format(color_name, color_code))

import  pandas as pd
url = "https://en.wikipedia.org/wiki/World_population"
data = requests.get(url).text
soup = BeautifulSoup(data, "html.parser")
tables = soup.find_all('table')
sad = len(tables)
print(sad)

for index, table in enumerate(tables):
    if("10 most densely populated" in str(tables)):
        table_index = index
        print(tables[table_index].prettify())

population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])

population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])

for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)

population_data


lase = pd.read_html(str(tables[5]), flavour='bs4')
print(lase)

population_data_read_html = pd.read_html(str(tables[5]), flavor='bs4')[0]

print(population_data_read_html)


