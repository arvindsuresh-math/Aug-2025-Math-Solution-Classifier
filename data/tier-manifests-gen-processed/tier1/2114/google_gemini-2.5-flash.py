def solve():
    """Index: 2114.
    Returns: the number of pages in the longest collection.
    """
    # L1
    miles_height_inches = 240 # Miles's books are 240 inches tall
    miles_pages_per_inch = 5 # 1 inch equals 5 pages
    miles_total_pages = miles_height_inches * miles_pages_per_inch

    # L2
    daphne_height_inches = 25 # Daphne's collection is 25 inches tall
    daphne_pages_per_inch = 50 # 1 inch equals 50 pages
    daphne_total_pages = daphne_height_inches * daphne_pages_per_inch

    # L3
    longest_collection_pages = max(miles_total_pages, daphne_total_pages)

    # FA
    answer = longest_collection_pages
    return answer