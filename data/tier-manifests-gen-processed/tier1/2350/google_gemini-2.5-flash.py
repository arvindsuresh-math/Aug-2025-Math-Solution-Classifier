def solve():
    """Index: 2350.
    Returns: the number of apps Roger must delete.
    """
    # L1
    recommended_apps = 35 # recommended number of apps is 35
    multiplier_for_current_apps = 2 # twice the recommended number of apps
    current_apps = recommended_apps * multiplier_for_current_apps

    # L2
    maximum_apps = 50 # maximum of 50 apps
    apps_to_delete = current_apps - maximum_apps

    # FA
    answer = apps_to_delete
    return answer