import pygame, sys, random as r
from pygame.locals import*
import time

#게임 종료 함수 정의
def exit_game():
    pygame.quit()
    sys,exit()

#화면 설정
w,h=960,640
size=(w,h)

#파이게임 초기화
pygame.init()

#clock 설정
clock= pygame.time.Clock()

#screen 설정
screen = pygame.display.set_mode(size)

#폰트 설정
font1=pygame.font.SysFont("arial",50)
font2=pygame.font.SysFont("한컴산뜻돋움",70)
font3=pygame.font.SysFont("한컴산뜻돋움",20)

#글씨 색 설정
normal_color=(0,0,0)
hover_color=(200,50,50)

#좌표 설정
x,y=800,200

#게임 제목 텍스트 함수 정의
def titleDisp():
    text=font2.render("꽃 키우기 게임", 1, (0,0,0))
    textpos=text.get_rect()
    textpos.center=(480,100)
    screen.blit(text,textpos)

#배경화면 지정
background = pygame.transform.scale(pygame.image.load('1bg.jpg'),(960,640))

#불러올 이미지 지정
sunflowersoso=pygame.transform.scale(pygame.image.load("images/sunflowersoso.jpg"), (320,412))
sunflowersad= pygame.transform.scale(pygame.image.load("images/sunflowersad.jpg"), (320,412))
sunflowergood=pygame.transform.scale(pygame.image.load("images/sunflowergood.jpg"), (320,412))
tulipsoso=pygame.transform.scale(pygame.image.load("images/tulipsoso.jpg"), (320, 412))
tulipsad= pygame.transform.scale(pygame.image.load("images/tulipsad.jpg"), (320, 412))
tulipgood= pygame.transform.scale(pygame.image.load("images/tulipgood.jpg"),(320,412))
sunflower= pygame.image.load("images/sunflower.jpg")
tulip= pygame.image.load("images/tulip.jpg")
sun= pygame.image.load("images/sun.jpg")
soil= pygame.image.load("images/soil.jpg") 
water=pygame.image.load("images/water.jpg") 
base=pygame.image.load("images/base.jpg")



#텍스트 버튼 정의
def textbutton(msg,x,y,color):
    active= False
    (mx,my)= pygame.mouse.get_pos()
    
    text=font1.render(msg, 1, normal_color) #원래 normal_color(검은색)
    textRect= text.get_rect()
    textRect.topleft= (x,y)

    tw= textRect[2]; th= textRect[3]
    if (x+tw > mx > x) and (y+th > my >y):  #마우스가 텍스트 버튼 안 영역이면
        active= True
        text= font1.render(msg, 1, hover_color) #hover_color(붉은색)으로 바뀜
    screen.blit(text, textRect)
    return active

#Clock 오브젝트
c=pygame.time.Clock()


#처음 페이지 변수 1로 설정
page= 1

#page3에서의  초기설정
px=540 #받침대 위치
speedx=0 #스피드
gx=0 #게이치 채워진 정도
sx, sy= 0,0 #햇빛 위치
sox, soy= 228,0 #거름 위치
wx, wy= 433,0 #물 위치
totalscore= 150 #처음 점수
sunscore= 0 #햇빛 점수
soilscore= 0 #거름 점수
waterscore= 0 #물 점수


#page1 함수 설정
def page1(): #시작 페이지
    global page
    screen.blit(background, (0,0)) #배경화면 이미지 띄우기
    titleDisp() #타이틀(제목) 띄우기
    start_button= textbutton('Start', x,y, normal_color) #스타트 버튼 지정
    if event.type==MOUSEBUTTONUP: #마우스 클릭
        '''if pygame.mouse.get_pressed()[0]: #왼쪽 마우스 클릭상태이면'''
        if start_button: #start_button 상태이면
            page=2 #page 변수 2로 바뀜(2페이지로 넘어감)

    

