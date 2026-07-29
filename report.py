def print_report(name, employee_id, basic, allowance, overtime_hours, years_worked,
                 gross, epf, socso, net):
    print("\n=== SALARY REPORT ===")
    print(f"Employee Name   : {name}")
    print(f"Employee ID     : {employee_id}")
    print(f"Basic Salary    : RM {basic:.2f}")
    print(f"Allowance       : RM {allowance:.2f}")
    overtime_value = overtime_hours * 25
    print(f"Overtime        : {overtime_hours} hours (RM {overtime_value:.2f})")
    print(f"Years Worked    : {years_worked}")
    if years_worked > 3:
        print("Bonus (reward)   : RM 300.00 (for >3 years)")
    print(f"Gross Salary    : RM {gross:.2f}")
    print(f"EPF (11%)       : RM {epf:.2f}")
    print(f"SOCSO (0.5%)    : RM {socso:.2f}")
    print(f"Net Salary      : RM {net:.2f}")
    print("========================")
