import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyCdVsOk8b7qrXcAYsQ9UXgyDJL2cEGJW6c")
model = genai.GenerativeModel("gemini-pro")
st.title("แปลภาษา")
ch = st.selectbox("เลือกภาษาปลายทาง",("ไทย","อังกฤษ","เกาหลี","ญี่ปุ่น"))
text_in = st.text_input("ป้อนข้อความที่ต้องการแปล: ")
prompt = "แปลข้อความต่อไปนี้เป็นภาษา"+ ch + " " + text_in
st.text(prompt)
if st.button("แปล"):
    try:
        response = model.generate_content(prompt)
        st.text(response.text)
    except:
        st.text("no response")
        