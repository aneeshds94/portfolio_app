import streamlit as st
import smtplib
import ssl

import pandas


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "aneeshiocl@gmail.com"
    password = "lrkljnbyswrgpttp"
    receiver = "aneeshiocl@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


df = pandas.read_csv("topics.csv")

with st.form(key='contact_form'):
    email = st.text_input("You Email Address")
    option = st.selectbox("What topic do you want to discuss?", df["topic"])
    text = st.text_area("Text", key="text")
    message = f"""\
Subject: New email from {email}

From: {email}
Topic : {option}
{text}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Email sent successfully!")