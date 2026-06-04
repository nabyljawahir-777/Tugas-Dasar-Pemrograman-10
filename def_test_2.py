def calculate_overtime_salary(base_salary, total_hours_worked):
    bonus_salary = ((total_hours_worked - 40) * 50000)
    final_salary =  bonus_salary + base_salary
    if (total_hours_worked > 40):
        print ("final salary")
        print (base_salary, '+', bonus_salary, '=', final_salary)
    else:
        print ("final salary")
        print (base_salary)
    return final_salary
base_salary = 1000000
total_hours_worked = 41
total_salary = calculate_overtime_salary(base_salary, total_hours_worked)