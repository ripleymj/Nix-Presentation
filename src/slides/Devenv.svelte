<script lang="ts">
    import Devenv from '/devenv.webp'

    const Code = import.meta.glob('../code/devenv/*.nix', { as: 'raw', eager: true })
</script>

<section>
    <section>
        <div id="devenv">
            <div style="text-align: left;">
                <strong>devenv</strong>
                <p class="description">
                    devenv enables declarative & reproducible developer environments using the nix
                    language. Declare all the programming languages, packages, scrips, environments
                    variables, etc. that your project relies on.
                </p>
            </div>
            <img src={Devenv} alt="devenv" />
        </div>
    </section>
    <section>
        <div id="slides-env">
            <div style="text-align: left;">
                <strong>The env for these slides</strong>
                <ul class="description">
                    <li>Python virtual environment with exact requiremnts</li>
                    <li>Typesciprt & Javascript support</li>
                    <li>Automatic JS runtime setup and dependecy installation with bun</li>
                </ul>
            </div>
            <div style="font-size: 13pt;">
                <pre><code data-trim data-line-numbers class="language-nix">
{Object.values(Code)[0]}
                </code></pre>
            </div>
        </div>
    </section>
</section>

<style>
    #devenv,
    #slides-env {
        display: grid;
        grid-template-rows: 1fr;
        grid-template-columns: 2fr 1fr;
        align-items: center;
        gap: 40px;
    }

    .description {
        color: #aaaaaa;
        font-size: 24pt;
    }
</style>
