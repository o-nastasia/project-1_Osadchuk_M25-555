import math

from constants import (
    EVENT_PROBABILITY,
    EVENT_TYPES_COUNT,
    FATAL_TRAP_DAMAGE_THRESHOLD,
    MAX_TRAP_DAMAGE,
    ROOMS,
)


def describe_current_room(game_state):
    room = game_state['current_room']
    print(room.upper())
    print(ROOMS[room]['description'])
    if ROOMS[room]['items']:
        print("Заметные предметы:", ", ".join(ROOMS[room]['items']))
    print("Выходы:", ", ".join(f"{key}: {value}" for key, value 
                               in ROOMS[room]['exits'].items()))
    if ROOMS[room]['puzzle']:
        print("Кажется, здесь есть загадка (используйте команду solve).")

def solve_puzzle(game_state):
    room = game_state["current_room"]
    if ROOMS[room]['puzzle']:
        print(ROOMS[room]['puzzle'][0])
        correct_answers = {
            'hall': ['10', 'десять'],
            'trap_room': ['шаг шаг шаг'],
            'library': ['резонанс'],
            'treasure_room': ['10', 'десять'],
            'crypt': ['тьма']
        }
        while True:
            answer = input("Ваш ответ: ").strip().lower()
            if answer in correct_answers[room]:
                print("Вы угадали!")
                if room == 'crypt':
                    if 'treasure key' not in game_state['player_inventory']:
                        ROOMS[room]['items'].remove('treasure key')
                        game_state['player_inventory'].append('treasure key')
                        print('Вы получили награду - treasure key')
                elif room == 'trap_room':
                    if 'rusty key' not in game_state['player_inventory']:
                        ROOMS[room]['items'].remove('rusty key')
                        game_state['player_inventory'].append('rusty key')
                        print('Вы получили награду - rusty key')
                ROOMS[room]['puzzle'] = None
                return answer
            else:
                print("Неверно. Попробуйте снова.")
                if room == 'trap_room':
                    trigger_trap(game_state)
                    if game_state['game_over']:
                        return
    else:
        print("Загадок здесь нет.")
    return


def attempt_open_treasure(game_state):
    global GAME_OVER
    room = game_state["current_room"]
    if 'treasure chest' in ROOMS[room]['items']:
        if 'treasure key' in game_state['player_inventory']:
            print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
            ROOMS[room]['items'].remove('treasure chest')
            print("В сундуке сокровище! Вы победили!")
            game_state["game_over"] = True
        else:
            answer = input("Сундук заперт. ... Ввести код? (да/нет): ").lower().strip()
            if answer == 'да':
                right_answer = ROOMS[room]['puzzle'][1]
                code = solve_puzzle(game_state)
                if code == right_answer:
                    print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
                    ROOMS[room]['items'].remove('treasure chest')
                    print("В сундуке сокровище! Вы победили!")
                    game_state["game_over"] = True
                else:
                    print("Код неверный")
                    return
            else:
                print("Вы отступаете от сундука.")
                return
    else:
        print("Сундук уже открыт или отсутствует в комнате.")
        return
    

def show_help(COMMANDS):
    print("\nДоступные команды:")
    for command, description in COMMANDS.items():
        print(f"{command:<16} - {description}")

def pseudo_random(seed, modulo):
    value = math.sin(seed * 12.9898) * 43758.5453
    fractional_part = value - math.floor(value)
    return int(fractional_part * modulo)

def trigger_trap(game_state):
    print("Ловушка активирована! Пол стал дрожать...")
    if game_state['player_inventory']:
        modulo = len(game_state['player_inventory'])
        item_index = pseudo_random(game_state['steps_taken'], modulo)
        lost_item = game_state['player_inventory'].pop(item_index)
        print(f"Вы потеряли предмет: {lost_item}")
    else:
        damage = pseudo_random(game_state['steps_taken'], MAX_TRAP_DAMAGE)
        if damage < FATAL_TRAP_DAMAGE_THRESHOLD:
            print("Ловушка оказалась смертельной! Вы проиграли.")
            game_state['game_over'] = True
        else:
            print("Вы чудом уцелели, но ловушка была близко!")

def random_event(game_state):
    if pseudo_random(game_state['steps_taken'], EVENT_PROBABILITY) == 0:
        event = pseudo_random(game_state['steps_taken'] + 1, EVENT_TYPES_COUNT)
        room = game_state['current_room']
        match event:
            case 0:  # Сценарий 1: Находка монетки
                print("Вы замечаете блестящую монетку на полу!")
                if 'coin' not in ROOMS[room]['items']:
                    ROOMS[room]['items'].append('coin')
            case 1:  # Сценарий 2: Шорох
                print("Вы слышите странный шорох в темноте...")
                if 'sword' in game_state['player_inventory']:
                    print("Вы махнули мечом, шорох стих. Вы отпугнули существо!")
            case 2:  # Сценарий 3: Ловушка в trap_room
                if (room == 'trap_room' and
                    'torch' not in game_state['player_inventory']):
                    print("Опасность! Пол начинает дрожать!")
                    trigger_trap(game_state)