#page2 함수 설정
def page2(): #꽃 종류 선택 페이지
    global page, sunflower, tulip
    screen.fill((255,255,255))#배경 흰색으로 설정
    select=font2.render("꽃의 종류를 선택하세요", 1, (0,0,0))  #꽃 종류 선택 안내 문구
    selectpos=select.get_rect()  
    selectpos.center=(480, 100) #문구의 위치 설정
    screen.blit(select, selectpos) #문구가 뜨도록
    sunflower= pygame.image.load("images/sunflower.jpg") #해바라기 이미지 로드
    tulip= pygame.image.load("images/tulip.jpg")
    screen.blit(sunflower, (100,200)) #해바라기 이미지가 (100,200) 위치에 뜨도록
    screen.blit(tulip, (550,200)) #튤립 이미지가 (550, 200) 위치에 뜨도록 
    if event.type==MOUSEBUTTONDOWN: #마우스 버튼
        if pygame.mouse.get_pressed()[0]: #마우스 왼쪽 버튼 눌렸을 때
            mx, my= pygame.mouse.get_pos() #마우스 위치(좌표)
            if ((100<mx<420) and (200<my<612)): #해바라기 그림 영역에 놓이면
                page=9 #page3 변수 9으로 바뀜(9페이지로 넘어감)
            elif ((550<mx<867) and (200<my<608)):
                page=10
    


#page3 함수 설정
def page3(): #해바라기 키우는 페이지
    global page, totalscore, sunscore, soilscore, waterscore,sunflowersoso,sunflowersad,sunflowergood,\
    sun, soil, water
    screen.fill((255,255,255)) #배경 흰색으로 설정
    #gauge 글씨 띄우기
    gauge=font1.render("guage",1,(0,0,0)) #gauge글씨 지정
    gaugepos= gauge.get_rect()
    gaugepos.center=(800,560) #gauge글씨 (800,560)위치에 지정
    screen.blit(gauge, gaugepos)
    #gauge 칸 띄우기
    points= [(640,522),(640,600),(960,600),(960,522)] #point리스트
    pygame.draw.polygon(screen,(0,0,0),points, 5) #직사각형 그리기
    #gauge 채우는 그림
    gx=totalscore
    gaugeimg= pygame.Surface((gx, 78))
    gaugeimg.set_alpha(128)
    gaugeimg.fill((250,250,0))
    screen.blit(gaugeimg,(640, 522))

    #햇빛, 거름, 물 이미지 설정한 위치에 띄우기
    screen.blit(sun, (0,10))
    screen.blit(soil, (228,10)) 
    screen.blit(water, (433, 10))
    #글로벌 함수 불러오기
    global px, speedx, sx, sy, sox, soy, wx, wy
    base= pygame.image.load("images/base.jpg") #받침대 이미지
    sun= pygame.image.load("images/sun.jpg") #햇빛 이미지
    if event.type==KEYUP: speedx=0 #키보드 뗐을 때 speedx=0
    elif event.type==KEYDOWN: #키보드 눌렀을 때
        if event.key==K_LEFT: speedx=-5 #좌버튼일 때 speedx=-5
        elif event.key==K_RIGHT: speedx=+5 #우버튼일 때 speedx=+5
    screen.blit(base, (px,610)) #받침대 이미지 띄우기
    
    #햇빛 위에서 아래로 내려오기
    sx=0 ; sy= sy+8
    sun_= screen.blit(sun, (sx, sy)) #햇빛 이미지 띄우기
    if sy > 640: #햇빛이 바닥까지  내려오면
        sy= 0 #다시 위에서 내려오기
    if 0<px<118: #받침대가 햇빛이랑 겹치면
        if sy>600:
            sunscore+=4 #햇빛 점수 올라감
            totalscore+=4 #총 점수 올라감
    #거름 위에서 아래로 내려오기
    sox=228 ; soy= soy+8
    soil_= screen.blit(soil, (sox, soy))
    if soy> 640:
        soy= 0
    if 228< px < 323:
        if soy>600:
            soilscore+=4
            totalscore+=4
            
    #물 위에서 아래로 내려오기
    wx=433 ; wy= wy+8
    water_= screen.blit(water, (wx, wy))
    if wy> 640:
        wy= 0
    if 433<px<508:
        if wy>600:
            waterscore+=4
            totalscore+=4
            
    #조건 불만족시 게이지 감소
    if sunscore>soilscore:
        totalscore=totalscore-1
    if waterscore>soilscore:
        totalscore=totalscore-1
    if sunscore>waterscore:
        totalscore=totalscore-1

    #게이지에 따른 꽃의 상태 변화
    if 0<totalscore<100:
        screen.blit(sunflowersad,(640,10))
    if 99<totalscore<220:
        screen.blit(sunflowersoso,(640,10))
    if 219<totalscore<320:
        screen.blit(sunflowergood, (640,10))

    #게이지 꽉 차면 성공
    if 319<totalscore:
        page=4

    #게이지 0이면 실패
    if totalscore<1:
        page=5
        
    #점수 이미지, 띄우기
    conditionscore_img= font3.render('햇빛:{}      거름:{}      물:{}'.format(sunscore, soilscore, waterscore), True, (0,0,0))
    screen.blit(conditionscore_img, (680, 450))
    
    c.tick(30)

