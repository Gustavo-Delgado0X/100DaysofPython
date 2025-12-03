# from another_module import another_variable

# print(another_variable)

# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green","black")
# timmy.forward(100)

# my_screen = Screen()

# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Squartle", "Charzard"])
table.add_column("Type",["Lightning", "Water", "Fire"])

table.align = "l"
print(table.align)

print(table)