def solve():
    """Index: 4522.
    Returns: the total number of keys Tim needs.
    """
    # L1
    num_apartment_complexes = 2 # two apartment complexes
    apartments_per_complex = 12 # each have 12 apartments
    total_apartments = num_apartment_complexes * apartments_per_complex

    # L2
    keys_per_lock = 3 # 3 keys per lock
    total_keys = total_apartments * keys_per_lock

    # FA
    answer = total_keys
    return answer