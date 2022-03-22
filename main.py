
# part 1

scorer_1 = "Gullit"
scorer_2 = "Van Basten"

goal_0 = str(32)
goal_1 = str(54)

scorers = scorer_1 + " scored in the " + goal_0 + "nd minute and later on " + scorer_2 + " scored in the " + goal_1 + "th minute"
print(f"{scorers}")

sc_go_01 = f"{scorer_1} scored in the {goal_0}nd minute"
sc_go_02 = f"{scorer_2} scored in the {goal_1}th minute"
print(sc_go_01)
print(sc_go_02)


# part 2

player = "Jan Wouters"
first_name_end = player.find(" ") 
print(player[0:first_name_end])

last_name_start = player.find("Wouters")
print(player[last_name_start:])

last_name_len = len(player[last_name_start:])
print(last_name_len)

name_short = player[:1] + ". " + player[last_name_start:]
print(name_short)

x = len(player[0:first_name_end])
chant = (player[0:first_name_end] + "!") * x
print(chant)
print(chant[-1] != " ")
