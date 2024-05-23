import random
import time

import serial
import struct

bdr = 115200
port = serial.Serial('/dev/ttyTHS1', bdr)

labels = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]


def send_list_data(label):
    data = [1, label[0], label[1], label[2], 1]
    data = bytearray(data)

    print('send:', data)
    port.write(data)


def send_pack_data(label):
    data = struct.pack("<bbbbb", 1, label[0], label[1], label[2], 1)
    port.write(data)


def serial_send_run(length, result_classid, result_scores):
    default = bytearray([0, 0, 0, 0, 0])

    try:
        while True:
            if port.inWaiting() > 0:
                receive = port.read()
                print('receive:', receive)
            max_score = 0
            index = 8

            if length != 0:
                for i in range(length):
                    max_score = max(max_score, float(result_scores[i]))
                    if max_score == float(result_scores[i]):
                        index = int(result_classid[i])
            if index >= 8:
                port.write(default)
            else:
                send_list_data(labels[index])
    except KeyboardInterrupt:
        print('Exiting Program')


if __name__ == '__main__':
    serial_send_run()
