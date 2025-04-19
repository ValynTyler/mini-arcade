#include "controller.h"

Controller c;

void setup() {
  Serial.begin(115200);

  c.init();
}

void loop() {
  c.poll();

  Serial.println(c.get_menu());

  if (!c.get_menu()) {
    c.set_motor(255);
  } else {
    c.set_motor(0);
  }
}
