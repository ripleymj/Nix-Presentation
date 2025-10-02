{
  pkgs,
  ...
}:

{
  # https://devenv.sh/packages/
  packages = [ pkgs.git ];

  # https://devenv.sh/languages/
  languages = {
    javascript = {
      enable = true;
      npm = {
        enable = true;
        install.enable = true;
      };
    };
    typescript.enable = true;
  };

  # See full reference at https://devenv.sh/reference/options/
}
