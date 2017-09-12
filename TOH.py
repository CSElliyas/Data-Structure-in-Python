#!/usr/bin/python

#Tower of Hanoi Problem with Python
#By Elliyas Ahmed
#12.09.2017
#Method Recursive
def TOH(n, fromTower, withTower, toTower):
	if n>0:
		TOH(n-1, fromTower, toTower, withTower)
		moveDisk(fromTower, toTower)
		TOH(n-1, withTower, fromTower, toTower)

def moveDisk(fromT, toT):
	print("Move Disk from", fromT, "-", toT)

TOH(3, '1', '2', '3')
