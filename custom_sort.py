from random import randint

class custom_sort:
    def __init__(self):
        self.n = 10000
        self.a = []
        while len(self.a) != self.n:
            r = randint(1,self.n)
            if r not in self.a:
                self.a.append(r)
        self.last = 0
        self.comp = 0
        self.swap = 0
        self.loop = 0
        self.main_loop()

    def binary_search_and_insert(self,current):
        i,j = 0,self.last
        while j-i > 1:
            mid = (i+j)//2
            if self.a[mid] > self.a[current]:
                j = mid
            else:
                i = mid
            self.comp += 1
            self.loop += 1
        
        temp = self.a.pop(current)
        if temp < self.a[i]:
            self.a.insert(i,temp)
            self.swap += current - i + 1
        elif temp > self.a[j]:
            self.a.insert(j+1,temp)
            self.swap += current - j
        else:
            self.a.insert(j,temp)
            self.swap += current - j + 1
        
        self.last += 1
        self.comp += 1

    def main_loop(self):
        #print(self.a)

        for i in range(1,len(self.a)):
            self.binary_search_and_insert(i)

        print('\nswaps: ',self.swap,'\ncomps: ',self.comp,'\nloops: ',self.loop)


CS = custom_sort()