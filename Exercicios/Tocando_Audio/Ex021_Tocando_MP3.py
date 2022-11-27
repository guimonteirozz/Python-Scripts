# Ex021-Tocando MP3 #
# essa lib e mais simples e mais atualizada 
from playsound import playsound # pip install playsound
playsound('pacmanAudio.mp3')

'''
import pygame #pip install pygame

pygame.mixer.init() #1º inicializar o modulo mixer com mixer.init 

pygame.init() #2º inicializar o pygame com .init 

pygame.mixer.music.load('pacmanAudio.mp3') # ERRO para LER O FORMATO DO ARQUIVO  
#libvorbisfile-3.dll (ogg) | libmpg123-0.dll (mp3)

pygame.mixer.music.play(-1) #4º tocar arquivo -1 para toca em loop 
'''