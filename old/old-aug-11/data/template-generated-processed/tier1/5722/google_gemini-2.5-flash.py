def solve():
    """Index: 5722.
    Returns: the total number of cookies Mona, Jasmine, and Rachel brought to share in class.
    """
    # L1
    mona_cookies = 20 # Mona brought 20 cookies
    jasmine_fewer_than_mona = 5 # Jasmine brought 5 fewer cookies than Mona
    jasmine_cookies = mona_cookies - jasmine_fewer_than_mona

    # L2
    rachel_more_than_jasmine = 10 # Rachel brought 10 more cookies than Jasmine
    rachel_cookies = jasmine_cookies + rachel_more_than_jasmine

    # L3
    total_cookies = mona_cookies + jasmine_cookies + rachel_cookies

    # FA
    answer = total_cookies
    return answer