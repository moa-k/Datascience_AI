import numpy as np
import pandas as pd
import matplotlib as plt
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, 'swedish_population_by_year_and_sex_1860-2022.csv')  

# Read CSV file
swedish_population = pd.read_csv(file_path)

print(swedish_population)

plt.plot(swedish_population['x'], swedish_population['y'])
plt.xlabel('Year')
plt.ylabel('Ratio')
plt.title('Dependency ratio of Sweden from 1860 to 2022')
plt.show()