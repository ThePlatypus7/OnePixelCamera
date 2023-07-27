#include "Arduino.h"
#include "shiftRegisterToSegment.h"

shiftToSegment::shiftToSegment(int clk, int clr, int writ, int store, bool segmentTest)
{
  shiftClk = clk;
  shiftClr = clr;
  shiftWrite = writ;
  shiftStore = store;
  
  setupPins();

  digitalWrite(shiftClr  , LOW);
  delay(1);
  digitalWrite(shiftClr  , HIGH);
  digitalWrite(shiftClk  , LOW);
  digitalWrite(shiftWrite, LOW);
  digitalWrite(shiftStore, LOW);
  if(segmentTest)
  {
    testSegment();
  }
}

void shiftToSegment::setupPins()
{
  pinMode(shiftClk, OUTPUT);
  pinMode(shiftClr, OUTPUT);
  pinMode(shiftWrite, OUTPUT);
  pinMode(shiftStore, OUTPUT);
}

void shiftToSegment::testSegment()
{
  digitalWrite(shiftWrite, HIGH);
  digitalWrite(shiftClk, HIGH);
  digitalWrite(shiftClk, LOW);
  digitalWrite(shiftStore, HIGH);
  digitalWrite(shiftStore, LOW);
  digitalWrite(shiftWrite, LOW);
  for(int i = 0; i < 8; i++)
  {
    digitalWrite(shiftClk, HIGH);
    delay(100);
    digitalWrite(shiftClk, LOW);
    digitalWrite(shiftStore, HIGH);
    digitalWrite(shiftStore, LOW);
  }
  clrSegment();
}

void shiftToSegment::clrSegment()
{
 digitalWrite(shiftClr, LOW);
 delay(1);
 digitalWrite(shiftClr, HIGH);
 digitalWrite(shiftStore, HIGH); 
 delay(1);
 digitalWrite(shiftStore, LOW);
}

void shiftToSegment::writeToSegemnt(int number)
{
  clrSegment();
  for(int i = 7; i >= 0; i--)
  {
    digitalWrite(shiftWrite, intToSegment[number][i]);
    digitalWrite(shiftClk, HIGH);
    digitalWrite(shiftClk, LOW);
  }
  digitalWrite(shiftStore, HIGH);
  digitalWrite(shiftStore, LOW);
}
