# alexaSurfaceHub

The serial_communication.py file contains the initial code used to interact with the Hub's serial interface which was done by physically inputting the commands. The lambda_function file was used to post messages into the SQS based on the intent received by the Echo. Finally, the sqs_reader.py file was used to pull the information from the SQS and send messages to the serial based on the message received. As you can see, the code from the serial_communication.py file was implemented into the code for the sqs_reader.py.