def page4(): #해바라기 성공 페이지
    global page, sunflowergood, setup
    screen.fill((255,255,255))
    sunflowergood_=pygame.image.load("images/sunflowergood.jpg")
    screen.blit(sunflowergood_, (480,0))
    success1=font2.render("축하합니다.",1,(0,0,0))
    success2=font2.render("꽃키우기 성공!!",1,(0,0,0))
    successpos1=success1.get_rect()
    successpos2=success2.get_rect()
    successpos1.topleft=(0,0)
    successpos2.topleft=(0,100)
    screen.blit(success1, successpos1)
    screen.blit(success2, successpos2)
    quit_button= textbutton('Quit',100, 400, normal_color) #종료 버튼 지정
    if event.type==MOUSEBUTTONUP: #마우스 클릭
        if quit_button: #restart_button 상태이면
            exit_game()


    
    

def page5(): #해바라기 실패 페이지
    global page, sunflowersad, setup
    screen.fill((255,255,255))
    sunflowersad_=pygame.image.load("images/sunflowersad.jpg")
    screen.blit(sunflowersad_, (460, 0))
    fail1=font2.render("꽃이 시들었어요.",1,(0,0,0))
    fail2=font2.render("꽃키우기 실패..",1,(0,0,0))
    failpos1= fail1.get_rect()
    failpos2= fail2.get_rect()
    failpos1.topleft=(0,0)
    failpos2.topleft=(0,100)
    screen.blit(fail1, failpos1)
    screen.blit(fail2, failpos2)
    quit_button= textbutton('Quit',100, 400, normal_color) #종료 버튼 지정
    if event.type==MOUSEBUTTONUP: #마우스 클릭
        if quit_button: #restart_button 상태이면
            exit_game()

    
def page6(): #튤립 키우는 페이지
    global page, totalscore, sunscore, soilscore, waterscore,tulipsoso,tulipsad,tulipgood,\
    sun, soil, water,gx
    screen.fill((255,255,255)) #배경 흰색으로 설정
    #gauge 글씨 띄우기
    gauge=font1.render("guage",1,(0,0,0)) #gauge글씨 지정
    gaugepos= gauge.get_rect()
    gaugepos.center=(800,560) #gauge글씨 (800,560)위치에 지정
    screen.blit(gauge, gaugepos)
    #gauge 칸 띄우기
    points= [(640,522),(640,600),(960,600),(960,522)] #point리스트
    pygame.draw.polygon(screen,(0,0,0),points, 5) #직사각형 그리기
    #gauge 채우는 그림
    gx=totalscore
    gaugeimg= pygame.Surface((gx, 78))
    gaugeimg.set_alpha(128)
    gaugeimg.fill((250,250,0))
    screen.blit(gaugeimg,(640, 522))

    #햇빛, 거름, 물 이미지 설정한 위치에 띄우기
    screen.blit(sun, (0,10))
    screen.blit(soil, (228,10)) 
    screen.blit(water, (433, 10))
    #글로벌 함수 불러오기
    global px, speedx, sx, sy, sox, soy, wx, wy
    base= pygame.image.load("images/base.jpg") #받침대 이미지
    sun= pygame.image.load("images/sun.jpg") #햇빛 이미지
    if event.type==KEYUP: speedx=0 #키보드 뗐을 때 speedx=0
    elif event.type==KEYDOWN: #키보드 눌렀을 때
        if event.key==K_LEFT: speedx=-5 #좌버튼일 때 speedx=-5
        elif event.key==K_RIGHT: speedx=+5 #우버튼일 때 speedx=+5
    screen.blit(base, (px,610)) #받침대 이미지 띄우기
    #햇빛 위에서 아래로 내려오기
    sx=0 ; sy= sy+8
    sun_= screen.blit(sun, (sx, sy)) #햇빛 이미지 띄우기
    if sy > 640: #햇빛이 바닥까지  내려오면
        sy= 0 #다시 위에서 내려오기
    if 0<px<118: #받침대가 햇빛이랑 겹치면
        if sy>600:
            sunscore+=4 #햇빛 점수 올라감
            totalscore+=4 #총 점수 올라감
    #거름 위에서 아래로 내려오기
    sox=228 ; soy= soy+8
    soil_= screen.blit(soil, (sox, soy))
    if soy> 640:
        soy= 0
    if 228< px < 323:
        if soy>600:
            soilscore+=4
            totalscore+=4
            
    #물 위에서 아래로 내려오기
    wx=433 ; wy= wy+8
    water_= screen.blit(water, (wx, wy))
    if wy> 640:
        wy= 0
    if 433<px<508:
        if wy>600:
            waterscore+=4
            totalscore+=4
            
    #조건 불만족시 게이지 감소
    if sunscore<soilscore:
        totalscore=totalscore-1
    if waterscore<soilscore:
        totalscore=totalscore-1
    if sunscore<waterscore:
        totalscore=totalscore-1

    #게이지에 따른 꽃의 상태 변화
    if 0<totalscore<100:
        screen.blit(tulipsad,(640,10))
    if 99<totalscore<220:
        screen.blit(tulipsoso,(640,10))
    if 219<totalscore<320:
        screen.blit(tulipgood, (640,10))

    if 319<totalscore:
        page=7

    if totalscore<1:
        page=8
        
    #점수 이미지, 띄우기
    conditionscore_img= font3.render('햇빛:{}      거름:{}      물:{}'.format(sunscore, soilscore, waterscore), True, (0,0,0))
    screen.blit(conditionscore_img, (680, 450))
    
    c.tick(30)
    

