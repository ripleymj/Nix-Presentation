<section>
    <section>
        <div style="text-align: left;">
            <strong>Rebuilding the System</strong>
            <p class="description">
                To apply new configuration changes, run the <code
                    style="font-size: 20pt !important;">nixos-rebuild</code
                > command. This evalutates your nix configuration, downloads any packages necessary,
                and build the result.
            </p>
        </div>
    </section>
    <section>
        <div id="wrapper">
            <pre><code data-trim class="language-shell">
    nixos-rebuild switch
                </code></pre>
            <span>Activate new generation and make it default boot option</span>
            <pre><code data-trim class="language-shell">
    nixos-rebuild boot
                </code></pre>
            <span>Make new generation default boot option, don't activate until reboot</span>
            <pre><code data-trim class="language-shell">
    nixos-rebuild test
                </code></pre>
            <span>Activate new generation but don't make a boot option</span>
            <pre><code data-trim class="language-shell">
    nixos-rebuild build
                </code></pre>
            <span>Create a symlink called result pointing to the new generation</span>
            <pre><code data-trim class="language-shell">
    nixos-rebuild dry-acitvate
                </code></pre>
            <span>Don't actiave new changes, show the changes that would have been applied</span>
            <pre><code data-trim class="language-shell">
    nixos-rebuild build-vm
                </code></pre>
            <span>Create a QEMU VM of the resulting generation</span>
        </div>
    </section>
</section>

<style>
    #wrapper {
        display: grid;
        grid-template-columns: 1fr 1fr;
        grid-template-rows: repeat(1fr, 6);
        text-align: left;
        align-items: center;
    }
    #wrapper span {
        font-size: 18pt;
    }
    .description {
        color: #aaaaaa;
        font-size: 24pt;
    }
</style>
