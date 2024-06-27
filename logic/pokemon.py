import pygame

class Pokemon:
    pygame.font.init()
    font = pygame.font.Font("graphics/menus/fonts/standard_font.ttf", 10)
    def __init__(self, name, type, sex, pokedex_number, moves, level, experience, status, hp, max_hp, attack, defense, special_attack, special_defense, speed):
        self.name = name
        self.battle_name = Pokemon.font.render(name, True, (0, 0, 0))
        self.type = type
        self.sex = sex
        self.pokedex_number = pokedex_number
        self.moves = moves
        self.sprite_front = pygame.image.load("graphics/Pokemon/Front/" + name.upper() + ".png").convert_alpha()
        self.sprite_back = pygame.image.load("graphics/Pokemon/Back/" + name.upper() + ".png").convert_alpha()
        self.level = level
        self.level_surf = Pokemon.font.render(str(level), True, (0, 0, 0))
        self.experience = experience #Experience points until next level
        self.status = status #'normal', 'paralyzed', 'poisoned', 'burned', 'frozen', 'asleep', 'confused', 'dead', '' 
        self.stats = {
            'hp': hp,
            'max_hp': max_hp,
            'attack': attack,
            'defense': defense,
            'special_attack': special_attack,
            'special_defense': special_defense,
            'speed': speed
        }

        def update_level(self):
            self.level += 1
            self.level_surf = Pokemon.font.render(str(self.level), True, (0, 0, 0))