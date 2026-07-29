def calculate_gross(basic, allowance, overtime_hours, years_worked):
    overtime_pay = overtime_hours * 25
    bonus = 300 if years_worked > 3 else 0
    return basic + allowance + overtime_pay + bonus

def calculate_epf(gross):
    return gross * 0.11

def calculate_socso(gross):
    return gross * 0.005

def calculate_net(gross, epf, socso):
    return gross - epf - socso
