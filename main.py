#from dotenv import load_dotenv
#load_dotenv()
from langchain_openai import ChatOpenAI
import streamlit as st

chat_model = ChatOpenAI()

st.title('Cahtgpt 시인')

title = st.text_input("주제 입력")
st.write("시의 주제는", title)

result = chat_model.predict(title+"에 대한 시를 써줘")

if st.button('시 작성 요청'):
   with st.spinner("시 작성 중...."):
      st.write(result)
