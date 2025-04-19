#ifndef CONTROLLER_H
#define CONTROLLER_H

class Controller {
private:
  bool _menu = true;
  uint8_t _motor = 0;

public:
  static const uint8_t MENU_PIN = 13;
  static const uint8_t MOTOR_PIN = 12;

  void init();
  void poll();
  uint32_t serialize();

  bool get_menu();
  bool get_motor();
  void set_motor(uint8_t value);
};

#endif