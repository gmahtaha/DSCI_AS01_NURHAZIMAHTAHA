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


# to read data from dataset
df = pd.read_csv("SupermarketSales.csv")

# to show title in the center
st.markdown("<h1 style='text-align: center;'>SUPERMARKET SALES DASHBOARD</h1>", unsafe_allow_html=True)

# for the option dashboar
selected = option_menu (
        menu_title = None, 
        options = ['Supermarket Sales Dashboard' , 'General Dashboard'],
        orientation= "horizontal",
       )

if selected == "Supermarket Sales Dashboard" :
     
    # filterisations : 
    st.sidebar.title('SELECT THE FILTERS')

    # filter for graph 1
    st.sidebar.write ("**Total Transaction by Customer's Filter**")
    gender = st.sidebar.multiselect('Select the Gender:', df['Gender'].unique())
    products = st.sidebar.selectbox('Select the Products:', df['Product line'].unique())
    graph1 = df[(df['Gender'].isin( gender) )& (df['Product line'] == products)]

    #filter for graph 2 
    st.sidebar.write ("**Total Transaction by Day's Filter**")
    city = st.sidebar.radio('Select the City:', df['City'].unique())
    prod = st.sidebar.multiselect('Select the Products:', df['Product line'].unique())
    graph2 = df[(df['City'] == city ) & (df['Product line'].isin(prod))]

    #filter for graph 3
    st.sidebar.write ("**Total Transaction by Month's Filter**")
    cit = st.sidebar.selectbox('Select the City:', df['City'].unique())
    payment = st.sidebar.radio('Select the Payment:', df['Payment'].unique())
    graph3 = df[(df['City'] == city ) & (df['Payment'] == payment)]

     #filter for graph 4
    st.sidebar.write ("**Total Transaction by Payment Method's Filter**")
    customer = st.sidebar.selectbox('Select the Customer Type:', df['Customer type'].unique())
    month  = st.sidebar.selectbox('Select the Month:', df['Month'].unique())
    graph4 = df[(df['Customer type'] == customer ) & (df['Month'] == month)]

    #filter for graph 5
    st.sidebar.write ("**Total Transaction by Hour's Filter**")
    day = st.sidebar.multiselect('Select the Day in a week:', df['Day'].unique())
    gen  = st.sidebar.multiselect('Select the gender:', df['Gender'].unique())
    graph5 = df[(df['Day'].isin(day) ) & (df['Gender'].isin(gen))]

    #filter for graph 6
    st.sidebar.write ("**Total Transaction by Gender's Filter**")
    quantity = st.sidebar.selectbox('Select the Quantiy sold:', df['Quantity'].unique())
    pro  = st.sidebar.radio('Select the Product line:', df['Product line'].unique())
    graph6 = df[(df['Quantity'] == quantity ) & (df['Product line'] == (pro))]


    #KPI calculations 

    st.write("**Sales Performance throughout 3 Months**")
    Total_sales = int (df['Total'].sum())
    Total_Gross_Income = int(df['gross income'].sum())
    Average_rating = round(df['Rating'].mean(), 1)
    Total_sold_unit = int (df['Quantity'].sum())

    col1 , col2 , col3 , col4 = st.columns(4)

    col1.metric("Total Sales", f"$ {Total_sales}")

    col2.metric("Total Gross Income", f"$ {Total_Gross_Income}")

    col3.metric("Total Sold Unit", Total_sold_unit)

    col4.metric("Average ", Average_rating ,)

    style_metric_cards(border_left_color="#0C0C0C")  #styling purposes


    # for the first row ( graph )
    left_column, right_column = st.columns(2)

    with left_column:
        st.write("**Sales Performance Graphs**")

        if not graph1.empty :
            customer = graph1.groupby('Customer type')['Total'].sum()
            fig, ax = plt.subplots()
            ax.pie(customer, labels=customer.index, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.4), colors=sns.color_palette('crest'))
            plt.axis('equal') 
            plt.title('Total Transaction by Customer Type')
            st.pyplot(fig)
        else:
            st.write("No data available for the selected filters.")

    with right_column:
        
        if not graph2.empty:
                fig, ax = plt.subplots()
                sns.barplot(data= graph2, x='Day', y='Total', errorbar= None , palette='crest')  
                plt.xlabel('Day')
                plt.ylabel('Total Sales')
                plt.title('Total Transaction by Day')
                plt.gca().yaxis.set_major_formatter('${:,.0f}'.format)
                st.pyplot(fig)

        else:
                 st.write("No data available for the selected filters.")

    c1, c2 = st.columns(2)

    with c1 :
            
            if not graph3.empty:

                fig, ax = plt.subplots()
                monthly_sales = graph3.groupby('Month')['Total'].mean().reset_index()
                sns.lineplot(x='Month', y='Total', data=monthly_sales, marker='o', color='skyblue', linewidth=2, label='Total Sales')
                plt.fill_between(monthly_sales['Month'], monthly_sales['Total'], color='skyblue', alpha=0.3)
                plt.xlabel('Month')
                plt.ylabel('Total Sales')
                plt.title('Total Transaction by Month')
                plt.gca().yaxis.set_major_formatter('${:,.0f}'.format)
                plt.legend()
                st.pyplot(fig)

            else:
                st.write("No data available for the selected filters.")


    with c2:
            
            if not graph4.empty:

                fig , ax = plt.subplots()
                sns.barplot(data = graph4 , x='Payment', y='Total', errorbar= None , palette= 'crest')
                plt.xlabel('Payment Method')
                plt.ylabel('Total Sales')
                plt.title('Total Transaction by Payment Method')
                plt.gca().yaxis.set_major_formatter('${:,.0f}'.format)
                st.pyplot(fig)

            else:
                st.write("No data available for the selected filters.")

    no1, no2  = st.columns(2)
    with no1 : 
            
            if not graph5.empty:

                fig , ax = plt.subplots()
                Payment = graph5.groupby('Hour')['Total'].mean().reset_index()
                sns.lineplot(x='Hour', y='Total', data= Payment, marker='o', palette= 'crest', linewidth=2)
                plt.xlabel('Hour')
                plt.ylabel('Total Sales')
                plt.title('Total Transaction by Hour')
                plt.gca().yaxis.set_major_formatter('${:,.0f}'.format)
                st.pyplot(fig)

            else:
                st.write("No data available for the selected filters.")


    with no2 :
            if not graph6.empty:

                fig, ax = plt.subplots()
                total_sales_by_gender = graph6.groupby('Gender')['Total'].sum()
                ax.pie(total_sales_by_gender, labels=total_sales_by_gender.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('crest'))
                plt.axis('equal')  
                plt.title('Total Transaction by Gender')
                st.pyplot(fig)

            else:
                st.write("No data available for the selected filters.")




