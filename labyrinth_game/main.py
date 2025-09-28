#!/usr/bin/env python3
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from constants import COMMANDS, ROOMS
from player_actions import get_input, move_player, show_inventory, take_item, use_item
from utils import attempt_open_treasure, describe_current_room, show_help, solve_puzzle

game_state = {
    'player_inventory': [],  # Инвентарь игрока
    'current_room': 'entrance',  # Текущая комната
    'game_over': False,  # Значения окончания игры
    'steps_taken': 0  # Количество шагов
}

def process_command(game_state, command):
    command = command.lower().strip()
    words = command.split(" ")
    directions = ['north', 'south', 'east', 'west']
    if command in directions:
        move_player(game_state, command)
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
        case "solve":
            if (game_state['current_room'] == 'treasure_room' 
                and 'treasure chest' in ROOMS[game_state['current_room']]['items']):
                attempt_open_treasure(game_state)
            else:
                solve_puzzle(game_state)
        case "quit":
            print("Вы выходите из игры.")
            return 'exit'
        case "exit":
            print("Вы выходите из игры.")
            return 'exit'
        case _:
            show_help(COMMANDS)

def main():
    print("Добро пожаловать в Лабиринт сокровищ!")
    describe_current_room(game_state)
    while not game_state["game_over"]:
        command = get_input()
        if process_command(game_state, command) == 'exit':
            game_state["game_over"] = True
            return

if __name__ == "__main__":
    main()