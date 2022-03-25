
# part 1

#1
from tkinter import N


scorer_name_1 = "Ruud Gullit"
scorer_name_2 = "Marco van Basten"

#2
goal_0_minute = 32
goal_1_minute = 54

#3
scorers = scorer_name_1 + " " + str(goal_0_minute) + ", " + scorer_name_2 + " " + str(goal_1_minute)  

#4
report = f"{scorer_name_1} scored in the {goal_0_minute}nd minute \n{scorer_name_2} scored in the {goal_1_minute}th minute"
print(report)



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
chant = (player[0:first_name_end] + "! ") * Num_char_first_name 
chant = chant[:-1]
print(chant)

#6
good_chant = chant
print(good_chant[-1] != " ")
