def solve():
    """Index: 604.
    Returns: how many more presents Santana has to buy in the second half of the year than the first half.
    """
    # L1
    brothers_october = 1 # 1 of them has a birthday in October
    brothers_november = 1 # 1 has a birthday in November
    brothers_december = 2 # another 2 of them were born in December
    brothers_second_half = brothers_october + brothers_november + brothers_december

    # L2
    total_brothers = 7 # Santana has 7 brothers
    brothers_first_half = total_brothers - brothers_second_half

    # L3
    presents_per_brother = 1 # birthday present per brother (per year)
    presents_christmas = total_brothers # a Christmas present for each brother
    presents_second_half = brothers_second_half * presents_per_brother + presents_christmas

    # L4
    presents_first_half = brothers_first_half * presents_per_brother
    difference = presents_second_half - presents_first_half

    # FA
    answer = difference
    return answer