class custom_sort:
    def __init__(self):
        self.a = [5,2,6,8,4,3,1]
        self.last = 1
        self.comp = 0
        self.swap = 0
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
        
        temp = self.a.pop(current)
        if temp < self.a[i]:
            self.a.insert(i,temp)
        elif temp > self.a[j]:
            self.a.insert(j+1,temp)
        else:
            self.a.insert(j,temp)
        
        self.last += 1
        self.comp += 1

    def main_loop(self):
        print(self.a)

        if self.a[0] > self.a[1]:
            temp = self.a[0]
            self.a[0] = self.a[1]
            self.a[1] = temp
            self.swap += 1
        self.comp += 1

        for i in range(2,len(self.a)):
            self.binary_search_and_insert(i)

        print(self.a,'\n',self.swap,'\n',self.comp)


CS = custom_sort()