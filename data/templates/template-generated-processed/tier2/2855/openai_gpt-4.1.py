def solve():
    """Index: 2855.
    Returns: the total amount Erica spends on ice cream in 6 weeks.
    """
    # L1
    creamsicle_days = 3 # Monday, Wednesday, Friday
    creamsicle_price = 2.00 # $2.00 orange creamsicle
    creamsicle_weekly = creamsicle_days * creamsicle_price

    # L2
    sandwich_days = 2 # Tuesday and Thursday
    sandwich_price = 1.50 # $1.50 ice cream sandwich
    sandwich_weekly = sandwich_days * sandwich_price

    # L3
    nutty_buddy_days = 2 # Saturday and Sunday
    nutty_buddy_price = 3.00 # $3.00 Nutty-Buddy
    nutty_buddy_weekly = nutty_buddy_days * nutty_buddy_price

    # L4
    weekly_total = creamsicle_weekly + sandwich_weekly + nutty_buddy_weekly

    # L5
    num_weeks = 6 # 6 weeks in the summer
    total_spent = num_weeks * weekly_total

    # FA
    answer = total_spent
    return answer