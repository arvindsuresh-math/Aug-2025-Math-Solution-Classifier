def solve():
    """Index: 1936.
    Returns: the amount of money third place gets.
    """
    # L1
    friends_count = 7 # 7 friends
    josh_count = 1 # Everyone including him
    total_people = friends_count + josh_count

    # L2
    money_per_person = 5 # puts 5 dollars into a pot
    total_pot_money = total_people * money_per_person

    # L3
    first_place_percent = 0.8 # 80% of the money
    first_place_money = total_pot_money * first_place_percent

    # L4
    remaining_money = total_pot_money - first_place_money

    # L5
    split_places = 2 # Second and third place split the rest
    third_place_money = remaining_money / split_places

    # FA
    answer = third_place_money
    return answer