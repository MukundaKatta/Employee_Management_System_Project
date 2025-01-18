import csv
file_path = "employees.csv"

def load_employees(file_path):
    employees = []
    try:
        with open(file_path) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                employees.append(row)
        print(f"Successfully loaded {len(employees)} employees")
    except FileNotFoundError:
        print(f"File {file_path} not found")
    except Exception as error:
        print(f"An error occurred while loading employees: {error}")
    return employees

if __name__ == "__main__":
    file_path = "employees.csv"
    employees = load_employees(file_path)
    if employees:
        print("Employees loaded")
        for emp in employees:
            print(f"ID: {emp['EmployeeID']}, Name: {emp['Name']}, "
                  f"Department: {emp['Department']}, "
                  f"Position: {emp['Position']}, "
                  f'salary: {emp["Salary"]}')
    else:
        print("Employees not found")



