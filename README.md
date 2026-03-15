# Global-Seismic-Trends-Data-Driven-Earthquake-Insights.
Analyze and interpret global earthquake data to identify seismic patterns, trends, and risk zones. ● Build a data-driven system using API-based retrieval, preprocessing, and SQL analytics for meaningful earthquake insights

Business Use Cases:
● Enable governments, insurers, and researchers to assess earthquake risks, plan
disaster management strategies, and support informed decision-making..
● Facilitate data-driven policies for urban safety, infrastructure resilience, and
effective emergency response.
Approach:

● Retrieve earthquake data from the USGS API for a defined time range.
● Clean and preprocess the data using Python (Pandas and Regex) for
consistency and accuracy.
● Convert timestamps, handle missing values, and derive new analytical
columns such as year, month, and depth category.
● Store the cleaned and structured dataset in MySQL for efficient querying
and analysis.
● Use SQL to perform detailed analytical exploration, uncovering trends and
insights in global seismic activity.


outcomes by this  of the project:

● A clean and normalized earthquake dataset covering the past 5 years.
● A MySQL database with all 26 features and derived metrics.
● A series of analytical SQL queries providing actionable insights on
earthquake trends.
● A Streamlit dashboard with interactive visualizations.
● Documentation describing key findings, patterns, and recommendations.

Dataset retrival procedure:
● Use the USGS earthquake API:
https://earthquake.usgs.gov/fdsnws/event/1/query
● Understand the parameters: starttime, endtime, minmagnitude, and format=geojson.
● Decide the years and months you want to collect data for (e.g., last 5 years).
● Loop through each month and year, create start and end dates for the API request.
● Use requests.get(url, params=parameters) to fetch data for each month.
● Check the response status code and handle any failures.
● Convert the JSON response into a list of dictionaries. Extract data from properties
(magnitude, place, status, etc.) and geometry (longitude, latitude, depth).
● Convert timestamp fields from milliseconds to datetime.
● Store all extracted records in a list and then convert it into a Pandas DataFrame.
● Check the DataFrame shape, sample rows, and data types to ensure everything
looks correct.

Description of features.
Earthquake Dataset Description (26 Features)

Delivered:
1. MySQL Database – fully cleaned, stored with all features.
2. SQL Queries – covering magnitude, depth, casualties, time trends, and
quality metrics.
3. Python Analysis – full exploratory analysis using Pandas, Regex,

4. Streamlit Dashboard – interactive, multi-filtered visualization.
5. Documentation – explaining each feature, analysis, and insights.
