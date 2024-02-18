from datetime import datetime
import pygame
import time

i = int(input("ne kadar tekrar etsin: "))
x = 0

saat = input("saat: ")
dakika = inprut("dakika: ")
saniye = input("saniye: ")


while True:
    suan = datetime.now()
    dt = datetime.strftime(suan, '%H:%M:%S')
    print(dt)
    time.sleep(1)

if dt == f"{saat}:{dakika}:{saniye}":
    while x < i:
        pygame.init()
        pygame.mixer.music.load("music gelicek")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.event.get()
        x+=1