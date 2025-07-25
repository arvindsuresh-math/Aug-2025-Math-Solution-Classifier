def solve():
    """Index: 3160.
    Returns: the total number of tabs opened in all browsers together.
    """
    # L1
    tabs_per_window = 10 # each with ten tabs
    windows_per_browser = 3 # opened three windows
    tabs_per_browser = tabs_per_window * windows_per_browser

    # L2
    num_browsers = 2 # two browsers
    total_tabs = num_browsers * tabs_per_browser

    # FA
    answer = total_tabs
    return answer