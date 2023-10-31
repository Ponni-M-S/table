import pandas as pd
import plotly.express as px
import streamlit as st
st.set_page_config ( page_title="sales dasboard",
                   page_icon=":bar_chart:",
                   layout="wide"
)
df = pd.read_excel(
    io="sales.xlsx",
    engine="openpyxl",
    sheet_name="Sales",
    skiprows=3,
    usecols="B:R",
    nrows=1000,
    
)   
print(df)
   
st.dataframe(df)
st.sidebar.header("filter here:")
city = st.sidebar.multiselect(
    "select the City:",
    options=df["City"].unique(),
    
    default=df["City"].unique(),
    
)
customer_type = st.sidebar.multiselect(
    
    "select the Customer_type:",
    options=df["Customer_type"].unique(),
    default=df["Customer_type"].unique(),
    
)
Gender= st.sidebar.multiselect(
    
    "select the Gender:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique(),
)
Branch= st.sidebar.multiselect(
    
    "select the Branch:",
    options=df["Branch"].unique(),
    default=df["Branch"].unique(),
)

    
Quantity= st.sidebar.multiselect(
    
    "select the Quantity:",
    options=df["Quantity"].unique(),
    default=df["Quantity"].unique(),
 )
df_selection = df.query(
    "City == @city & Branch ==@Branch & Quantity ==@Quantity & Gender == @Gender"

)

st.dataframe(df_selection)

st.title("bar_chart: Sales Dashboard")
st.markdown("##")

total_Sales = int(df_selection["Total"].sum())
average_rateing = round(df_selection["Rating"].mean(),1)
star_rateing = ":star:" * int(round(average_rateing,0))
average_sale_by_transcation = round(df_selection["Total"].mean(),2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Sales:")
    st.subheader(f"us $ [total_sales,]")
with middle_column:
    st.subheader("Total Sales:")
    st.subheader(f"[Average Rating][star_rating]") 
with right_column:
    st.subheader("Average Sales per Transaction:")
    st.subheader(f"us $ [average_Sales_by_Transaction]")
    st.markdown("___")
    Sales_by_product_line =(
        df_selection.groupby(by=["product line"]).sum()[["Total"]].sort_values(by="Total")
    )
    fig_product_Sales = px.bar(
        Sales_by_product_line,
        x="Total",
        y=Sales_by_product_line.Index,
        orientation="h",
        title="Sales_by_product_line",
        color_discrete_sequence=["#008383"]*len(Sales_by_product_line),
        template="ploty_red"
    
    )
    fig_product_Sales.update_layout(
        plot_bgcolor="right(0,0,0)",
        xasis=(dict(showgrid=False))
    )
    
    
    Sales_by_hour = df_selection.groupby(by=["hour"]).sum()[["Total"]]
    fig_hourly_Sales = px.bar(
        Sales_by_hour,
        x=Sales_by_hour.index,
        y="Total",
        totle="<b>Sales ny hour</b>",
        color_discrete_sequence=["#008388"]*len(Sales_by_hour),
        template="plotly_white",
    
    )
    fig_hourly_Sales.update_layout(
        xaxis=dict(tickmode="linear"),
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=(dict(showgrid=False)),
    )
    left_column,right_column = st.columns(2)
    left_column.plotly_chart(fig_hourly_Sales,use_container_width=True)
    right_column.plotly_chart(fig_product_Sales,use_container_width=True)
       
    
    
   