#!/usr/bin/python

#Tower of Hanoi Problem with Python
#By Elliyas Ahmed
#12.09.2017
#www.compromath.com
#Method Recursive
def TOH(n, fromTower, withTower, toTower):
	if n>0:
		TOH(n-1, fromTower, toTower, withTower)
		moveDisk(fromTower, toTower)
		TOH(n-1, withTower, fromTower, toTower)

def moveDisk(fromT, toT):
	print("Move Disk from", fromT, "to", toT)

TOH(3, 'A', 'B', 'C')
#Here A, B, C the number of Tower
#3 is the number of Disk
