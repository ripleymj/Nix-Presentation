<script lang="ts">
    import 'reveal.js/dist/reveal.css'
    import 'reveal.js/dist/theme/black.css'
    import 'reveal.js/plugin/highlight/monokai.css'

    import Reveal from 'reveal.js'
    import Markdown from 'reveal.js/plugin/markdown/markdown.esm.js'
    import RevealHighlight from 'reveal.js/plugin/highlight/highlight.esm.js'

    import { onMount, tick } from 'svelte'

    import Title from './slides/Title.svelte'
    import PackageGraph from './slides/PackageGraph.svelte'
    import WhatIsNix from './slides/WhatIsNix.svelte'
    import AboutMe from './slides/AboutMe.svelte'
    import History from './slides/History.svelte'
    import CoreIdea from './slides/CoreIdea.svelte'
    import TheProblem from './slides/TheProblem.svelte'

    onMount(async () => {
        await tick()
        const deck = new Reveal({
            plugins: [Markdown, RevealHighlight],
        })
        deck.initialize()
    })
</script>

<svelte:head>
    <title>Nix Presentation</title>
</svelte:head>

<div class="reveal">
    <div class="slides">
        <Title />
        <AboutMe />
        <WhatIsNix />
        <TheProblem />
        <CoreIdea />
        <History />
        <PackageGraph />
    </div>
</div>
