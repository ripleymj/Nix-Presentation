<script lang="ts">
    import Age from '/age.svg'
</script>

<section>
    <div id="agenix">
        <div style="text-align: left;">
            <strong>Agenix</strong>
            <p class="description">
                Agenix allos you to store encypted secrets directly in your Nix configuration.
                Safely share and deploy your configurations
            </p>
        </div>
        <img src={Age} alt="age" />
    </div>
</section>

<style>
    #agenix {
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