if selected == "General Dashboard" :
    # filterisations : 
    st.sidebar.title('SELECT THE FILTERS')


    #KPI calculations 

    st.write("**Sales Performance throughout 3 Months**")
    Total_sales = int (df['Total'].sum())
    Total_Gross_Income = int(df['gross income'].sum())
    Average_rating = round(df['Rating'].mean(), 1)
    Total_sold_unit = int (df['Quantity'].sum())

    col1 , col2 , col3 , col4 = st.columns(4)

    col1.metric("Total Sales", f"$ {Total_sales}")

    col2.metric("Total Gross Income", f"$ {Total_Gross_Income}")

    col3.metric("Total Sold Unit", Total_sold_unit)

    col4.metric("Average ", Average_rating ,)

    style_metric_cards(border_left_color="#0C0C0C")  #styling purposes


    # filter for graph 1
    st.sidebar.write ("**Rating by City's Filter**")
    pl = st.sidebar.selectbox('Select the Products:', df['Product line'].unique())
    ct = st.sidebar.selectbox('Select the Customer Type:', df['Customer type'].unique())
    first = df[(df['Product line'] == (pl) )& (df['Customer type'] == ct)]

    #filter for graph 2 
    st.sidebar.write ("**Sales by City's Filter**")
    month  = st.sidebar.radio('Select the Month:', df['Month'].unique())
    products = st.sidebar.multiselect('Select the Products:', df['Product line'].unique())
    second = df[(df['Month'] == month ) & (df['Product line'].isin(products))]

    #filter for graph 3
    st.sidebar.write ("**Distribution of Gender's Filter**")
    city = st.sidebar.selectbox('Select the City:', df['City'].unique())
    quantity = st.sidebar.selectbox('Select the Quantiy sold:', df['Quantity'].unique())
    third = df[(df['City'] == city ) & (df['Quantity'] == quantity)]

     #filter for graph 4
    st.sidebar.write ("**Total product Distribution's Filter**")
    days = st.sidebar.multiselect('Select the Day in a week:', df['Day'].unique())
    sex  = st.sidebar.multiselect('Select the gender:', df['Gender'].unique())
    forth = df[(df['Day'].isin(days) ) & (df['Gender'].isin(sex))]

    #filter for graph 5
    st.sidebar.write ("**Customer type by gender's Filter**")
    days = st.sidebar.selectbox('Select the Day in a week:', df['Day'].unique())
    branch = st.sidebar.radio('Select the City:', df['City'].unique())
    fifth = df[(df['Day'] == (days) ) & (df['City'] == branch)]

    #filter for graph 6


    left_column, right_column= st.columns(2)

    with left_column:
            
            if not first.empty :
                fig, ax = plt.subplots()
                rating = first.groupby('City')['Rating'].sum().reset_index()  # Reset index to use 'City' column in barplot
                sns.barplot(data=rating, x='City', y='Rating', palette='crest')
                plt.xlabel('City')
                plt.ylabel('Rating')
                plt.title('Rating by City')
                st.pyplot(fig)
            else:
                st.write("No data available for the selected filters.")


    with right_column:
            
            if not second.empty :

                fig , ax = plt.subplots()
                sns.barplot(data = second , x='City', y='Total', errorbar= None , palette= 'crest')
                plt.xlabel('City')
                plt.ylabel('Total Sales')
                plt.title('Sales by City')
                plt.gca().yaxis.set_major_formatter('${:,.0f}'.format)
                st.pyplot(fig)

            else:
                st.write("No data available for the selected filters.")


    left, right = st.columns(2)
            
    with left:

        if not third.empty :

            fig, ax = plt.subplots()
            gender_counts = third['Gender'].value_counts()
            ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.4), colors=sns.color_palette('crest'))
            plt.title('Distribution of Gender')
            st.pyplot(fig)

        else:
                st.write("No data available for the selected filters.")

    with right:
            
            if not forth.empty :

                fig, ax = plt.subplots()
                products = forth['Product line'].value_counts()
                ax.pie(products, labels=products.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('crest'))
                plt.axis('equal')
                plt.title('Total Products Distribution')
                st.pyplot(fig)


            else:
                st.write("No data available for the selected filters.")
    
    col1, col2 = st.columns(2)

    with col1:
            
            if not fifth.empty:

                fig, ax = plt.subplots()
                custom_palette = {'Male': '#289E8F', 'Female': '#1C3269'}
                sns.countplot(data= fifth,x=fifth['Customer type'],hue =fifth['Gender'], palette=custom_palette)
                plt.title('Customer type by Gender')
                st.pyplot(fig)

            else:
                st.write("No data available for the selected filters.")

    

