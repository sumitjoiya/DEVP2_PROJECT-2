#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("world food production.csv")  # Replace with the actual dataset file path

# Sidebar
st.sidebar.title("Crop Production Dashboard")

# Feature 1: Interactive Line Chart for Multiple Crops
st.sidebar.header("Feature 1: Crop Production Trends")
selected_crops = st.sidebar.multiselect('Select Crops', df.columns[2:])

# Feature 2: Bar Chart for Total Production by Year
st.sidebar.header("Feature 2: Total Production Over the Years")

# Feature 3: Heatmap for Crop Correlation
st.sidebar.header("Feature 3: Crop Correlation Heatmap")

# Feature 4: Area Chart for Top N Crops
st.sidebar.header("Feature 4: Top N Crop Production")
top_n = st.sidebar.slider('Select Top N Crops', min_value=1, max_value=len(df.columns[2:]), value=5)

# Feature 5: Dropdown for Country Selection
st.sidebar.header("Feature 5: Country Selection")
selected_country = st.sidebar.selectbox('Select Country', df['Entity'].unique())

# Main content
st.title("Crop Production Dashboard")

# Feature 1
if selected_crops:
    fig_line = px.line(df, x='Year', y=selected_crops, title='Crop Production Over the Years')
    st.plotly_chart(fig_line)

# Feature 2
total_production = df.iloc[:, 2:].sum(axis=1)
fig_bar = px.bar(x=df['Year'], y=total_production, title='Total Crop Production Over the Years')
st.plotly_chart(fig_bar)

# Feature 3
correlation_matrix = df.iloc[:, 2:].corr()
fig_heatmap = px.imshow(correlation_matrix, x=correlation_matrix.index, y=correlation_matrix.columns,
                        title='Crop Production Correlation Heatmap')
st.plotly_chart(fig_heatmap)

# Feature 4
top_n_crops = df.iloc[:, 2:].sum().nlargest(top_n).index
fig_area = px.area(df, x='Year', y=top_n_crops, title=f'Top {top_n} Crop Production Over the Years')
st.plotly_chart(fig_area)

# Feature 5
country_data = df[df['Entity'] == selected_country]
fig_country = px.line(country_data, x='Year', y='Maize Production (tonnes)',
                      title=f'Maize Production Over the Years in {selected_country}')
st.plotly_chart(fig_country)


# The Crop Production Dashboard aims to offer a comprehensive visualization and analysis of global crop production trends. Users can interact with the dashboard to explore crop production data, identify correlations between different crops, and analyze production trends in specific countries.
# 
# Key Features:
# 
# 1. Interactive Line Chart for Multiple Crops:
# 
# Users can select one or more crops from the sidebar.
# An interactive line chart dynamically displays the production trends for the selected crops over the years.
# Insights: Enables users to compare and contrast the production patterns of different crops.
# 
# 2. Bar Chart for Total Production by Year: 
# 
# A bar chart illustrates the total crop production across all crops for each year.
# Insights: Provides a high-level overview of the overall crop production trends over the years.
# 
# 3. Heatmap for Crop Correlation: 
# 
# A heatmap visually represents the correlation between different crops based on their production over the years.
# Insights: Helps users identify relationships and dependencies between various crops.
# 
# 4. Area Chart for Top N Crops: 
# 
# Users can select the number of top crops to be displayed using a slider.
# An area chart showcases the production trends for the top N crops over the years.
# Insights: Facilitates the identification of the most significant crops in terms of production.
# 
# 
# 5. Dropdown for Country Selection: 
# 
# Users can choose a specific country from the dropdown menu.
# A line chart displays the production trend for a chosen crop (Maize, in this case) in the selected country.
# Insights: Allows users to focus on a specific geographical region and understand the production dynamics for a particular crop.
# 
# 
# 
# Usage Instructions:
# 
# The usage instructions guide users on how to access and utilize the dashboard effectively. The dashboard is designed to provide a user-friendly interface for exploring and analyzing crop production data. The interactive visualizations enhance user engagement and facilitate a deeper understanding of the data. Features such as the correlation heatmap and country-specific production charts enable users to derive meaningful insights. The ability to choose specific crops, countries, and the number of top crops enhances the flexibility of the dashboard for various analytical purposes.
# 
# 
# 
# Analysis:
# 
# The dashboard provides a user-friendly interface for exploring and analyzing crop production data.
# Interactive visualizations enhance user engagement and facilitate a deeper understanding of the data.
# Features such as the correlation heatmap and country-specific production charts enable users to derive meaningful insights.
# The ability to choose specific crops, countries, and the number of top crops enhances the flexibility of the dashboard for various analytical purposes.
# 
# 
# 
# Managerial Implications:
# 
# Strategic Planning:
# Insights into Top Crops- Identify and focus on the cultivation of top-performing crops, as indicated by the "Top N Crop Production" feature. This can guide strategic planning for agricultural investments and resource allocation.
# 
# Diversification and Risk Management:
# Correlation Heatmap- Understand the correlation between different crops to inform diversification strategies. Diversifying crops with low correlation can mitigate risks associated with market fluctuations and climate-related challenges.
# 
# Country-Specific Decision Making:
# Country Selection Feature- Tailor strategies for specific countries based on their crop production trends. This feature can help in customizing marketing approaches, supply chain logistics, and partnerships with local stakeholders.
# 
# Market Trend Analysis:
# Total Production Over the Years- Monitor overall crop production trends to anticipate market dynamics. This can inform decisions related to pricing, supply chain optimization, and market positioning.
# 
# Resource Optimization:
# Interactive Line Chart for Multiple Crops-Optimize resource allocation by understanding the demand for specific crops. This feature enables a more efficient use of resources such as land, water, and labor.
# 
# Supply Chain Management:
# Country-Specific Production Trends- Evaluate the production trends of specific crops in different countries to enhance supply chain management. This can guide decisions related to sourcing, transportation, and inventory management.
# 
# Policy Formulation:
# Insights from Country-Specific Data- Governments and policymakers can utilize the dashboard to formulate agricultural policies. This includes subsidies, incentives, and regulations based on the specific needs and challenges of different regions.
# 
# Investment Decision Support:
# Visualizations for Decision Making- Investors in the agriculture sector can utilize the dashboard to make informed investment decisions. The visualizations provide a clear understanding of market trends and potential areas for growth.
# 
# Collaboration and Partnerships:
# Correlation Heatmap-Identify opportunities for collaboration with other stakeholders in the agricultural value chain. Understanding the correlation between crops can facilitate strategic partnerships for mutual benefit.
# 
# Adaptation to Climate Change:
# Country-Specific Data- Use the country-specific data to assess the impact of climate change on crop production in different regions. This information is crucial for developing adaptive strategies and resilient agricultural practices.
# 
# 
# 
# Recommendations:
# 
# Ensure that the dataset is up-to-date and relevant for accurate analysis. Consider adding additional features or filters based on user feedback and specific analytical needs. Encourage users to actively explore and interpret the visualizations for valuable insights.
# 
# 
# 
# In conclusion, the Crop Production Dashboard serves as a valuable tool for researchers, policymakers, and agricultural enthusiasts to gain insights into global crop production trends and make informed decisions. It provides a powerful platform for analyzing and understanding the complexities of crop production on a global scale.
# 

# In[ ]:




