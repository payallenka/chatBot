import streamlit as st
import google.generativeai as genai

#API configuration
genai.configure(api_key='AIzaSyCfZ6sArKBEnRpbWS3BjuRo0K2c_wjy6vI')


st.write("Hello")



user_input = st.text_input("Enter text")

if st.button("Enter"):
    st.write(f"you wrote {user_input}")
    response = genai.chat(messages=user_input)

    result = response.messages[1]['content']

    st.write(result)

