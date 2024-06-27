import pygame

class Pokemon:
    def __init__(self, name, type, sex, pokedex_number, moves, path, level, experience, status, hp, max_hp, attack, defense, special_attack, special_defense, speed):
        self.name = name
        self.type = type
        self.sex = sex
        self.pokedex_number = pokedex_number
        self.moves = moves
        self.sprite = pygame.image.load(path).convert_alpha()
        self.level = level
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

    def get_name(self):
        return self.name
    
    def get_type(self):
        return self.type
    
    def get_sex(self):
        return self.sex
    
    def get_pokedex_number(self):
        return self.pokedex_number
    
    def get_moves(self):
        return self.moves
    
    def set_moves(self, moves):
        self.moves = moves
    
    def get_sprite(self):
        return self.sprite
    
    def set_sprite(self, path):
        self.sprite = pygame.image.load(path).convert_alpha()

    def get_level(self):
        return self.level
    
    def set_level(self, level):
        self.level = level

    def get_exp(self):
        return self.experience
    
    def increase_exp(self, amount):
        self.experience += amount

    def get_status(self):
        return self.status
    
    def set_status(self, status):
        self.status = status

    def get_stats(self):
        return self.stats
    
    def get_hp(self):
        return self.stats['hp']
    
    def get_max_hp(self):
        return self.stats['max_hp']
    
    def get_attack(self):
        return self.stats['attack']
    
    def get_defense(self):
        return self.stats['defense']
    
    def get_special_attack(self):
        return self.stats['special_attack']
    
    def get_special_defense(self):
        return self.stats['special_defense']
    
    def get_speed(self):
        return self.stats['speed']

    def set_hp(self, hp):
        self.stats['hp'] = hp

    def set_attack(self, attack):
        self.stats['attack'] = attack
    
    def set_defense(self, defense):
        self.stats['defense'] = defense
    
    def set_special_attack(self, special_attack):
        self.stats['special_attack'] = special_attack
    
    def set_special_defense(self, special_defense):
        self.stats['special_defense'] = special_defense
    
    def set_speed(self, speed):
        self.stats['speed'] = speed