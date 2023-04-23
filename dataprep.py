# -*- coding: utf-8 -*-
'''
Documentation: - Delete when complete
* Talk to 'Future You' readint the methods and classes 6/8 months from now.
* Future you has spent those months on 5/6 other projects and cant
remember any of this.
* Future you doesn't have time to spend a full day trying to 'get
into' the code in order to fix a bug / adapt a method.
* Be Generous to future you, that will be you some day.

DESCRIPTION:

Feature: #Enter feature name here
# Enter feature description here

Scenario: #Enter scenario name here
# Enter steps here

:Author: Tom
:Created: 20/04/2023
:Copyright: Tom Welsh - twelsh37@gmail.com
'''

# Initial imports
import pandas as pd
import re
import openpyxl

# Housekeepimg Tasks

# Set width of dataframe to show all columns
pd.set_option('display.max_columns', None)

# Set depth of max_rows to unlimited
pd.set_option('display.max_rows', None)

# Setup Plotly as our backend graphing package
pd.options.plotting.backend = 'plotly'

# Display to 2 decimal points
pd.set_option("display.precision", 2)


# assign the output of our prep_data function to our dataframe


def import_data(data):
    # Set the 'de_oe' fields to upper case so its consistent
    data['de_oe'] = data['de_oe'].str.upper()

    prefix = []

    def business_unit():
        prefix_search = re.compile(r'^[a-zA-Z]+')

        for value in data['risk_id']:
            zz = prefix_search.findall(str(value))
            prefix.append(zz)

        return prefix

    business_unit()

    # Takes our list of lists, 'prefix', from the function
    # above and pulls out all its members into one list 'extract'
    extract = [item[0] for item in prefix]

    # Insert a new column to hold our business unit and populate it with Business Unit Names
    # We get the business unit names from the 'extract[]' list in the step above

    def append_col_names():

        result = []
        for value in extract:
            if value == 'DP':
                result.append('Data Privacy')
            elif value == 'COSECG':
                result.append('Company Secretariat')
            elif value == 'BI':
                result.append('Business Inteligence')
            elif value == 'ITDEV':
                result.append('IT Development')
            elif value == 'GMBH':
                result.append('GmbH')
            elif value == 'SEC':
                result.append('Information Security')
            elif value == 'FR':
                result.append('Financial Risk')
            elif value == 'CASS':
                result.append('Client Money')
            elif value == 'PROD':
                result.append('Market Data')
            elif value == 'CSA':
                result.append('Client Services APAC')
            elif value == 'SDBO':
                result.append('Stockbroking Dealing & Business Operations')
            elif value == 'SBDC':
                result.append('Stockbroking Business Change')
            elif value == 'SBBC':
                result.append('Stockbroking Operations')
            elif value == 'SCM':
                result.append('Stockbroking Client Money')
            elif value == 'SOS':
                result.append('Stockbroking Operations Scrip - APAC')
            elif value == 'SOC':
                result.append('Stockbroking Operations Cash - APAC')
            elif value == 'SOT':
                result.append('Stockbroking Operations Tax - APAC')
            elif value == 'COSECA':
                result.append('Company Secretariat - APAC')
            elif value == 'SP':
                result.append('Stockbroking Partners')
            elif value == 'WD':
                result.append('Stockbroking Web Development')
            elif value == 'HR':
                result.append('HR')
            elif value == 'BCG':
                result.append('Business Continuity Management')
            elif value == 'ISP':
                result.append('CMC Connect')
            elif value == 'CSG':
                result.append('Client Services')
            elif value == 'ST':
                result.append('Sales Trading')
            elif value == 'TAX':
                result.append('Tax')
            elif value == 'FIN':
                result.append('Finance')
            elif value == 'FACL':
                result.append('Facilities')
            elif value == 'ITPROD':
                result.append('IT Production')
            elif value == 'LEG':
                result.append('Legal')
            elif value == 'TRAD':
                result.append('Trading incl. Pricing and Risk Dev')
            elif value == 'MAR':
                result.append('Marketing')
            elif value == 'BO':
                result.append('Business Operations')
            elif value == 'OR':
                result.append('Operational Risk')
            elif value == 'LR':
                result.append('Liquidity Risk')
            elif value == 'FCT':
                result.append('Financial Crime')
            elif value == 'BCA':
                result.append('Business Change AUS')
            elif value == 'BC':
                result.append('Business Change')
            elif value == 'COMP':
                result.append('Compliance')
            elif value == 'CD':
                result.append('Corporate Development')
            elif value == 'PRU':
                result.append('Prudential Regulation - UK/ME')
            elif value == 'IR':
                result.append('Investor Relations')
            elif value == 'TRE':
                result.append('Treasuary')
            elif value == 'STBM':
                result.append('Stockbroking Marketing')
            else:
                display(f"Business Unit {value} has not been added to the function yet")

                # Apply reuslts to 'business_unit' to create the column in the dataframe
        data['business_unit'] = result
        return append_col_names

    # Run our function to add the 'business_unit' names to our data frame
    append_col_names()

    def add_risk_metrics():
        # Calculate our gross and net risk scores
        # it does this by multiplying the impact and likelihood columns
        # the results are appended to the raca_df dataframe under columns
        # gross_risk and net_risk respectivly
        data['gross_risk'] = data['gross_impact'] * data['gross_likelihood']

        data['net_risk'] = data['net_impact'] * data['net_likelihood']

    add_risk_metrics()

    return data


# Simple sanity check function to ensure we have data frames of data
# This displays the unique number of each

def sanity_check():

    # Load our RACA spreadsheets
    y2020raca = pd.read_excel('C:/Data/raca_data/raca2020.xlsx')
    # 2021 RACA
    y2021raca = pd.read_excel('C:/Data/raca_data/raca2021.xlsx')

    # 2022 RACA
    y2022raca = pd.read_excel('C:/Data/raca_data/raca2022.xlsx')

    # Read in our data
    y2021raca = import_data(y2021raca)
    y2021raca = import_data(y2021raca)
    y2022raca = import_data(y2022raca)

    # run our sanity check function on each dataframe
    # 2022
    # number of processes
    a_processes = y2022raca['process_title'].nunique()

    # number of risks
    a_risk = y2022raca['risk_id'].nunique()

    # Number of Controls
    a_control = y2022raca['control_id'].nunique()

    # Number of Actions
    a_action = y2022raca['action_id'].nunique()

    # number of processes
    b_processes = y2021raca['process_title'].nunique()

    # 2021
    # number of risks
    b_risk = y2021raca['risk_id'].nunique()

    # Number of Controls
    b_control = y2021raca['control_id'].nunique()

    # Number of Actions
    b_action = y2021raca['action_id'].nunique()

    # Control Activity - for guage
    ca = y2022raca['control_activity']
    cb = y2021raca['control_activity']

    return y2020raca, y2021raca, y2022raca, a_processes, a_risk, a_control, a_action, b_processes, b_risk, \
        b_control, b_action, ca, cb


    controla = ca.value_counts()
    controlb = ba.value_counts()

# Our Main function
def main():
    pass

if __name__ == '__main__':
    main()
