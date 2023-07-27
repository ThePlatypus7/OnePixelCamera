#ifndef SHIFTREGISTER_TO_SEGMENT_H
#define SHIFTREGISTER_TO_SEGMENT_H

#include "Arduino.h"

class shiftToSegment
{
  public:
    shiftToSegment(int clk, int clr, int writ, int store, bool segmentTest);
    void testSegment();
    void clrSegment();
    void writeToSegemnt(int number);
    void setupPins();
    
  private:
    int shiftClk, shiftClr, shiftWrite, shiftStore;
    int intToSegment[11][8] = {{1,1,1,1,1,1,0,0},{0,1,1,0,0,0,0,0},{1,1,0,1,1,0,1,0},{1,1,1,1,0,0,1,0},{0,1,1,0,0,1,1,0}
                            ,{1,0,1,1,0,1,1,0},{1,0,1,1,1,1,1,0},{1,1,1,0,0,0,0,0},{1,1,1,1,1,1,1,0},{1,1,1,1,0,1,1,0},{0,0,0,0,0,0,0,1}};
};

#endif
