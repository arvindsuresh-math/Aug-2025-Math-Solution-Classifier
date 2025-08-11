from fractions import Fraction

def solve():
    """Index: 1579.
    Returns: the total time Olive would be able to use her phone.
    """
    # L1
    charge_fraction = Fraction(3, 5) # 3/5 of the time she charged the phone last night
    last_night_charge_hours = 10 # charged her phone for 10 hours
    new_charge_hours = charge_fraction * last_night_charge_hours

    # L2
    hours_use_per_charge_hour = 2 # each hour of charge lasts the phone 2 hours of use
    total_use_time = new_charge_hours * hours_use_per_charge_hour

    # FA
    answer = total_use_time
    return answer