import pandas as pd

file_name = input("Enter the Excel file name: ")

try:
    data = pd.read_excel(file_name)
    print("\nData from Excel file:\n")
    print(data)

except FileNotFoundError:
    print("Error: File not found. Please check the file name.")
except ValueError:
    print("Error: Invalid file format. Please provide a valid Excel file.")
except Exception as e:
    print("Unexpected error occurred:", e)