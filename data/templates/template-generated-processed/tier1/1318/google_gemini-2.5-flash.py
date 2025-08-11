def solve():
    """Index: 1318.
    Returns: Ruby's height in centimeters.
    """
    # L1
    janet_height = 62 # Janet is 62 centimeters tall
    multiplier_for_charlene = 2 # Charlene is twice that tall
    charlene_height = multiplier_for_charlene * janet_height

    # L2
    pablo_taller_than_charlene = 70 # Pablo is 70 centimeters taller than Charlene
    pablo_height = pablo_taller_than_charlene + charlene_height

    # L3
    ruby_shorter_than_pablo = 2 # Ruby is 2 centimeters shorter than Pablo
    ruby_height = pablo_height - ruby_shorter_than_pablo

    # FA
    answer = ruby_height
    return answer