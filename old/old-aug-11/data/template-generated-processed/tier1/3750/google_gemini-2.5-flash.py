def solve():
    """Index: 3750.
    Returns: the total combined machine operation time in seconds.
    """
    # L1
    num_dolls = 12000 # 12000 dolls
    shoes_per_doll = 2 # 2 shoes
    total_shoes = num_dolls * shoes_per_doll

    # L2
    bags_per_doll = 3 # 3 bags
    total_bags = num_dolls * bags_per_doll

    # L3
    cosmetics_per_doll = 1 # 1 set of cosmetics
    total_cosmetics = num_dolls * cosmetics_per_doll

    # L4
    hats_per_doll = 5 # 5 hats
    total_hats = num_dolls * hats_per_doll

    # L5
    total_accessories_count = total_shoes + total_bags + total_cosmetics + total_hats

    # L6
    time_per_doll = 45 # 45 seconds
    total_doll_time = num_dolls * time_per_doll

    # L7
    time_per_accessory = 10 # 10 seconds
    total_accessory_time = total_accessories_count * time_per_accessory

    # L8
    total_combined_time = total_accessory_time + total_doll_time

    # FA
    answer = total_combined_time
    return answer