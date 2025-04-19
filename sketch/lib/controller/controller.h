#ifndef CONTROLLER_H
#define CONTROLLER_H

#include "dpad.h"
#include "joystick.h"

class Controller {
private:
  bool _menu = true;
  uint8_t _motor = 0;

  DPad _dpad;
  Joystick _joystick;

public:
  static const uint8_t MENU_PIN = 13;
  static const uint8_t MOTOR_PIN = 12;

  static const uint8_t DPAD_U_PIN = 32;
  static const uint8_t DPAD_D_PIN = 33;
  static const uint8_t DPAD_L_PIN = 25;
  static const uint8_t DPAD_R_PIN = 26;

  static const uint8_t JOYSTICK_X_PIN = 34;
  static const uint8_t JOYSTICK_Y_PIN = 35;
  static const uint8_t JOYSTICK_SW_PIN = 27;

  static const uint8_t LED_R_PIN = 23;
  static const uint8_t LED_G_PIN = 22;
  static const uint8_t LED_B_PIN = 21;

  void init();
  void poll();
  uint32_t serialize();

  bool menu();
  DPad dpad();
  Joystick joystick();

  bool get_motor();
  void set_motor(uint8_t value);
};

#endif