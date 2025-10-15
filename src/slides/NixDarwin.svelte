<script lang="ts">
    import NixDarwinLogo from '/nix-darwin-logo.png'
    import UmbraScreenshot from '/umbra-screenshot.png'
</script>

<section>
    <section>
        <div id="intro">
            <div style="text-align: left;">
                <h3>Nix Darwin</h3>
                <p class="description">
                    Nix Darwin allows you to use Nix's declarative system to manage your MacOS.
                    Built around nixpkgs, similar to NixOS.
                </p>
            </div>
            <img src={NixDarwinLogo} alt="nix-darwin-logo" />
        </div>
    </section>
    <section>
        <img src={UmbraScreenshot} alt="umbra-screenshot" />
    </section>
</section>

<style>
    #intro {
        display: grid;
        grid-template-rows: 1fr;
        grid-template-columns: 2fr 1fr;
        gap: 40px;
    }
    .description {
        color: #aaaaaa;
        font-size: 24pt;
    }
</style>
