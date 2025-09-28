ROOMS = {
    'entrance': {
        'description': 'Вы в темном входе лабиринта...',
        'exits': {'north': 'hall', 'east': 'trap_room'},
        'items': ['torch'],
        'puzzle': None
    },
    'hall': {
        'description': 'Большой зал с эхом. В центре — пьедестал с сундуком.',
        'exits': {
            'south': 'entrance',
            'west': 'library',
            'north': 'treasure_room',
            'east': 'dining room'
        },
        'items': [],
        'puzzle': (
            'Надпись: "Назови число после девяти". Ответ цифрой или словом.',
            '10'
        )
    },
    'trap_room': {
        'description': 'Комната с плиточной ловушкой. Надпись: "Осторожно".',
        'exits': {'west': 'entrance'},
        'items': ['rusty key'],
        'puzzle': (
            'Назови слово "шаг" три раза (введи "шаг шаг шаг")',
            'шаг шаг шаг'
        )
    },
    'library': {
        'description': 'Пыльная библиотека. На полках свитки, где-то ключ.',
        'exits': {'east': 'hall', 'north': 'armory'},
        'items': ['ancient book'],
        'puzzle': (
            'Загадка: "Что растет, когда его едят?" (одно слово)',
            'резонанс'
        )
    },
    'armory': {
        'description': 'Оружейная. Меч на стене, рядом бронзовая шкатулка.',
        'exits': {'south': 'library', 'north': 'crypt'},
        'items': ['sword', 'bronze box'],
        'puzzle': None
    },
    'treasure_room': {
        'description': 'Комната с сундуком. Дверь заперта — нужен ключ.',
        'exits': {'south': 'hall'},
        'items': ['treasure chest'],
        'puzzle': (
            'Код двери: число пятикратного шага, 2*5=?',
            '10'
        )
    },
    'dining room': {
        'description': 'Зал с длинным столом. Факелы, еда на столе.',
        'exits': {'west': 'hall'},
        'items': {'bread', 'water pot'},
        'puzzle': None
    },
    'crypt': {
        'description': 'Холодная крипта. В центре — саркофаг с рунами.',
        'exits': {'south': 'armory'},
        'items': ['treasure key'],
        'puzzle': (
            'Руны: "Противоположность света". Ответ — одно слово.',
            'тьма'
        )
    }
}

COMMANDS = {
    "go <direction>": "идти в направлении (north/south/east/west)",
    "look": "осмотреть комнату",
    "take <item>": "взять предмет",
    "use <item>": "использовать предмет из инвентаря",
    "inventory": "показать инвентарь",
    "solve": "решить загадку в комнате",
    "quit": "выйти из игры",
    "help": "показать это сообщение"
}

EVENT_PROBABILITY = 10  # Вероятность случайного события
EVENT_TYPES_COUNT = 3   # Количество типов событий
MAX_TRAP_DAMAGE = 10    # Максимальный урон от ловушки
FATAL_TRAP_DAMAGE_THRESHOLD = 3  # Порог смертельного урона