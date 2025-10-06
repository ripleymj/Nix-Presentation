{
  pkgs,
  ...
}:

{
  # https://devenv.sh/packages/
  packages = [ pkgs.git ];

  # https://devenv.sh/languages/
  languages = {
    python = {
      enable = true;
      venv = {
        enable = true;
        requirements = ''
          beautifulsoup4==4.14.2
          soupsieve==2.8
          typing_extensions==4.15.0
        '';
      };
    };
    javascript = {
      enable = true;
      bun = {
        enable = true;
        install.enable = true;
      };
    };
    typescript.enable = true;
  };

  # See full reference at https://devenv.sh/reference/options/
}
