{
  pkgs,
  config,
  ...
}:
{
  users.users.ripley = {
    isNormalUser = true;
    uid = 1000;
    description = "Benevolent dictator for life";
    extraGroups = [
      "networkmanager"
      "uug"
    ];
    hashedPasswordFile = config.age.secrets.ripley-password;
    shell = pkgs.zsh;
  };
}