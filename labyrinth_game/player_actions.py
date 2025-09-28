from constants import ROOMS
from utils import attempt_open_treasure

def show_inventory(game_state):
    if game_state['player_inventory']:
        print("Ваш инвентарь: ", game_state['player_inventory'])
    else:
        print("Инвентарь пуст.")

def get_input(prompt="> "):
    try:
        return input(prompt).strip()
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"

def move_player(game_state, direction):
    room = game_state['current_room']
    for exit in ROOMS[room]['exits']:
        if direction == exit:
            game_state['current_room'] = ROOMS[room]['exits'][exit]
            room = game_state['current_room']
            game_state['steps_taken'] += 1
            print(room.upper())
            print(ROOMS[room]['description'])
            return
    print("Нельзя пойти в этом направлении.")
    return

def take_item(game_state, item_name):
    item_name = item_name.strip()
    room = game_state['current_room']
    for item in ROOMS[room]['items']:
        if item_name == item:
            ROOMS[room]['items'].remove(item_name)
            game_state['player_inventory'].append(item_name)
            print("Вы подняли: ", item_name)
            return
    print("Такого предмета здесь нет..")
    return

def use_item(game_state, item_name):
    if item_name in game_state['player_inventory']:
        match item_name:
            case 'torch':
                print("Стало светлее")
            case 'sword':
                print("Вы стали увереннее")
            case 'bronze box':
                if 'rusty key' not in game_state['player_inventory']:
                    game_state['player_inventory'].append('rusty key')
                print("Вы открыли шкатулку с rusty key")
            case 'bread':
                print("Вы чувствуете прилив сил")
            case 'water':
                print('Вы утолили жажду')
            case 'treasure key':
                if 'treasure chest' in ROOMS[game_state['current_room']]['items']:
                    attempt_open_treasure(game_state)
                else:
                    print("Сундук уже открыт или отсутствует в комнате.")
            case 'rusty key':
                if 'treasure chest' in ROOMS[game_state['current_room']]['items']:
                    attempt_open_treasure(game_state)
                else:
                    print("Сундук уже открыт или отсутствует в комнате.")
            case _:
                print("Вы не знаете, как использовать этот предмет")
    else:
        print("У вас нет такого предмета.")
    return