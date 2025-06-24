def solve_73():
    # Number of baseball team members
    team_members = 13
    # Number of coaches
    coaches = 3
    # Number of helpers
    helpers = 2
    # Number of individual pouches per pack of trail mix
    pouches_per_pack = 6

    # Calculate the total number of people who need a snack
    total_people = team_members + coaches + helpers
    # Calculate the number of packs needed
    # Since each person needs one pouch, total_people is also the total pouches needed
    packs_needed = total_people / pouches_per_pack

    # If the result is not a whole number, Roger needs to buy an extra pack
    # However, in this specific problem, 18 / 6 is exactly 3, so no ceiling needed.
    # If it were, for example, 19 pouches, he would need math.ceil(19/6) = 4 packs.
    # For this problem, it's a direct division.

    return int(packs_needed)

# Execute the function to get the answer
# answer = solve_73()
# print(answer)