void setup() {
  Serial.begin(9600);
  //pinMode(8, OUTPUT);
}

int number = 0;

void loop() {
  Serial.println(analogRead(0));

  delay(250);
}
