import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 5))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], c='r', edgecolors='blue', label='original data')

    # Create first line of best fit
    y1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    m = y1.slope
    b = y1.intercept
    x1 = np.arange(df['Year'].min(), 2050, 1)
    y_hat = m * x1 + b

    plt.plot(x1, y_hat, label='fitted line1')

    # Create second line of best fit
    y2 = linregress(df[df['Year'] >= 2000]['Year'], df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])
    m1 = y2.slope
    b1 = y2.intercept
    x2 = np.arange(2000, 2050, 1)
    y_hat1 = m1 * x2 + b1
    plt.plot(x2, y_hat1, label='fitted line2')
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    # plt.show()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


draw_plot()
