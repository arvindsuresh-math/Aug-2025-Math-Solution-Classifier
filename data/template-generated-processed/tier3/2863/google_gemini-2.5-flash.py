def solve():
    """Index: 2863.
    Returns: the number of homes that had their panels installed.
    """
    # L1
    total_homes = 20 # total of 20 homes
    panels_per_home = 10 # Each home needed 10 panels
    total_panels_required = total_homes * panels_per_home

    # L2
    panels_less_delivered = 50 # 50 panels less than the required amount
    panels_available = total_panels_required - panels_less_delivered

    # L3
    homes_installed = panels_available / panels_per_home

    # FA
    answer = homes_installed
    return answer