def page7(): #튤립 성공 페이지
    global page, tulipgood
    screen.fill((255,255,255))
    tulipgood_=pygame.image.load("images/tulipgood.jpg")
    screen.blit(tulipgood_, (530,0))
    success1=font2.render("축하합니다.",1,(0,0,0))
    success2=font2.render("꽃키우기 성공!!",1,(0,0,0))
    successpos1=success1.get_rect()
    successpos2=success2.get_rect()
    successpos1.topleft=(0,0)
    successpos2.topleft=(0,100)
    screen.blit(success1, successpos1)
    screen.blit(success2, successpos2)
    quit_button= textbutton('Quit',100, 400, normal_color) #종료 버튼 지정
    if event.type==MOUSEBUTTONUP: #마우스 클릭
        if quit_button: #restart_button 상태이면
            exit_game()


    
def page8(): #튤립 실패 페이지
    global page, tulipsad
    screen.fill((255,255,255))
    tulipsad_=pygame.image.load("images/tulipsad.jpg")
    screen.blit(tulipsad_, (388, 0))
    fail1=font2.render("꽃이 시들었어요.",1,(0,0,0))
    fail2=font2.render("꽃키우기 실패..",1,(0,0,0))
    failpos1= fail1.get_rect()
    failpos2= fail2.get_rect()
    failpos1.topleft=(0,0)
    failpos2.topleft=(0,100)
    screen.blit(fail1, failpos1)
    screen.blit(fail2, failpos2)
    quit_button= textbutton('Quit',100, 400, normal_color) #종료 버튼 지정
    if event.type==MOUSEBUTTONUP: #마우스 클릭
        if quit_button: #restart_button 상태이면
            exit_game()



def page9():#해바라기 조건 페이지
    global page
    screen.fill((255,255,255))
    method= font2.render("조건은 '햇빛<물<거름' 입니다",1,(0,0,0))
    methodpos=method.get_rect()
    methodpos.topleft=(50, 50)
    screen.blit(method, methodpos)
    ok_button= textbutton('OK',400, 400, normal_color) #종료 버튼 지정
    if event.type==MOUSEBUTTONUP: #마우스 클릭
        if ok_button: #restart_button 상태이면
            page=3

def page10():#튤립 조건 페이지
    global page
    screen.fill((255,255,255))
    method= font2.render("조건은 '거름<물<햇빛' 입니다",1,(0,0,0))
    methodpos=method.get_rect()
    methodpos.topleft=(50, 50)
    screen.blit(method, methodpos)
    ok_button= textbutton('OK',400, 400, normal_color) #종료 버튼 지정
    if event.type==MOUSEBUTTONUP: #마우스 클릭
        if ok_button: #restart_button 상태이면
            page=6


    
    
    

    

while True:
    px+=speedx    
    for event in pygame.event.get():
        if event.type==QUIT: #프로그램 종료
            exit_game()
    
    if page==1: page1()
    if page==2: page2()
    if page==3: page3()
    if page==4: page4()
    if page==5: page5()
    if page==6: page6()
    if page==7: page7()
    if page==8: page8()
    if page==9: page9()
    if page==10: page10()

            
    pygame.display.flip()
    pygame.display.update()

