def solve():
    """Index: 1319.
    Returns: the amount each person owes when the bill is split equally.
    """
    # L1
    oysters_dozen = 3 # 3 dozen oysters
    oyster_price_per_dozen = 15.00 # $15.00 a dozen
    oyster_total = oysters_dozen * oyster_price_per_dozen

    # L2
    shrimp_pounds = 2 # 2 pounds of shrimp
    shrimp_price_per_pound = 14.00 # $14.00 a pound
    shrimp_total = shrimp_pounds * shrimp_price_per_pound

    # L3
    clams_pounds = 2 # 2 pounds of fried clams
    clams_price_per_pound = 13.50 # $13.50 a pound
    clams_total = clams_pounds * clams_price_per_pound

    # L4
    bill_total = oyster_total + shrimp_total + clams_total

    # L5
    num_people = 4 # party of 4
    each_owes = bill_total / num_people

    # FA
    answer = each_owes
    return answer