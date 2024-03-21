import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Locate file in directory
current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, 'swedish_population_by_year_and_sex_1860-2022.csv')  

# Read CSV file of Swedish population
swe_pop = pd.read_csv(file_path) 

# Remove 110+ to 110 and change type object to type int 
all_ages = swe_pop["age"]
all_ages = all_ages.str.replace('+', '') 
all_ages = all_ages.astype(str).astype(int) 

# Sort the population
children = swe_pop[all_ages < 15] 
lab_for = swe_pop[(all_ages > 14) & (all_ages < 65)] # Labor force
elderly = swe_pop[all_ages > 64 ]

# Remove age and sex
children = children.iloc[:, 2:]  
lab_for = lab_for.iloc[:, 2:]
elderly = elderly.iloc[:, 2:]
swe_pop = swe_pop.iloc[:, 2:]

# Sum of all ages each year (dataframes)
children_tot = children.sum()
lab_for_tot = lab_for.sum()
elderly_tot = elderly.sum()
swe_pop_tot = swe_pop.sum()

# Dependency ratio formula (dataframes)
dep_rat = 100 * ((children_tot + elderly_tot) / lab_for_tot)

# Fraction of total population
children_frac = 100 * (children_tot / swe_pop_tot)
elderly_frac = 100 * (elderly_tot / swe_pop_tot)
depen_frac = 100 * ((children_tot + elderly_tot) / swe_pop_tot)

# Timeline to plot x-axis
years = np.arange(1860, 2023)

# Plot 
plt.figure(1)
plt.plot(years, dep_rat, label="dependency ratio")
plt.xlabel('Timeline [years]')
plt.ylabel('Dependency ratio [percent]')
plt.title('Dependency ratio of Sweden from 1860 to 2022')


plt.figure(2)
plt.plot(years, children_frac, label='children')
plt.plot(years, elderly_frac, label='labor force')
plt.plot(years, depen_frac, label='elderly')
plt.xlabel('Timeline [years]')
plt.ylabel('Fraction of population [percent]')
plt.title('Fraction of children, elderly och total dependent population of the total Swedish population 1860-2022')

'''
plt.figure(2)
plt.plot(years, children_tot, label='children')
plt.plot(years, elderly_tot, label='labor force')
plt.plot(years, lab_for_tot, label='elderly')
plt.xlabel('Timeline [years]')
plt.ylabel('Total amount [individuals]')
plt.title('Total amount of people')
'''

plt.show()

#print('Dimensions:',dep_rat.ndim, 'Shape:', dep_rat.shape, 'Size:', dep_rat.size)
#print(years)
#print(children_tot.head())
#print(lab_for_tot.head())
#print(elderly_tot.head())
#print('Type:', children.dtypes )
#print(lab_for.head())
#print(swe_pop.groupby("sex")["1860"].count())
#print('Dimensions:',swe_pop.ndim, 'Shape:', swe_pop.shape, 'Size:', swe_pop.size)
#print('Type:', swe_pop.dtypes )
#print( all_ages.tail) 