def solve():
    """Index: 7271.
    Returns: the number of photos Clarissa needs to bring.
    """
    # L1
    cristina_photos = 7 # Cristina brings 7 photos
    john_photos = 10 # John brings 10 photos
    sarah_photos = 9 # Sarah brings 9 photos
    photos_excluding_clarissa = cristina_photos + john_photos + sarah_photos

    # L2
    total_slots = 40 # photo album has 40 slots available
    clarissa_needed_photos = total_slots - photos_excluding_clarissa

    # FA
    answer = clarissa_needed_photos
    return answer