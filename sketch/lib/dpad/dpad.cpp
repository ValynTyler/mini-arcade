#include <Arduino.h>

#include "dpad.h"

DPad::DPad()
  : u(true)
  , d(true)
  , l(true)
  , r(true)
{}

String DPad::toString() const {
  return "{ up: " + String(u) + ", down: " + String(d) + ", left: " + String(l) + ", right: " + String(r) + " }";
}

DPad::operator String() const {
  return toString();
}