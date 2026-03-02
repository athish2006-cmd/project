import csv

def calculate_column_average():
    filename = input("Enter the CSV filename (including .csv): ")
    column_name = input("Enter the name of the column to average: ")

    total_sum = 0
    count = 0

    try:
        with open(filename, mode='r', encoding='utf-8') as csvfile:
            # DictReader uses the first row as keys for a dictionary
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                try:
                    # Convert the string value to a float
                    value = float(row[column_name])
                    total_sum += value
                    count += 1
                except ValueError:
                    # Skip rows that don't have a valid number
                    continue
                except KeyError:
                    print(f"Error: Column '{column_name}' not found.")
                    return

        if count > 0:
            average = total_sum / count
            print(f"\nThe average of '{column_name}' is: {average:.2f}")
        else:
            print("No numerical data found in that column.")

    except FileNotFoundError:
        print("Error: The file was not found. Please check the name and try again.")

if __name__ == "__main__":
    calculate_column_average()