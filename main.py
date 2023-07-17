import streamlit as st

st.set_page_config(layout='wide')


col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png', width=350)

with col2:
    st.title("Aneesh D S")
    content = """
    Hi, I'm Aneesh, an aspiring python developer. I graduated in Mechanical Engineering 
    from University of Kerala. I'm currently working in the oil and gas industry. I had 
    always had a programming aptitude. This website showcases apps that I've coded as 
    part of an Udemy course by Ardit Sulce.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python.Feel free to contact me!
"""
st.write(content2)