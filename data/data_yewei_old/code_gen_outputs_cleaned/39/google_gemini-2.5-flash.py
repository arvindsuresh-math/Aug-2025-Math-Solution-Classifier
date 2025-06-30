def solve_39():
    # Anna's candy details
    anna_candy_per_house = 14
    anna_houses = 60

    # Billy's candy details
    billy_candy_per_house = 11
    billy_houses = 75

    # Calculate total candy for Anna
    anna_total_candy = anna_candy_per_house * anna_houses

    # Calculate total candy for Billy
    billy_total_candy = billy_candy_per_house * billy_houses

    # Calculate the difference in candy
    candy_difference = anna_total_candy - billy_total_candy

    return candy_difference

# Execute the function to get the answer
# print(solve_39())