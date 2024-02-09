import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from streamlit_option_menu import option_menu
from streamlit_extras.metric_cards import style_metric_cards


# to set the page into wide 
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded")

df = pd.read_csv("SupermarketSales.csv")


with st.sidebar:
       st.subheader ("SUPERMARKET SALES 🛒" )
       selected = option_menu (
              menu_title = "main menu" , 
              options = ['Supermarket Sales Dashboard' , 'General Dashboard']
       )

if selected == "Supermarket Sales Dashboard" :
    hi ,hi1 = st.columns(2)
    with hi :
        st.title('SUPERMARKET SALES DASHBOARD') 

    with hi1 :
        cont = st.container()
        with cont : 

            city = st.selectbox('Select a City to view respective stores data',
                                ['All', 'Yangon', 'Naypyitaw', 'Mandalay'])
            product = st.selectbox('Select a product', ['All'] + list(df['Product line'].unique()))

            if city == 'All' and product == 'All':
                filtered_data = df # display all

            elif city == 'All':
                filtered_data = df[df['Product line'] == product]
                
            elif product == 'All':
                filtered_data = df[df['City'] == city]

            else:
                filtered_data = df[(df['City'] == city) & (df['Product line'] == product)]



        #calculations 
    Total_sales = int (filtered_data['Total'].sum())
    Total_Gross_Income = int(filtered_data['gross income'].sum())
    Average_rating = round(filtered_data['Rating'].mean(), 1)
    Total_sold_unit = int (filtered_data['Quantity'].sum())

    col1 , col2 , col3 , col4 = st.columns(4)

    col1.metric("Total Sales", f"$ {Total_sales}")

    col2.metric("Total Gross Income", f"$ {Total_Gross_Income}")

    col3.metric("Total Sold Unit", Total_sold_unit)

    col4.metric("Average ", Average_rating ,)

    style_metric_cards(border_left_color="#0C0C0C")  #styling purposes



    left_column, right_column , end_column = st.columns(3)

    with left_column:
        customer = filtered_data.groupby('Customer type')['Total'].sum()
        fig, ax = plt.subplots()
        ax.pie(customer, labels=customer.index, autopct=lambda x: f'${x:.2f}', startangle=90, wedgeprops=dict(width=0.4), colors=sns.color_palette('crest'))
        plt.axis('equal') 
        plt.title('Total Transaction by Customer Type')
        st.pyplot(fig)

    with right_column:
            fig, ax = plt.subplots()
            daily_sales = filtered_data.groupby('Day')['Total'].mean().reset_index()
            sns.barplot(x='Day', y='Total', data=daily_sales, palette='crest')  
            plt.xlabel('Day')
            plt.ylabel('Total Sales')
            plt.title('Total Transaction by Day')
            plt.gca().yaxis.set_major_formatter('${:,.0f}'.format)
            st.pyplot(fig)

    with end_column :
            fig, ax = plt.subplots()
            monthly_sales = filtered_data.groupby('Month')['Total'].mean().reset_index()
            sns.lineplot(x='Month', y='Total', data=monthly_sales, marker='o', color='skyblue', linewidth=2, label='Total Sales')
            plt.fill_between(monthly_sales['Month'], monthly_sales['Total'], color='skyblue', alpha=0.3)
            plt.xlabel('Month')
            plt.ylabel('Total Sales')
            plt.title('Total Transaction by Month')
            plt.gca().yaxis.set_major_formatter('${:,.0f}'.format)
            plt.legend()
            st.pyplot(fig)


    left, right , end = st.columns(3)

    with left:
            fig , ax = plt.subplots()
            sns.barplot(data = filtered_data , x='Payment', y='Total', errorbar= None , palette= 'crest')
            plt.xlabel('Payment Method')
            plt.ylabel('Total Sales')
            plt.title('Total Transaction by Payment Method')
            plt.gca().yaxis.set_major_formatter('${:,.0f}'.format)
            st.pyplot(fig)

    with right : 
            fig , ax = plt.subplots()
            Payment = filtered_data.groupby('Hour')['Total'].mean().reset_index()
            sns.lineplot(x='Hour', y='Total', data= Payment, marker='o', palette= 'crest', linewidth=2)
            plt.xlabel('Hour')
            plt.ylabel('Total Sales')
            plt.title('Total Transaction by Hour')
            plt.gca().yaxis.set_major_formatter('${:,.0f}'.format)
            st.pyplot(fig)

    with end :
            fig, ax = plt.subplots()
            total_sales_by_gender = filtered_data.groupby('Gender')['Total'].sum()
            ax.pie(total_sales_by_gender, labels=total_sales_by_gender.index, autopct=lambda x: f'${x:.2f}', startangle=90, colors=sns.color_palette('crest'))
            plt.axis('equal')  
            plt.title('Total Transaction by Gender')
            st.pyplot(fig)


#Dashboard 2  
if selected == "General Dashboard" :
        st.title ("General Dashboard")
      
        left_column, right_column, ending_column = st.columns(3)

        with left_column:
                fig, ax = plt.subplots()
                rating = df.groupby('City')['Rating'].sum()
                ax.pie(rating, labels=rating.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('crest'))
                plt.axis('equal')  
                plt.title('Rating by City')
                st.pyplot(fig)

        with right_column:
                fig , ax = plt.subplots()
                sns.barplot(data = df , x='City', y='Total', errorbar= None , palette= 'crest')
                plt.xlabel('City')
                plt.ylabel('Total Sales')
                plt.title('Sales by City')
                plt.gca().yaxis.set_major_formatter('${:,.0f}'.format)
                st.pyplot(fig)
                
        with ending_column:
            fig, ax = plt.subplots()
            gender_counts = df['Gender'].value_counts()
            ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.4), colors=sns.color_palette('crest'))
            plt.title('Distribution of Gender')
            st.pyplot(fig)

        left, right , end = st.columns(3)

        with left:
                fig , ax = plt.subplots()
                products= df['Product line'].value_counts()
                sns.barplot(x=products.values, y=products.index, palette='crest')
                plt.ylabel('Products')
                plt.xlabel('Count (Products)')
                plt.title('Total Products Distribution')
                st.pyplot(fig)

        with right:
                fig, ax = plt.subplots()
                custom_palette = {'Male': '#289E8F', 'Female': '#1C3269'}
                sns.countplot(data=df,x=df['Customer type'],hue =df['Gender'], palette=custom_palette)
                plt.title('Customer type by Gender')
                st.pyplot(fig)

        with end:
            fig, ax = plt.subplots()
            custom_palette = {'Male': '#289E8F', 'Female': '#1C3269'}
            sns.countplot(data=df,x=df['Customer type'],hue =df['Gender'], palette=custom_palette)
            plt.title('Customer type by Gender')
            st.pyplot(fig)
