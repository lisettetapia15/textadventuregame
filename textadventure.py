#Start Page in a sense
print ("Hi! Welcome to Mad Libs; Lisette's Version! Let's Start!")

#Asks user's name which is apart of the story
name = raw_input("What's your name?: ")

#Asks for an adjective which is apart of the story
adjective = raw_input("")

Adjective1 = raw_input("Enter an adjective: ")
Adjective2 = raw_input("Enter a second adjective: ")
Adjective3 = raw_input("Enter a third adjective: ")

Verb1 = raw_input("Enter a verb: ")
Verb2 = raw_input("Enter a second verb: ")
Verb3 = raw_input("Enter a third verb: ")

Noun1 = raw_input("Enter a noun: ")
Noun2 = raw_input("Enter a noun: ")
Noun3 = raw_input("Enter a noun: ")
Noun4 = raw_input("Enter a noun: ")

animal = raw_input("Enter an animal: ")
food = raw_input("Enter a food: ")
fruit = raw_input("Enter a fruit: ")
number = raw_input("Enter a number: ")
superhero_name = raw_input("Enter a superhero_name")
country = raw_input("Enter a country")
dessert = raw_input("Enter a dessert")
year = raw_input("Enter a year")

#The template for the story
STORY = "This morning I woke up and felt %s because _ was going to finally %s over the big _ %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to _ to the rythym of the %s, which made all of the %ss very _. %s tried to _ into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping _ into a puddle of %s. %s then fell asleep and woke up in the year _, in a world where %ss ruled the world."

print STORY % (Adjective1, name, Verb1, Adjective2, Noun1, Noun2, animal, food, Verb2, Noun3, fruit, Adjective3, name, Verb3, number, name , superhero_name, superhero_name, name, country, name, dessert, name, year, Noun4)
Terminal :







originalStory = """
Once upon a time, {name} lived in a shack with her {animal}.

The End
"""
