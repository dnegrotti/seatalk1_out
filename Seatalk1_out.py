#!/usr/bin/env python
#Sends seatalk1 datagrams to serial output
#By Cari20 (2020) loosely based on Marco Bergman ST2000 RPi remote

import RPi.GPIO as GPIO
import serial
import binascii

msg2 = msg['payload']
lst = msg2.split("*")[0].split(",")
lst.append(msg2.split("*")[1])

if lst[0]=='$STALK':
  with serial.Serial('/dev/serial0', 4800, timeout=10, writeTimeout=0) as ser:
      ser.parity = serial.PARITY_MARK
      ser.write(binascii.unhexlify(lst[1]))
      ser.parity = serial.PARITY_SPACE
      for i in lst[2:-1]:
        ser.write(binascii.unhexlify(i))
      ser.close()

return msg
