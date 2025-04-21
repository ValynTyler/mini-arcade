#include <WiFi.h>
#include <WebSocketsClient.h>

#include "controller.h"
#include "secrets.h"

WebSocketsClient client;

unsigned long send_interval_ms = 10;
unsigned long time_ms = 0;
unsigned long last_ms = 0;

void setup() {
  Serial.begin(115200);
  Serial.setDebugOutput(true);

  delay_boot();

  init_wifi();
  init_ws();

  Controller::init();
}

void loop() {
  client.loop();
  Controller c = Controller::read();

  time_ms = millis();
  if (time_ms - last_ms > send_interval_ms) {
    last_ms = time_ms;

    uint32_t c_state = c.serialize();
    client.sendBIN((uint8_t *)&c_state, sizeof(c_state));
  }
}

void delay_boot() {
  for(uint8_t t = 4; t > 0; t--) {
		Serial.printf("Booting in %d...\n", t);
		Serial.flush();
		delay(1000);
	}
  Serial.println();
}

void init_wifi() {
  WiFi.begin(ssid, password);
  Serial.print("Connecting to ");
  Serial.print(ssid);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print('.');
    delay(100);
  }
  Serial.println();
  Serial.println("Successfully connected to WiFi!");
  Serial.print("Device IP address: ");
  Serial.print(WiFi.localIP());
  Serial.println();
  Serial.println();
}

void init_ws() {
  Serial.print("Connecting to WS server at ");
  Serial.print(host);
  Serial.print(":");
  Serial.print(port);
  Serial.println();
  client.begin(host, port, "/");
  client.setReconnectInterval(5000);
  client.onEvent(ws_event);
}

void ws_event(WStype_t type, uint8_t * payload, size_t length) {
  switch(type) {
    case WStype_CONNECTED:
      Serial.println("[WS] Connected to server!");
      break;
    case WStype_DISCONNECTED:
      Serial.println("[WS] Disconnected.");
      break;
    case WStype_TEXT:
      Serial.printf("[WS] Received text: %s\n", payload);
      break;
    case WStype_ERROR:
      Serial.println("[WS] An error occurred.");
    default:
      break;
  }
}
