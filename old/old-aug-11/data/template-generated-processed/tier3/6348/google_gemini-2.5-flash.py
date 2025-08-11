def solve():
    """Index: 6348.
    Returns: the total number of llamas Jill has now.
    """
    # L1
    llamas_pregnant_with_twins = 5 # 5 of them got pregnant with twins
    calves_per_twin_pregnancy = 2 # WK
    calves_from_twins = llamas_pregnant_with_twins * calves_per_twin_pregnancy

    # L2
    calves_from_single_births = 9 # Nine of her llamas got pregnant with 1 calf
    adult_llamas_pregnant_with_twins = 5 # 5 of them got pregnant with twins
    adult_llamas_pregnant_with_one_calf = 9 # Nine of her llamas got pregnant with 1 calf
    total_llamas_before_trade = calves_from_single_births + adult_llamas_pregnant_with_twins + adult_llamas_pregnant_with_one_calf + calves_from_twins

    # L3
    calves_traded = 8 # traded 8 of the calves
    llamas_after_calves_traded = total_llamas_before_trade - calves_traded

    # L4
    new_adult_llamas_gained = 2 # traded 8 of the calves for 2 new adult llamas
    llamas_after_trade = llamas_after_calves_traded + new_adult_llamas_gained

    # L5
    fraction_sold_denominator = 3 # sells 1/3 of her herd
    llamas_sold = llamas_after_trade / fraction_sold_denominator

    # L6
    final_llamas = llamas_after_trade - llamas_sold

    # FA
    answer = final_llamas
    return answer