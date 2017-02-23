# by Augustus Nightcustard
# heavily based upon work by Carl Monk (@ForToffee)
# based on work from http://playground.arduino.cc/Main/RoboSapienIR
# command codes originally from http://www.aibohack.com/robosap/ir_codes.htm

import robo
# import time

rs=robo.Robo(21)      	# Create Robo object for GPIO 21
rs.send_code(0xB1)      # Wake
# rs.send_code(0xAE)      # Reset
# rs.send_code(0xA3)      # Sleep
# time.sleep(10)          # Delay 10 secs
# rs.send_code(0x98)      # Quiet execute
# time.sleep(5)
# rs.send_code(0xD1)      # Rosebud