from fractions import Fraction

def solve():
    """Index: 3191.
    Returns: the total number of ads Vermont clicked on.
    """
    # L1
    first_page_ads = 12 # 12 ads on the first web page
    multiplier_second_page = 2 # twice as many ads
    second_page_ads = first_page_ads * multiplier_second_page

    # L2
    first_and_second_page_total = first_page_ads + second_page_ads

    # L3
    additional_ads_third_page = 24 # 24 more ads
    third_page_ads = additional_ads_third_page + second_page_ads

    # L4
    first_three_pages_total = third_page_ads + first_and_second_page_total

    # L5
    fourth_page_fraction = Fraction(3, 4) # 3/4 times as many ads
    fourth_page_ads = fourth_page_fraction * second_page_ads

    # L6
    total_ads_found = first_three_pages_total + fourth_page_ads

    # L7
    clicked_fraction = Fraction(2, 3) # 2/3 of them
    ads_clicked = clicked_fraction * total_ads_found

    # FA
    answer = ads_clicked
    return answer