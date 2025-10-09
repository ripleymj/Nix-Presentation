<script lang="ts">
    import Reproducible from '/reproducible.svg'
    import Declartive from '/declaritive.svg'
    import Reliable from '/reliable.svg'
</script>

<section>
    <section>
        <h3 style="text-align: left;">The Core Idea</h3>
        <div id="images">
            <img src={Reproducible} alt="Reproducible" />
            <img src={Declartive} alt="Declartive" />
            <img src={Reliable} alt="Reliable" />
            <strong>Reproducible</strong>
            <strong>Declarative</strong>
            <strong>Reliable</strong>
        </div>
    </section>
    <section>
        <div id="reproducible">
            <p style="text-align: left;">
                Nix is <strong>Purely Functional</strong>
            </p>
            <div>
                <img src={Reproducible} alt="Reproducible" />
                <strong>Reproducible</strong>
            </div>
        </div>
    </section>
    <section>
        <div id="declartive">
            <div>
                <img src={Declartive} alt="Declartive" />
                <strong>Declartive</strong>
            </div>
            <p style="text-align: right;">Packages & Systems are <strong>Declared</strong></p>
        </div>
    </section>
    <section>
        <div id="reliable">
            <p style="text-align: left;">
                <strong>Safe Upgrades</strong> and <strong>Rollbacks</strong>
            </p>
            <div>
                <img src={Reliable} alt="Reliable" />
                <strong>Reliable</strong>
            </div>
        </div>
    </section>
</section>

<style>
    #images {
        display: grid;
        grid-template-rows: 1fr 40px;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 40px;
    }

    #reproducible,
    #reliable {
        display: grid;
        grid-template-rows: 1fr;
        grid-template-columns: 2fr 1fr;
        gap: 40px;
    }

    #declartive {
        display: grid;
        grid-template-rows: 1fr;
        grid-template-columns: 1fr 2fr;
        gap: 40px;
    }
</style>
