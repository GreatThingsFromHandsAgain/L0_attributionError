import pandas as pd

# Load the data from the Excel file and the text file
fcfs_provisional_list = pd.read_excel('/Users/home/Desktop/fcfs_provisional_list.xlsx')
with open('/Users/home/Desktop/GTFH_totaladdresses.txt', 'r') as file:
    GTFH_totaladdresses = file.read().splitlines()

# Filter the data in the Excel file from the .txt file
filtered_list = fcfs_provisional_list[fcfs_provisional_list['Address'].isin(GTFH_totaladdresses)]

# Output the filtered data as .csv
filtered_list.to_csv('/Users/home/Desktop/GTFH_filtered_fcfs_provisional_list.csv', index=False)
