#!/usr/bin/python
import RPIO as GPIO
import time


def init(pin):
	GPIO.setup(pin, GPIO.OUT);
	GPIO.output(pin, GPIO.LOW);
	time.sleep(0.002);
	GPIO.output(pin, GPIO.HIGH);
	time.sleep(0.000030);
	GPIO.setup(pin, GPIO.IN);
	time.sleep(0.000020);
	assert GPIO.input(pin) == True, "Sensor did not pull line low after host start signal";
	time.sleep(0.000080);
	assert GPIO.input(pin) == False, "Sensor did not pull line high after host start signal";
	time.sleep(0.000060);
	return;


def receiveBit(pin):
	GPIO.setup(pin, GPIO.IN);
	assert GPIO.input(pin) == False, "Sensor did not pull line low before bit transmission";
	
	time.sleep(0.000077);

	if GPIO.input(pin):
		time.sleep(0.000041);
		return "1";
	else:
		return "0";
	

def getData(pin):
    dataStr = "";
    init(pin);
    time.sleep(0.000025);

    for i in range(40):
        dataStr += receiveBit(pin);

    # check checksum

    checksum = int(dataStr[32:], 2);
    check_against = int(dataStr[:8], 2) + \
                    int(dataStr[8:16], 2) + \
                    int(dataStr[16:24], 2) + \
                    int(dataStr[24:32], 2);

    check_against &= 0xff;

    error_str = "Checksum error: " + checksum + " != " + \
            check_against + " ; Data = " + dataStr;
    assert checksum == check_against, error_str;

    return dataStr;


def extractTemp(dataStr):
    temp_part = dataStr[17:32];
    temp = int(temp_part, 2) / 10;
    if dataStr[16] == "1":
        temp *= -1;
    return temp;


def extractRH(dataStr):
    rh_part = dataStr[:16];
    return int(rh_part, 2) / 10;

GPIO.setmode(GPIO.BOARD);

data = getData(3);
print(extractTemp(data));
print(extractRH(data));

GPIO.cleanup();
