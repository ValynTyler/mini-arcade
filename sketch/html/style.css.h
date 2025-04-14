#ifndef STYLE_CSS_H
#define STYLE_CSS_H

static const char *cssContent PROGMEM = R"(
:root {
  font-family: serif;
};

body {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
};
)";

#endif