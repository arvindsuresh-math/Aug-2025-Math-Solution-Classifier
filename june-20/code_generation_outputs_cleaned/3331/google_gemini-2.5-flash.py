def solve(
    initial_plates: int = 38, # fills a cardboard box with 38 dinner plates
    plate_weight_ounces: int = 10, # each of his plates weighs 10 ounces
    weight_limit_pounds: int = 20 # each shipping box can hold 20 pounds
):
    """Index: 3331.
    Returns: the number of plates Hasan needed to remove from the shipping box.
    """
    #: L2
    # Convert the weight limit from pounds to ounces (1 pound = 16 ounces)
    weight_limit_ounces = weight_limit_pounds * 16

    #: L5
    # Calculate the number of plates that can remain in the box to meet the weight limit
    # This is derived from (initial_plates - x) * plate_weight_ounces = weight_limit_ounces
    # So, (initial_plates - x) = weight_limit_ounces / plate_weight_ounces
    remaining_plates_count = weight_limit_ounces / plate_weight_ounces

    #: L7
    # Calculate the number of plates that needed to be removed
    # x = initial_plates - remaining_plates_count
    plates_removed = initial_plates - remaining_plates_count

    answer = plates_removed # FINAL ANSWER
    return answer