def solve():
    """Index: 3125.
    Returns: the percentage of werewolves Van Helsing removed.
    """
    # L1
    werewolves_removed = 8 # removes 8 werewolves
    werewolf_pay_per_unit = 10 # $10 per werewolf
    earned_from_werewolves = werewolves_removed * werewolf_pay_per_unit

    # L2
    total_earned = 105 # earned $105
    earned_from_vampires = total_earned - earned_from_werewolves

    # L3
    vampire_pay_per_unit = 5 # $5 per vampire
    vampires_removed = earned_from_vampires / vampire_pay_per_unit

    # L4
    vampires_removed_fraction = 0.5 # removes half the vampires
    total_vampires = vampires_removed / vampires_removed_fraction

    # L5
    werewolves_vampires_ratio = 4 # 4 times as many werewolves as vampires
    total_werewolves = werewolves_vampires_ratio * total_vampires

    # L6
    werewolves_removed_proportion = werewolves_removed / total_werewolves

    # L7
    percent_multiplier = 100 # WK
    werewolves_removed_percentage = percent_multiplier * werewolves_removed_proportion

    # FA
    answer = werewolves_removed_percentage
    return answer