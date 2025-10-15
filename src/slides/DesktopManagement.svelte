<script lang="ts">
    import NixLogo from '/nix.svg'
    import Plasma from '/kde-desktop.png'
    import PlasmaManager from '/plasma-manager.png'
    import Hyprland from '/hyprland.png'
    import HyprlandWiki from '/hyprland-wiki.png'
</script>

<section>
    <section>
        <div id="desktop-management">
            <div style="text-align: left;">
                <strong>Desktop Management</strong>
                <p class="description">
                    Configure everything about your desktop environment in a deterministic,
                    reproducible way using Nix.
                </p>
            </div>
            <img src={NixLogo} alt="nix-logo" />
        </div>
    </section>
    <section>
        <div id="plasma">
            <div>
                <img src={Plasma} alt="plasma" />
                <strong>KDE Plasma</strong>
            </div>
            <span>+</span>
            <div>
                <img src={PlasmaManager} alt="plasma-manager" />
                <strong>Plasma Manager</strong>
            </div>
        </div>
    </section>
    <section>
        <div id="hyprland">
            <div>
                <img src={Hyprland} alt="hyprland" />
                <strong>Hyprland</strong>
            </div>
            <span>+</span>
            <div>
                <img src={HyprlandWiki} alt="hyprland-wiki" />
                <strong>Home Manager Module</strong>
            </div>
        </div>
    </section>
</section>

<style>
    #desktop-management {
        display: grid;
        grid-template-rows: 1fr;
        grid-template-columns: 2fr 1fr;
        align-items: center;
        gap: 40px;
    }

    #plasma,
    #hyprland {
        display: grid;
        grid-template-columns: 1fr min-content 1fr;
        grid-template-rows: 1fr;
        gap: 40px;
        align-items: center;
    }

    .description {
        color: #aaaaaa;
        font-size: 24pt;
    }
</style>
