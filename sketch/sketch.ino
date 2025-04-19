#include "controller.h"

Controller c;

void setup() {
  Serial.begin(115200);
}

void loop() {
  Serial.println(c.serialize());
}
