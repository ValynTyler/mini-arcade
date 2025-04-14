def main [] {
  print "Sourcing content headers..."

  let source = "./source" | path expand
  let target = "./sketch/html" | path expand

  mkdir $target

  ls $source | each {|file|
    let name = $file.name | path basename
    let path = [ $target $"($name).h" ] | path join

    let text = [
      $'#ifndef ($file.name | path basename | str replace -a '.' '_' | str upcase)_H'
      $'#define ($file.name | path basename | str replace -a '.' '_' | str upcase)_H'
      ''
      $"static const char *($file.name | path parse | get extension)Content PROGMEM = R\"\("
      $'(open $file.name)'
      ')";'
      ''
      '#endif'
    ] | str join "\n"

    print $"Writing to ($path)"
    $text | save -f $path
  }

  null
}