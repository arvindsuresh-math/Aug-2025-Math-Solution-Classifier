def solve():
    """Index: 604.
    Returns: the number of more presents Santana has to buy in the second half of the year than the first half of the year.
    """
    # L1
    brothers_bday_october = 1 # 1 of them has a birthday in October
    brothers_bday_november = 1 # 1 has a birthday in November
    brothers_bday_december = 2 # another 2 of them were born in December
    brothers_bday_second_half = brothers_bday_october + brothers_bday_november + brothers_bday_december

    # L2
    total_brothers = 7 # Santana has 7 brothers
    brothers_bday_first_half = total_brothers - brothers_bday_second_half

    # L3
    # The problem states that Santana buys a Christmas present for each of her brothers, and Christmas is in the second half of the year.
    # So, the total number of presents in the second half includes birthday presents for brothers born in the second half
    # and Christmas presents for all brothers.
    presents_second_half = brothers_bday_second_half + total_brothers

    # L4
    # The number of presents in the first half of the year corresponds to the number of brothers with birthdays in the first half.
    presents_first_half = brothers_bday_first_half
    more_presents_second_half = presents_second_half - presents_first_half

    # FA
    answer = more_presents_second_half
    return answer