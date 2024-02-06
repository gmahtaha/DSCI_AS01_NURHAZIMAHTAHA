import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import altair as alt


# to set the page into wide 
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded")

df = pd.read_csv("SupermarketSales.csv")

st.sidebar.header ("Supermarket Dashboard")
dashboard = st.sidebar.selectbox('Please Choose Dashboard' , ['Supermarket Sales Dashboard' , 'General Dashboard'])


hi ,hi1 = st.columns(2)
with hi :
    st.title('SUPERMARKET SALES DASHBOARD') 

with hi1 :
    city = st.selectbox('Select a City to view respective stores data' , 
                                ['Yangon', 'Naypyitaw', 'Mandalay'])
    filteredbycity = df.loc[df ['City']== city]
    Total_sales = int (filteredbycity['Total'].sum())
    Total_Gross_Income = int(filteredbycity['gross income'].sum())
    Average_rating = round(filteredbycity['Rating'].mean(), 1)
    Total_sold_unit = int (filteredbycity['Quantity'].sum())

col1 , col2 , col3 , col4 , col = st.columns(5)

col1.metric("Total Sales", f"$ {Total_sales}")

col2.metric("Total Gross Income", f"$ {Total_Gross_Income}")

col3.metric("Total Sold Unit", Total_sold_unit)

col4.metric("Average ", Average_rating ,)



left_column, right_column = st.columns(2)

with left_column:
        fig , ax = plt.subplots(figsize=(10, 5))
        sns.barplot(data = filteredbycity , x='Total', y='Product line', errorbar= None , palette= 'crest')
        plt.xlabel('Product Line')
        plt.ylabel('Total Sales')
        plt.title('Sales by Product')
        plt.gca().xaxis.set_major_formatter('${:,.0f}'.format)
        st.pyplot(fig)

with right_column:
        fig , ax = plt.subplots(figsize=(12, 5))
        Payment = filteredbycity.groupby('Day')['Total'].mean().reset_index()
        sns.lineplot(x='Day', y='Total', data= Payment, marker='o', palette= 'crest', linewidth=2)
        plt.xlabel('Day')
        plt.ylabel('Total Sales')
        plt.title('Sales by Day')
        st.pyplot(fig)

left, right , end = st.columns(3)

with left:
        fig , ax = plt.subplots()
        sns.barplot(data = filteredbycity , x='Gender', y='Total', errorbar= None , palette= 'crest')
        plt.xlabel('Gender')
        plt.ylabel('Total Sales')
        plt.title('Sales by Gender')
        plt.gca().yaxis.set_major_formatter('${:,.0f}'.format)
        st.pyplot(fig)

with right : 
        fig , ax = plt.subplots()
        Payment = filteredbycity.groupby('Hour')['Total'].mean().reset_index()
        sns.lineplot(x='Hour', y='Total', data= Payment, marker='o', palette= 'crest', linewidth=2)
        plt.xlabel('Hour')
        plt.ylabel('Total Sales')
        plt.title('Sales by Hour')
        plt.gca().yaxis.set_major_formatter('${:,.0f}'.format)
        st.pyplot(fig)

with end :
        fig , ax = plt.subplots()
        sns.barplot(data = filteredbycity , x='Payment', y='Total', errorbar= None , palette= 'crest')
        plt.xlabel('Payment Method')
        plt.ylabel('Total Sales')
        plt.title('Total Sales by Payment Method')
        plt.gca().yaxis.set_major_formatter('${:,.0f}'.format)
        st.pyplot(fig)