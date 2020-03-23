#!/usr/bin/python3
import time

"""
Find Duplicate Number
Given an array nums containing n+1 integers where
each integer is between 1 and n inclusive. Prove
that at least one duplicate number exist. Assume
there are only one duplicate number, find that
number

Proven with pigeonhole's principle
"""

#toy = [3,2,1,4,5,7,7,8,10]
toy = [1,4,3,2,7,5,4,6,8]

# sort the number and perform a linear scan
def sortscan(nums):
    nums.sort()
    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]:
            #found
            return nums[i]

# use a hashmap to check if a num has already been seen
def hashmap(nums):
    seen = {}
    for n in nums:
        if n in seen:
            return n
        seen[n] = True

def torthare(nums):
    # start tortoise and hare at same pointer
    t = nums[0]
    h = nums[0]
    # try to find a cycle
    while True:
        t = nums[t] #linear
        h = nums[nums[h]] #2x
        if t == h:
            #found
            break

    ptr1 = nums[0]
    ptr2 = t
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    return ptr1

stime = time.time()
print(sortscan(toy))
print( (time.time() - stime)*1000000,"us" )

stime = time.time()
print(hashmap(toy))
print( (time.time() - stime)*1000000,"us" )

stime = time.time()
print(torthare(toy))
print( (time.time() - stime)*1000000,"us" )

