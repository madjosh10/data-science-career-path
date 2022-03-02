# create the initial variables below
age = 28
bmi = 26.2
num_of_children = 3
sex = 0
smoker = 0

# Add insurance estimate formula below
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print(f"This person's insurance cost is {insurance_cost} dollars.")
# Age Factor
age += 4
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print(f"The change in cost of insurance after increasing the age by 4 years is {change_in_insurance_cost} dollars.")
# print(change_in_insurance_cost)
# BMI Factor
bmi += 3.1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print(f"The change in estimated insurance cost after increasing BMI by 3.1 is {change_in_insurance_cost} dollars.")
# Male vs. Female Factor
print("\n")
bmi = 26.2
sex = 1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print(f"The change in estimated cost for being male instead of female is {change_in_insurance_cost} dollars.")
# Extra Practice
smoker = 1
# num_of_children = 5
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost
print(f"The change in estimated cost for being a smoker vs nonsmoker is {change_in_insurance_cost} dollars")
