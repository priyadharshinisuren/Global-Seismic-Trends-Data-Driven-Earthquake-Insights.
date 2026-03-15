import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from numpy.random import default_rng as rng
db_URL = "postgresql://postgres:root@localhost:5432/earthquake"
engine = create_engine(db_URL)
r = st.sidebar.radio('Navigation', ['Home','Analysis'])
if r == 'Home':
  st.title("Global Seismic Trends: Data-Driven Earthquake Insights")

  df = pd.read_csv("C:/Users/priya/OneDrive/Desktop/datascience/earthquake/earthquakes.csv")
  st.map(df)

elif r =='Analysis':
  select =st.selectbox("Select analysis", ["Magnitude & Depth", "Time Analysis","Event Type & Quality Metrics","Tsunamis","Seismic Pattern & Trends Analysis","Depth, Location & Distance-Based Analysis"],width="stretch")
  if select == "Magnitude & Depth":
      query = """SELECT  "id","place","mag"
        FROM driven
        ORDER BY 
        "mag" DESC
        LIMIT 10;"""
      df = pd.read_sql_query(query, engine)
      st.write("1.Top 10 strongest earthquakes (mag)")
      st.dataframe(df)
    ######################################
      query="""SELECT 
        "id",
        "place",
        "depth_km"
        FROM 
          driven
        ORDER BY 
         "depth_km" DESC
            LIMIT 10;""" 
      df = pd.read_sql_query(query, engine)
      st.write("2.Top 10 deepest earthquakes (depth_km)")
      st.dataframe(df)
      ################################################
      query="""SELECT "id","place","mag","depth_km" FROM 
         driven
        WHERE 
         "depth_km" < 50
         AND "mag" > 7.5
        ORDER BY 
        "mag" DESC;"""
      df = pd.read_sql_query(query, engine)
      st.write("3. Shallow earthquakes < 50 km and mag > 7.5.")
      st.dataframe(df)
    ###############################################################
      query="""SELECT 
     "place",
        AVG("depth_km") AS avg_depth_km
        FROM 
      driven
        GROUP BY 
     "place"
        ORDER BY 
     avg_depth_km DESC;"""
      df = pd.read_sql_query(query, engine)
      st.write("4. Average depth per continent.")
      st.dataframe(df)
      ########################################################
      query="""SELECT 
        "magType",
        AVG("mag") AS avg_magnitude
        FROM 
         driven
        GROUP BY 
         "magType"
        ORDER BY 
        avg_magnitude DESC;"""
      df = pd.read_sql_query(query, engine)
      st.write("5. Average magnitude per magnitude type (magType).")
      st.dataframe(df)
      ##############################
  elif select == "Time Analysis":  
      query="""SELECT 
      year,
      COUNT(*) AS earthquake_count
      FROM driven
      GROUP BY year
      ORDER BY year 
      LIMIT 5;"""
      df = pd.read_sql_query(query, engine)
      st.write("6. Year with most earthquakes.")
      st.table(df)
      ############################################
      query="""SELECT 
      month,
      COUNT(*) AS earthquake_count
      FROM driven
      GROUP BY month
      ORDER BY month 
      LIMIT 5;"""
      df = pd.read_sql_query(query, engine)
      st.write("7.Month with highest number of earthquakes.")
      st.table(df)
      ##########################################
      query="""SELECT 
      day_of_week,
      COUNT(*) AS earthquake_count
      FROM driven
      GROUP BY day_of_week
      ORDER BY day_of_week
      LIMIT 5;"""
      df = pd.read_sql_query(query, engine)
      st.write("8. Day of week with most earthquakes.")
      st.table(df)
      ###################################################################
      query="""SELECT 
      time,
      COUNT(*) AS earthquake_count
      FROM driven
      GROUP BY time
      ORDER BY time;"""
      df = pd.read_sql_query(query, engine)
      st.write("9.Count of earthquakes per hour of day.")
      st.table(df)
      #####################################################################
      query="""SELECT 
        net,
      COUNT(*) AS earthquake_count
      FROM driven
      GROUP BY net
      ORDER BY earthquake_count DESC
      LIMIT 10;"""
      df = pd.read_sql_query(query, engine)
      st.write("10. Most active reporting network (net).")
      st.table(df)
      ################################################################
  elif select== "Event Type & Quality Metrics":
       query="""SELECT 
      status,
       COUNT(*) AS earthquake_count
        FROM driven
      GROUP BY status
      ORDER BY earthquake_count DESC;"""
       df = pd.read_sql_query(query, engine)
       st.write("11. Count of reviewed vs automatic earthquakes (status).")
       st.table(df)
       ############################################################
       query="""SELECT 
       type,
       COUNT(*) AS earthquake_count
      FROM driven
      GROUP BY type
      ORDER BY earthquake_count DESC;"""
       df = pd.read_sql_query(query, engine)
       st.write("12. Count by earthquake type (type).")
       st.table(df)
       ######################################################
       query="""SELECT 
       types,
        COUNT(*) AS earthquake_count
        FROM driven
        GROUP BY types
        ORDER BY earthquake_count DESC
        limit 10;"""
       df = pd.read_sql_query(query, engine)
       st.write("13. Number of earthquakes by data type (types).")
       st.table(df)
       #################################################
       query="""SELECT 
       place,
       AVG(rms) AS avg_rms,
        AVG(gap) AS avg_gap
        FROM driven
       GROUP BY place
        ORDER BY place;"""
       df = pd.read_sql_query(query, engine)
       st.write("14. Average RMS and gap per continent.")
       st.table(df)
       #################################################
       query="""SELECT 
        id,
         place,
        nst,
          mag,
          time
          FROM driven
        WHERE nst > 50
        ORDER BY nst DESC;"""
       df = pd.read_sql_query(query, engine)
       st.write("15. Events with high station coverage (nst > threshold).")
       st.table(df)
       ######################################################
  elif select == "Tsunamis":   
       query="""SELECT 
        year,
        COUNT(*) AS tsunami_count
        FROM driven
        WHERE tsunami = 1
        GROUP BY year
        ORDER BY year;"""
       df = pd.read_sql_query(query, engine)
       st.write("16. Number of tsunamis triggered per year.")
       st.table(df)
       ############################################################
  elif select == "Seismic Pattern & Trends Analysis":
       query="""SELECT 
        place,
        ROUND(AVG(mag)::numeric, 2) AS avg_magnitude
        FROM driven
        WHERE time >= NOW() - INTERVAL '10 years'
        GROUP BY place
        ORDER BY avg_magnitude DESC
        LIMIT 5;"""
       df = pd.read_sql_query(query, engine)
       st.write("17.Find the top 5 countries with the highest average magnitude")
       st.table(df)
       #############################################
       query="""SELECT 
     place,
    DATE_TRUNC('month', time) AS month
      FROM driven
      GROUP BY place, DATE_TRUNC('month', time)
    HAVING COUNT(DISTINCT earthquake_flag) = 2
    ORDER BY place, month;"""
       df = pd.read_sql_query(query, engine)
       st.write("18.Find countries that have experienced both shallow and deep earthquakes within the same month.")
       st.table(df)
       ###################################
       query="""WITH yearly_counts AS (
        SELECT 
        year,
        COUNT(*) AS total_quakes
        FROM driven
         GROUP BY year
        )
        SELECT 
        year,
        total_quakes,
       LAG(total_quakes) OVER (ORDER BY year) AS prev_year_quakes,
        ROUND(
        CASE 
            WHEN LAG(total_quakes) OVER (ORDER BY year) IS NULL THEN NULL
            ELSE ((total_quakes - LAG(total_quakes) OVER (ORDER BY year))::numeric 
                  / LAG(total_quakes) OVER (ORDER BY year)) * 100
        END, 2
          ) AS yoy_growth_rate
        FROM yearly_counts
        ORDER BY year;"""
       df = pd.read_sql_query(query, engine)
       st.write("19.Compute the year-over-year growth rate in the total number of earthquakes globally.")
       st.table(df)
       ##############################################################
       query="""SELECT 
        place,
         quake_count,
         avg_magnitude,
         activity_score
          FROM ranked
          ORDER BY activity_score DESC
          LIMIT 3;"""
       df = pd.read_sql_query(query, engine)
       st.write("20. List the 3 most seismically active regions by combining both frequency and average magnitude.")
       st.table(df)
       ##############################################
  elif select == "Depth, Location & Distance-Based Analysis": 
       query="""SELECT 
        place,
         ROUND(AVG(depth_km)::numeric, 2) AS avg_depth
          FROM driven
          WHERE latitude BETWEEN -5 AND 5
            GROUP BY place
            ORDER BY avg_depth DESC;""" 
       df = pd.read_sql_query(query, engine)
       st.write("21. For each country, calculate the average depth of earthquakes within ±5° latitude range of the equator.")
       st.table(df)
       #############################################################################
       query="""SELECT 
        CASE 
        WHEN tsunami = 1 THEN 'with_tsunami'
        ELSE 'without_tsunami'
        END AS alert_group,
          ROUND(AVG(mag)::numeric, 2) AS avg_magnitude
          FROM driven
        GROUP BY alert_group;"""
       df = pd.read_sql_query(query, engine)
       st.write("22. Find the average magnitude difference between earthquakes with tsunami alerts and those without.")
       st.table(df)
       #####################################################################
       query="""SELECT 
        place,
        time,
       ROUND(((gap + rms)::numeric / 2), 2) AS avg_error_margin
      FROM driven
      ORDER BY avg_error_margin DESC
      LIMIT 10;"""
       df = pd.read_sql_query(query, engine)
       st.write("23. Using the gap and rms columns, identify events with the lowest data reliability(highest average error margins).")
       st.table(df)
       #####################################################################
       query="""SELECT 
        place,
        COUNT(*) AS deep_quake_count
        FROM driven
        WHERE depth_km > 300
        GROUP BY place
        ORDER BY deep_quake_count DESC
        LIMIT 10;"""
       df = pd.read_sql_query(query, engine)
       st.write("24. Determine the regions with the highest frequency of deep-focus earthquakes depth > 300 km).")
       st.table(df)
       
       

       
       
       
       
          
       
       
       
       
       

       
      
    
    