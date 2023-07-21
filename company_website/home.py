import streamlit as st
import pandas

st.set_page_config(layout='wide')
st.header("The Best Company")
content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Donec scelerisque viverra eros sit amet feugiat. 
Ut et tortor maximus, vehicula felis non, iaculis odio. 
Pellentesque suscipit iaculis ante, quis accumsan tortor. 
Praesent condimentum a ligula ac vestibulum. 
Aenean rhoncus facilisis purus vel porta. Nam lacinia ultrices sem ut blandit. 
"""

st.write(content)

st.subheader("Our Team")
df = pandas.read_csv('company_data.csv')
print(df)
col1, col2, col3 = st.columns(3)
with col1:
    for index, row in df[:4].iterrows():
        print(row['first name'])
        name = f"{row['first name']} {row['last name']}"
        st.subheader(name.title())
        st.write(row['role'])
        st.image(f"images/{row['image']}")

with col2:
    for index, row in df[4:8].iterrows():
        name = row['first name'] + ' ' + row["last name"]
        st.subheader(name.title())
        st.write(row['role'])
        st.image(f"images/{row['image']}")

with col3:
    for index, row in df[8:].iterrows():
        name = row['first name'] + ' ' + row["last name"]
        st.subheader(name.title())
        st.write(row['role'])
        st.image(f"images/{row['image']}")
