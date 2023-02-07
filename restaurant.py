#CS175L
#Brian Mohabeer
#restaurant

keep_going = "yes"

while keep_going == "yes":
    vegetarian = False
    vegan = False
    gluten_free = False
    response1 = input("Is anyone in your party a vegentarian?: ")
    response2 = input("Is anyone in your party a vegan?: ")
    response3 = input("Is anyone in your party gluten free?: ")
    if response1 == "yes":
        vegetarian = True
    if response2 == "yes":
        vegan = True
    if response3 == "yes":
        gluten_free = True
    print("Here are your restaurant choices:")
    if not vegetarian and not vegan and not gluten_free == True:
        print("Joe's Gourmet Butgers")
    if not vegan and not gluten_free == True:
        print("Mama's Fine Italian")
    if not vegan == True:
        print("Main Street Pizza Company")
        print("Corner Cafe")
        print("Chef's Kitchen")
    keep_going = input("Enter 'yes' if you would like to do another" +
                       " restaurant search (enter 'no' to end): ")
