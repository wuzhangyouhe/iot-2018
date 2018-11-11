import time
 
try:
    while True:
        tempfile = open("/sys/bus/w1/devices/28-2239a3000900/w1_slave")
        content = tempfile.read()
        tempfile.close()
        tempdata = content.split("t=")[1]
        temperature = float(tempdata)
        temperature = temperature / 1000
        print temperature
        time.sleep(1)
except KeyboardInterrupt:
    print "Aborted"
    pass
