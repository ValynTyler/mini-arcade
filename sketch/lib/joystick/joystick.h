#ifndef JOYSTICK_H
#define JOYSTICK_H

struct Joystick {
  uint16_t x;
  uint16_t y;
  bool sw;

  Joystick();

  String toString() const;
  operator String() const;
};

#endif