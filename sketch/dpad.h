#ifndef DPAD_H
#define DPAD_H

struct DPad {
  static const uint8_t PIN_UP = 32;
  static const uint8_t PIN_DOWN = 33;
  static const uint8_t PIN_LEFT = 25;
  static const uint8_t PIN_RIGHT = 26;

  bool up;
  bool down;
  bool left;
  bool right;

  DPad()
    : up(true)
    , down(true)
    , left(true)
    , right(true)
  {}

  DPad(
    bool up,
    bool down,
    bool left,
    bool right
  )
    : up(up)
    , down(down)
    , left(left)
    , right(right)
  {}

  static void init() {
    pinMode(PIN_UP, INPUT_PULLUP);
    pinMode(PIN_DOWN, INPUT_PULLUP);
    pinMode(PIN_LEFT, INPUT_PULLUP);
    pinMode(PIN_RIGHT, INPUT_PULLUP);
  }

  static DPad read() {
    return DPad(
      digitalRead(PIN_UP),
      digitalRead(PIN_DOWN),
      digitalRead(PIN_LEFT),
      digitalRead(PIN_RIGHT)
    );
  }

  operator String() const {
    return toString();
  }

  String toString() const {
    return ""
      + String("{ up: ")
      + String(up)
      + String(", down: ")
      + String(down)
      + String(", left: ")
      + String(left)
      + String(", right: ")
      + String(right)
      + String(" }")
    ;
  }
};

#endif
