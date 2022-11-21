import pygame
import os
########################################################################
#기본 초기화 (반드시 해야 함)
pygame.init() #초기화

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height)) #화면 크기

pygame.display.set_caption("터트리기")

#프레임
clock = pygame.time.Clock()
#########################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트, 시간 등)

current_path = os.path.dirname(__file__) #현재 py파일의 위치 반환
image_path = os.path.join(current_path, "images") #이미지 폴더 위치 반환

#배경
background = pygame.image.load(os.path.join(image_path,"background.png"))

#발판 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] #스테이지의 높이만 가져오기

#캐릭터
character = pygame.image.load(os.path.join(image_path,"character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height - stage_height

gamerun = True
while gamerun:
    dt = clock.tick(60) #초당 프레임 수 설정

    # 2. 이벤트 처리 (키보드, 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창 X버튼 누를 시 작동
            gamerun = False
        
    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(stage,(0,screen_height-stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))

    pygame.display.update()

pygame.quit()