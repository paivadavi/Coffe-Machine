#Stage 3/6 implementation

print('Write how many ml of water the coffee machine has: ')
ml_of_water = int(input())
print('Write how many ml of milk the coffee machine has: ')
ml_of_milk = int(input())
print('Write how many grams of coffee beans the coffee machine has: ')
g_of_beans = int(input())
print('Write how many cups of coffee you will need: ')
needed_cups = int(input())

necessary_water = 200
necessary_milk = 50
necessary_beans = 15

needed_water = needed_cups * necessary_water
needed_milk = needed_cups * necessary_milk
needed_beans = needed_cups * necessary_beans

material_cups = [int(ml_of_water // necessary_water),
                 int(ml_of_milk // necessary_milk),
                 int(g_of_beans // necessary_beans)]
made_cups = min(material_cups)

if needed_water <= ml_of_water and needed_milk <= ml_of_milk and needed_beans <= g_of_beans:
    extra_cups = (made_cups - needed_cups) - (needed_cups // made_cups)
    if extra_cups > 0:
        print(extra_cups)
        print(made_cups)
        print("Yes, I can make that amount of coffee (and even {} more than that)".format(extra_cups))
    else:
        print("Yes, I can make that amount of coffee")

elif needed_water > ml_of_water or needed_milk > ml_of_milk or needed_beans > g_of_beans:
    print("No, I can make only {} cup(s) of coffee".format(made_cups))
