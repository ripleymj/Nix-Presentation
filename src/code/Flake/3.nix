{
  description = "System configuration flake";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { nixpkgs, ... }@inputs: {
    nixosConfigurations.${host} = nixpkgs.lib.nixosSystem {
      system = "x86_64-linux";
      modules = [
        # Import your modules here
      ];
    };
  };
}