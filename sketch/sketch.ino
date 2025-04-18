#include <Arduino.h>
#include <AsyncTCP.h>
#include <WiFi.h>

#include <ESPAsyncWebServer.h>
#include <LittleFS.h>

static AsyncWebServer server(80);

void setup() {
  Serial.begin(115200);

#ifndef CONFIG_IDF_TARGET_ESP32H2
  WiFi.mode(WIFI_AP);
  WiFi.softAP("esp-captive");
#endif

  LittleFS.begin(false); // don't format

  // curl -v http://192.168.4.1/index.html
  server.serveStatic("/", LittleFS, "/").setDefaultFile("index.html");

  server.begin();
}

// not needed
void loop() {
  delay(100);
}
