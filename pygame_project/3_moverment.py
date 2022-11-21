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

character_to_x_right = 0
character_to_x_left = 0

#플레이어 이속
chracter_speed = 5

#맵 총알 수 제한
max_weapon = 1

#무기 만들기
weapon = pygame.image.load(os.path.join(image_path,"weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

#무기는 한 번에 여러 발 발사 가능
weapons = []

#무기 이동 속도
weapon_speed = 10

#공 만들기 (4개 크기 따로 처리)
ball_images = [
    pygame.image.load(os.path.join(image_path,"ballon1.png")),
    pygame.image.load(os.path.join(image_path,"ballon2.png")),
    pygame.image.load(os.path.join(image_path,"ballon3.png")),
    pygame.image.load(os.path.join(image_path,"ballon4.png"))]

#공 크기별 스피드
ball_speed_y = [-18, -15, 12, 9]

#공들
balls = []

#첫 공 추가 (제일 큰 공)
balls.append({
    "pos_x" : 50,
    "pos_y" : 50,
    "img_idx" : 0,
    "to_x" : 3,
    "to_y" : -6,
    "init_spd_y" : ball_speed_y[0]})

gamerun = True
while gamerun:
    dt = clock.tick(60) #초당 프레임 수 설정

    # 2. 이벤트 처리 (키보드, 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창 X버튼 누를 시 작동
            gamerun = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x_left -= chracter_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x_right += chracter_speed
            elif event.key == pygame.K_SPACE:
                if len(weapons) >= max_weapon :
                    continue
                else:
                    weapon_x_pos = character_x_pos + character_width / 2 - weapon_width / 2
                    weapon_y_pos = character_y_pos
                    weapons.append([weapon_x_pos,weapon_y_pos])
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                character_to_x_left = 0
            elif event.key == pygame.K_RIGHT:
                character_to_x_right = 0
        
    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x_left + character_to_x_right

    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #무기 위치 조정
    weapons = [[w[0],w[1] - weapon_speed]for w in weapons] #무기 위치 위로
    
    #천장에 닿은 무기 없애기
    weapons = [ [w[0],w[1] ] for w in weapons if w[1] > -10]

    #공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        #벽에 닿았을 때 공 위치 변경
        if ball_pos_x <= 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1

        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else:
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background,(0,0))
    
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(stage,(0,screen_height-stage_height))

    

    pygame.display.update()

pygame.quit()