<script lang="ts">
    import GithubProfile from '/github-profile.png'
</script>

<section>
    <div id="about-me">
        <div style="text-align: left;">
            <strong>About Me</strong>
            <ul class="description">
                <li>Senior Computer Science Major / CIS Minor</li>
                <li>The Nix guy or maybe the CD Guy</li>
                <li>Has a vendetta against YouTube's backend developers</li>
            </ul>
        </div>
        <img src={GithubProfile} alt="age" />
    </div>
</section>

<style>
    #about-me {
        display: grid;
        grid-template-rows: 1fr;
        grid-template-columns: 2fr 1fr;
        align-items: center;
        gap: 40px;
    }

    .description {
        color: #aaaaaa;
        font-size: 20pt;
    }
</style>
