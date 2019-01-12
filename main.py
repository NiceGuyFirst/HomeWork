# using requests to get the html page.
import requests
# using BeautifulSoup to parse html pages.
# install using: pip install beautifulsoup4
from bs4 import BeautifulSoup
# using json to dump the data into a json file
import json

# this is the URL that will be parsed
URL = "https://weather.com/weather/hourbyhour/l/ISXX0026:1:IS"

# in the data we will save all the collected information.
data = {}

# Get the page content
a = requests.get(URL)
#Parse the content
sop = BeautifulSoup(a.content, "html.parser")

# get only the table content
table = sop.tbody

# Loop over each table row
for row in table.find_all("tr"):
    # Extract row data
    time = row.find(headers="time")
    time = time.find(class_="dsx-date").text
    
    description = row.find(headers="description").find("span").text
    temp = row.find(headers="temp").find("span").text
    feels = row.find(headers="feels").find("span").text
    precip = row.find(headers="precip").find_all("span")[1].find("span").text
    humidity = row.find(headers="humidity").find("span").text
    wind = row.find(headers="wind").find("span").text
    
    # save all the data is dictionary
    data[time] = {"description": description, "temp": temp, "feels": feels, "precip":precip, "humidity": humidity, "wind":wind }

# save the collected data as json file.
with open("data.json", "w") as f:
    json.dump(data, f)

print "Done"
