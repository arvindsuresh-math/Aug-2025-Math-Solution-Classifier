def solve_50():
    # Given values
    monthly_supply_cost = 100
    season_length_months = 4
    total_months_in_year = 12
    cost_per_chore = 10

    # L1: Calculate the total amount Gerald needs to save for the entire season.
    total_savings_needed = monthly_supply_cost * season_length_months

    # L2: Calculate the number of months Gerald has to save (off-season).
    saving_months = total_months_in_year - season_length_months

    # L3: Calculate the amount Gerald needs to save per month during the off-season.
    monthly_savings_goal = total_savings_needed / saving_months

    # L4: Calculate the number of chores he needs to do per month to meet the monthly savings goal.
    chores_per_month = monthly_savings_goal / cost_per_chore

    return int(chores_per_month)