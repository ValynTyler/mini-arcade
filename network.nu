def --env main [] {
  for key in [
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
    '#ifndef NETWORK_H'
    '#define NETWORK_H'
    ''
    $'const char* host = "($env.host)";'
    $'const uint16_t port = ($env.port);'
    ''
    '#endif'
  ] | str join "\n" | save -f sketch/network.h
}
