def solve():
    """Index: 1319.
    Returns: the amount each person will owe after splitting the bill equally.
    """
    # L1
    num_dozen_oysters = 3 # 3 dozen oysters
    cost_per_dozen_oysters = 15.00 # $15.00 a dozen
    cost_oysters = num_dozen_oysters * cost_per_dozen_oysters

    # L2
    pounds_shrimp = 2 # 2 pounds of steamed shrimp
    cost_per_pound_shrimp = 14.00 # $14.00 a pound
    cost_shrimp = pounds_shrimp * cost_per_pound_shrimp

    # L3
    pounds_clams = 2 # 2 pounds of fried clams
    cost_per_pound_clams = 13.50 # $13.50 a pound
    cost_clams = pounds_clams * cost_per_pound_clams

    # L4
    total_bill = cost_oysters + cost_shrimp + cost_clams

    # L5
    num_people = 4 # A party of 4
    cost_per_person = total_bill / num_people

    # FA
    answer = cost_per_person
    return answer