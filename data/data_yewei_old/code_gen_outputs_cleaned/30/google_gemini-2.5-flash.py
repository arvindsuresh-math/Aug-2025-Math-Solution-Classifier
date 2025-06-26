def solve():
    # Number of people
    num_people = 4
    # Pieces per personal pan pizza
    pieces_per_pizza = 4

    # Calculate the total number of pizza pieces
    total_pizza_pieces = num_people * pieces_per_pizza

    # Number of people who eat 50% (Bill and Dale)
    num_50_percent_eaters = 2
    # Percentage of pizza eaten by Bill and Dale
    percent_eaten_50 = 0.50
    # Pieces eaten by Bill and Dale
    pieces_eaten_50_percent_group = num_50_percent_eaters * pieces_per_pizza * percent_eaten_50

    # Number of people who eat 75% (Ann and Cate)
    num_75_percent_eaters = 2
    # Percentage of pizza eaten by Ann and Cate
    percent_eaten_75 = 0.75
    # Pieces eaten by Ann and Cate
    pieces_eaten_75_percent_group = num_75_percent_eaters * pieces_per_pizza * percent_eaten_75

    # Calculate the total number of pieces eaten by all four
    total_pieces_eaten = pieces_eaten_50_percent_group + pieces_eaten_75_percent_group

    # Calculate the number of pizza pieces left uneaten
    pieces_left_uneaten = total_pizza_pieces - total_pieces_eaten

    return {
        "total_pizza_pieces": total_pizza_pieces,
        "pieces_eaten_50_percent_group": pieces_eaten_50_percent_group,
        "pieces_eaten_75_percent_group": pieces_eaten_75_percent_group,
        "total_pieces_eaten": total_pieces_eaten,
        "pieces_left_uneaten": pieces_left_uneaten
    }

# Execute the function and get the results
results = solve()
total_pizza_pieces = results["total_pizza_pieces"]
pieces_eaten_50_percent_group = results["pieces_eaten_50_percent_group"]
pieces_eaten_75_percent_group = results["pieces_eaten_75_percent_group"]
total_pieces_eaten = results["total_pieces_eaten"]
pieces_left_uneaten = results["pieces_left_uneaten"]