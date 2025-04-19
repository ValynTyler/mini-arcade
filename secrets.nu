def --env main [] {

  for key in [ ssid password ] {
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
    $'const char* ssid = "($env.ssid)";'
    $'const char* password = "($env.password)";'
    ''
    '#endif'
  ] | str join "\n" | save -f sketch/secrets.h
}
