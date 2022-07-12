import pygame
from visual_class_1 import menu_group,Speed
from visual_class_2 import Bars
pygame.init()

WIDTH = 800
HEIGHT = 800
speed = 1000
speed_change = {1000:10,10:0,0:1000}
speed_rate_change = {60:300,300:60}
speed_group = pygame.sprite.GroupSingle()
speed_rate = 60
value = 0
press = False

click = False
click_timer = 0

menu_active = True


display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Visualiser')

menu_group.create()
bars_group = Bars()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #if event.type == pygame.MOUSEBUTTONDOWN:
            #if not click:
                #pos = pygame.mouse.get_pos()
                #print(f'entered {pos}')
                #for i in menu_group:
                    #if i.rect.collidepoint(pos):
                        #if i.type == '+':
                            #menu_group.change(1)
                            #print('collision +')
                        #elif i.type == '-':
                            #menu_group.change(-1)
                            #print('collision -')
                        #elif i.type == 'submit':
                            #menu_active = False
                            #value = [i for i in menu_group if i.type == 'number'][0].value
                           # bars_group.create(value)
        if event.type == pygame.KEYDOWN and not click:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                menu_group.change(1)
            elif keys[pygame.K_d]:
                menu_group.change(100)
            elif keys[pygame.K_a]:
                menu_group.change(-10)
            elif keys[pygame.K_LEFT]:
                menu_group.change(-1)
            elif keys[pygame.K_SPACE]:
                if menu_active:
                    menu_active = False
                    value = [i for i in menu_group if i.type == 'number'][0].value
                    bars_group.create(value,0)
                    #b_it = bars_group.quick_sort_mechanism(0,value - 1)
                else:
                    speed = speed_change[speed]
                    speed_rate = speed_rate_change[speed_rate]
                    Speed(speed,speed_group)
            elif keys[pygame.K_m]:
                if menu_active:
                    menu_active = False
                    value = [i for i in menu_group if i.type == 'number'][0].value
                    bars_group.create(value,1)                    
            elif keys[pygame.K_r]:
                if not menu_active and bars_group.end:
                    menu_active = True
                    menu_group.empty()
                    menu_group.create()
                    bars_group.empty()
                    speed_rate = 60
                    speed = 1000
                    #bars_group.create(value)
            elif keys[pygame.K_p]:
                press = False
                while(not press):
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_p]:
                        press = True

            click = True
            click_timer = pygame.time.get_ticks()           

    if click:
        if pygame.time.get_ticks() - click_timer >= 50:
            click = False
            if menu_active:
                warning = [i for i in menu_group if i.type == 'warning']
                if warning:
                    warning = warning[0]
                    warning.kill()
    
    if menu_active:

        display.fill('white')
        menu_group.draw(display)

    elif not bars_group.end:

        if bars_group.sort_type == 1:

            bars_group.custom_draw()
            bars_group.merge_sort_mechanism(0,value - 1)

        else:

            bars_group.custom_draw()
            bars_group.pancake_sort_mechanism()

        speed_group.draw(display)         
    else:

        bars_group.custom_draw()

    pygame.display.update()

    clock.tick(speed_rate)