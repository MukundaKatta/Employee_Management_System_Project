import argparse
import csv


def load_employees(file_path):
    """Load employees from a CSV file. Returns (employees, error) tuple."""
    try:
        with open(file_path, encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            employees = []
            for row in reader:
                if not all(key in row for key in ['EmployeeID', 'Name', 'Department', 'Position', 'Salary']):
                    return [], "File format is incorrect or corrupted."
                employees.append(row)
        return employees, None
    except FileNotFoundError:
        return [], f"File '{file_path}' not found."
    except Exception as error:
        return [], f"An unexpected error occurred: {error}"


def print_employees(employees):
    for emp in employees:
        print(f"ID: {emp['EmployeeID']}, Name: {emp['Name']}, "
              f"Department: {emp['Department']}, "
              f"Position: {emp['Position']}, Salary: {emp['Salary']}")


def main():
    parser = argparse.ArgumentParser(description="Load and display employees from a CSV file.")
    parser.add_argument("file", nargs="?", help="Path to the employees CSV file")
    args = parser.parse_args()

    if args.file:
        employees, error = load_employees(args.file)
        if error:
            print(f"Error: {error}")
            return
        if not employees:
            print("No employee records found in the file.")
            return
        print(f"Successfully loaded {len(employees)} employees:")
        print_employees(employees)
    else:
        while True:
            file_path = input("Enter the path to the employees file: ").strip()
            employees, error = load_employees(file_path)
            if error:
                print(f"Error: {error} Please try again.")
                continue
            if not employees:
                print("No employee records found in the file.")
                break
            print(f"Successfully loaded {len(employees)} employees:")
            print_employees(employees)
            break


if __name__ == "__main__":
    main()
