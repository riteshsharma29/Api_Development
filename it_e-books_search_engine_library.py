import streamlit as st
import os
import requests
import pandas as pd
import streamlit.components.v1 as components

st.sidebar.title("IT E-Book Search Engine/Library")

# passing integer input
page_num = st.sidebar.number_input('Provide Page Number For Search', min_value=1)
# passing string input
keyword = st.sidebar.text_input("PROVIDE KEYWORD")
keyword = keyword.strip()

st.sidebar.success("Search IT e-books by providing page number and meaningful keyword !")

# api endpoint
endpoint = "https://api.itbook.store/1.0/search/"
# create search url
res = requests.get(endpoint + keyword + "/" + str(page_num))
content = res.json()['books']

# empty list for df
title = []
subtitle = []
price = []
image = []
url = []

for sub_con in content:
    title.append(sub_con['title'])
    subtitle.append(sub_con['subtitle'])
    price.append(sub_con['price'])
    image.append(sub_con['image'])
    url.append(sub_con['url'])

if len(keyword) > 0 and len(content) > 0:
    # st.sidebar.text_area("JSON Output", title, height=200)
    df = pd.DataFrame({"Title":title,"Subtitle":subtitle,"Price":price,"URL":url,"Cover Image":image})
    df.style.set_properties(subset=["Feature", "Value"], **{'text-align': 'center'}).hide(axis='index')
    # code to add html tags to image links
    df['Cover Image'] = '''<img src="''' + df['Cover Image'] + '''"width="80">'''
    # appending html content to file
    with open('source.html', 'w') as fo:
        fo.write(df.to_html(render_links=True, escape=False))

    # read source.html and adding align tags to header
    with open(os.path.join(os.getcwd(), 'source.html'),'r') as file:
        filedata = file.read()
        # Replace the target string
        filedata = filedata.replace('<th>Title</th>', '<th><center>Title</center></th>')
        filedata = filedata.replace('<th>Subtitle</th>', '<th><center>Subtitle</center></th>')
        filedata = filedata.replace('<th>Price</th>', '<th><center>Price</center></th>')
        filedata = filedata.replace('<th>URL</th>', '<th><center>URL</center></th>')
        filedata = filedata.replace('<th>Cover Image</th>', '<th><center>Cover Image</center></th>')

    # Write the file out again
    with open(os.path.join(os.getcwd(), 'output.html'), 'w') as file:
        file.write(filedata)

    # reading html source code and displaying using streamlit components
    HtmlFile = open("output.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    # print(source_code)
    components.html(source_code,width=800,height=1200)
#  error handling
elif len(keyword) > 0 and len(content) == 0:
    st.error("Please provide meaningful keyword and try again !!!")