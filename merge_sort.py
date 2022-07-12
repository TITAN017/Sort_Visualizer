class MS:
    a = [11,4,3,7,1,2,6,9,8,13,12,34,53,49]
    b = []

    def merge_sort(self,start,end):
        if end - start > 1:
            mid = (start + end - 1) //2
            self.merge_sort(start,mid)
            self.merge_sort(mid + 1,end)
        else:
            self.sort_swap(start,end)
            a_p = start
            a_end = end
            b_p = 0
            b_end = len(self.b) - 1
            while b_p <= b_end and a_p <= a_end:
                if self.a[a_p] < self.b[b_p]:
                    self.b.insert(b_p,self.a[a_p])
                    a_p += 1
                    b_end += 1
                b_p += 1
            
            if a_p <= a_end:
                for i in self.a[a_p:a_end + 1]:
                    self.b.append(i)

            self.a[:len(self.b)] = self.b[:len(self.b)]
            print(f'partial : {self.b}')

    def sort_swap(self,i,j):
        if self.a[i] > self.a[j]:
            temp = self.a[i]
            self.a[i] = self.a[j]
            self.a[j] = temp


ms = MS()
ms.merge_sort(0,len(ms.a) - 1)
print(ms.a)
#commit 1