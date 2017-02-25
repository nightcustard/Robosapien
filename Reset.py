# by Augustus Nightcustard
# heavily based upon work by Carl Monk (@ForToffee)
# based on work from http://playground.arduino.cc/Main/RoboSapienIR
# command codes originally from http://www.aibohack.com/robosap/ir_codes.htm

import robo
import time

rs=robo.Robo(21)	#create Robo object for GPIO 21

rs.send_code(0xAE) # Reset