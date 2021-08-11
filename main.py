# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import dht11
import time
import datetime
import slackweb
import config

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# initialize Slack
slack = slackweb.Slack(url = config.slack_url)

# read data using pin 14
instance = dht11.DHT11(pin=14)

# output value a time
result = instance.read()
if result.is_valid():
    # print("Last valid input: " + str(datetime.datetime.now()))
    #print("Temperature: %-3.1f C" % result.temperature)
    #print("Humidity: %-3.1f %%" % result.humidity)

    msg = u"温度：{0:0.1f}℃ 湿度：{1:0.1f}%".format(result.temperature, result.humidity)
    slack.notify(text=msg)

# cleanup GPIO
#print("Cleanup")
GPIO.cleanup()
