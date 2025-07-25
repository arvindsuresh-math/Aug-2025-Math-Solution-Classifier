def solve():
    """Index: 4860.
    Returns: the total earnings of the factory in one day.
    """
    # L1
    num_machines_initial = 3 # 3 machines
    hours_per_day_initial_machine = 23 # 23 hours a day
    total_runtime_initial_machines = num_machines_initial * hours_per_day_initial_machine

    # L2
    kg_per_hour_per_machine = 2 # 2 kg of material every hour
    production_initial_machines = total_runtime_initial_machines * kg_per_hour_per_machine

    # L3
    hours_per_day_fourth_machine = 12 # works only 12 hours a day
    production_fourth_machine = hours_per_day_fourth_machine * kg_per_hour_per_machine

    # L4
    total_production_per_day = production_initial_machines + production_fourth_machine

    # L5
    price_per_kg = 50 # $50 per 1 kg
    daily_earnings = total_production_per_day * price_per_kg

    # FA
    answer = daily_earnings
    return answer