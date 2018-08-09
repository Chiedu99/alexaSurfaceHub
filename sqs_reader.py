import boto3
import os
import time
import serial

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
while (time.time() - time_start < 60000000000000):
        print("Checking...")
        try:
                message = pop_message(client, queue_url)
                print(message)
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
                                # Python 3 users
                                # input = input(">> ")
                        if input == 'exit':
                            ser.close()
                            exit()
                        else:
                                # send the character to the device
                                # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
                            ser.write(input + '\r\n')
                            out = ''
                                # let's wait one second before reading output (let's give device time to answer)
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
                                # Python 3 users
                                # input = input(">> ")
                        if input == 'exit':
                            ser.close()
                            exit()
                        else:
                                # send the character to the device
                                # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
                            ser.write(input + '\r\n')
                            out = ''
                                # let's wait one second before reading output (let's give device time to answer)
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
                                # Python 3 users
                                # input = input(">> ")
                        if input == 'exit':
                            ser.close()
                            exit()
                        else:
                                # send the character to the device
                                # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
                            ser.write(input + '\r\n')
                            out = ''
                                # let's wait one second before reading output (let's give device time to answer)
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
                                # Python 3 users
                                # input = input(">> ")
                        if input == 'exit':
                            ser.close()
                            exit()
                        else:
                                # send the character to the device
                                # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
                            ser.write(input + '\r\n')
                            out = ''
                                # let's wait one second before reading output (let's give device time to answer)
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
                                # Python 3 users
                                # input = input(">> ")
                        if input == 'exit':
                            ser.close()
                            exit()
                        else:
                                # send the character to the device
                                # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
                            ser.write(input + '\r\n')
                            out = ''
                                # let's wait one second before reading output (let's give device time to answer)
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
                                # Python 3 users
                                # input = input(">> ")
                        if input == 'exit':
                            ser.close()
                            exit()
                        else:
                                # send the character to the device
                                # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
                            ser.write(input + '\r\n')
                            out = ''
                                # let's wait one second before reading output (let's give device time to answer)
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
                                # Python 3 users
                                # input = input(">> ")
                        if input == 'exit':
                            ser.close()
                            exit()
                        else:
                                # send the character to the device
                                # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
                            ser.write(input + '\r\n')
                            out = ''
                                # let's wait one second before reading output (let's give device time to answer)
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
                                # Python 3 users
                                # input = input(">> ")
                        if input == 'exit':
                            ser.close()
                            exit()
                        else:
                                # send the character to the device
                                # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
                            ser.write(input + '\r\n')
                            out = ''
                                # let's wait one second before reading output (let's give device time to answer)
                            time.sleep(1)
                            while ser.inWaiting() > 0:
                                out += ser.read(1)

                            if out != '':
                                print ">>" + out
        except:
                pass


