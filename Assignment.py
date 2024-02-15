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
    left_column, right_column , next_column , end_column = st.columns([0.2,0.3,0.2,0.3])

    with left_column:
          # filter for graph 1
            
            st.write("**Total Sales by Customer Segmentation's Filter**")
            gender = st.selectbox('Select the Gender:', df['Gender'].unique())
            products = st.selectbox('Select the Products:', df['Product line'].unique())
            graph1 = df[(df['Gender'] == gender)& (df['Product line'] == products)]

    
    with right_column:
            customer = graph1.groupby('Customer type')['Total'].sum()
            fig, ax = plt.subplots()
            ax.pie(customer, labels=customer.index, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.4), colors=sns.color_palette('crest'))
            plt.axis('equal') 
            plt.title('Total Sales by Customer Segmentation')
            st.pyplot(fig)
    
    with next_column:
        # Filter for graph 2 
        st.write("**Total Sales by Day's Filter**")
        Gender = st.radio('Select the Gender:', df['Gender'].unique())
        City = st.radio('Select the City:', df['City'].unique())
        data1 = df[(df['Gender'] == Gender) & (df['City'] == City)]

    with end_column:
                fig, ax = plt.subplots()
                sns.barplot(data= data1, x='Day', y='Total', errorbar= None , palette='crest')  
                plt.xlabel('Day')
                plt.ylabel('Total Sales')
                plt.title('Total Sales by Day')
                plt.gca().yaxis.set_major_formatter('${:,.0f}'.format)
                st.pyplot(fig)

      
    column1, column2, column3 , column4 = st.columns([0.2,0.3,0.2,0.3])

    with column1 :
            #filter for graph 3
            st.write ("**Total Sales by Month's Filter**")
            cit = st.selectbox('Select the City:', df['City'].unique())
            payment = st.radio('Select the Product Category:', df['Product line'].unique())
            graph3 = df[(df['City'] == cit ) & (df['Product line'] == payment)]

    with column2 :

                fig, ax = plt.subplots()
                monthly_sales = graph3.groupby('Month')['Total'].mean().reset_index()
                sns.lineplot(x='Month', y='Total', data=monthly_sales, marker='o', color='skyblue', linewidth=2, label='Total Sales')
                plt.fill_between(monthly_sales['Month'], monthly_sales['Total'], color='skyblue', alpha=0.3)
                plt.xlabel('Month')
                plt.ylabel('Total Sales')
                plt.title('Total Sales by Month')
                plt.gca().yaxis.set_major_formatter('${:,.0f}'.format)
                plt.legend()
                st.pyplot(fig)

    with column3 :
                #filter for graph 4
                st.write ("**Total Sales by Payment Method's Filter**")
                customer = st.selectbox('Select the Customer Type:', df['Customer type'].unique())
                month  = st.selectbox('Select the Month:', df['Month'].unique())
                graph4 = df[(df['Customer type'] == customer ) & (df['Month'] == month)]     


    with column4:
            
                fig , ax = plt.subplots()
                sns.barplot(data = graph4 , x='Payment', y='Total', errorbar= None , palette= 'crest')
                plt.xlabel('Payment Method')
                plt.ylabel('Total Sales')
                plt.title('Total Sales by Payment Method')
                plt.gca().yaxis.set_major_formatter('${:,.0f}'.format)
                st.pyplot(fig)

      
    no1, no2 , no3 , no4  = st.columns([0.2,0.3,0.2,0.3])

    with no1 :
             #filter for graph 5
            st.write ("**Total Sales by Hour's Filter**")
            day = st.multiselect('Select the Day in a week:', df['Day'].unique())
            gen  = st.multiselect('Select the gender:', df['Gender'].unique())
            graph5 = df[(df['Day'].isin(day) ) & (df['Gender'].isin(gen))]

    with no2 : 
            
            fig , ax = plt.subplots()
            Payment = graph5.groupby('Hour')['Total'].mean().reset_index()
            sns.lineplot(x='Hour', y='Total', data= Payment, marker='o', palette= 'crest', linewidth=2)
            plt.xlabel('Hour')
            plt.ylabel('Total Sales')
            plt.title('Total Sales by Hour')
            plt.gca().yaxis.set_major_formatter('${:,.0f}'.format)
            st.pyplot(fig)

    with no3 :
             #filter for graph 6
            st.write ("**Total Sales by Gender's Filter**")
            cust = st.radio('Select the Month:', df['Month'].unique())
            pro  = st.radio('Select the Product line:', df['Product line'].unique())
            graph6 = df[(df['Month'] == cust ) & (df['Product line'] == (pro))]           


    with no4 :

                fig, ax = plt.subplots()
                total_sales_by_gender = graph6.groupby('Gender')['Total'].sum()
                ax.pie(total_sales_by_gender, labels=total_sales_by_gender.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('crest'))
                plt.axis('equal')  
                plt.title('Total Sales by Gender')
                st.pyplot(fig)

         
