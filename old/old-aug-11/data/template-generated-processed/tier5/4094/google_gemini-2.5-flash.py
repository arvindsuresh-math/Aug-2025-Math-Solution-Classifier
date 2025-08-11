def solve():
    """Index: 4094.
    Returns: the number of books Susan has in her collection.
    """
    # L1
    # "Let x be the number of books in Susan's collection."
    # This line introduces the variable x, which represents Susan's books.
    # The problem states Lidia's collection is four times bigger than Susan's.
    lidia_multiplier = 4 # four times bigger than
    total_books = 3000 # In total Susan and Lidia, both have 3000 books

    # L2
    # "The collection of both Susan and Lidia would then be 4*x + x = 3000."
    # This step combines Susan's books (x) and Lidia's books (4*x) to form the total.
    # The '5' in the next step comes from 4 (Lidia's multiplier) + 1 (Susan's own collection).
    combined_multiplier = lidia_multiplier + 1

    # L3
    # "5*x = 3000"
    # This is an algebraic simplification of the equation from L2, not a new computation.

    # L4
    x_value_from_calc = total_books / combined_multiplier
    susan_books = x_value_from_calc

    # FA
    answer = susan_books
    return answer