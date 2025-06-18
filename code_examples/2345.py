def solve(
        peppers_per_very_spicy: int = 3,  # Peppers needed for very spicy curries
        peppers_per_spicy: int = 2,  # Peppers needed for spicy curries
        peppers_per_mild: int = 1,  # Peppers needed for mild curries
        previous_very_spicy_curries: int = 30, # Number of very spicy curries previously made
        previous_spicy_curries: int = 30, # Number of spicy curries previously made
        previous_mild_curries: int = 10, # Number of mild curries previously made
        spicy_curries_now: int = 15, # Number of spicy curries now
        mild_curries_now: int = 90 # Number of mild curries now
):
    """Code for Q 2345 from the GSM8K dataset (train).
    Returns how many fewer peppers the curry house buys now compared to before."""
    # The curry house previously bought 3 peppers per very spicy curry * 30 very spicy curries = <<3*30=90>>90 peppers for very spicy curries.
    previous_peppers_for_very_spicy = peppers_per_very_spicy * previous_very_spicy_curries

    # They also bought 2 peppers per spicy curry * 30 spicy curries = <<2*30=60>>60 peppers for spicy curries.
    previous_peppers_for_spicy = peppers_per_spicy * previous_spicy_curries

    # They also bought 1 pepper per mild curry * 10 mild curries = <<1*10=10>>10 peppers for mild curries.
    previous_peppers_for_mild = peppers_per_mild * previous_mild_curries

    # So they were previously buying 90 + 60 + 10 = <<90+60+10=160>>160 peppers.
    previous_total_peppers = (previous_peppers_for_very_spicy + 
                            previous_peppers_for_spicy + 
                            previous_peppers_for_mild)
    
    # They now buy 2 peppers per spicy curry * 15 spicy curries = <<2*15=30>>30 peppers for spicy curries.
    new_peppers_for_spicy = peppers_per_spicy * spicy_curries_now

    #They also now buy 1 pepper per mild curry * 90 mild curries = <<1*90=90>>90 peppers for mild curries.
    new_peppers_for_mild = peppers_per_mild * mild_curries_now

    #So they now buy 30 + 90 = <<30+90=120>>120 peppers.
    new_total_peppers = new_peppers_for_spicy + new_peppers_for_mild

    #This is a difference of 160 peppers bought originally - 120 peppers bought now = <<160-120=40>>40 peppers.
    fewer_peppers = previous_total_peppers - new_total_peppers

    # The final answer is the number of fewer peppers bought
    return fewer_peppers