if selected == "General Dashboard" :
        

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


        left_column, right_column , next_column , end_column = st.columns([0.2,0.3,0.2,0.3])

        with left_column :
                # filter for graph 1
                    st.write ("**Rating by City's Filter**")
                    pl = st.selectbox('Select the Products:', df['Product line'].unique())
                    ct = st.selectbox('Select the Customer Type:', df['Customer type'].unique())
                    first = df[(df['Product line'] == (pl) )& (df['Customer type'] == ct)]


        with right_column:
                    
                    fig, ax = plt.subplots()
                    rating = first.groupby('City')['Rating'].sum().reset_index()  # Reset index to use 'City' column in barplot
                    sns.barplot(data=rating, x='City', y='Rating', palette='crest')
                    plt.xlabel('City')
                    plt.ylabel('Rating')
                    plt.title('Rating by City')
                    st.pyplot(fig)

        with next_column :
            
                    #filter for graph 2 
                    st.write ("**Total Sales by City's Filter**")
                    month  = st.radio('Select the Month:', df['Month'].unique())
                    products = st.radio('Select the Products:', df['Product line'].unique())
                    second = df[(df['Month'] == month ) & (df['Product line'] == products)]

        with end_column:

                    fig , ax = plt.subplots()
                    sns.barplot(data = second , x='City', y='Total', errorbar= None , palette= 'crest')
                    plt.xlabel('City')
                    plt.ylabel('Total Sales')
                    plt.title('Total Sales by City')
                    plt.gca().yaxis.set_major_formatter('${:,.0f}'.format)
                    st.pyplot(fig)

        left, right , righted , lefted = st.columns([0.2,0.3,0.2,0.3])
                
        with left:
            #filter for graph 3
            st.write ("**Total Customers by Gender's Filter**")
            city = st.selectbox('Select the City:', df['City'].unique())
            client = st.radio('Select the Customer Type:', df['Customer type'].unique())
            third = df[(df['City'] == city ) & (df['Customer type'] == client)]


        with right:

                fig, ax = plt.subplots()
                gender_counts = third['Gender'].value_counts()
                ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.4), colors=sns.color_palette('crest'))
                plt.title('Total Customer by Gender')
                st.pyplot(fig)
        
        with righted:
                #filter for graph 4
                st.write ("**Total Customer by Category's Filter**")
                days = st.multiselect('Select the Day in a week:', df['Day'].unique())
                sex  = st.multiselect('Select the gender:', df['Gender'].unique())
                forth = df[(df['Day'].isin(days) ) & (df['Gender'].isin(sex))]


        with lefted:
                
    
                    fig, ax = plt.subplots()
                    products = forth['Product line'].value_counts()
                    ax.pie(products, labels=products.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('crest'))
                    plt.axis('equal')
                    plt.title('Total Customer by Category')
                    st.pyplot(fig)

        col1, col2,col3 ,col4 = st.columns([0.2,0.3,0.2,0.3])

        with col1:
                
            #filter for graph 5
            st.write ("**Customer type by gender's Filter**")
            days = st.selectbox('Select the Day in a week:', df['Day'].unique())
            branch = st.radio('Select the City:', df['City'].unique())
            fifth = df[(df['Day'] == (days) ) & (df['City'] == branch)]
                
        with col2 :

                    fig, ax = plt.subplots()
                    custom_palette = {'Male': '#289E8F', 'Female': '#1C3269'}
                    sns.countplot(data= fifth,x=fifth['Customer type'],hue =fifth['Gender'], palette=custom_palette)
                    plt.title('Customer type by Gender')
                    st.pyplot(fig)

        with col3:
                
            #filter for graph 5
            st.write ("**Customer type by gender's Filter**")
            retail = st.multiselect('Select the City:', df['City'].unique())
            months = st.selectbox('Select the Month:', df['Month'].unique())
            fifth = df[(df['City'].isin(retail)) & (df['Month'] == months)]
                
        with col4 :

                    fig , ax = plt.subplots()
                    gross = fifth.groupby('Product line')['gross income'].mean().reset_index()
                    sns.lineplot(x='gross income', y='Product line', data= gross, marker='o', palette= 'crest', linewidth=2)
                    plt.xlabel('Category')
                    plt.ylabel('Total Gross Income')
                    plt.title('Total Gross Income by Category')
                    plt.gca().xaxis.set_major_formatter('${:,.0f}'.format)
                    st.pyplot(fig)



        

    

