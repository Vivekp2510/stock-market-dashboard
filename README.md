
# Stock Market Dashboard

## Overview
This Stock Market Dashboard is a user-friendly web application designed to provide insightful analysis of stock market data. It's built using Streamlit, a powerful tool for creating interactive web applications. This dashboard allows users to visualize stock data for several major companies, including Amazon, Google, Meta (formerly Facebook), Netflix, Starbucks, and Tesla.

## Data Source Credits
The stock data used in this project is sourced from Kaggle, specifically from the following datasets:
- [Meta Platforms Inc. (META)](https://www.kaggle.com/datasets/henryshan/meta-platforms-inc-meta)
- [Tesla Stock Price (TSLA)](https://www.kaggle.com/datasets/henryshan/tesla-stock-price)
- [Starbucks Stock Price (SBUX)](https://www.kaggle.com/datasets/henryshan/starbucks-stock-price)
- [Netflix Stock Price (NFLX)](https://www.kaggle.com/datasets/henryshan/netflix-stock-price)
- [Amazon.com Inc. (AMZN)](https://www.kaggle.com/datasets/henryshan/amazon-com-inc-amzn)
- [Google Stock Price (GOOG)](https://www.kaggle.com/datasets/henryshan/google-stock-price)

The images used in the dashboard are also sourced from these Kaggle datasets.

## Installation and Running the Application
To get started with this dashboard, you need to have Python installed on your computer. Follow these steps:

### Step 1: Install Python
If you don’t have Python installed, download and install it from [python.org](https://www.python.org/downloads/).

### Step 2: Download the Project Files
Download the project files from the provided link or repository.

### Step 3: Install Required Libraries
Open your command prompt or terminal and navigate to the project directory. Then run the following command to install the required libraries:

```bash
pip install -r requirements.txt
```

This command will install the following necessary libraries:
- Pandas: For data manipulation and analysis.
- Matplotlib: For creating static, interactive, and animated visualizations.
- Plotly: For interactive data visualization.
- Streamlit: For creating the web application.

### Step 4: Run the Application
In the same command prompt or terminal window, execute the following command:

```bash
streamlit run dashboard.py
```

This command will start the Streamlit server and open the dashboard in your web browser.

## Using the Dashboard
The dashboard is intuitive and easy to use. Here's a quick guide:

- **Select Companies**: Choose one or more companies to compare their stock data.
- **Choose Attributes**: Select stock attributes like Low, High, Open, Close, or Volume for comparison.
- **View Individual Company Data**: Click on a specific company to view its detailed stock analysis.
- **Download Data**: Use the sidebar option to download stock data for individual companies.

## Features
- Interactive stock data comparison for multiple companies.
- Detailed analysis for individual companies, including advanced stock metrics like Moving Averages, Bollinger Bands, and RSI.
- Option to download stock data in CSV format.

## Acknowledgements
- Dashboard created using [Streamlit](https://streamlit.io/).
- Data analysis powered by Pandas, Matplotlib, and Plotly.

## Contact
For any queries or suggestions regarding this project, feel free to reach out.


##  Additional Information (Files in the Project Directory)

1. dashboard.py: This is the main Python script that runs the Streamlit application. It contains the logic for loading and visualizing stock data, handling user interactions, and rendering the dashboard interface.

2. requirements.txt: This file lists all the Python libraries that are needed to run the application. These dependencies can be installed using pip install -r requirements.txt.

3. Data Files (*.csv): AMZN.csv, GOOG.csv, META.csv, NFLX.csv, SBUX.csv, TSLA.csv: These CSV files contain historical stock data for Amazon, Google, Meta, Netflix, Starbucks, and Tesla, respectively. They are used as the data source for the dashboard.

4. stock_analysis.py: This Python script includes functions and logic for analyzing the stock data. It is used by dashboard.py to perform various calculations and transformations on the stock data.

5. Image Files (*.png): Images like AMZN.png, GOOG.png, META.png, NFLX.png, SBUX.png, TSLA.png: These are logo images for the respective companies. They are used in the dashboard to visually represent each company.

6. README.md: This file provides an overview of the project, detailed instructions on how to install and run the application, a description of the project's features, and credits for data sources and technologies used.


