/*
 * temp.c
 *
 */
#include <assert.h>
#include <stdio.h>
#include <wiringPi.h>

void startSignal(int pin)
{
    pinMode(pin, OUTPUT);        
    digitalWrite(pin, LOW);
    delay(10); // 10 ms
    digitalWrite(pin, HIGH);
    delayMicroseconds(30); // range is 20-40 us

    pinMode(pin, INPUT);

    int limit = 0;
    
    // some waiting for RHT03 to pull line low (possibly unnecessary)
    while(digitalRead(pin) == HIGH) {
        delayMicroseconds(2);
        printf("loop 1");
    }
    while(digitalRead(pin) == LOW) {
        delayMicroseconds(2);
        printf("loop 2");
    }
    // currently, we never get here :(
    while(digitalRead(pin) == HIGH) {
        delayMicroseconds(2);
        printf("loop 3");
    }

    // test function 
    while(limit < 1000) {
        printf("%d", digitalRead(pin));
        limit++;
    }
}

int main (void)
{
    printf ("Raspberry Pi Temp\n") ;

    if (wiringPiSetup () == -1)
        return 1;

    startSignal(3);

    return 0;
}
