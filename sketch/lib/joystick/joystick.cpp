#include <Arduino.h>

#include "joystick.h"

Joystick::Joystick()
  : x(2048)
  , y(2048)
  , sw(true)
{}

String Joystick::toString() const {
  return "{ x: " + String(x) + ", y: " + String(y) + ", sw: " + String(sw) + " }";
}

Joystick::operator String() const {
  return toString();
}