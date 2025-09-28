from constants import ROOMS

def describe_current_room(game_state):
    room = game_state['current_room']
    print(room.upper())
    print(ROOMS[room]['description'])
    if ROOMS[room]['items']:
        print("Заметные предметы:", ", ".join(ROOMS[room]['items']))
    print("Выходы:", ", ".join(f"{key}: {value}" for key, value in ROOMS[room]['exits'].items()))
    if ROOMS[room]['puzzle']:
        print("Кажется, здесь есть загадка (используйте команду solve).")

def solve_puzzle(game_state):
    room = game_state["current_room"]
    if ROOMS[room]['puzzle']:
        print(ROOMS[room]['puzzle'][0])
        while True:
            answer = input("Ваш ответ: ").strip()
            if answer == ROOMS[room]['puzzle'][1]:
                print("Вы угадали!")
                ROOMS[room]['puzzle'] = None
                return
            else:
                print("Неверно. Попробуйте снова.")
    else:
        print("Загадок здесь нет.")
    return

def attempt_open_treasure(game_state):
    global GAME_OVER
    room = game_state["current_room"]
    if 'treasure chest' in ROOMS[room]['items']:
        if 'treasure key' in game_state['player_inventory'] or 'rusty key' in game_state['player_inventory']:
            print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
            ROOMS[room]['items'].remove('treasure chest')
            print("В сундуке сокровище! Вы победили!")
            game_state["game_over"] = True
        else:
            answer = input("Сундук заперт. ... Ввести код? (да/нет): ").lower().strip()
            if answer == 'да':
                code = input("Введите код: ").lower().strip()
                if code == ROOMS[room]['puzzle'][1]:
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
    

def show_help():
    print("\nДоступные команды:")
    print("  go <direction>  - перейти в направлении (north/south/east/west)")
    print("  look            - осмотреть текущую комнату")
    print("  take <item>     - поднять предмет")
    print("  use <item>      - использовать предмет из инвентаря")
    print("  inventory       - показать инвентарь")
    print("  solve           - попытаться решить загадку в комнате")
    print("  quit            - выйти из игры")
    print("  help            - показать это сообщение")