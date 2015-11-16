#!/usr/bin/env python

import math


class Heap():
    def __init__(self):
        self.hlist = []
    
    def parent(self, n):
        if n == 0:
            return None
        return (n-1)/2 

    def l_child(self, n):
        res = 2*n+1
        if res + 1 > len(self.hlist):
            return None
        return res
    
    def r_child(self, n):
        res = 2*n+2 
        if res + 1> len(self.hlist):
            return None
        return res

    def get_min(self):
        res = self.hlist[0]
        self.hlist[0] = self.hlist.pop()
        n = 0
        while True:
            l = self.l_child(n)
            r = self.r_child(n)
            if r != None and self.hlist[r] < self.hlist[n]:
                self.swap(r,n)
                n = r 
        

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
        
