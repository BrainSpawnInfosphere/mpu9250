#!/usr/bin/env python

from mpu9250 import mpu9250
from time import sleep

imu = mpu9250()

try:
	while True:
		a = imu.accel
		print 'Accel: {:.3f} {:.3f} {:.3f} mg'.format(*a)
		# g = imu.gyro
		# print 'Gyro: {:.3f} {:.3f} {:.3f} dps'.format(*g)
		# m = imu.mag
		# print 'Magnet: {:.3f} {:.3f} {:.3f} mT'.format(*m)
		# m = imu.temp
		# print 'Temperature: {:.3f} C'.format(m)
		sleep(0.5)
except KeyboardInterrupt:
	print 'bye ...'
