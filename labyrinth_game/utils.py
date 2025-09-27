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