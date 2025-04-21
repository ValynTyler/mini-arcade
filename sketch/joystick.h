#ifndef JOYSTICK_H
#define JOYSTICK_H

struct Joystick {
  static const uint8_t PIN_X = 35;
  static const uint8_t PIN_Y = 34;
  static const uint8_t PIN_SW = 27;

  uint16_t x;
  uint16_t y;
  bool sw;

  Joystick()
    : x(2048)
    , y(2048)
    , sw(true)
  {}

  Joystick(
    uint16_t x,
    uint16_t y,
    bool sw
  )
    : x(x)
    , y(y)
    , sw(sw)
  {}

  static void init() {
    pinMode(PIN_X, INPUT);
    pinMode(PIN_Y, INPUT);
    pinMode(PIN_SW, INPUT_PULLUP);
  }

  static Joystick read() {
    return Joystick(
      analogRead(PIN_X),
      analogRead(PIN_Y),
      digitalRead(PIN_SW)
    );
  }

  operator String() const {
    return toString();
  }

  String toString() const {
    return ""
      + String("{ x: ")
      + String(x)
      + String(", y: ")
      + String(y)
      + String(", sw: ")
      + String(sw)
      + String(" }")
    ;
  }
};

#endif
