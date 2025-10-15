<script lang="ts">
    import HomeIcon from '/home-icon.png'
</script>

<section>
    <div id="intro">
        <div style="text-align: left;">
            <h3>Home Manager</h3>
            <p class="description">
                Nix module that extends user configuraiton capabilities. Allows for easy management
                of per-user packages and dotfiles.
            </p>
        </div>
        <img src={HomeIcon} alt="nix-darwin-logo" />
    </div>
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
