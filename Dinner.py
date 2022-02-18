day = input("What is the day? ")
if day == 'Wednesday':
    print("Pizza time! ")

else:
    import random

    dinner = ['Mac & Cheese', 'Ramen', 'Spaghetti & Meatballs', 'burrito/Taco', 'Cheese Omelette', 'BLM Sandwich']
    random_dinner = random.choice(dinner)

    additions = input("would you like any sides with your meal? ")



    if additions == 'yes':
        sides = input("what will that be? ")
        print("you will be having", random_dinner, "with", sides, "tonight")

    else:
        sides = None
        print("you will be having", random_dinner, "tonight")
