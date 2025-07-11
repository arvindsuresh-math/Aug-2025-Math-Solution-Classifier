def solve():
    """Index: 1866.
    Returns: the total number of minutes Carolyn needs to spend embroidering.
    """
    # L1
    num_flowers = 50 # 50 flowers
    stitches_per_flower = 60 # 60 stitches to embroider
    total_flower_stitches = num_flowers * stitches_per_flower

    # L2
    num_unicorns = 3 # 3 unicorns
    stitches_per_unicorn = 180 # 180 stitches
    total_unicorn_stitches = num_unicorns * stitches_per_unicorn

    # L3
    stitches_godzilla = 800 # Godzilla takes 800 stitches
    total_stitches = stitches_godzilla + total_unicorn_stitches + total_flower_stitches

    # L4
    stitches_per_minute = 4 # sew 4 stitches/minute
    total_minutes = total_stitches / stitches_per_minute

    # FA
    answer = total_minutes
    return answer