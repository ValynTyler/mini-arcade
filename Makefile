FQBN = esp32:esp32:esp32
PORT = /dev/ttyUSB0
BAUD = 115200
DATA = sketch/data
SKETCH = sketch

default: compile upload monitor

install:
	@ arduino-cli config init --overwrite
	@ arduino-cli core update-index
	@ arduino-cli core install esp32:esp32
	@ arduino-cli lib update-index
	@ arduino-cli lib install "ESP Async WebServer"
	@ arduino-cli lib install "Async TCP"

flash:
	@ mklittlefs -c $(DATA) -p 256 -b 4096 -s 1048576 littlefs.bin
	@ esptool.py --chip esp32 --port $(PORT) --baud 921600 write_flash -z 0x290000 littlefs.bin

compile:
	@ arduino-cli compile --fqbn $(FQBN) $(SKETCH)

upload:
	@ arduino-cli upload -p $(PORT) --fqbn $(FQBN) $(SKETCH)

monitor:
	@ arduino-cli monitor -p $(PORT) -c baudrate=$(BAUD)
