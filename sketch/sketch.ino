#include "controller.h"

void setup() {
  Serial.begin(115200);

  Controller::init();
}

void loop() {
  Controller c = Controller::read();

  Serial.println(String(c.serialize(), BIN));

  delay(10);
}
