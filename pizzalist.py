list_of_pizzas = ["chicken Pizza", "pizzeria", "Donna", "pineapple pizza"]  # make a list of food
friend_pizza = []  # A list in which the above list of food is copied into

"""
#game records
score = 0
gameover = True
while(gameover):
    score = input("type 1 for a goal: ") + score
    gameover = input("type True or False: ")
else:
    print("end of game sore: ", score)
"""

# make a copy of the food list and display each pizza name
print("-------------pizza menu-------------")
for pizza in list_of_pizzas:
    # print(pizza)

    # A copy of the original list
    friend_pizza.append(pizza)

# for friend in friend_pizza:
print("original list: ", list_of_pizzas)
print("copy of the original list: ", friend_pizza)


# add one pizza to both lists
list_of_pizzas.append("chicken")
friend_pizza.append("Goat")
print(list_of_pizzas)
print(friend_pizza)

# Tuple. five basic foods in a restaurant stored in a tuple
foods = ("beans", "Bread", "orange", "Yam", "Rice")
print(foods)
print(foods[0])

# print the tuple title or name starting with capital letter
for food in foods:
    print(food.title())

# Dictionaries
phone_contacts = {"Edu": "004934567223", "Njaba": "njaba@njaba.com", "Igwe": "igwe@workforc.com"}
# access the phone contact
njabaemail = phone_contacts["Njaba"]
print("Njaba Email: ", njabaemail)

# add a number
phone_contacts["esther"] = "Esther@Robi.com"
print("my contacts: \n", phone_contacts)

# loop throughout dictionary
for name, mobile_number in phone_contacts.items():
    print("\nname: " + name)
    print("Number: " + mobile_number)

# a dictionary of lists
students_id = {
    "Imoh Emmanuel": ["1999093008", 30, "Abuja", "Anambra", "ebenato"],
    "Bon Jack": ["1999093487", 32, "Nnewi", "Anambra", "Nnewi"],
    "Ugorji Anselm": ["200395673", 35, "onitsha", "Imo", "Akulu"]
}

# make a list of the above names
student_names = []
for name in students_id.keys():
    student_names.append(name)
# or
name_roll_call = ["Imoh Emmanuel", "Bon Jack", "Ugorji Anselm"]
# retrieve Imoh's data
print(students_id[student_names[1]])
