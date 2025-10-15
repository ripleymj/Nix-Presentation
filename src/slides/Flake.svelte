<script>
    const Code = import.meta.glob('../code/Flake/*.nix', { as: 'raw', eager: true })
</script>

<section style="font-size: 20pt;">
    {#each Object.values(Code) as code}
        <section data-auto-animate>
            <pre data-id="flake-animation"><code data-trim data-line-numbers class="language-nix">
{code}
        </code></pre>
        </section>
    {/each}
</section>
