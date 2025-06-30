# Calculate the down payment
down_payment_percentage = 0.20
laptop_cost = 1000
down_payment = laptop_cost * down_payment_percentage

# Calculate the adjusted down payment
additional_down_payment = 20
adjusted_down_payment = down_payment + additional_down_payment

# Calculate the remaining balance after the down payment
remaining_balance = laptop_cost - adjusted_down_payment

# Calculate the monthly installment amount
# The problem states the installment is $65 per month, but let's verify based on the remaining balance and a typical 12-month plan.
# If the remaining balance is to be paid over 12 months:
# monthly_installment = remaining_balance / 12
# However, the problem explicitly states the installment is $65 per month.
# Let's use the given $65 per month for calculations.
monthly_installment = 65

# Calculate the total paid after 4 months
months_paid = 4
total_paid_installments = monthly_installment * months_paid

# Calculate the final balance after 4 months
final_balance = remaining_balance - total_paid_installments

print(f"The down payment is: ${down_payment}")
print(f"The adjusted down payment is: ${adjusted_down_payment}")
print(f"The remaining balance after down payment is: ${remaining_balance}")
print(f"The monthly installment is: ${monthly_installment}")
print(f"The total paid in installments after 4 months is: ${total_paid_installments}")
print(f"The final balance after 4 months is: ${final_balance}")

def solve_66():
    # Calculate the down payment
    down_payment = 1000 * 0.20

    # Calculate the adjusted down payment
    adjusted_down_payment = down_payment + 20

    # Calculate the remaining balance after the down payment
    remaining_balance = 1000 - adjusted_down_payment

    # The problem states the installment is $65 per month.
    monthly_installment = 65

    # Calculate the total paid after 4 months
    total_paid_installments = monthly_installment * 4

    # Calculate the final balance after 4 months
    final_balance = remaining_balance - total_paid_installments
    return int(final_balance)