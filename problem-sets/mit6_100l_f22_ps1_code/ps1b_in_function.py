def part_b(yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise):
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
	return months