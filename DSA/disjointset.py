class DisJointSet:
    def __init__(self,n):
        self.arr = [-1] * n
        self.rank = [0] * n
    def find(self,x):
        return x if self.arr[x] == -1 else self.find(self.arr[x])
    def union(self,x,y):
        if self.find(x) != self.find(y):
            if self.rank[x] > self.rank[y]:
                self.arr[y] = x
                self.rank[x] += 1
            else:
                self.arr[x] = y
                self.rank[y] += 1

dset = DisJointSet(5)

dset.union(0,1)
dset.union(1,2)

print(dset.find(0))
print(dset.find(1))
print(dset.find(2))
print(dset.find(3))
print(dset.find(4))
            



