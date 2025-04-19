#ifndef CONTROLLER_h
#define CONTROLLER_H

#include "dpad.h"
#include "joystick.h"

struct Controller {
  static const uint8_t PIN_MENU = 13;

  bool menu;
  DPad dpad;
  Joystick joystick;

  Controller()
    : menu(true)
    , dpad(DPad())
    , joystick(Joystick())
  {}

  Controller(bool menu, DPad dpad, Joystick joystick)
    : menu(menu)
    , dpad(dpad)
    , joystick(joystick)
  {}

  static void init() {
    pinMode(PIN_MENU, INPUT_PULLUP);

    DPad::init();
    Joystick::init();
  }

  static Controller read() {
    return Controller(
      digitalRead(PIN_MENU),
      DPad::read(),
      Joystick::read()
    );
  }

  operator String() const {
    return toString();
  }

  String toString() const {
    return ""
      + String("controller: ")
      + String("{ menu: ")
      + String(menu)
      + String(", dpad: ")
      + String(dpad)
      + String(", joystick: ")
      + String(joystick)
      + String(" }")
      + String()
    ;
  }

  uint32_t serialize() {
    return 0x0000'0000
      | (0b11         << 30)
      | (joystick.sw  << 29)
      | (menu         << 28)
      | (joystick.x   << 16)
      | (dpad.up      << 15)
      | (dpad.down    << 14)
      | (dpad.left    << 13)
      | (dpad.right   << 12)
      | (joystick.y)
    ;
  }
};

#endif
