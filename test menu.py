import pygame, pygame_menu
pygame.init()
surface = pygame.display.set_mode((600,400))

def level (self, value):
    print("난이도 선택값",value)

def start():
    print("게임시작")

t = pygame_menu.themes.THEME_BLUE
t.widget_font = pygame.font.SysFont("gulim",30)
menu = pygame_menu.Menu("Menu",400,300,theme=t)
menu.add.selector("난이도",[("Hard",1),("Easy",2)],onchange=level)
menu.add.button("게임종료",pygame_menu.events.EXIT)
menu.mainloop(surface)
