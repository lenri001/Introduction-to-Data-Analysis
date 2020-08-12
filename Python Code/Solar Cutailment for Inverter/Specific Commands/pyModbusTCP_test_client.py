# USE THIS CODE FIRST 
# THIS CODE IS INTENDED TO CONFIRM IF CLIENT IS CONNECTING TO SERVER
# IN SIMPLER TERMS THIS CODE COMFIRMS THAT YOU COMPUTER IS CONNECTED TO THE MOBUS DEVICE

# Write to registers for solar curtailement 

# you can use the tiny modbus server "mbserverd" to test this code
# mbserverd is here: https://github.com/sourceperl/mbserverd

# the command line modbus client mbtget can also be useful
# mbtget is here: https://github.com/sourceperl/mbtget

from pyModbusTCP.client import ModbusClient
import time

SERVER_HOST = "" # Insert Modbus Inverter IP address here 
SERVER_PORT = 502 # Default Modbus port. There should be no need to change this

c = ModbusClient()

# uncomment this line to see debug message
#c.debug(True)

# define modbus server host, port
c.host(SERVER_HOST)
c.port(SERVER_PORT)

while True:
    # open or reconnect TCP to server
    if not c.is_open():
        if not c.open():
            print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))

    # if open() is ok, write registers
    if c.is_open():
        print("Sucessfully connected to Server:" + SERVER_HOST)

    # sleep 2s before next polling
    time.sleep(2)