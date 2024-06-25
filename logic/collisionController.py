from time import perf_counter
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
        self.zone_change_cooldown = (1000 / MAX_FPS) / 1000 * 5 #Moltiplicato per 5 per avere un cooldown di 0.08s se il gioco gira a 60 fps  
                                                                #frametimes: 60 fps -> 0.016s circa, 30 fps -> 0.033 s circa
        print("Cooldown:", self.zone_change_cooldown)
    
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

        if zone_num == 0: zone = maps[0]
        elif zone_num == 1: zone = maps[1]
        elif zone_num == 2: zone = maps[2]
        elif zone_num == 3: zone = maps[3]
        else:
            #zone_num = 1 #Da sistemare (lasciato così per andare a dormire trova un modo per dargli il numero precedente di zona)
            zone = maps[zone_num-1] #Se non trova la zona ritorna alla zona precedente
            print(zone_num-1)
            print("Zone not found") 
            #raise Exception("Zone not found") #Da togliere messe per debugging

        try: #Try catch non strettamente necessario, ma utile per evitare crash in caso di errori (se il giocatore appositamente continua ad andare avanti e indietro sulla riga di confine tra due zone)
            pixel_color = zone.getpixel((desired_coords[0], desired_coords[1]))

            #print("Desired coords:", desired_coords[0], desired_coords[1], "Pixel color:", pixel_color)
            
            if pixel_color == (0, 183, 239, 255): #Colore che segna il cambio di zona
                current_time = perf_counter()
                if current_time - self.last_zone_change_time >= self.zone_change_cooldown: #Cambia la zona solamente se è finito il cooldown
                    if self.player.verse == "right" or self.player.verse == "down": #Il numero può aumentare solamente se il giocatore si muove verso destra o verso il basso
                        print("cambio zona")
                        self.camera_group.zone_num += 1
                        self.camera_group.calculate_new_player_relative_coords()
                    else: #Il numero può diminuire solamente se il giocatore si muove verso sinistra o verso l'alto
                        self.camera_group.zone_num -= 1 
                        self.camera_group.calculate_new_player_relative_coords()
                    self.last_zone_change_time = current_time
                
            elif pixel_color == (34, 177, 76, 255): #Colore che segna la presenza di un cespuglio
                #print("Cespuglio")
                pass
            
            elif pixel_color == (0,0,0,0): #Se il pixel è trasparente rifiuta il movimento
                return False
        
            return True
        
        except Exception: #Se il giocatore è fuori dalla mappa rifiuta il movimento
            return False  #In teoria può generare solamente IndexError e UnboundLocalError ma metto Exception per sicurezza