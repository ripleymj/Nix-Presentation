<script>
    const Code = import.meta.glob('../code/Language/*.nix', { as: 'raw', eager: true })
</script>

<section style="font-size: 26pt;">
    {#each Object.values(Code) as code}
        <section data-auto-animate>
            <pre data-id="example-animation"><code data-trim class="language-nix">
{code}
        </code></pre>
        </section>
    {/each}
</section>
