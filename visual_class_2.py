from cv2 import sort
import pygame
from random import randint
from visual_class_1 import Time
pygame.init()

font = pygame.font.Font('OpenSans-Regular.ttf',40)

class Bars(pygame.sprite.Group):

    def create(self,value,sort_type):
        self.colours = [(0,0,0),(255,0,0),(255,255,255)]
        self.numbers = []
        self.end = False
        self.sort_type = sort_type
        self.stop = False
        self.width = 800/value

        for i in range(value - 1):
            #j = (randint(0,255),randint(0,255),randint(0,255))
            #while j in self.colours:
             #   j = (randint(0,255),randint(0,255),randint(0,255))
            #self.colours.append(j)
            j = 600*randint(1,value-1)//value
            while j in self.numbers:
                j = 600*randint(1,value-1)//value
            self.numbers.append(j)
            Bar_sprite(self,i,800/value,self.numbers[-1],'white')
        self.numbers.append(600)
        Bar_sprite(self,value - 1,800/value,600,'white')
        self.sprite_list = [i for i in self]
        self.aux = []
        #self.sprite_list.sort(key = lambda s:s.rect.x)
        self.select = 0
        self.victim_1 = -1
        self.victim_2 = -1
        self.count = value
        self.swap = 0
        self.comparison = 0
        self.notif = pygame.sprite.Group()
        self.time_group = pygame.sprite.GroupSingle()
        self.recent = 0
        self.dir = 1
    
    def wait(self):
        if self.sort_type == 0:
            self.recent = pygame.time.get_ticks()
            while pygame.time.get_ticks() - self.recent <= 10:
                pass
        else:
            self.recent = pygame.time.get_ticks()
            while pygame.time.get_ticks() - self.recent <= 100:
                pass

    def check_sort(self):
        b = sorted(self.numbers)
        if self.numbers == b:
            self.end = True

    def custom_draw(self):
        self.wait()
        self.status()
        #if not self.end:
        pygame.display.get_surface().fill('black')
        for i in self.sprite_list:
            self.sprite_list[self.sprite_list.index(i)].image.fill(i.col)
            if self.select > 0:
                if i == self.sprite_list[self.select]:
                    self.sprite_list[self.select].image.fill('red')
            if self.victim_1 >=0:
                if i == self.sprite_list[self.victim_1]:
                    self.sprite_list[self.victim_1].image.fill('yellow')
            if self.victim_2 >=0:
                if i == self.sprite_list[self.victim_2]:
                    self.sprite_list[self.victim_2].image.fill('yellow')
            pygame.display.get_surface().blit(i.image,i.rect)
        self.notif.draw(pygame.display.get_surface())
        if not self.end:
            Time(pygame.time.get_ticks(),self.time_group)
        self.time_group.draw(pygame.display.get_surface())
        pygame.display.update()
            #pygame.time.delay(100)
   
    def exchange_sort_mechanism(self):
            #if pygame.time.get_ticks() - self.recent>=1000:
                if self.count == len(self.sprite_list):
                    self.end = True
                    Status(self.notif,'success')
                    self.notif.draw(pygame.display.get_surface())
                elif self.victim >=0:

                    #self.sprite_list[self.select].image.fill(self.sprite_list[self.select].col)
                    #self.sprite_list[self.victim].image.fill(self.sprite_list[self.victim].col)

                    self.sort_swap(self.select,self.victim)

                    #self.complete.append(temp)
                    #self.search_list.remove(temp)

                    #self.select = (self.select + self.dir)%len(self.sprite_list)
                    self.victim = -1

                elif self.dir == 1:     
                    if self.select != len(self.sprite_list) - 1:
                        if self.sprite_list[self.select].value >  self.sprite_list[(self.select + self.dir)%len(self.sprite_list)].value:
                            self.victim = (self.select + self.dir)%len(self.sprite_list)
                                #self.progress = 1
                                #self.diff = self.sprite_list[self.victim].rect.x - self.sprite_list[self.select].rect.x
                                #self.dir = 1
                            self.swap += 1
                            self.count = 0
                            self.dir = -1
                            #self.recent = pygame.time.get_ticks()
                        else:
                            self.select = (self.select + self.dir)%len(self.sprite_list)
                            self.count += 1
                    else:
                        if self.sprite_list[self.select].value <  self.sprite_list[(self.select + self.dir)%len(self.sprite_list)].value:
                            self.victim = (self.select + self.dir)%len(self.sprite_list)
                                #self.progress = 1
                                #self.diff = self.sprite_list[self.select].rect.x - self.sprite_list[self.victim].rect.x
                            self.dir = -1
                            self.count = 0
                            self.swap += 1
                            #self.dir = -1
                            #self.recent = pygame.time.get_ticks()
                        else:
                            self.select = (self.select + self.dir)%len(self.sprite_list)
                            self.count += 1
                    self.comparison += 1
                else:
                    if self.select != 0:
                        if self.sprite_list[self.select].value <  self.sprite_list[(self.select + self.dir)%len(self.sprite_list)].value:
                            self.victim = (self.select + self.dir)%len(self.sprite_list)
                                #self.progress = 1
                                #self.diff = self.sprite_list[self.victim].rect.x - self.sprite_list[self.select].rect.x
                                #self.dir = 1
                            self.swap += 1
                            self.count = 0
                            self.dir = 1
                            #self.recent = pygame.time.get_ticks()
                        else:
                            self.select = (self.select + self.dir)%len(self.sprite_list)
                            self.count += 1
                    else:
                        if self.sprite_list[self.select].value >  self.sprite_list[(self.select + self.dir)%len(self.sprite_list)].value:
                            self.victim = (self.select + self.dir)%len(self.sprite_list)
                                #self.progress = 1
                                #self.diff = self.sprite_list[self.select].rect.x - self.sprite_list[self.victim].rect.x
                                #self.dir = -1
                            self.count = 0
                            self.swap += 1
                            self.dir = 1
                            #self.recent = pygame.time.get_ticks()
                        else:
                            self.select = (self.select + self.dir)%len(self.sprite_list)
                            self.count += 1
                    self.comparison += 1

    def quick_sort_partition(self,start,end):
        self.select = start
        pivot = self.sprite_list[start].value
        i = start + 1
        j = end
        while i < j:
            while self.sprite_list[i].value < pivot and i <= end:
                i += 1
                self.comparison += 1
            while self.sprite_list[j].value > pivot and j > start:
                self.comparison += 1
                j -= 1

            if i < j:
                self.victim_1 = i
                self.victim_2 = j
                self.sort_swap(i,j)
                self.custom_draw()
    
            self.victim_2 = -1
            self.victim_1 = -1
        
        self.sort_swap(start,j)
        return j

    def quick_sort_mechanism(self,start,end):
        if not self.end:
            if end - start == 1:
                self.comparison += 1
                self.sort_swap(start,end)
            elif end-start>1:
                self.check_sort()
                mid = self.quick_sort_partition(start,end)
                self.quick_sort_mechanism(start,mid)
                self.quick_sort_mechanism(mid+1,end)
    
    def merge_sort_partition(self,i,j):
        return (i+j-1)//2

    def merge_sort_merge(self,start,end):
        self.sort_swap(start,end)
        aux_pointer = 0
        aux_end = len(self.aux) - 1
        sprite_pointer = start
        sprite_end = end
        while aux_pointer <= aux_end and sprite_pointer <= sprite_end:
            if self.sprite_list[sprite_pointer].value < self.aux[aux_pointer].value:
                self.aux.insert(aux_pointer,self.sprite_list[sprite_pointer])
                #self.aux[aux_pointer].rect.midbottom = self.aux[aux_pointer+1].rect.midbottom
                #for i in self.aux[aux_pointer + 1:]:
                    #i.rect.x += self.width
                #self.custom_draw()
                sprite_pointer += 1
                aux_end += 1
                self.swap += 1
            aux_pointer += 1
            self.comparison += 1
        
        if sprite_pointer <= sprite_end:
            for i in self.sprite_list[sprite_pointer:sprite_end + 1]:
                self.aux.append(i)
                #if len(self.aux) == 1:
                    #self.aux[0].rect.bottomleft = (0,800)
                #else:
                    #self.aux[-1].rect.x = self.aux[-2].rect.x + self.width
                #else:
                    #self.aux[1].rect.bottomleft = (self.width,0)
                #self.custom_draw()
    def merge_draw(self):
        self.wait()
        pygame.display.get_surface().fill('black')
        for i in self.aux:
            self.aux[self.aux.index(i)].image.fill(i.col)
            if i == self.aux[self.select]:
                self.aux[self.select].image.fill('red')
            if self.victim_1 >=0:
                if i == self.aux[self.victim_1]:
                    self.aux[self.victim_1].image.fill('yellow')
            if self.victim_2 >=0:
                if i == self.aux[self.victim_2]:
                    self.aux[self.victim_2].image.fill('yellow')
            pygame.display.get_surface().blit(i.image,i.rect)
            print(i.value,f'co-ord : {i.rect.bottomleft}',end=" ")
        self.notif.draw(pygame.display.get_surface())
        print('\n')
        pygame.display.update()

    def merge_sort_mechanism(self,start,end):
        if end - start > 1:
            mid = self.merge_sort_partition(start,end)
            self.select,self.victim_1,self.victim_2 = mid,start,mid - 1
            self.merge_sort_mechanism(start,mid)
            self.select,self.victim_1,self.victim_2 = mid,mid + 1,end
            self.merge_sort_mechanism(mid + 1,end)
            if end == len(self.sprite_list) - 1:
                self.end = True
        else:
            self.merge_sort_merge(start,end)
            for i,j in enumerate(self.aux):
                self.sprite_list[i] = j
                self.sprite_list[i].rect.bottomleft = (i*self.width,800)
                self.custom_draw()

    def gnome_sort_mechanism(self):
        i = 0
        while i != len(self.sprite_list) - 1:
            self.input_check()
            self.select = i
            self.victim = -1
            if self.sprite_list[i].value > self.sprite_list[i+1].value and i >= 0:
                self.sort_swap(i,i+1)
                self.victim = i + 1
                i -= 1
            elif self.sprite_list[i-1].value > self.sprite_list[i].value and i != 0:
                self.sort_swap(i-1,i)
                self.victim = i - 1
                i -= 1
            else:
                i += 1
                self.select = i
            self.custom_draw()
                
            self.comparison += 1
        self.end = True

    def pancake_sort_mechanism(self):
        max = self.sprite_list[0].value
        max_p = 0
        p = len(self.sprite_list) - 1
        while p>0:
            self.input_check()
            #find max
            #flip 0 to max
            #flip 0 to p - 1
            for i in self.sprite_list[:p + 1]:
                if i.value > max:
                    max = i.value
                    max_p = self.sprite_list.index(i)
            
            self.flip(max_p)

            self.flip(p)

            max = 0

            p -= 1
        self.end = True
                
    def custom_sort(self):

        for i in range(1,len(self.sprite_list)):
            self.custom_sort_mechanism(i)

    def custom_sort_mechanism(self,current):
        i,j,self.select = 0,current - 1,current

        while j - i > 1:
            mid = (i+j)//2
            if self.sprite_list[current].value > self.sprite_list[mid].value:
                i = mid
            else:
                j = mid

        temp = self.sprite_list.pop(current)
        self.victim_1 = i
        self.victim_2 = j

        if temp.value < self.sprite_list[i].value:
            self.sprite_list.insert(i,temp)
        elif temp.value > self.sprite_list[j]:
            self.sprite_list.insert(j + 1,temp)
        else:
            self.sprite_list.insert(j,temp)

        for k in range(current):
            self.sprite_list[k].rect.bottomleft = (k * self.width,800)
            self.custom_draw()


    def sort_swap(self,i,j):
        #if self.sprite_list[i].value > self.sprite_list[j].value:

            temp = self.sprite_list[i].rect.midbottom
            self.sprite_list[i].rect.midbottom = self.sprite_list[j].rect.midbottom
            self.sprite_list[j].rect.midbottom = temp

            temp = self.sprite_list[i]
            self.sprite_list[i] = self.sprite_list[j]
            self.sprite_list[j] = temp

            temp = self.numbers[i]
            self.numbers[i] = self.numbers[j]
            self.numbers[j] = temp         

            self.swap += 1

    def input_check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

    def flip(self,p):
        self.sprite_list[:p+1] = self.sprite_list[:p+1][::-1]
        for i,j in enumerate(self.sprite_list):
            j.rect.bottomleft = (i*self.width,800)
            self.swap += 1
            self.custom_draw()
        self.select = p
        


    def status(self):
        self.notif.empty()
        Status(self.notif,'bg')
        Status(self.notif,'S',self.swap)
        Status(self.notif,'C',self.comparison)
        Status(self.notif,'c',self.count)


class Bar_sprite(pygame.sprite.Sprite):
    def __init__(self,group,i,x,y,col):
        super().__init__([group])
        self.image = pygame.Surface((x,y))
        self.image.fill(col)
        self.rect = self.image.get_rect(bottomleft = (i*x,800))
        self.value = y
        self.col = col

class Status(pygame.sprite.Sprite):
    def __init__(self,group,type,value = None):
        super().__init__([group])
        if type == 'bg':
            self.image = pygame.Surface((800,200))
            self.image.fill('black')
            self.rect = self.image.get_rect(topleft = (0,0))
        elif type == 'S':
            self.image = font.render(f'Swaps : {value}',True,'white').convert_alpha()
            self.rect = self.image.get_rect(topleft = (0,0))
        elif type == 'c':
            self.image = font.render(f'Count : {value}',True,'white').convert_alpha()
            self.rect = self.image.get_rect(center = (400,100))
        elif type == 'success':
            self.image = font.render(f'Sorted!',True,'white').convert_alpha()
            self.rect = self.image.get_rect(midbottom = (400,200))
        else:
            self.image = font.render(f'Comparisons : {value}',True,'white').convert_alpha()
            self.rect = self.image.get_rect(topright = (800,0))