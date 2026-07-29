import employee
import salary
import report

def main():
    # جمع معلومات الموظف
    name, emp_id, basic, allowance, overtime, years = employee.get_employee()
    
    # حساب الراتب
    gross = salary.calculate_gross(basic, allowance, overtime, years)
    epf = salary.calculate_epf(gross)
    socso = salary.calculate_socso(gross)
    net = salary.calculate_net(gross, epf, socso)
    
    # عرض التقرير
    report.print_report(name, emp_id, basic, allowance, overtime, years,
                        gross, epf, socso, net)

if __name__ == "__main__":
    main()
