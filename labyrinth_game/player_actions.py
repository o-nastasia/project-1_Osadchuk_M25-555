from constants import ROOMS
from utils import attempt_open_treasure, random_event


def show_inventory(game_state):
    """Показывает содержимое инвентаря игрока."""
    if game_state['player_inventory']:
        print("Ваш инвентарь: ", game_state['player_inventory'])
    else:
        print("Инвентарь пуст.")

def get_input(prompt="> "):
    """Получает ввод от игрока."""
    try:
        return input(prompt).strip()
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"

def move_player(game_state, direction):
    """Перемещает игрока в указанном направлении."""
    room = game_state['current_room']
    for exit in ROOMS[room]['exits']:
        if direction == exit:
            next_room = ROOMS[room]['exits'][exit]
            if next_room == 'treasure_room' and room != 'treasure_room':
                if 'rusty key' in game_state['player_inventory']:
                    print("Вы используете найденный ключ, " \
                    "чтобы открыть путь в комнату сокровищ.")
                else:
                    print("Дверь заперта. Нужен ключ, чтобы пройти дальше.")
                    return
            game_state['current_room'] = ROOMS[room]['exits'][exit]
            room = game_state['current_room']
            game_state['steps_taken'] += 1
            print(room.upper())
            print(ROOMS[room]['description'])
            random_event(game_state)
            return
    print("Нельзя пойти в этом направлении.")
    return

def take_item(game_state, item_name):
    """Позволяет игроку взять предмет."""
    item_name = item_name.strip()
    room = game_state['current_room']
    for item in ROOMS[room]['items']:
        if item_name == item:
            ROOMS[room]['items'].remove(item_name)
            game_state['player_inventory'].append(item_name)
            print("Вы получили: ", item_name)
            return
    print("Такого предмета здесь нет..")
    return

def use_item(game_state, item_name):
    """Использует предмет из инвентаря."""
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
            case 'coin':
                print('Вы чувствуете себя богаче')
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