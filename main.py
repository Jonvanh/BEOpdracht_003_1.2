
# part 1

#1
scorer_1 = "Gullit"
scorer_2 = "Van Basten"

#2
goal_0 = 32
goal_1 = 54

#3
scorers = scorer_1 + " scored in the " + str(goal_0) + "nd minute and later on " + scorer_2 + " scored in the " + str(goal_1) + "th minute"
report = f"{scorers}"
print(report)


sc_go_01 = f"{scorer_1} scored in the {goal_0}nd minute"
sc_go_02 = f"{scorer_2} scored in the {goal_1}th minute"

Scoresheet = f"{sc_go_01} \n{sc_go_02}"
print(Scoresheet)


# part 2

#1
player = "Jan Wouters"

#2
first_name_end = player.find(" ") 
first_name = player[:first_name_end]
print(first_name)

#3
last_name_start = player.find(" ")
last_name = player[last_name_start+1:]
print(last_name)

last_name_len = len(player[last_name_start+1:])
print(last_name_len)

#4
name_short = player[0] + ". " + player[last_name_start+1:]
print(name_short)

#5
Num_char_first_name = len(player[0:first_name_end])
Bad_chant = (player[0:first_name_end] + "! ") * Num_char_first_name 
good_chant = Bad_chant[:-1]
print(good_chant)

#6
print(good_chant[-1] != " ")
