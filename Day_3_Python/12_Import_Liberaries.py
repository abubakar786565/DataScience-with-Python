import math
print('The value of pi ', math.pi)


import statistics
x = [2000,2,3333,33,444,65]
print('The mean of the list is ', int(statistics.mean(x)))

print("\n-----------------------------------------------------------------------------------------\n")

import pandas as pd

# Create the dataset
data = {
    'Name': [
        'Fatimah', 'Alia', 'Alia', 'Abubakar', 'hammad', 'Ali', 'hassan',
        'malaika', 'maryam', 'qandeel', 'luqman', 'qasim', 'fatimah', 'mhsin',
        'malaika', 'parveen', 'jack', 'abdullah', 'fatimah', 'jack'
    ],
    'Gender': [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1],
    'Age': [11, 11, 11, 11, 11, 11, 11, 22, 22, 22, 22, 22, 33, 111, 33, 33, 33, 33, 44, 44]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Count occurrences of each name
name_counts = df['Name'].value_counts()

# Display the result
print(name_counts)
