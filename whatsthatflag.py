import requests
import json

url = "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles=List_of_flags_by_color_combination&explaintext=1&exsectionformat=wiki&formatversion=2"

response = requests.get(url)
data = response.json()

text_blob = data.get("query").get("pages")[0].get("extract")

print(text_blob)