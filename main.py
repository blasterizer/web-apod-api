import streamlit as st
import requests

# Get API key from NASA Open APIs
api_key = "aCSVjCeBcNjf9aqHEWg7qZz1UNIjQnETlTTt8ov7"

url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# Get the request data as a dictionary
response1 = requests.get(url)
data = response1.json()

# Extract the image, title, explanation and url
title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

# Get the image FilePath
image_filepath = "img.png"
response2 = requests.get(image_url)
with open(image_filepath, "wb") as file:
    file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)




