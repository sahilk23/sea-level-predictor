#importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


# reading csv file
df = pd.read_csv('epa-sea-level.csv')

# x,y co-ordinates for scatter plot
x = df['Year']
y = df['CSIRO Adjusted Sea Level']


# finding slope and intercept using linregress function (year 1880)
line1 = linregress(x, y)
reg_line = line1.slope * x + line1.intercept  # slope-intercept form ( y=mx+c )


# plotting the data points (x,y) using scatter plot
plt.figure().set_figwidth(9)
plt.scatter(x,y, color = 'red', label='Data points')
plt.xlabel('Years')
plt.ylabel('CSIRO Adjusted Sea Level')
plt.legend()
plt.show()


# plotting the first regression line from 1880-2050 to predict sea level in year 2050
plt.figure().set_figwidth(11)
plt.scatter(x,y, color = 'red', label='Data points')
plt.plot(x, reg_line, color='blue', label='Regression Line')

extended_x1= np.arange(1880, 2050)
reg_line1 = line1.slope * extended_x1 + line1.intercept  # slope-intercept form ( y=mx+c )
plt.plot(extended_x1, reg_line1, color='blue',linestyle='dashed', label='Extended Regression Line (2050)')

plt.xlabel('Years')
plt.ylabel('CSIRO Adjusted Sea Level')

plt.legend()
plt.show()


# Now as the direction of data points in scatter plot is changing from year 2000, plotting another regression line

# filtering out data from the year 2000 onwards. 
df2 = df.loc[df['Year']>=2000]
x2 = df2['Year']
y2 = df2['CSIRO Adjusted Sea Level']



# plotting the second regression line to predict the sea level in 2050 using the data collected from 2000 onwards 

plt.figure().set_figwidth(11)
plt.scatter(x,y, color = 'red', label='Data points')
plt.plot(x, reg_line, color='blue', label='Regression Line')

extended_x1= np.arange(1880, 2050)
reg_line1 = line1.slope * extended_x1 + line1.intercept
plt.plot(extended_x1, reg_line1, color='blue',linestyle='dashed', label='Extended Regression Line (1880-2050)')


line2 = linregress(x2, y2)  # finding slope and intercept using linregress function (year 2000)

extended_x2= np.arange(2000, 2050)
reg_line2 = line2.slope * extended_x2 + line2.intercept
plt.plot(extended_x2, reg_line2, color='green',linestyle='dashed', label='Extended Regression Line (2000-2050)')

plt.xlabel('Years')
plt.ylabel("Sea Level (inches)")
plt.title('Rise in Sea Level')
plt.legend()
plt.show()







