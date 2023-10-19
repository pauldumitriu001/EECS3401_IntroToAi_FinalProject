import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('wages_by_education.csv')

# Extract the years from the 'Year' column
years = df['year'][::-1]

# Extract the categories and associated data
categories = df.columns[1:]  # Exclude the 'year' column

# Create a figure and axes
fig, ax = plt.subplots()

# Loop through each category and plot a line
for category in categories:
    data = df[category][::-1]
    ax.plot(years, data, label=category)

# Customize the plot
ax.set_xlabel('Years')
ax.set_ylabel('Wages (in $)')
ax.set_title('Category Lines Over Time')
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

# Display the plot
plt.grid(True)
plt.show()