import serial
from comands_at import COMANDS_AT_GENERALS, COMANDS_AT_MQTT
from time import sleep
from dotenv import load_dotenv

load_dotenv()

PORT = 'COM9'
BAUD = 115200


def connection():
    return serial.Serial(port=PORT, baudrate=BAUD, bytesize=8, parity='N', stopbits=1, timeout=1, xonxoff=False, rtscts=False, dsrdtr=False)

def main():
    serial_connection = connection()
    for i in range(len(COMANDS_AT_GENERALS)):
        sleep(1)
        serial_connection.write((COMANDS_AT_GENERALS[i]+"\r").encode())
        msg=serial_connection.read(128)
        print(msg.decode())
    # for i in range(len(COMANDS_AT_MQTT)):
    #     sleep(1)
    #     serial_connection.write((COMANDS_AT_MQTT[i]+"\r").encode())
    #     msg=serial_connection.read(128)
    #     print(msg.decode())

main()