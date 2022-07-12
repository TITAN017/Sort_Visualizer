import pygame
pygame.init()

font = pygame.font.Font('OpenSans-Regular.ttf',40)
menu = None

class Main_Menu(pygame.sprite.Group):
    def bar(self):
        Menu_sprite('+')
        Menu_sprite('-')
    def create(self):
        Menu_sprite('display')
        Menu_sprite('prompt')
        self.bar()
        Menu_sprite(0)
        Menu_sprite('Ok')
        Menu_sprite('hint')
    def change(self,value):
        for i in self:
            if i.type == 'number':
                actual_value = i.value
                value += actual_value
                if value>=0:
                    i.kill()
                    Menu_sprite(value)
                else:
                    Menu_sprite('warning')

menu_group = Main_Menu()

class Menu_sprite(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__([menu_group])
        self.type = None
        self.main_create(type)
    
    def main_create(self,type):
        if type == 'display':
            self.display()
        elif type == 'prompt':
            self.prompt()
        elif type == '+':
            self.bar(type)
        elif type == '-':
            self.bar(type)
        elif type == 'warning':
            self.warning()
        elif type == 'Ok':
            self.ok()
        elif type == 'hint':
            self.hint()
        else:
            self.num(type)
        
    def display(self):
        global menu
        self.image = pygame.Surface((400,400))
        self.image.fill('red')
        self.rect = self.image.get_rect(center = (400,400))
        self.type = 'display'
        menu = self.rect

    def prompt(self):
        global menu
        self.image = font.render('Enter N:',True,'green').convert_alpha()
        self.rect = self.image.get_rect(midtop = menu.midtop)
        self.type = 'prompt'

    def bar(self,type):
        global menu
        self.image = font.render(type,True,'blue')
        if type == '-':
            self.rect = self.image.get_rect(midleft = menu.midleft)
            self.type = '-'
        else:
            self.rect = self.image.get_rect(midright = menu.midright)
            self.type = '+'

    def num(self,value):
        global menu
        self.image = font.render(str(value),True,'black').convert_alpha()
        self.rect = self.image.get_rect(center = menu.center)
        self.type = 'number'
        self.value = value

    def warning(self):
        global menu
        self.image = font.render('N cannot be below 0',True,'black').convert_alpha()
        self.rect = self.image.get_rect(midbottom = menu.midbottom)
        self.type = 'warning'

    def ok(self):
        global menu
        self.image = font.render('Ok',True,'black').convert_alpha()
        self.rect = self.image.get_rect(midtop = menu.midbottom)
        self.type = 'submit'

    def hint(self):
        global menu
        self.image = font.render('Merge Sort - m | Quick Sort - space_bar',True,'black').convert_alpha()
        self.rect = self.image.get_rect(midtop = (400,0))

class Speed(pygame.sprite.Sprite):
    def __init__(self,value,group):
        super().__init__([group])
        self.image = font.render(f'Speed:{value}',True,'white').convert_alpha()
        self.rect = self.image.get_rect(topleft = (0,100))

class Time(pygame.sprite.Sprite):
    def __init__(self,value,group):
        super().__init__([group])
        self.image = font.render(f'Time : {value/1000} s',True,'white').convert_alpha()
        self.rect = self.image.get_rect(midright = (800,100))