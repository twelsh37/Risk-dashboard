# Risk-dashboard
Dashboard for investigating risk

## About the Project
The aim of this project is to construct a dashboard to look at risks loaded in via Excel file into Pandas dataframes.
We wil utilise the Dash framework and plotly to create the dashboard. Pandas will be used to store data.<br> Below is 
the current layout of the dashboard but expect this to evolve as it grows.

![screenshot.png](assets%2Fscreenshot.png)

# Instalation
Instalation is simple, just clone the repo and run the following command in the terminal:
```text
git clone https://github.com/twelsh37/Risk-dashboard.git
```

To install the required modules run the following command in the terminal:
```text
pip install -r requirements.txt 
```

# Data Files
Inside the data folder you will find the following files:
* test_2020.xlsx - This is a test file to test the dashboard
* test_2021.xlsx - This is a test file to test the dashboard
* test_2022.xlsx - This is a test file to test the dashboard

These files have random data just to fill the dashboard with data. The dashboard will be able to read in any excel file
with the correct format. 

