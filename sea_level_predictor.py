import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(1)
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    years = pd.Series(list(range(2014, 2051))) 
    nans = np.empty(len(years))
    nans[:] = np.nan
    future_df = pd.DataFrame({
        'Year': years,
        'CSIRO Adjusted Sea Level': nans,
        'Lower Error Bound': nans,
        'Upper Error Bound': nans,
        'NOAA Adjusted Sea Level': nans
        
    })
    comb_df = pd.concat([df, future_df], ignore_index=True)

    res = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    plt.plot(comb_df['Year'], res.intercept + res.slope * comb_df['Year'], 'r')


    # Create second line of best fit
    recent_df = df[df['Year'] >= 2000]
    res2 = linregress(x=recent_df['Year'], y=recent_df['CSIRO Adjusted Sea Level'])
    comb_df_2 = pd.concat([recent_df, future_df], ignore_index=True)
    plt.plot(comb_df_2['Year'], res2.intercept + res2.slope * comb_df_2['Year'], 'm')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()