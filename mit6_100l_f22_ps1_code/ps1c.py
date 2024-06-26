initial_deposit = float(input("Enter the initial deposit: "))

# Constants
total_cost = 800000
down_payment = 0.25 * total_cost
target_savings = down_payment - 100
low = 0.0
high = 1.0
steps = 0

if initial_deposit >= target_savings:
    print("Best savings rate: 0.0")
    print("Steps in bisection search: 0")
else:
    while low <= high:
        steps += 1
        mid = (low + high) / 2
        amount_saved = initial_deposit * ((1 + mid / 12) ** 36)
        
        if amount_saved > target_savings:
            high = mid - 0.0001  # Slightly reduce high bound
        else:
            low = mid + 0.0001   # Slightly increase low bound
        
        if abs(amount_saved - target_savings) <= 100:
            best_rate = mid
            break

    print(f"Best savings rate: {best_rate}")
    print(f"Steps in bisection search: {steps}")
