def solve():
    """Index: 5957.
    Returns: the average number of different birds Kendra saw per site.
    """
    # L1
    monday_sites = 5 # On Monday they visited 5 sites
    monday_avg_birds = 7 # saw an average of 7 birds at each site
    monday_total_birds = monday_sites * monday_avg_birds

    # L2
    tuesday_sites = 5 # On Tuesday, Kendra visited 5 sites
    tuesday_avg_birds = 5 # saw an average of 5 birds at each site
    tuesday_total_birds = tuesday_sites * tuesday_avg_birds

    # L3
    wednesday_sites = 10 # On Wednesday visited 10 sites
    wednesday_avg_birds = 8 # saw an average of 8 birds at each site
    wednesday_total_birds = wednesday_sites * wednesday_avg_birds

    # L4
    total_birds_seen = monday_total_birds + tuesday_total_birds + wednesday_total_birds

    # L5
    total_sites_visited = monday_sites + tuesday_sites + wednesday_sites

    # L6
    average_birds_per_site = total_birds_seen / total_sites_visited

    # FA
    answer = average_birds_per_site
    return answer