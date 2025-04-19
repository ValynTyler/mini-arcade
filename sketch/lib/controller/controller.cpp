#include <cstdint>
#include <Arduino.h>

#include "controller.h"

void Controller::init() {
  pinMode(MENU_PIN, INPUT_PULLUP);
  pinMode(MOTOR_PIN, OUTPUT);

  pinMode(DPAD_U_PIN, INPUT_PULLUP);
  pinMode(DPAD_D_PIN, INPUT_PULLUP);
  pinMode(DPAD_L_PIN, INPUT_PULLUP);
  pinMode(DPAD_R_PIN, INPUT_PULLUP);

  pinMode(JOYSTICK_X_PIN, INPUT);
  pinMode(JOYSTICK_Y_PIN, INPUT);
  pinMode(JOYSTICK_SW_PIN, INPUT_PULLUP);

  pinMode(LED_R_PIN, OUTPUT);
  pinMode(LED_G_PIN, OUTPUT);
  pinMode(LED_B_PIN, OUTPUT);
}

void Controller::poll() {
  _menu = digitalRead(MENU_PIN);

  _dpad.u = digitalRead(DPAD_U_PIN);
  _dpad.d = digitalRead(DPAD_D_PIN);
  _dpad.l = digitalRead(DPAD_L_PIN);
  _dpad.r = digitalRead(DPAD_R_PIN);

  _joystick.x = analogRead(JOYSTICK_X_PIN);
  _joystick.y = analogRead(JOYSTICK_Y_PIN);
  _joystick.sw = digitalRead(JOYSTICK_SW_PIN);
}

uint32_t Controller::serialize() {
  return 0;
}

bool Controller::menu() { return _menu; }
DPad Controller::dpad() { return _dpad; }
Joystick Controller::joystick() { return _joystick; }

bool Controller::get_motor() { return _motor; }
void Controller::set_motor(uint8_t value) {
  _motor = value;
  analogWrite(MOTOR_PIN, value);
}