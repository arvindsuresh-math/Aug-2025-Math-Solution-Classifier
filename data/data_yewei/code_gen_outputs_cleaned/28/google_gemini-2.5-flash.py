def solve_28():
    # Number of houses with a known number of gnomes
    num_first_houses = 4
    # Number of gnomes in each of the first four houses
    gnomes_per_house = 3
    # Total number of gnomes on the street
    total_gnomes_on_street = 20

    # Calculate the total gnomes in the first four houses
    gnomes_in_first_four_houses = num_first_houses * gnomes_per_house

    # Calculate the number of gnomes in the fifth house
    gnomes_in_fifth_house = total_gnomes_on_street - gnomes_in_first_four_houses

    return gnomes_in_fifth_house