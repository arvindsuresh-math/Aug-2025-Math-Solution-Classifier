def solve():
    """Index: 4531.
    Returns: the total number of photos used in the newspaper.
    """
    # L1
    num_pages_batch1 = 12 # 12 pages
    photos_per_page_batch1 = 2 # 2 photos
    photos_batch1 = num_pages_batch1 * photos_per_page_batch1

    # L2
    num_pages_batch2 = 9 # another 9 pages
    photos_per_page_batch2 = 3 # 3 photos
    photos_batch2 = num_pages_batch2 * photos_per_page_batch2

    # L3
    total_photos = photos_batch1 + photos_batch2

    # FA
    answer = total_photos
    return answer