def solve():
    # John's base daily pay
    base_daily_pay = 80
    # John's base daily work hours
    base_daily_hours = 8
    
    # Performance bonus amount
    bonus_amount = 20
    # Extra hours worked for the bonus
    extra_hours_for_bonus = 2
    
    # Calculate total daily hours worked with the bonus
    total_daily_hours = base_daily_hours + extra_hours_for_bonus
    
    # Calculate total daily pay with the bonus
    total_daily_pay = base_daily_pay + bonus_amount
    
    # Calculate hourly rate when earning the bonus
    hourly_rate = total_daily_pay / total_daily_hours
    
    return hourly_rate

# Execute the function to get the answer
answer = solve()