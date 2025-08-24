import streamlit as st
from dbhelper import DB
import plotly.graph_objects as go

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
    airline,frequency=db.fetch_airlines_frequency()
    fig=go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo="label+percent",
            textinfo="value"
        ))

    st.header("Pie chart")
    st.plotly_chart(fig)

    city, frequency = db.busy_airport()
    # Bar chart
    bar_fig = go.Figure(
        data=[go.Bar(
            x=city,
            y=frequency,
            text=frequency,
            textposition="auto"
        )]
    )

    st.header("Busiest Airports (Bar Chart)")
    st.plotly_chart(bar_fig)


else:
    st.title("Tell about the  Project")

