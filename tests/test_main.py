import csv

import pytest

from main import load_employees, print_employees

HEADER = ["EmployeeID", "Name", "Department", "Position", "Salary"]
ROWS = [
    ["101", "Mukunda", "Engineering", "Software Engineer", "80000"],
    ["102", "Seshu", "HR", "HR Manager", "90000"],
]


def _write_csv(path, header, rows):
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(header)
        writer.writerows(rows)
    return str(path)


def test_load_employees_valid(tmp_path):
    csv_path = _write_csv(tmp_path / "employees.csv", HEADER, ROWS)
    employees, error = load_employees(csv_path)

    assert error is None
    assert len(employees) == 2
    assert employees[0]["EmployeeID"] == "101"
    assert employees[0]["Name"] == "Mukunda"
    assert employees[1]["Salary"] == "90000"


def test_load_employees_missing_file():
    employees, error = load_employees("/no/such/file.csv")

    assert employees == []
    assert error is not None
    assert "not found" in error


def test_load_employees_empty_file(tmp_path):
    csv_path = _write_csv(tmp_path / "empty.csv", HEADER, [])
    employees, error = load_employees(csv_path)

    assert error is None
    assert employees == []


def test_load_employees_bad_format(tmp_path):
    bad_header = ["EmployeeID", "Name", "Department"]
    csv_path = _write_csv(tmp_path / "bad.csv", bad_header, [["1", "A", "Eng"]])
    employees, error = load_employees(csv_path)

    assert employees == []
    assert error == "File format is incorrect or corrupted."


def test_print_employees(capsys):
    employees = [
        {
            "EmployeeID": "101",
            "Name": "Mukunda",
            "Department": "Engineering",
            "Position": "Software Engineer",
            "Salary": "80000",
        }
    ]
    print_employees(employees)
    captured = capsys.readouterr()

    assert "ID: 101" in captured.out
    assert "Name: Mukunda" in captured.out
    assert "Department: Engineering" in captured.out
    assert "Position: Software Engineer" in captured.out
    assert "Salary: 80000" in captured.out


def test_print_employees_empty(capsys):
    print_employees([])
    captured = capsys.readouterr()

    assert captured.out == ""


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
