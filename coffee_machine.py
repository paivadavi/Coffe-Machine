#Stage 4/6 implementation

m_state = [400, 540, 120, 9, 550]


def print_state(machine_state):
    print('\nThe coffee machine has: ')
    print('{} ml of water'.format(machine_state[0]))
    print('{} ml of milk'.format(machine_state[1]))
    print('{} g of coffee beans'.format(machine_state[2]))
    print('{} disposable cups'.format(machine_state[3]))
    print('${} of money'.format(machine_state[4]))


def get_action(machine_state):
    print('\nWrite action (buy, fill, take): ')
    action = input()
    if action == 'buy':
        machine_state = buy(machine_state)
    elif action == 'fill':
        machine_state = fill(machine_state)
    elif action == 'take':
        machine_state = take(machine_state)

    return machine_state


def buy(machine_state):
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino')
    buy_option = int(input())
    if buy_option == 1:
        machine_state = espresso(machine_state)
    elif buy_option == 2:
        machine_state = latte(machine_state)
    elif buy_option == 3:
        machine_state = cappuccino(machine_state)

    return machine_state


def espresso(machine_state):
    machine_state[0] -= 250  # 1 espresso = 250 ml of water
    machine_state[2] -= 16  # 1 espresso = 16 g of coffee beans
    machine_state[3] -= 1  # It uses one cup
    machine_state[4] += 4  # it costs 4

    return machine_state


def latte(machine_state):
    machine_state[0] -= 350  # 350 ml of water
    machine_state[1] -= 75  # 75 ml of milk
    machine_state[2] -= 20  # 20 g of coffee beans
    machine_state[3] -= 1  # uses 1 cup
    machine_state[4] += 7  # costs 7

    return machine_state


def cappuccino(machine_state):
    machine_state[0] -= 200
    machine_state[1] -= 100
    machine_state[2] -= 12
    machine_state[3] -= 1
    machine_state[4] += 6

    return machine_state


def fill(machine_state):
    print('Write how many ml of water you want to add: ')
    machine_state[0] += int(input())
    print('Write how many ml of milk you want to add: ')
    machine_state[1] += int(input())
    print('Write how many grams of coffee beans you want to add: ')
    machine_state[2] += int(input())
    print('Write how many disposable cups you want to add: ')
    machine_state[3] += int(input())

    return machine_state


def take(machine_state):
    money = machine_state[4]
    machine_state[4] = 0
    print('I gave you {}'.format(money))
    return machine_state


print_state(m_state)
m_state = get_action(m_state)
print_state(m_state)
