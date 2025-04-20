def --env main [] {
  for key in [
    ssid
    password
    host
    port
  ] {
    if not ($key in $env) {
      let value = input $"($key): "
      $"($key)=($value)\n" | save -a .env
      load-env { $key: $value }
    }
  }

  [
    '#ifndef SECRETS_H'
    '#define SECRETS_H'
    ''
    '// WiFi'
    $'const char* ssid = "($env.ssid)";'
    $'const char* password = "($env.password)";'
    ''
    '// WS'
    $'const char* host = "($env.host)";'
    $'const uint16_t port = ($env.port);'
    ''
    '#endif'
  ] | str join "\n" | save -f sketch/secrets.h
}
