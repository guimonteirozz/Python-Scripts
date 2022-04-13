# Ex021-Tocando MP3 #
import pygame
pygame.mixer.init() # 1º inicializar o modulo mixer com mixer.int #
pygame.init() # 2º inicializar o pygame com .int #
pygame.mixer.music.load("/home/guifilho/Área de Trabalho/projetos_python/cursoemvideoex/pacman.mp3") # 3º carregar arquivo #
pygame.mixer.music.play(-1) # 4º tocar arquivo -1 para toca em loop #

# gambiarra para encerra sistema #
x = input('Aperte ENTER para sair...')
