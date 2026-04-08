
# Documentation: https://devenv.sh/

{ pkgs, lib, config, inputs, ... }:

{
  packages = with pkgs; [ stdenv.cc.cc zlib git pandoc ];

  cachix.enable = true;
  cachix.pull = [ "nixpkgs-python" ];

  languages.python = {
    enable = true;
    version = "3.14";
    venv.enable = true;
    uv = {
      enable = true;
      sync = {
        enable = true;
        allGroups = true;
        allExtras = true;
      };
    };
  };
}
