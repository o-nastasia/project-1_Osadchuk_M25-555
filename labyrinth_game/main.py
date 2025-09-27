#!/usr/bin/env python3
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import describe_current_room
from player_actions import get_input, take_item, move_player, show_inventory, use_item

game_state = {
    'player_inventory': [],  # Инвентарь игрока
    'current_room': 'entrance',  # Текущая комната
    'game_over': False,  # Значения окончания игры
    'steps_taken': 0  # Количество шагов
}

def process_command(game_state, command):
    command = command.lower().strip()
    words = command.split(" ")
    match words[0]:
        case "look":
            describe_current_room(game_state)
        case "use":
            item_name = ' '.join(words[1:])
            use_item(game_state, item_name)
        case "go":
            if len(words) > 1:
                move_player(game_state, words[1])
            else:
                print("Укажите направление (например, go north).")
        case "take":
            if len(words) > 1:
                item_name = ' '.join(words[1:])
                take_item(game_state, item_name)
            else:
                print("Укажите предмет (например, take torch).")
        case "inventory":
            show_inventory(game_state)
        case "quit":
            print("Вы выходите из игры.")
            return 'exit'
        case "exit":
            print("Вы выходите из игры.")
            return 'exit'
        case _:
            print("Неизвестная команда.")

def main():
    print("Добро пожаловать в Лабиринт сокровищ!")
    describe_current_room(game_state)
    while True:
        command = get_input()
        if process_command(game_state, command) == 'exit':
            return

if __name__ == "__main__":
    main()