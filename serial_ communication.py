import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

ser.isOpen()

print 'Enter your commands below.\r\nInsert "exit" to leave the application.'

input=1
while 1 :
    # get keyboard input
    input = raw_input(">> ")
        
        
    if input == 'exit':
        ser.close()
        exit()
    else:
        # send the character to the device
        ser.write(input + '\r\n')
        out = ''
        # wait one second before reading output 
        time.sleep(1)
        while ser.inWaiting() > 0:
            out += ser.read(1)

        if out != '':
            print ">>" + out
