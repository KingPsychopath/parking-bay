# parking-bay

A Parking Bay Data Visualiser that in-takes ingress XML data for Human Readable Visualisation, built in Python with re-usable components alongside a focus on scalability and maintainability via distributed data-processing using Apache Spark.

# The Data

The [data set](https://www.data.gov.uk/dataset/563a5530-a7a2-46aa-925e-41fe09de7ea3/parking-bays) is a collection of public parking lot data intended to mimic data from Parkopedia, a company that provides detailed information about parking lots in cities around the world. The data is in XML format and contains information about the location, capacity, and occupancy of each parking lot.

The data schema is as follows:

```xml
    'nearest_machine',
    'postcode',
    'easting',
    'cashless_identifier',
    'epsg_27700_geojson_geometry',
    'controlled_parking_zone',
    'restriction_type',
    'tariff',
    'road_name',
    'location',
    'times_of_operation',
    'epsg_4326_geojson_geometry',
    'longitude',
    'response',
    'unique_identifier',
    'parking_bay_length_metres',
    'epsg_4326_well_known_text_geometry',
    'organisation_uri',
    'northing',
    'latitude',
    'disclaimer',
    'row',
    'parking_spaces',
    'spatial_accuracy',
    'epsg_27700_well_known_text_geometry',
    'maximum_stay',
    'valid_parking_permits',
    'last_uploaded'
```

# Objectives

<table>
<tr>
<td>

- [x] Ingest & Parse XML Data to DataFrames
- [ ] Visualise Data (Human Readable Visualisation)
- [ ] Create Widgets for Interactive Usage (i.e. Slider for Time)
- [ ] Storing the Data?

</td>
<td>

- [ ] Unit Tests
- [ ] Integration Tests
- [ ] Documentation

</td>
<td>

- [ ] Dockerise
- [ ] Deploy to Cloud
- [ ] Monitoring
- [ ] Alerting
- [ ] Logging

</td>
</tr>

</table>

# Tech Stack

Ranges from a simple Python Flask/Django app to a full-fledged microservices architecture with a front-end and back-end; with a database and a message broker dependant on the scale of the project _(i.e. If we are ingesting live data like available parking spots)_.

For truly large-scale data, we might need to aggregate or sample the data before visualizing it. Apache Spark has built-in functions for these operations. (_Similar to Pagination_)

## The Pipeline

### Primary Functionality
Pre-processing Data(XML) to Pandas DataFrame -> Data Processing with Apache Spark -> Visualisation with Matplotlib/Plotly -> Interactive Display with Streamlit or Dash

### Secondary Functionality
Unit Testing with Pytest -> Integration Testing with Pytest -> Documentation with Sphinx -> Dockerise with Docker -> Deploy to Cloud with AWS/GCP/Azure

### Tertiary Functionality (Unconfirmed/Potential)
API for Querying Data -> Monitoring HTTP requests with Prometheus -> Alerting  and Logging with Grafana -> Store Long-Term Logs in S3 (should be cheap unless we need to access them frequently???)

# Intuition

I need to decide on the best way to visualise the data, preferably in a way similar to what will be relevant for the senior engineers to read and understand, after HD Map data ingest.

Currently, looking at open-source libraries to lighten the load on the project and focus on the core functionality. Requirements are ease of use and the ability to handle large data-sets at scale.

## Options

**matplotlib**, _is whats installed, pandas plots uses it, everyone hates the syntax but its established._

There are several popular libraries and frameworks in Python for creating interactive dashboards:

1. **Dash:** Developed by Plotly, Dash is a powerful library for creating interactive dashboards with pure Python. It's built on top of Flask Plotly.js, and React.js, and allows you to create rich web applications integrated with interactive visualizations.

2. **Plotly:** Also developed by Plotly, this library is great for creating interactive and complex plots and visualizations. It can be used in combination with Dash to create interactive dashboards.

3. **Streamlit:** Streamlit is an open-source Python library that makes it easy to create custom web apps for machine learning and data science. It's designed to help data scientists and engineers turn data processes into interactive web applications quickly. (**Bonus Points for Interactive Usage**)

Each of these libraries and frameworks has its own strengths and weaknesses, and the best one to use depends on specific needs and circumstances.

## Decision

Decided against options like **Bokeh** and **Holoviews** as they are more complex and require more time to learn and implement.

Not sure if we will be working with Jupyter Notebooks, so foregoing **Voila** and **Panel**.

**Streamlit** is good for basic dashboards that have a few users. It is NOT a replacement for a real web framework, and it isn't even close and it appears Parkopedia has a preference for flexibility with in-house builds. (It's not even a web framework, it's a data app framework.)

Therefore, I will be using **matplotlib** for the initial visualisation, and then move on to **Streamlit or Dash+Plotly** for the interactive usage.

## Proposed Functionality

1. **3D Map Visualization**: Display the 3D maps of the parking lots. This could be done using libraries like Three.js or Babylon.js if we're working in a web context. Python also has libraries like Mayavi or Plotly for 3D visualization.

2. **Parking Lot Metrics**: Display key metrics about each parking lot, such as its total area, the number of parking spaces, the percentage of occupied spaces, and the flow of cars in and out of the lot.

3. **Query Interface**: Provide an interface for engineers to query the data. This could be a simple form that allows users to select a parking lot and a date/time range, or it could be a more complex SQL-like query interface.

4. **Data Tables**: Display the results of queries in a tabular format. This could include information about specific parking spaces, such as their size, location, and occupancy history.

5. **Time Series Graphs**: Show graphs of how key metrics have changed over time. For example, we could show a line graph of the occupancy rate of a parking lot over the course of a day.

6. **Heatmaps**: If we have data on the occupancy of individual parking spaces, we could display a heatmap on top of the 3D map showing which spaces are most frequently occupied.

7. **Alerts and Notifications**: If there are certain conditions that the engineers are particularly interested in (like a parking lot being full), we could include a system of alerts or notifications.

It would be a good idea to involve the engineers in the design process to ensure that the dashboard meets their needs. I primarily want to reduce scope creep. They may have specific requirements for the types of data they want to see, the way they want to interact with the data, as well as the way they want the data to be visualized.

# Dependencies

Python 3.8, matplotlib, pandas, numpy, xml.etree.ElementTree, apache spark, pytest, requests, flask, dash, streamlit, plotly
