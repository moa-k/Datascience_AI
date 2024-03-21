import numpy as np
import pandas as pd
import matplotlib as plt
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, 'swedish_population_by_year_and_sex_1860-2022.csv')  

# Read CSV file
swe_pop = pd.read_csv(file_path) # Swedish population
#print('Dimensions:',swe_pop.ndim, 'Shape:', swe_pop.shape, 'Size:', swe_pop.size)
# print('Type:', swe_pop.dtypes )


all_ages = swe_pop["age"]
all_ages = all_ages.str.replace('+', '') # Remove 110+ to 110
all_ages = all_ages.astype(str).astype(int) # From object to int type
#print( all_ages.tail) 

#print( all_ages.head() )
#print('Dimensions:',all_ages.ndim, 'Shape:', all_ages.shape, 'Size:', all_ages.size)
#print('Type:', all_ages.dtypes )

children = swe_pop[all_ages < 15] 
lab_for = swe_pop[(all_ages > 14) & (all_ages < 65)] # Labor force
elderly = swe_pop[all_ages > 64 ]

children = children.iloc[:, 2:]
lab_for = lab_for.iloc[:, 2:]
elderly = elderly.iloc[:, 2:]

children_tot = children.sum()
lab_for_tot = lab_for.sum()
elderly_tot = elderly.sum()

print(children.head())

#print(lab_for.head())

print(children_tot)
print('Dimensions:',children.ndim, 'Shape:', children.shape, 'Size:', children.size)
#print('Type:', children.dtypes )


#print(swe_pop.groupby("sex")["1860"].count())





'''plt.plot(swedish_population['x'], swedish_population['y'])
plt.xlabel('Year')
plt.ylabel('Ratio')
plt.title('Dependency ratio of Sweden from 1860 to 2022')
plt.show()
'''