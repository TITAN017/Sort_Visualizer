class custom_sort:
    def __init__(self):
        self.a = [5,2,6,8,4,3,1]
        self.last = 0
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
        
        temp,j = self.a.pop(current),j-1
        self.a.insert(j,temp)
        
        self.last += 1

    def main_loop(self):
        print(self.a)

        if self.a[0] > self.a[1]:
            temp = self.a[0]
            self.a[0] = self.a[1]
            self.a[1] = temp

        for i in range(2,len(self.a)-1):
            self.binary_search_and_insert(i)

        print(self.a)


CS = custom_sort()