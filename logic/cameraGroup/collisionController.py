from time import perf_counter
from settings import ZONE_CHANGE_COOLDOWN
from PIL import Image

class CollisionController:
    def __init__(self, camera_group, player, MAX_FPS):
        #Load images
        first_level_first_zone = Image.open("graphics/collision_maps/1_1.png")
        first_level_second_zone = Image.open("graphics/collision_maps/1_2.png")
        first_level_third_zone = Image.open("graphics/collision_maps/1_3.png")
        first_level_fourth_zone = Image.open("graphics/collision_maps/1_4.png")
        self.first_level_maps = [first_level_first_zone, first_level_second_zone, first_level_third_zone, first_level_fourth_zone]

        #Assigning istances of other classes
        self.camera_group = camera_group
        self.player = player

        #Cooldown per il cambio di zona
        self.last_zone_change_time = perf_counter()             
        self.zone_change_cooldown = ZONE_CHANGE_COOLDOWN
    
    #Check if the player can move to the desired coordinates
    def allow_movement(self, desired_coords):

        level_num = self.camera_group.level_num

        if level_num == 0:
            maps = self.first_level_maps
        #Aggiungi altri elif per altri livelli TODO
        else:
            print("level num non trovato")
            #raise Exception("level num not found") #Da togliere messe per debugging

        zone_num = self.camera_group.zone_num
        try:
            if zone_num == 0: zone = maps[0]
            elif zone_num == 1: zone = maps[1]
            elif zone_num == 2: zone = maps[2]
            elif zone_num == 3: zone = maps[3]
        except Exception:
            if self.player.verse == "right" or self.player.verse == "down": zone = maps[zone_num+1]
            elif self.player.verse == "up" or self.player.verse == "left": zone = maps[zone_num-1] 
            print("Zone not found") 

        try: #Try catch non strettamente necessario, ma utile per evitare crash in caso di errori (se il giocatore appositamente continua ad andare avanti e indietro sulla riga di confine tra due zone)
            pixel_color = zone.getpixel((desired_coords[0], desired_coords[1]))
            
            if pixel_color == (255, 255, 255, 255): #Colore che segna la presenza di un percorso
                self.camera_group.is_player_in_grass = False
                return True 

            elif pixel_color == (0,0,0,0): #Se il pixel è trasparente rifiuta il movimento
                self.camera_group.is_player_in_grass = False
                return False

            elif pixel_color == (34, 177, 76, 255): #Colore che segna la presenza di un cespuglio
                self.camera_group.is_player_in_grass = True
                return True

            elif pixel_color == (0, 183, 239, 255): #Colore che segna il cambio di zona
                self.camera_group.is_player_in_grass = False
                current_time = perf_counter()
                if current_time - self.last_zone_change_time >= self.zone_change_cooldown: #Cambia la zona solamente se è finito il cooldown
                    if self.player.verse == "right" or self.player.verse == "down": #Il numero può aumentare solamente se il giocatore si muove verso destra o verso il basso
                        self.camera_group.zone_num += 1
                        self.camera_group.calculate_new_player_relative_coords()
                    else: #Il numero può diminuire solamente se il giocatore si muove verso sinistra o verso l'alto
                        self.camera_group.zone_num -= 1 
                        self.camera_group.calculate_new_player_relative_coords()
                    
                    self.camera_group.last_player_collision_verse = self.player.verse
                    self.last_zone_change_time = current_time
                return True
    
        except Exception: #Se il giocatore è fuori dalla mappa rifiuta il movimento
            return False  #In teoria può generare solamente IndexError e UnboundLocalError ma metto Exception per sicurezza