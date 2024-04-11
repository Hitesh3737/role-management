import csv

# Specify the path to your CSV file
csv_file_path = 'user_data.csv'

# Read the CSV file and print its contents
with open("D:/hitesh/user_data.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
