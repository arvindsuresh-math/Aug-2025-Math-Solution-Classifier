def solve(
    num_green_beads_per_repeat: int = 3, # 3 green beads
    num_purple_beads_per_repeat: int = 5, # 5 purple beads
    red_bead_multiplier: int = 2, # twice as many red beads as green beads
    repeats_per_bracelet: int = 3, # pattern repeats three times per bracelet
    repeats_per_necklace: int = 5, # 5 times per necklace
    num_bracelets_to_make: int = 1, # make 1 bracelets
    num_necklaces_to_make: int = 10 # and 10 necklaces
):
    """Code for Q 3779 from the GSM8K dataset (train).
    Returns the total number of beads needed to make the specified number of bracelets and necklaces.
    """
    # First find the number of red beads per repeat: 3 green * 2 red/green = <<3*2=6>>6 red
    num_red_beads_per_repeat = num_green_beads_per_repeat * red_bead_multiplier

    # Then add the number of beads of each color to find the total number of bead per repeat: 6 beads + 3 beads + 5 beads = <<6+3+5=14>>14 beads
    total_beads_per_repeat = num_red_beads_per_repeat + num_green_beads_per_repeat + num_purple_beads_per_repeat

    # Then multiply the number of beads per repeat by the number of repeats per bracelet to find the number of beads per bracelet: 14 beads/repeat * 3 repeats/bracelet = <<14*3=42>>42 beads/bracelet
    beads_per_bracelet = total_beads_per_repeat * repeats_per_bracelet

    # Then multiply the number of beads per repeat by the number of repeats per necklace to find the number of beads per necklace: 14 beads/repeat * 5 repeats/necklace = <<14*5=70>>70 beads/necklace
    beads_per_necklace = total_beads_per_repeat * repeats_per_necklace

    # Then multiply the number of beads per necklace by the number of necklaces to find the total number of beads used in the necklaces: 70 beads/necklace * 10 necklaces = <<70*10=700>>700 beads
    total_beads_necklaces = beads_per_necklace * num_necklaces_to_make

    # Then add the number of beads used in a bracelet to the number of beads in the necklaces to find the total number of beads used: 700 beads + 42 beads = <<700+42=742>>742 beads
    total_beads_bracelets = beads_per_bracelet * num_bracelets_to_make # Calculate beads for the specified number of bracelets
    total_beads_used = total_beads_necklaces + total_beads_bracelets

    # The final answer is the total number of beads used
    return total_beads_used