## 6.100A PSet 1: Part A
## Name:
## Time Spent:
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25
r = 0.05
down_payment = cost_of_dream_home * portion_down_payment
monthly_salary = yearly_salary / 12
amount_saved = 0.0
months = 0
###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
while amount_saved < down_payment:
    monthly_savings = monthly_salary * portion_saved
                   
    monthly_return = amount_saved * (r/12)
    semi_annual_return =yearly_salary*(semi_annual_raise/12)*6
    amount_saved += monthly_savings + monthly_return 
    months +=1
    if months %6 == 0:
        yearly_salary+= yearly_salary*semi_annual_raise
        monthly_salary= yearly_salary/12
print ("Number of months:", months)