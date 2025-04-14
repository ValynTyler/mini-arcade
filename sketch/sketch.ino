#include <Arduino.h>
#include <AsyncTCP.h>
#include <WiFi.h>

#include <ESPAsyncWebServer.h>
#include <LittleFS.h>

#include "html/index.html.h"
#include "html/script.js.h"
#include "html/style.css.h"

static AsyncWebServer server(80);

void setup() {
  Serial.begin(115200);

#ifndef CONFIG_IDF_TARGET_ESP32H2
  WiFi.mode(WIFI_AP);
  WiFi.softAP("esp-captive");
#endif

  LittleFS.begin(true);

  {
    File f = LittleFS.open("/index.html", "w");
    assert(f);
    f.print(htmlContent);
    f.close();
  }

  {
    File f = LittleFS.open("/script.js", "w");
    assert(f);
    f.print(jsContent);
    f.close();
  }

  {
    File f = LittleFS.open("/style.css", "w");
    assert(f);
    f.print(cssContent);
    f.close();
  }

  // curl -v http://192.168.4.1/
  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request) {
    request->redirect("/index.html");
  });

  // curl -v http://192.168.4.1/index.html
  server.serveStatic("/index.html", LittleFS, "/index.html");
  server.serveStatic("/script.js", LittleFS, "/script.js");
  server.serveStatic("/style.css", LittleFS, "/style.css");

  server.begin();
}

// not needed
void loop() {
  delay(100);
}
