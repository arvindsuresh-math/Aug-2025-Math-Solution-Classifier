def solve():
    """Index: 3694.
    Returns: the number of Pelicans remaining in Shark Bite Cove.
    """
    # L1
    sharks_pelican_bay = 60 # 60 sharks in Pelican Bay
    sharks_multiple_of_pelicans = 2 # twice the number of Pelicans
    initial_pelicans_shark_bite_cove = sharks_pelican_bay / sharks_multiple_of_pelicans

    # L3
    fraction_moved_denominator = 3 # one-third of the Pelicans
    pelicans_moved_away = initial_pelicans_shark_bite_cove / fraction_moved_denominator

    # L4
    remaining_pelicans_shark_bite_cove = initial_pelicans_shark_bite_cove - pelicans_moved_away

    # FA
    answer = remaining_pelicans_shark_bite_cove
    return answer