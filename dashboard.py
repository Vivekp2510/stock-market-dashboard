import streamlit as st
import pandas as pd
import plotly.express as px
from stock_analysis import load_stock_data, calculate_statistics

# Define company colors and names for consistency
company_info = {
    'AMZN': {'color': '#FF9900', 'name': 'Amazon', 'logo': 'images/AMZN.png'},
    'GOOG': {'color': '#4285F4', 'name': 'Google', 'logo': 'images/GOOG.png'},
    'META': {'color': '#4267B2', 'name': 'Meta', 'logo': 'images/META.png'},
    'NFLX': {'color': '#E50914', 'name': 'Netflix', 'logo': 'images/NFLX.png'},
    'SBUX': {'color': '#00704A', 'name': 'Starbucks', 'logo': 'images/SBUX.png'},
    'TSLA': {'color': '#CC0000', 'name': 'Tesla', 'logo': 'images/TSLA.png'}
}

# Streamlit layout configuration
st.set_page_config(layout="wide")
st.title("Market Master: Interactive Stock Visualization")

# Function to create an interactive chart for multiple companies
def create_multi_company_chart(companies, attribute, chart_type, start_year, end_year):
    data_frames = []
    for company in companies:
        data = load_stock_data(f'./data/{company}.csv')
        data = data[(data.index.year >= start_year) & (data.index.year <= end_year)]
        data['Company'] = company_info[company]['name']
        data_frames.append(data)
    combined_data = pd.concat(data_frames)

    chart_dispatch = {
        'Line': px.line,
        'Bar': px.bar,
        'Scatter': px.scatter
    }
    fig = chart_dispatch[chart_type](combined_data, x=combined_data.index, y=attribute, color='Company')
    fig.update_layout(hovermode='x unified', xaxis_title='Year')
    return fig


# Sidebar for company and attribute selection
st.sidebar.header("Visualization Settings")
selected_companies = st.sidebar.multiselect('Select Companies', company_info.keys(),
    format_func=lambda x: company_info[x]['name'])
selected_attribute = st.sidebar.selectbox('Select Attribute', ['Low', 'High', 'Open', 'Close', 'Volume'])
chart_type = st.sidebar.radio("Choose Chart Type", ['Line', 'Bar', 'Scatter'])
start_year, end_year = st.sidebar.select_slider(
    'Select the range of years',
    options=list(range(1990, 2023)),
    value=(1990, 2022)
)

# Sidebar option for downloading individual company data
st.sidebar.header("Download Data")
download_selected_company = st.sidebar.selectbox('Select Company for Download', list(company_info.keys()), format_func=lambda x: company_info[x]['name'])
if st.sidebar.button('Download Data'):
    st.sidebar.download_button(label='Download Data', data=pd.read_csv(f'./data/{download_selected_company}.csv').to_csv(), file_name=f'{download_selected_company}.csv')

# Plotting the main graph based on selections
if selected_companies and selected_attribute:
    main_chart = create_multi_company_chart(selected_companies, selected_attribute, chart_type, start_year, end_year)
    st.plotly_chart(main_chart, use_container_width=True)

if selected_companies:
    combined_data = pd.concat([load_stock_data(f'./data/{company}.csv') for company in selected_companies])
    stats = calculate_statistics(combined_data, selected_attribute)
    st.subheader(f"Statistics for Selected Companies ({selected_attribute}):")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Mean", value=f"{stats['mean']:.2f}", delta=None)
    with col2:
        st.metric(label="Median", value=f"{stats['median']:.2f}", delta=None)
    with col3:
        st.metric(label="Standard Deviation", value=f"{stats['std']:.2f}", delta=None)
    with col4:
        st.metric(label="Variance", value=f"{stats['var']:.2f}", delta=None)

# Individual company analysis
st.header("Individual Company Stock Analysis")
selected_company = st.selectbox('Select Company', list(company_info.keys()), format_func=lambda x: company_info[x]['name'])
company_data = load_stock_data(f'./data/{selected_company}.csv')

# Show the company's image
st.image(company_info[selected_company]['logo'], width=350)

# Calculate and display statistics for individual company
stats = calculate_statistics(company_data, 'Close')
st.subheader(f"Statistics for {company_info[selected_company]['name']} (Close):")
st.markdown(f'''
    **Mean**: {stats['mean']:.2f}  
    **Median**: {stats['median']:.2f}  
    **Standard Deviation**: {stats['std']:.2f}  
    **Variance**: {stats['var']:.2f}
''')


# Individual company graphs
col1, col2 = st.columns(2)
with col1:
    st.subheader('High/Low')
    high_low_fig = px.line(company_data, y=['High', 'Low'], color_discrete_map={'High': 'red', 'Low': 'green'})
    st.plotly_chart(high_low_fig, use_container_width=True)

with col2:
    st.subheader('Open/Close')
    open_close_fig = px.line(company_data, y=['Open', 'Close'], color_discrete_map={'Open': 'green', 'Close': 'red'})
    st.plotly_chart(open_close_fig, use_container_width=True)

col3, col4 = st.columns(2)
with col3:
    st.subheader('Volume')
    volume_fig = px.line(company_data, y='Volume')
    st.plotly_chart(volume_fig, use_container_width=True)

with col4:
    st.subheader('Advanced Stock Metrics')
    additional_attribute = st.selectbox('Select Advanced Metric', 
                                        ['Adjusted Close', '20-Day Moving Average', '50-Day Exponential Moving Average', 
                                         'Bollinger Bands', 'Relative Strength Index (RSI)', 'Your Custom Metric'])
    
    # Depending on the selected attribute, calculate the necessary values
    if additional_attribute == 'Adjusted Close':
        additional_fig = px.line(company_data, y='Adj Close')
    elif additional_attribute == '20-Day Moving Average':
        company_data['20-Day MA'] = company_data['Close'].rolling(window=20).mean()
        additional_fig = px.line(company_data, y='20-Day MA')
    elif additional_attribute == '50-Day Exponential Moving Average':
        company_data['50-Day EMA'] = company_data['Close'].ewm(span=50, adjust=False).mean()
        additional_fig = px.line(company_data, y='50-Day EMA')
    elif additional_attribute == 'Bollinger Bands':
        company_data['20-Day MA'] = company_data['Close'].rolling(window=20).mean()
        company_data['Upper Band'] = company_data['20-Day MA'] + (company_data['Close'].rolling(window=20).std() * 2)
        company_data['Lower Band'] = company_data['20-Day MA'] - (company_data['Close'].rolling(window=20).std() * 2)
        additional_fig = px.line(company_data, y=['20-Day MA', 'Upper Band', 'Lower Band'])
    elif additional_attribute == 'Relative Strength Index (RSI)':
        delta = company_data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        company_data['RSI'] = 100 - (100 / (1 + rs))
        additional_fig = px.line(company_data, y='RSI')
    elif additional_attribute == 'Your Custom Metric':
        # Replace with your custom metric calculation
        additional_fig = px.line(company_data, y='Close') 
    
    st.plotly_chart(additional_fig, use_container_width=True)


# Display raw data preview outside the 2x2 table
st.subheader("Raw Data Preview:")
st.dataframe(company_data.head())

# Credits
st.markdown("---")
st.markdown("Data provided by Kaggle. Dashboard powered by Streamlit.")

# Ensure to replace the file paths and calculations with the actual data and logic you have.
