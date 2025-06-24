def solve():
    total_weight_lost = 103  # kilograms
    weight_lost_person1 = 27  # kilograms
    difference_person2 = 7  # kilograms

    # Calculate weight lost by the second person
    weight_lost_person2 = weight_lost_person1 - difference_person2

    # Calculate the total weight lost by the first two people
    weight_lost_first_two = weight_lost_person1 + weight_lost_person2

    # Calculate the remaining weight lost by the last two people
    remaining_weight_lost = total_weight_lost - weight_lost_first_two

    # Since the two remaining people lost the same amount, divide the remaining weight by 2
    weight_lost_each_last_two = remaining_weight_lost / 2

    return weight_lost_each_last_two

# Execute the function to get the answer
answer = solve()