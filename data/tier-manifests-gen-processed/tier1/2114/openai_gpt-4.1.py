def solve():
    """Index: 2114.
    Returns: the number of pages in the longest collection.
    """
    # L1
    miles_inches = 240 # Miles's books are 240 inches tall
    miles_pages_per_inch = 5 # for Miles, 1 inch equals 5 pages
    miles_pages = miles_inches * miles_pages_per_inch

    # L2
    daphne_inches = 25 # Daphne's collection is 25 inches tall
    daphne_pages_per_inch = 50 # for Daphne 1 inch equals 50 pages
    daphne_pages = daphne_inches * daphne_pages_per_inch

    # L3
    largest_collection_pages = daphne_pages if daphne_pages > miles_pages else miles_pages

    # FA
    answer = largest_collection_pages
    return answer