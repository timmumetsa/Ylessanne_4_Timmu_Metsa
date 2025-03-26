import pygame  # Impordib Pygame'i mooduli mängu loomiseks.
import random  # Impordib random-mooduli juhuslike väärtuste genereerimiseks.

# Pygame'i initsialiseerimine.
pygame.init()  # Initsialiseerib Pygame'i.

# Ekraani suurus ja seadistamine.
screen_width, screen_height = 640, 480  # Määrab ekraani laiuse ja kõrguse.
screen = pygame.display.set_mode((screen_width, screen_height))  # Loob ekraani antud suurusega.
pygame.display.set_caption("Autode animatsioon")  # Seab mänguakna pealkirja.

# Värvid
white = (255, 255, 255)  # Valge värv (skoori teksti jaoks).

# Pildid.
background = pygame.image.load("bg_rally.jpg")  # Laeb taustapildi.
red_car = pygame.image.load("f1_red.png")  # Laeb punase auto pildi.
blue_car = pygame.image.load("f1_blue.png")  # Laeb sinise auto pildi.

# Auto suurused.
car_width, car_height = blue_car.get_width(), blue_car.get_height()  # Saab auto laiuse ja kõrguse.

# Algväärtused.
score = 0  # Määrab algskoori väärtuse.
base_speed = 2  # Siniste autode algkiirus.
speed_increment = 0.5  # Kiiruse suurenemine iga punktiga.

# Siniste autode rajakeskmed (fikseeritud x-positsioonid).
lane_positions = [200, 320, 440]  # Kolme raja keskpunktid (x-koordinaadid).

# Siniste autode andmed (mitu autot korraga).
blue_cars = [{"x": lane_positions[i], "y": random.randint(-500, -50), "speed": base_speed} for i in range(3)]
# Loob kolm sinist autot juhuslike y-positsioonidega ja fikseeritud x-positsioonidega radade keskmetel.

# Font skoori kuvamiseks.
font = pygame.font.Font(None, 36)  # Määrab fondi ja suuruse skoori teksti jaoks.

# Mängu tsükkel.
running = True  # Määrab mängu töötamise oleku.
while running:  # Käivitab peamise mängutsükli.
    for event in pygame.event.get():  # Kontrollib kõiki sündmusi (nt akna sulgemine).
        if event.type == pygame.QUIT:  # Kui kasutaja sulgeb akna.
            running = False  # Lõpetab mängu tsükli.

    # Tausta joonistamine
    screen.blit(background, (0, 0))  # Joonistab taustapildi ekraanile.

    # Punase auto joonistamine ekraani alla keskele.
    red_car_x = (screen_width - car_width) // 2  # Arvutab punase auto x-positsiooni keskel.
    red_car_y = screen_height - car_height - 10  # Arvutab punase auto y-positsiooni ekraani allosas.
    screen.blit(red_car, (red_car_x, red_car_y))  # Joonistab punase auto ekraanile.

    # Siniste autode animatsioon ja uuendamine.
    for blue_car_data in blue_cars:
        blue_car_data["y"] += blue_car_data["speed"] + score * speed_increment
        # Liigutab sinise auto alla vastavalt kiirusele ja lisab punkte kiiruse suurendamiseks.

        if blue_car_data["y"] > screen_height:
            # Kui sinine auto jõuab alla serva:
            blue_car_data["y"] = random.randint(-500, -50)
            blue_car_data["x"] = random.choice(lane_positions)
            blue_car_data["speed"] += speed_increment
            score += 1

        screen.blit(blue_car, (blue_car_data["x"] - car_width // 2, blue_car_data["y"]))
        # Joonistab sinise auto täpselt raja keskpunkti.

    # Skoori kuvamine ekraani ülaosas vasakul.
    score_text = font.render(f"Skoor: {str(score)}", True, white)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()