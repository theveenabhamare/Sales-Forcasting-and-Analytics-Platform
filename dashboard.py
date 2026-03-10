import streamlit as st
import pandas as pd
import plotly.express as px

# Load Dataset
df = pd.read_csv("sales_data.csv")

df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

# Title
st.title("Sales Forecasting & Analytics Platform")

st.write("Interactive dashboard for analyzing sales performance.")

# Dataset Preview
st.header("Dataset Preview")

st.write(df.head())

# Sales by Category
st.header("Sales by Category")

fig1 = px.bar(df,
              x="Category",
              y="Sales",
              color="Category",
              title="Sales Distribution by Category")

st.plotly_chart(fig1)

# Sales by Region
st.header("Sales by Region")

region_sales = df.groupby("Region")["Sales"].sum().reset_index()

fig2 = px.pie(region_sales,
              names="Region",
              values="Sales",
              title="Regional Sales Contribution")

st.plotly_chart(fig2)

# Sales Trend
st.header("Sales Trend Over Time")

sales_trend = df.groupby("Order Date")["Sales"].sum().reset_index()

fig3 = px.line(sales_trend,
               x="Order Date",
               y="Sales",
               title="Sales Trend")

st.plotly_chart(fig3)

# Top Products
st.header("Top Products by Sales")

top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

st.bar_chart(top_products)

# Insights
st.header("Key Business Insights")

st.markdown("""
• Some product categories generate significantly higher sales compared to others.

• Regional analysis shows that certain regions contribute more to total revenue.

• Sales trend indicates fluctuations over time suggesting seasonal demand patterns.

• Identifying top-selling products helps businesses focus on profitable items.

• Sales forecasting and analytics help organizations plan inventory and marketing strategies effectively.
""")
