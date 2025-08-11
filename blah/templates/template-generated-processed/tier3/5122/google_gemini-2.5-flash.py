def solve():
    """Index: 5122.
    Returns: the time in minutes to put out the fire.
    """
    # L1
    num_firefighters = 5 # team of 5 firefighters
    gallons_per_hose_per_minute = 20 # 20 gallons of water per minute
    team_delivery_rate_gpm = num_firefighters * gallons_per_hose_per_minute

    # L2
    total_gallons_needed = 4000 # requires 4000 gallons of water
    time_to_extinguish_minutes = total_gallons_needed / team_delivery_rate_gpm

    # FA
    answer = time_to_extinguish_minutes
    return answer