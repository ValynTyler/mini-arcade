#ifndef DPAD_H
#define DPAD_H

struct DPad {
  bool u;
  bool d;
  bool l;
  bool r;

  DPad();

  String toString() const;
  operator String() const;
};

#endif