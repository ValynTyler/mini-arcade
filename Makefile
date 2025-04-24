FQBN = esp32:esp32:esp32
PORT = /dev/ttyUSB0
BAUD = 115200
SKETCH = sketch

default: compile upload monitor

install:
	@ arduino-cli config init --overwrite
	@ arduino-cli core update-index
	@ arduino-cli core install esp32:esp32
	@ arduino-cli lib update-index
	@ arduino-cli lib install "WebSockets"

compile:
	@ nu network.nu
	@ nu secrets.nu
	@ arduino-cli compile --fqbn $(FQBN) $(SKETCH)

upload:
	@ arduino-cli upload -p $(PORT) --fqbn $(FQBN) $(SKETCH)

monitor:
	@ arduino-cli monitor -p $(PORT) -c baudrate=$(BAUD)
