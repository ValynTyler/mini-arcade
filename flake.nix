{
  description = "A simple template for quickly creating websites";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";

    flake-utils.url = "github:numtide/flake-utils";

    mklittlefs.url = "github:valyntyler/mklittlefs";
    mklittlefs.inputs.nixpkgs.follows = "nixpkgs";
  };

  outputs = { nixpkgs, flake-utils, ... }@inputs:
    flake-utils.lib.eachDefaultSystem (system:
      let pkgs = nixpkgs.legacyPackages.${system}; in {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            inputs.mklittlefs.packages.x86_64-linux.default
            arduino-cli
            esptool
            python3
          ];
        };
      }
    );
}
