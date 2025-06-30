def solve_83():
    # Paityn's hats
    paityn_red_hats = 20
    paityn_blue_hats = 24
    paityn_total_hats = paityn_red_hats + paityn_blue_hats

    # Zola's hats
    zola_red_hats = (4/5) * paityn_red_hats
    zola_blue_hats = 2 * paityn_blue_hats
    zola_total_hats = zola_red_hats + zola_blue_hats

    # Combined hats
    combined_total_hats = paityn_total_hats + zola_total_hats

    # Hats per person when shared equally
    num_people = 2
    hats_per_person = combined_total_hats / num_people

    return int(hats_per_person)

# The final answer is the result of the function call.
# solve_83()