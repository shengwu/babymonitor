/*
 * temp.c
 *
 */
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>

#define BUFFER_SIZE 10000
#define THRESHOLD 10
#define DATA_SIZE 41


void startSignal(int pin)
{
    pinMode(pin, OUTPUT);        
    digitalWrite(pin, LOW);
    delayMicroseconds(1100); // 1.1 ms
    digitalWrite(pin, HIGH);
    delayMicroseconds(35); // range is 20-40 us
}

/*
 * readData
 *
 * reads data from <pin> into the buffer at <buffer_ptr>,
 * sampling the line every 2 us
 */
void readData(int pin, char *buffer_ptr)
{
    pinMode(pin, INPUT);
    int limit = 0;
    while (limit < BUFFER_SIZE) {
        buffer_ptr[limit] = digitalRead(pin);
        delayMicroseconds(2);
        limit++;
    }
}

void dispData(char *data_ptr, size_t len)
{
    int i = 0;
    for (; i < len; i++)
        printf("%d", data_ptr[i]);
    printf("\n");
}

size_t rawToBinary(char *buffer_ptr, char *data_ptr, const int threshold)
{
    char lastBit = buffer_ptr[0];
    int counter = 0;
    int data_length = 0;

    int i;
    for (i = 0; i < BUFFER_SIZE; i++) {
        if (buffer_ptr[i] != lastBit) {
            if (lastBit == 1) {
                if (data_length < DATA_SIZE) {
                    if (counter > threshold)
                        data_ptr[data_length] = 1;
                    else
                        data_ptr[data_length] = 0;
                }
                data_length++;
            }
            counter = 0;
            lastBit = buffer_ptr[i];
        }
        counter++;
    }

    return data_length;
}


int validData(char *data)
{
    int checksum = 0;
    int parts[4] = {0, 0, 0, 0};
    int i = 1;

    for (; i <= 32; i++) {
        parts[(i - 1) / 8] <<= 1;
        parts[(i - 1) / 8] |= data[i];
    }

    for (; i <= 40; i++) {
        checksum <<= 1;
        checksum |= data[i];
    }
    
    int check_against = parts[0] + parts[1] + parts[2] + parts[3];
    return (check_against & 0xFF) == checksum;
}


float getTemp(char *data)
{
    int temp = 0;

    int i = 2;
    for (; i <= 16; i++) {
        temp <<= 1;
        temp |= data[i];
    }

    return (float)(data[1] == 1 ? - temp : temp) / 10;
}


float getHum(char *data)
{
    int hum = 0;

    int i = 17;
    for (; i <= 32; i++) {
        hum <<= 1;
        hum |= data[i];
    }

    return (float)hum / 10;
}


int main (void)
{
    printf("Raspberry Pi Temp\n") ;

    char *buffer = malloc(BUFFER_SIZE);
    char *data = malloc(DATA_SIZE);
    size_t len;

    if (wiringPiSetup () == -1)
        return 1;

    do {
        startSignal(8);
        readData(8, buffer);
//    dispData(buffer, BUFFER_SIZE); displays 2-us sample data from buffer
        len = rawToBinary(buffer, data, THRESHOLD);
        printf("%d\n", len);
        delay(2000); // wait 2 sec before next iteration.
    } while (!(len == DATA_SIZE && validData(data)));

    dispData(data, len);

    float temp = getTemp(data);
    float hum = getHum(data);

    printf("temp: %f humidity: %f\n", temp, hum);

    free(buffer);
    free(data);

    return 0;
}
