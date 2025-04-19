#include "controller.h"

Controller c;

void setup() {
  Serial.begin(115200);

  c.init();
}

void loop() {
  c.poll();

  Serial.print("controller: { dpad: ");
  Serial.print(c.dpad());
  Serial.print(", joystick: ");
  Serial.print(c.joystick());
  Serial.println(" }");

  if (c.menu()) {
    c.set_motor(0);
  } else {
    c.set_motor(255);
  }

  delay(10);
}
