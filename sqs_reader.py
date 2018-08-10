import boto3
import os
import time
import serial

# Input your own information into lines below.
access_key = "<<ACCESS KEY>>"
access_secret = "<<SECRET KEY>>"
region ="<<REGION>>"
queue_url = "<<QUEUE URL>>"

def pop_message(client, url):
    response = client.receive_message(QueueUrl = url)

    #last message posted becomes messages
    message = response['Messages'][0]['Body']
    receipt = response['Messages'][0]['ReceiptHandle']
    client.delete_message(QueueUrl = url, ReceiptHandle = receipt)
    return message
    
client = boto3.client('sqs', aws_access_key_id = access_key, aws_secret_access_key = access_secret, region_name = region)

waittime = 20
client.set_queue_attributes(QueueUrl = queue_url, Attributes = {'ReceiveMessageWaitTimeSeconds': str(waittime)})

time_start = time.time()
# any time can be set before program stops checking.
while (time.time() - time_start < 60000000000000):
        print("Checking...")
        try:
                message = pop_message(client, queue_url)
                print(message)
                # code from serial_communication.py implementation.
                # if statement based on what message is pulled from SQS.
                if message == "DP":
    
                        ser = serial.Serial(
                            port='/dev/ttyUSB0',
                            baudrate=115200,
                            parity=serial.PARITY_NONE,
                            stopbits=serial.STOPBITS_ONE,
                            bytesize=serial.EIGHTBITS
                        )

                        ser.isOpen()

                        print 'Enter your commands below.\r\nInsert "exit" to leave the application.'
                            # get keyboard input
                        input = "source=1"
                                
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

                elif message == "HDMI":
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
                            # get keyboard input
                        input = "source=2"
                                
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
                elif message == "VGA":
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
                            # get keyboard input
                        input = "source=3"
                                
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
                elif message == "PC":
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
                            # get keyboard input
                        input = "source=0"
                                
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
                elif message == "Now powering on the hub":
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
                            # get keyboard input
                        input = "poweron"
                                
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
                elif message == "Now turning off the hub":
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
                            # get keyboard input
                        input = "poweroff"
                              
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
                elif message == "Turning up brightness":
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
                            # get keyboard input
                        input = "brightness+"
                                
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
                elif message == "Turning down brightness":
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
                            # get keyboard input
                        input = "brightness-"
                                
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
        except:
                pass


