def solve():
    """Index: 4366.
    Returns: the total money Seal gets in his first 3 years.
    """
    # L1
    years = 3 # first 3 years
    months_per_year = 12 # WK
    total_months = years * months_per_year

    # L2
    songs_per_month = 3 # 3 songs every month
    total_songs = total_months * songs_per_month

    # L3
    money_per_song = 2000 # $2000 per song
    total_money = total_songs * money_per_song

    # FA
    answer = total_money
    return answer