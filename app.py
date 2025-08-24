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

    city, frequency1 = db.busy_airport()
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

    date, frequency = db.daily_frequency()
    # line chart
    lin_fig = go.Figure(
        data=[go.Scatter(
            x=date,
            y=frequency,
            mode="lines",  # line chart
            line=dict(color="blue", width=2)
        )]
    )

    st.header("Daily number of flights (Line Chart filtered by airlines)")
    st.plotly_chart(lin_fig)

else:
    st.title("Tell about the Project")

    st.markdown("""
    ## ✈️ Flight Analytics Dashboard  

    This is a data analytics project built with **Python, SQL Server, Pandas, Plotly, and Streamlit**.  

    ### 🔹 Features
    - Search flights between **Source** and **Destination** cities  
    - View **airline-wise frequency** of flights (Pie Chart)  
    - Check **busiest airports** (Bar Chart)  
    - Analyze **daily flight trends** (Line Chart)  

    ### 🔹 Tech Stack
    - **Database**: SQL Server  
    - **Backend**: Python (PyODBC, Pandas, SQLAlchemy)  
    - **Frontend/Dashboard**: Streamlit + Plotly  

    ### 🔹 How it Works
    1. Flight dataset is imported into **SQL Server**  
    2. SQL queries fetch required data  
    3. Python + PyODBC connect SQL Server with Streamlit  
    4. Data is visualized using **Plotly charts**  

    ### 🔹 Future Enhancements
    - Add filters for **price, duration, airlines**  
    - Compare flights across multiple routes  
    - Deploy the dashboard on **Streamlit Cloud / Azure**  
    """)

    st.info("💡 This project is part of my portfolio to demonstrate SQL + Python + Streamlit integration.")



