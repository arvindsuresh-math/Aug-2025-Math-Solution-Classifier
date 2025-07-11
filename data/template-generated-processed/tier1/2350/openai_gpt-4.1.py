def solve():
    """Index: 2350.
    Returns: the number of apps Roger must delete for his phone to function optimally.
    """
    # L1
    recommended_apps = 35 # recommended number of apps is 35
    multiplier = 2 # twice the recommended number
    roger_apps = recommended_apps * multiplier

    # L2
    max_apps = 50 # maximum of 50 apps
    apps_to_delete = roger_apps - max_apps

    # FA
    answer = apps_to_delete
    return answer