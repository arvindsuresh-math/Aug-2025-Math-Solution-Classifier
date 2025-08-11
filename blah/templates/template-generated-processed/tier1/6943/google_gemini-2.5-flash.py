def solve():
    """Index: 6943.
    Returns: the number of photos Lisa took last weekend.
    """
    # L1
    photos_animals = 10 # 10 photos of animals
    multiplier_flowers = 3 # 3 times as many photos of flowers as animals
    photos_flowers = photos_animals * multiplier_flowers

    # L2
    fewer_scenery_than_flowers = 10 # 10 fewer scenery than the flowers
    photos_scenery = photos_flowers - fewer_scenery_than_flowers

    # L3
    total_photos_this_week = photos_animals + photos_flowers + photos_scenery

    # L4
    fewer_last_weekend = 15 # 15 fewer photos last weekend
    photos_last_weekend = total_photos_this_week - fewer_last_weekend

    # FA
    answer = photos_last_weekend
    return answer