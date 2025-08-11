def solve():
    """Index: 5032.
    Returns: the total number of minutes it took to charge the devices.
    """
    # L1
    phone_full_charge_minutes = 26 # smartphone in 26 minutes
    halfway_divisor = 2 # phone halfway
    phone_half_charge_minutes = phone_full_charge_minutes / halfway_divisor

    # L2
    tablet_full_charge_minutes = 53 # tablet in 53 minutes
    total_charge_minutes = phone_half_charge_minutes + tablet_full_charge_minutes

    # FA
    answer = total_charge_minutes
    return answer