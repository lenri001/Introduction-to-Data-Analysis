# This code is an Python implementation of Example 2: Setting Curtailment (Page 7-8) described in the Advanced Energy ® Advanced Power Controls TM Manual 
# This manual can be found as "Advanced controls-Modbus mapping unedited.pdf" in the CERT GitHub Repo. Link https://github.com/ucr-cert/Solar-Curtailment/tree/master/Inverter%20Manuals/AE%20Inverter%20(CE-CERT%20Solar)
# Write to registers for solar curtailement 
# This code is intended to run on its own

from pyModbusTCP.client import ModbusClient
import time

###################### THESE SHOULD BE THE ONLY VALUES THAT ARE MODIFIED. THE REST SHOULD BE UNCHANGED ######################

SERVER_HOST = "" # Insert Modbus Inverter IP address here 
print("The server host is: " + SERVER_HOST)
SERVER_PORT = 502 # Default Modbus port. There should be no need to change this
curtailment_set_point = 20 # Set curtailment at "x-amount" % of full power. The "x-amount" is user defined by the curtailment_set_point
time_interval_step = 60 # The amount of time between the implemantation of each function 
ramp_rate = 5 # Decrease power by "x-amount" kVA per second ramp rate. The "x-amount" is user defined by the variable ramp_rate
delay = False # When true, this delays time between each register
delay_value = 5 # Determine the length of the delay between registers. delay must be set to true for this to work 
current_time = 0 # Desctibes the time for every iteration of code. Do not change from 0.
iteration = 0 # Desctibes iteration of code. Do not change from 0.
#############################################################################################################################

###################### THE CODE BELOW SHOULD NOT NEED TO BE MODIFIED TO RUN ######################

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
        print("\n ############# TIME : " + str(current_time) + " seconds. ITERATION: " + str(iteration) + " ############# \n")
        # Print a comment to confirm connection
        print 
        print("Sucessfully connected to "+SERVER_HOST+":"+str(SERVER_PORT))

        # Advanced Power Controls must be enabled (register 3035 = 5)
        # Check if Advanced Power Controls is enabled
        # Read 1 register at address 3035, store result in reg_advanced_power_control list
        reg_advanced_power_control = c.read_holding_registers(3035, 1) # Checks if Advanced Power Controls is enabled
        # if success display register
        if reg_advanced_power_control:
            print("Advanced Power Controls Register set to: " + str(reg_advanced_power_control))
            if reg_advanced_power_control[0] != 5: # If Advanced Power Controls is not enabled, enable it 
                # write register for Action delay
                reg_action_delay = c.write_single_register(3305, 5) # Set Advanced Power Controls to enable 
                # if success display register
                if reg_action_delay:
                    print("Advanced Power Controls Register reset to: 5")
        
        # Read power factor operation error 
        # Read 1 register at address 4006, store result in reg_power_factor_error_2 list
        reg_power_factor_error_1 = c.read_holding_registers(4006, 1)
        # if success display register
        if reg_power_factor_error_1:
            print("Power Factor Operation Error: "+str(reg_power_factor_error_1) + "\n Power Factor Operation Error needs to be 0 for solar curtailment to commence")
            if reg_power_factor_error_1[0] == 0:
                # Print that Power Factor Operation Error has passed
                print("Power Factor Operation Error passed. Solar Curtailment will begin")
                # This creates a delay between registers if delay is set to true
                if delay:
                    time.sleep(delay_value) # Will delay "delay_value" seconds

                ### Once No Power Factor Operation Error is Verified, the Solar Curtailmnet will begin by writing the registers ### 

                # write register for Power factor mode 
                reg_power_factor_mode = c.write_single_register(4101, 0) # 0 = No change to power factor. Power factor = 1.0.
                # if success display register
                if reg_power_factor_mode:
                    print("Power Factor Mode Set to 1.0")
                    # This creates a delay between registers if delay is set to true
                    if delay:
                        time.sleep(delay_value) # Will delay "delay_value" seconds
                
                # write register for Curtailment mode
                reg_curtailment_mode = c.write_single_register(4102, 0) # Set fixed curtailment mode
                # if success display register
                if reg_curtailment_mode:
                    print("Curtialmnet Mode Turned Off")
                    # This creates a delay between registers if delay is set to true
                    if delay:
                        time.sleep(delay_value) # Will delay "delay_value" seconds
                else:
                    print ("Curtailment mode not working")
    current_time += time_interval_step
    iteration += 1
    # sleep time_interval_step seconds before next polling
    print("Please wait " + str(time_interval_step) + " seconds for the next iteration")
    time.sleep(time_interval_step)