/*
 * temp.c
 *
 */
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>


void startSignal(int pin)
{
    pinMode(pin, OUTPUT);        
    digitalWrite(pin, LOW);
    delayMicroseconds(1100); // 1.1 ms
    digitalWrite(pin, HIGH);
    delayMicroseconds(35); // range is 20-40 us
}

void readData(int pin, char *data_ptr)
{
    pinMode(pin, INPUT);
    int limit = 0;
    while (limit < 10000) {
        data_ptr[limit] = digitalRead(pin);
        delayMicroseconds(2);
        limit++;
    }
}

void dispData(char *data_ptr)
{
    int limit = 0;
    while (limit < 10000) {
        printf("%d", data_ptr[limit]);
        limit++;
    }
}


int main (void)
{
    printf ("Raspberry Pi Temp\n") ;

    char *data = malloc(10000);

    if (wiringPiSetup () == -1)
        return 1;

    startSignal(8);

    readData(8, data);

    dispData(data);

    return 0;
}
