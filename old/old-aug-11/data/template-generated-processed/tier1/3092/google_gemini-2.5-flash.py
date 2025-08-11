def solve():
    """Index: 3092.
    Returns: the total money earned by the store this week.
    """
    # L1
    num_graphics_cards = 10 # 10 graphics cards
    cost_graphics_card = 600 # $600 each
    earned_graphics_cards = num_graphics_cards * cost_graphics_card

    # L2
    num_hard_drives = 14 # 14 hard drives
    cost_hard_drive = 80 # $80 each
    earned_hard_drives = num_hard_drives * cost_hard_drive

    # L3
    num_cpus = 8 # 8 CPUs
    cost_cpu = 200 # $200 each
    earned_cpus = num_cpus * cost_cpu

    # L4
    num_ram_pairs = 4 # 4 pairs of RAM
    cost_ram_pair = 60 # $60 for each pair
    earned_ram = num_ram_pairs * cost_ram_pair

    # L5
    total_earnings = earned_graphics_cards + earned_hard_drives + earned_cpus + earned_ram

    # FA
    answer = total_earnings
    return answer