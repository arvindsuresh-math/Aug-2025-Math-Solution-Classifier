def solve():
    """Index: 5913.
    Returns: the total number of hours it will take to make all cakes.
    """
    # L1
    mix_time_per_cake = 12 # 12 minutes to mix
    additional_bake_time = 9 # needs 9 more minutes to bake than mix
    bake_time_per_cake = mix_time_per_cake + additional_bake_time

    # L2
    additional_cool_decorate_time = 6 # takes 6 more minutes to cool and decorate than to bake
    cool_decorate_time_per_cake = bake_time_per_cake + additional_cool_decorate_time

    # L3
    total_minutes_per_cake = mix_time_per_cake + bake_time_per_cake + cool_decorate_time_per_cake

    # L4
    minutes_per_hour = 60 # WK
    hours_per_cake = total_minutes_per_cake / minutes_per_hour

    # L5
    num_cakes = 6 # 6 cakes
    total_hours_all_cakes = hours_per_cake * num_cakes

    # FA
    answer = total_hours_all_cakes
    return answer