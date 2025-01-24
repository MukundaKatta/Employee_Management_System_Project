import csv

def load_employees(file_path):
    employees = []
    try:
        with open(file_path) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                # Validate the presence of expected keys
                if not all(key in row for key in ['EmployeeID', 'Name', 'Department', 'Position', 'Salary']):
                    raise ValueError("File format is incorrect or corrupted.")
                employees.append(row)
        print(f"Successfully loaded {len(employees)} employees")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")
    return employees

def main():
    while True:
        file_path = input("Enter the path to the employees file: ").strip()
        employees = load_employees(file_path)

        if employees:
            print("Employees loaded successfully:")
            for emp in employees:
                print(f"ID: {emp['EmployeeID']}, Name: {emp['Name']}, "
                      f"Department: {emp['Department']}, "
                      f"Position: {emp['Position']}, Salary: {emp['Salary']}")
            break  # Exit the loop if employees are loaded successfully
        else:
            print("Failed to load employees. Please try again.")

if __name__ == "__main__":
    main()
