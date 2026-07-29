def get_employee():
    print("=== Employee Information ===")
    name = input("Enter employee name: ")
    employee_id = input("Enter employee ID: ")
    basic_salary = float(input("Enter basic salary (RM): "))
    allowance = float(input("Enter allowance (RM): "))
    overtime_hours = float(input("Enter overtime hours: "))
    years_worked = int(input("Enter years worked: "))
    return name, employee_id, basic_salary, allowance, overtime_hours, years_worked
