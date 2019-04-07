import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
gpio.setup(7,gpio.OUT)
gpio.output(7,1)
gpio.output(11,1)
gpio.output(13,0)
gpio.output(15,1)
