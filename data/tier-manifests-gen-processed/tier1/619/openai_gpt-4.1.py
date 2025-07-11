def solve():
    """Index: 619.
    Returns: the total number of dollars Harry earns in a week.
    """
    # L1
    num_days_7dogs = 3 # Monday, Wednesday, and Friday
    dogs_per_7dog_day = 7 # walks 7 dogs
    dogs_7dog_days = num_days_7dogs * dogs_per_7dog_day

    # L2
    dogs_tuesday = 12 # Tuesday, he walks 12 dogs
    dogs_thursday = 9 # Thursday he walks 9 dogs
    total_dogs = dogs_7dog_days + dogs_tuesday + dogs_thursday

    # L3
    pay_per_dog = 5 # paid $5 for each dog
    total_pay = pay_per_dog * total_dogs

    # FA
    answer = total_pay
    return answer