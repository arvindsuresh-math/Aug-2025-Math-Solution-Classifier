def solve():
    """Index: 4633.
    Returns: the amount of change Toby is bringing home.
    """
    # L1
    num_cookies = 3 # three cookies
    cost_per_cookie = 0.5 # $.5 each
    cost_cookies = num_cookies * cost_per_cookie

    # L2
    num_hamburgers = 2 # They each order a cheeseburger
    cost_per_hamburger = 3.65 # $3.65
    cost_hamburgers = num_hamburgers * cost_per_hamburger

    # L3
    cost_milkshake = 2 # milkshake for $2
    cost_coke = 1 # friend gets a coke for $1
    cost_fries = 4 # large fries that cost $4
    tax = 0.2 # tax is $.2
    total_bill = cost_hamburgers + cost_milkshake + cost_coke + cost_fries + cost_cookies + tax

    # L4
    num_people_splitting = 2 # They agree to split the bill
    cost_per_person = total_bill / num_people_splitting

    # L5
    toby_initial_money = 15 # Toby arrived with $15
    toby_change = toby_initial_money - cost_per_person

    # FA
    answer = toby_change
    return answer