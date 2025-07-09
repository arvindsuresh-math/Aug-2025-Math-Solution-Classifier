def solve(
    total_weight_loss: int = 103,  # Four people lost a total of 103 kilograms of weight
    first_person_loss: int = 27,   # The first person lost 27 kilograms
    second_person_less: int = 7    # The second person lost 7 kilograms less than the first person
):
    """Index: 74.
    Returns: the weight loss for each of the last two people."""
    
    #: L1
    second_person_loss = first_person_loss - second_person_less
    
    #: L2
    remaining_weight_loss = total_weight_loss - first_person_loss - second_person_loss
    
    #: L3
    last_two_people_loss = remaining_weight_loss / 2
    
    #: L4
    answer = last_two_people_loss  # FINAL ANSWER
    return answer