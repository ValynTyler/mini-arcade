FQBN = esp32:esp32:esp32
PORT = /dev/ttyUSB0
BAUD = 115200
SKETCH = sketch

default: compile upload monitor

install:
	@ arduino-cli config init
	@ arduino-cli core update-index
	@ arduino-cli core install esp32:esp32

compile:
	@ arduino-cli compile --fqbn $(FQBN) --libraries $(SKETCH)/lib $(SKETCH)

upload:
	@ arduino-cli upload -p $(PORT) --fqbn $(FQBN) $(SKETCH)

monitor:
	@ arduino-cli monitor -p $(PORT) -c baudrate=$(BAUD)
