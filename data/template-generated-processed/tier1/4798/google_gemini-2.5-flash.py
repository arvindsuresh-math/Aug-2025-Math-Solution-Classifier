def solve():
    """Index: 4798.
    Returns: the number of gallons of milk left in the storage tank.
    """
    # L1
    pumping_hours = 4 # 4 hours pumping milk
    pumping_rate = 2880 # rate of 2,880 gallons/hour
    pumped_milk = pumping_hours * pumping_rate

    # L2
    initial_milk = 30000 # collected 30,000 gallons of milk
    remaining_after_pumping = initial_milk - pumped_milk

    # L3
    adding_hours = 7 # next 7 hours
    adding_rate = 1500 # rate of 1,500 gallons per hour
    added_milk = adding_rate * adding_hours

    # L4
    final_milk_in_tank = remaining_after_pumping + added_milk

    # FA
    answer = final_milk_in_tank
    return answer