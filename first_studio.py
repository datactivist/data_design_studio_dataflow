#!/usr/bin/env python
# coding: utf-8

# Import modules
import streamlit as st
import pandas as pd
import numpy as np
import requests
import json
import openai
import random


#Setting titles
st.title("Dataflow design studio")
st.markdown('<p style="font-size:25px">Statistics are just <b style="color:blue">one face</b> of reality</p>', unsafe_allow_html=True)


# Step 2: Connect to the ChatGPT API
@st.cache
def query_chatgpt(prompt):
    api_key = st.secrets["API_KEY"]
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'system', 'content': 'You are a human-data interaction designer that can explain to a five year old children some insights about dataset.'},
                     {'role': 'user', 'content': prompt}],
        'temperature': 0.7
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_json = response.json()
    print(response_json)
    answer = response_json['choices'][0]['message']['content']
    return answer


# Step 3: Prepare the prompt
@st.cache
def prepare_prompt(data):
    prompt = f"Tell me what are the two most pertinent columns/variables to understand the dataset and explain to me why. Create one sentence (max 20 words long) for each variable and use metaphors to explain. Space the two sentences:\n\n{data}"
    return prompt

# Step 4: Send the prompt to ChatGPT
@st.cache
def send_prompt_to_chatgpt(prompt):
    answer = query_chatgpt(prompt)
    return answer

# Step 5: Display the response
@st.cache
def display_response(response):
    words = response.split()  # Split the response into individual words
    colored_response = ""

    # Define a list of colors to assign to each word
    colors = ["red", "blue", "green", "orange", "purple"]

    # Iterate over each word and apply a different color
    for i, word in enumerate(words):
        color = colors[i % len(colors)]  # Use modulo operator to cycle through colors
        colored_word = f'<span style="color: {color};">{word}</span>'
        colored_response += colored_word + " "

    st.markdown(f'<div style="font-size: 14px; margin-bottom: 20px; font-weight: bold;">{colored_response}</div>', unsafe_allow_html=True)



# Streamlit app code
st.subheader('Throw your messy, queasy fabric in !')

# Create three columns for the file uploaders
col1, col2, col3 = st.columns(3)

# File uploader in the first column
with col1:
    uploaded_file1 = st.file_uploader("Fabric 1b")
    if uploaded_file1 is not None:
        @st.cache
        def load_data1():
            dataframe1 = pd.read_csv(uploaded_file1, nrows=10)
            return dataframe1

        dataframe1 = load_data1()
        first_10_rows1 = dataframe1.head(10)
        
        # Apply random color styling to the dataframe
        styled_dataframe1 = first_10_rows1.style.applymap(lambda x: 'background-color: #{:06x}'.format(random.randint(0, 256**3-1)))
        
        prompt1 = prepare_prompt(first_10_rows1)
        response1 = send_prompt_to_chatgpt(prompt1)
        
        st.write(styled_dataframe1)  # Display the styled dataframe
        display_response(response1)

# File uploader in the second column
with col2:
    uploaded_file2 = st.file_uploader("Fabric 2b")
    if uploaded_file2 is not None:
        @st.cache
        def load_data2():
            dataframe2 = pd.read_csv(uploaded_file2, nrows=10)
            return dataframe2

        dataframe2 = load_data2()
        first_10_rows2 = dataframe2.head(10)
        
        # Apply random color styling to the dataframe
        styled_dataframe2 = first_10_rows2.style.applymap(lambda x: 'background-color: #{:06x}'.format(random.randint(0, 256**3-1)))
        
        prompt2 = prepare_prompt(first_10_rows2)
        response2 = send_prompt_to_chatgpt(prompt2)
        
        st.write(styled_dataframe2)  # Display the styled dataframe
        display_response(response2)

# File uploader in the third column
with col3:
    uploaded_file3 = st.file_uploader("Fabric 3b")
    if uploaded_file3 is not None:
        @st.cache
        def load_data3():
            dataframe3 = pd.read_csv(uploaded_file3, nrows=10)
            return dataframe3

        dataframe3 = load_data3()
        first_10_rows3 = dataframe3.head(10)
        
        # Apply random color styling to the dataframe
        styled_dataframe3 = first_10_rows3.style.applymap(lambda x: 'background-color: #{:06x}'.format(random.randint(0, 256**3-1)))
        
        prompt3 = prepare_prompt(first_10_rows3)
        response3 = send_prompt_to_chatgpt(prompt3)
        
        st.write(styled_dataframe3)  # Display the styled dataframe
        display_response(response3)





