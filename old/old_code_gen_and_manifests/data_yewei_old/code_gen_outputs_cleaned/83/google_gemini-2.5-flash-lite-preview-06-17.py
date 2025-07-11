# Calculate the total number of hats Paityn has.
paityn_red_hats = 20
paityn_blue_hats = 24
paityn_total_hats = paityn_red_hats + paityn_blue_hats

# Calculate the number of red hats Zola has.
zola_red_hats = (4/5) * paityn_red_hats

# Calculate the number of blue hats Zola has.
zola_blue_hats = 2 * paityn_blue_hats

# Calculate the total number of hats Zola has.
zola_total_hats = zola_red_hats + zola_blue_hats

# Calculate the combined total number of hats.
combined_total_hats = paityn_total_hats + zola_total_hats

# Calculate the number of hats each person gets when shared equally.
hats_per_person = combined_total_hats / 2

# Print the results in the specified format.
print(f'{{"L1": "Paityn has a total of {paityn_red_hats} hats + {paityn_blue_hats} hats = [[{paityn_red_hats}+{paityn_blue_hats}={paityn_total_hats}]] {paityn_total_hats} hats.", "L2": "The number of red hats that Zola has is 4/5 * {paityn_red_hats} hats = [[4/5*{paityn_red_hats}={int(zola_red_hats)}]] {int(zola_red_hats)} hats", "L3": "Zola also has 2 * {paityn_blue_hats} hats = [[2*{paityn_blue_hats}={zola_blue_hats}]] {zola_blue_hats} blue hats.", "L4": "Zola has a total of {zola_blue_hats} hats + {int(zola_red_hats)} hats = [[{zola_blue_hats}+{int(zola_red_hats)}={int(zola_total_hats)}]] {int(zola_total_hats)} hats.", "L5": "When they combine their hats, they have {int(zola_total_hats)} hats + {paityn_total_hats} hats = [[{int(zola_total_hats)}+{paityn_total_hats}={int(combined_total_hats)}]] {int(combined_total_hats)} hats", "L6": "If they share the hats equally, each get {int(combined_total_hats)} hats / 2 people = [[{int(combined_total_hats)}/2={int(hats_per_person)}]] {int(hats_per_person)} hats/person"}}')