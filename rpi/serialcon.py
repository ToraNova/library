#!/usr/bin/python3
# PySerial library that allows easy usage of the serial obj
import serial
import time,sys

if __name__ == "__main__":

    dev = '/dev/ttyS0'
    bdr = 57600

    scon = serial.Serial(
        port=dev,
        baudrate = bdr,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        bytesize = serial.EIGHTBITS,
        timeout = 3
    )

    if(len(sys.argv) < 2):
        print("Please specify mode")
        exit()

    run_mode = sys.argv[1]
    print("Running serialcon on mode",run_mode)

    if(run_mode == "loop"):
        while True:
            uinput = input("Input ({},{})".format(dev,bdr))
            binput = uinput.encode('utf-8')
            scon.write(binput)
            print("Sent [{}]".format(binput))
            time.sleep(0.2)
            if(scon.in_waiting > 0):
                print("Bytes received.")
                print(scon.read(scon.in_waiting))

    elif(run_mode == "listen"):
        while True:
            crd = scon.in_waiting
            if(crd > 0):
                ctr = 0
                while True:
                    time.sleep(0.1)
                    if(scon.in_waiting == crd or ctr > 30):
                        break
                    else:
                        crd = scon.in_waiting
                        ctr += 1
                crd = scon.in_waiting
                print(scon.read(crd))
            else:
                time.sleep(0.1)

    elif(run_mode == "test"):
        if(len(sys.argv) < 3):
            write_tar = b'AA4FF01234ZZ'
        else:
            write_tar = sys.argv[2].encode('utf-8')
        print(write_tar)
        scon.write(write_tar)
        time.sleep(0.5)
        print(scon.in_waiting)
        print(scon.read(scon.in_waiting))

    else:
        print("Undefined mode.")

# SAMPLE USAGE
# com = serial.Serial(
#         port='/dev/ttyUSB0',
#         baudrate = 57600,
#         parity = serial.PARITY_ODD,
#         stopbits = serial.STOPBITS_TWO,
#         bytesize = serial.EIGHTBITS,
#         timeout = a_time
# )
