def solve(
    green_beads_per_repeat: int = 3,  # There are 3 green beads per repeat
    purple_beads_per_repeat: int = 5,  # There are 5 purple beads per repeat
    red_beads_per_repeat_multiplier: int = 2,  # There are twice as many red beads as green beads per repeat
    repeats_per_bracelet: int = 3,  # The pattern repeats 3 times per bracelet
    repeats_per_necklace: int = 5,  # The pattern repeats 5 times per necklace
    num_bracelets: int = 1,  # Susan is making 1 bracelet
    num_necklaces: int = 10  # Susan is making 10 necklaces
):
    """Code for Q 3779 from the GSM8K dataset (train).
    Returns the total number of beads needed to make the bracelets and necklaces.
    """
    # First find the number of red beads per repeat: 3 green * 2 red/green = <<3*2=6>>6 red
    red_beads_per_repeat = green_beads_per_repeat * red_beads_per_repeat_multiplier

    # Then add the number of beads of each color to find the total number of bead per repeat: 6 beads + 3 beads + 5 beads = <<6+3+5=14>>14 beads
    total_beads_per_repeat = red_beads_per_repeat + green_beads_per_repeat + purple_beads_per_repeat

    # Then multiply the number of beads per repeat by the number of repeats per bracelet to find the number of beads per bracelet: 14 beads/repeat * 3 repeats/bracelet = <<14*3=42>>42 beads/bracelet
    beads_per_bracelet = total_beads_per_repeat * repeats_per_bracelet

    # Then multiply the number of beads per repeat by the number of repeats per necklace to find the number of beads per necklace: 14 beads/repeat * 5 repeats/necklace = <<14*5=70>>70 beads/necklace
    beads_per_necklace = total_beads_per_repeat * repeats_per_necklace

    # Then multiply the number of beads per necklace by the number of necklaces to find the total number of beads used in the necklaces: 70 beads/necklace * 10 necklaces = <<70*10=700>>700 beads
    total_beads_in_necklaces = beads_per_necklace * num_necklaces

    # Then add the number of beads used in a bracelet to the number of beads in the necklaces to find the total number of beads used: 700 beads + 42 beads = <<700+42=742>>742 beads
    total_beads_used = total_beads_in_necklaces + (beads_per_bracelet * num_bracelets)

    # The final answer is the total number of beads used
    return total_beads_used