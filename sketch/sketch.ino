#include <WiFi.h>

#include "secrets.h"

void setup() {
  Serial.begin(115200);
  delay(3000);

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
}

void loop() {
}
