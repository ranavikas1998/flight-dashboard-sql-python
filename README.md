#  Flight Analytics Dashboard — SQL + Python + Streamlit

*Visualize flight data in real time with SQL-powered insights and a sleek Streamlit interface.*

---

##  Overview
This project is an interactive **Flight Analytics Dashboard**, designed to analyze and visualize flight-related data using **Python**, **SQL**, and **Streamlit**. Monitor trends, identify inefficiencies, and gain insights through engaging charts and visualizations.

---

##  Key Features
-  Connects to a SQL database (e.g., sql server ) to fetch flight data.
-  Displays metrics like flight counts, delays, average airtime, and route frequencies.
-  Interactive filters for airline name, origin/destination airport, or date ranges.
-  Dynamic visualizations using **Plotly** (bar charts, line charts, maps).
-  Live updates upon filter changes via Streamlit's reactive interface.

---

##  Tools & Technologies
- **Python**
  - `pandas`, `numpy` → Data manipulation
  - `sqlalchemy` / `pyodbc` → SQL connectivity
  - `streamlit` → Web dashboard framework
  - `plotly` → Interactive plotting
- **SQL Database** (e.g.,sql  server ) for structured storage
- **Jupyter Notebook** for EDA (optional)

---

##  Project Structure
```
flight-dashboard-sql-python/
├── data/                # SQL schema files and sample CSVs (if any)
├── notebooks/           # Jupyter notebooks for exploration
├── app.py               # Main Streamlit dashboard script
├── requirements.txt     # Project dependencies
└── README.md            # Dashboard documentation
```

---

##  How to Run
1. **Clone the repo**  
   ```bash
   git clone https://github.com/ranavikas1998/flight-dashboard-sql-python.git
   cd flight-dashboard-sql-python
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure database connection**  
   Update the connection string in `app.py` or create a `.env` file with credentials:
   ```env
   DATABASE_URL="postgresql://username:password@host:port/dbname"
   ```

4. **Run the dashboard**  
   ```bash
   streamlit run app.py
   ```

5. **Open your browser** at the local URL shown in the terminal.

---

##  Sample Dashboard Features
- Summary KPIs: Total flights, average delay, etc.
- Trend charts: Daily flight counts or average airtime.
- Route maps: Visualize popular origin–destination pairs.
- Data tables: Filtered flight records in tabular form.

---

##  Data Sources
- Real airline or flight log datasets
- Public datasets (e.g., OpenFlights, Kaggle flight data)
- Custom SQL database populated with flight records

---

##  Contributing
Contributions, bug fixes, and enhancements are welcome!
- Fork the repo  
- Create a new branch (`feature/awesome-feature`)  
- Commit changes and open a Pull Request

---

**Author:** *Vikas Rana*  
**GitHub:** [ranavikas1998](https://github.com/ranavikas1998)  
