# input statements
salary = 30000
numDependents = 6
state_tax_rate = 0.065
federal_tax_rate = 0.28
dependent_deduction_rate = 0.025

# Calculate taxes
state_tax = salary * state_tax_rate
federal_tax = salary * federal_tax_rate
dependent_deduction = numDependents * (salary * dependent_deduction_rate)
total_withholding = state_tax + federal_tax + dependent_deduction
take_home_pay = salary - total_withholding

# output statements
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(take_home_pay))
print(f"State Withholding Tax: ${state_tax:.2f}")
print(f"Federal Withholding Tax: ${federal_tax:.2f}")
print(f"Dependent Deduction: ${dependent_deduction:.2f}")
print(f"Total Withholding: ${total_withholding:.2f}")
print(f"Take Home Pay: ${take_home_pay:.2f}")