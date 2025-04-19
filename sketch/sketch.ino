#include "dpad.h"
#include "joystick.h"

void setup() {
  Serial.begin(115200);

  pinMode(13, INPUT_PULLUP);

  DPad::init();
  Joystick::init();
}

void loop() {
  bool menu = digitalRead(13);

  DPad dpad = DPad::read();
  Joystick joystick = Joystick::read();

  Serial.print("controller: ");
  Serial.print("{ menu: ");
  Serial.print(menu);
  Serial.print(", dpad: ");
  Serial.print(dpad);
  Serial.print(", joystick: ");
  Serial.print(joystick);
  Serial.print(" }");
  Serial.println();

  delay(10);
}
