import streamlit as st
import requests

st.title("Amazing Weather Viewer")

city_name = input('Enter a City name: ')


city = st.text_input("City name", city_name)
if st.button("Get a weather report"):
    # Demo REST call using a free placeholder API
    url = "https://jsonplaceholder.typicode.com/posts?userId=3"
    resp = requests.get(url)
    resp.raise_for_status()            # 4xx / 5xx → exception
    data = resp.json()                 # list of dicts

    st.subheader("Raw JSON")
    st.json(data)

    # Show only titles
    st.subheader("Titles only")
    titles = [item["title"] for item in data]
    st.write(titles)