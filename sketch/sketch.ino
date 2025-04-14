#include <Arduino.h>
#include <AsyncTCP.h>
#include <WiFi.h>

#include <ESPAsyncWebServer.h>
#include <LittleFS.h>

#include "html/index.html.h"
#include "html/bundle.min.js.h"

static AsyncWebServer server(80);

static const size_t htmlContentLength = strlen_P(htmlContent);

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
    File f = LittleFS.open("/bundle.min.js", "w");
    assert(f);
    f.print(jsContent);
    f.close();
  }

  LittleFS.mkdir("/files");

  {
    File f = LittleFS.open("/files/a.txt", "w");
    assert(f);
    f.print("Hello from a.txt");
    f.close();
  }

  {
    File f = LittleFS.open("/files/b.txt", "w");
    assert(f);
    f.print("Hello from b.txt");
    f.close();
  }

  // curl -v http://192.168.4.1/
  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request) {
    request->redirect("/index.html");
  });

  // curl -v http://192.168.4.1/index.html
  server.serveStatic("/index.html", LittleFS, "/index.html");
  server.serveStatic("/bundle.min.js", LittleFS, "/bundle.min.js");

  // Example to serve a directory content
  // curl -v http://192.168.4.1/base/ => serves a.txt
  // curl -v http://192.168.4.1/base/a.txt => serves a.txt
  // curl -v http://192.168.4.1/base/b.txt => serves b.txt
  server.serveStatic("/base", LittleFS, "/files").setDefaultFile("a.txt");

  server.begin();
}

// not needed
void loop() {
  delay(100);
}
