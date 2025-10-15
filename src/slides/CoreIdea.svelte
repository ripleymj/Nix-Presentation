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
            <div style="text-align: left;">
                <span>Nix is <strong>Purely Functional</strong></span>
                <p class="description">
                    Given the same inputs, Nix will always produce the same output, regardless of
                    the state of the rest of the system.
                </p>
            </div>
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
            <div style="text-align: right;">
                <span>Packages & Systems are <strong>Declared</strong></span>
                <p class="description">
                    Declare exact dependencies and let nix take care of the build step. Allows for
                    easy sharing of developer environments.
                </p>
            </div>
        </div>
    </section>
    <section>
        <div id="reliable">
            <div style="text-align: left;">
                <span><strong>Safe Upgrades</strong> and <strong>Rollbacks</strong></span>
                <p class="description">
                    Nix ensures that upgrading a package will never break other packages and allows
                    you to rollback to previous versions.
                </p>
            </div>
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
        align-items: center;
        gap: 40px;
    }

    #declartive {
        display: grid;
        grid-template-rows: 1fr;
        grid-template-columns: 1fr 2fr;
        align-items: center;
        gap: 40px;
    }

    .description {
        color: #aaaaaa;
        font-size: 24pt;
    }
</style>
