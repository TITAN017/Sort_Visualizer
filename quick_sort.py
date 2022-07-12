class QS:

    def quick_partition(self,start,end):
        pivot = self.a[start]
        i = start + 1
        j = end
        while i < j:
            while self.a[i] < pivot and i <= end:
                i += 1
            while self.a[j] > pivot and j > start:
                j -= 1

            if i < j:
                self.sort_swap(i,j)
        
        self.sort_swap(start,j)
        return j

    def quick_sort(self,start,end):
        if end - start == 1:
            self.sort_swap(start,end)
        if end - start > 1:
            mid = self.quick_partition(start,end)
            self.quick_sort(start,mid)
            self.quick_sort(mid + 1,end)

    def sort_swap(self,i,j):
        if self.a[i] > self.a[j]:
            temp = self.a[i]
            self.a[i] = self.a[j]
            self.a[j] = temp

qs = QS()
qs.quick_sort(0,len(qs.a) - 1)
print(qs.a)