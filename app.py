import streamlit as st
from dbhelper import DB

db=DB()

st.sidebar.title("Flights Analytics")

user_option=st.sidebar.selectbox('Menu',['Select One','Check Flights','Analytics'])

if user_option =="Check Flights":
    st.title("Check Flights")

    col1,col2=st.columns(2)
    city = db.fetch_city_names()

    with col1:
        source=st.selectbox("source",sorted(city))
    with col2:
        destination= st.selectbox("Destination", sorted(city))

    if st.button("Search"):
        results=db.fetch_all_flights(source,destination)
        st.dataframe(results)

elif user_option =="Analytics":
    st.title("Analytics")
else:
    st.title("Tell about the  Project")

