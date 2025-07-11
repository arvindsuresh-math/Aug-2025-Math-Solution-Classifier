def solve():
    """Index: 670.
    Returns: Gracie's height in inches.
    """
    # L1
    griffin_height = 61 # Griffin is 61 inches tall
    grayson_taller_than_griffin = 2 # Grayson was 2 inches taller than Griffin
    grayson_height = griffin_height + grayson_taller_than_griffin

    # L2
    gracie_shorter_than_grayson = 7 # Gracie was 7 inches shorter than Grayson
    gracie_height = grayson_height - gracie_shorter_than_grayson

    # FA
    answer = gracie_height
    return answer