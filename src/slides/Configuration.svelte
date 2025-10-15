<script lang="ts">
    import NixLogo from '/nix.svg'
    import ModularConfig from '/modular-config.png'

    const Code = import.meta.glob('../code/Configuration/*.nix', { as: 'raw', eager: true })
</script>

<section>
    <section>
        <div id="generate-config">
            <div>
                <pre><code data-trim class="language-shell">
nixos-generate-config
        </code></pre>
            </div>
            <div id="initial-files">
                <div class="file-line">
                    <span>configuration.nix</span>
                    <img src={NixLogo} alt="nix-logo" />
                </div>
                <div class="file-line">
                    <span>hardware-configuration.nix</span>
                    <img src={NixLogo} alt="nix-logo" />
                </div>
            </div>
        </div>
    </section>
    <section data-auto-animate>
        <pre data-id="flake-animation"><code
                data-trim
                data-line-numbers="4-7|9-10|12-14|20-23|25-31|33-38"
                class="language-nix">
{Object.values(Code)[0]}
    </code></pre>
    </section>
    <section>
        <div>
            <img id="modular-config" src={ModularConfig} alt="modular-config" />
        </div>
    </section>
</section>

<style>
    #generate-config {
        display: grid;
        grid-template-rows: 1fr;
        grid-template-columns: 2fr 3fr;
    }
    #initial-files {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: end;
        gap: 2rem;
        font-size: 24pt;
    }
    .file-line {
        display: flex;
        align-items: center;
        gap: 1rem;
        height: 4rem;
    }
    #modular-config {
        height: 40rem;
    }
</style>
