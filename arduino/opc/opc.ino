#include "shiftRegisterToSegment.h"

int number = 0;
bool connectedToPc = false;
int width, height;



shiftToSegment segment(8, 3, 4, 2, true);

void setup() {
  Serial.begin(9600);
}

void loop() {
  /*
  if(Serial.available() > 0)
  {
    incomingByte = Serial.read();
    Serial.println(incomingByte, DEC);
  }

  if(connectedToPc)
  {
    for(int i = 0, i < width * height, i++)
    {
      Serial.println(analogRead(0));
      delay(1);
    }
  }*/

  for(int i = 0; i < 11; i++)
  {
    segment.writeToSegemnt(i);
    delay(200);
  }
}
