import pandas as pd
import streamlit as st

@st.cache_data
def load_stock_data(filename):
    """
    Loads stock data from a CSV file into a Pandas DataFrame.
    
    Args:
    filename (str): The path to the CSV file.

    Returns:
    pandas.DataFrame: The loaded data.
    """
    data = pd.read_csv(filename, parse_dates=['Date'])
    data.set_index('Date', inplace=True)
    return data

def calculate_statistics(data, attribute):
    """
    Calculates statistical measures for a given attribute in the data.
    
    Args:
    data (pandas.DataFrame): The stock data.
    attribute (str): The attribute to calculate statistics on.

    Returns:
    dict: Statistical measures including mean, median, standard deviation, and variance.
    """
    stats = {
        'mean': data[attribute].mean(),
        'median': data[attribute].median(),
        'std': data[attribute].std(),
        'var': data[attribute].var()
    }
    return stats

def get_company_color(company):
    """
    Returns the color associated with the company.
    
    Args:
    company (str): The company's stock symbol.

    Returns:
    str: The color associated with the company.
    """
    company_colors = {
        'AMZN': '#FF9900', 'GOOG': '#4285F4', 'META': '#4267B2',
        'NFLX': '#E50914', 'SBUX': '#00704A', 'TSLA': '#CC0000'
    }
    return company_colors.get(company, '#333333')  # Default to a dark grey color if not found
