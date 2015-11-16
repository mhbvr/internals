#!/usr/bin/env python

import math
import time


class Heap():
    def __init__(self):
        self.hlist = []
    
    def parent(self, n):
        if n == 0:
            return None
        return (n-1)/2 

    def swap(self, x, y):
        tmp = self.hlist[x]
        self.hlist[x] = self.hlist[y]
        self.hlist[y] = tmp

    def min_child(self, n):
        l = 2*n+1 
        r = 2*n+2
        num = len(self.hlist)
        if l+1 > num and r+1 > num:
            return None
        elif l+1 > num and r+1 <= num:
            return r
        elif l+1 <= num and r+1 > num:
            return l
        elif self.hlist[r] > self.hlist[l]:
            return l
        else:
            return r

    def get_min(self):
        res = self.hlist[0]
        last = self.hlist.pop()
        if not self.hlist:
            return res
        self.hlist[0] = last
        n = 0
        while True:
            m = self.min_child(n)
            if m != None and self.hlist[m] < self.hlist[n]:
                self.swap(n,m)
                n = m
            else:
                return res

    def add(self, x):
        self.hlist.append(x)
        n = len(self.hlist) - 1
  
        while True:
            p = self.parent(n)
            if p == None:
                break
            if self.hlist[p] > self.hlist[n]:
                self.swap(n, p)
                n = p
            else:
                break
         
    def __len__(self):
        return len(self.hlist)
    
    
if __name__ == "__main__":
    lst = [2,34,1,52,3,6,321,1,5,26,2,4,1,0,12,3,45,1,34,23,26,10,29,13,18,20]
    h = Heap()
    for i in lst:
        h.add(i)
    
    print h.hlist
    for i in range(len(lst)):
        print h.get_min()
