#include <cstdint>
#include <Arduino.h>

#include "controller.h"

void Controller::init() {
  pinMode(MENU_PIN, INPUT_PULLUP);
  pinMode(MOTOR_PIN, OUTPUT);
}

void Controller::poll() {
  _menu = digitalRead(MENU_PIN);
}

uint32_t Controller::serialize() {
  return 0;
}

bool Controller::get_menu() { return _menu; }

bool Controller::get_motor() { return _motor; }
void Controller::set_motor(uint8_t value) {
  _motor = value;
  analogWrite(MOTOR_PIN, value);
}