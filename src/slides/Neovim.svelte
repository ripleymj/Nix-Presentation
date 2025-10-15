<script lang="ts">
    import NVF from '/nvf.svg'
</script>

<section>
    <div id="intro">
        <div style="text-align: left;">
            <strong>Neovim</strong>
            <p class="description">
                Projects like Nixvim, NVF, and nixCats allow you to integrate your neovim
                configuration into your Nix config. With Nixvim and NVF write your entire neovim
                config using nix, or use nixCats if you want to stick with lua.
            </p>
        </div>
        <img src={NVF} alt="nvf-log" />
    </div>
</section>

<style>
    #intro {
        display: grid;
        grid-template-rows: 1fr;
        grid-template-columns: 2fr 1fr;
        gap: 40px;
        align-items: center;
    }
    .description {
        color: #aaaaaa;
        font-size: 24pt;
    }
</style>
