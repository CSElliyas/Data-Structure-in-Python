#!/usr/bin/python
# This program will print the element of list LA where K is a counter with while loop.
# PROGRAM BY ELLIYAS AHMED
# Blog: www.compromath.com

LA = [2, 1, 3, 4, 5] #in Python list works as array in C
K = 0 # INITIALIZE COUNTER
while K < LA[len(LA)-1]: #REPEAT TILL K<= Length of List
	print LA[K] #PRINT List Element
	K = K + 1 # INCREASE COUNTER
print 'End of Traversing' #PRINT END OF TRAVERSING
