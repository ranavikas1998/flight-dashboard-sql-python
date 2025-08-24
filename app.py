import streamlit as st
from dbhelper import DB

db=DB()

st.sidebar.title("Flights Analytics")

user_option=st.sidebar.selectbox('Menu',['Select One','Check Flights','Analytics'])

if user_option =="Check Flights":
    st.title("Check Flights")

    col1,col2=st.columns(2)

    with col1:
        city=db.fetch_city_names()
        st.selectbox("source",sorted(city))
    with col2:
        st.selectbox("Destination", sorted(city))

    if st.button("Search"):
        pass

elif user_option =="Analytics":
    st.title("Analytics")
else:
    st.title("Tell about the  Project")

