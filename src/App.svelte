<script lang="ts">
    import 'reveal.js/dist/reveal.css'
    import 'reveal.js/dist/theme/black.css'
    import './github-dark-dimmed.css'

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
    import Channels from './slides/Channels.svelte'
    import TitleNixOS from './slides/TitleNixOS.svelte'
    import NixOSInstall from './slides/NixOSInstall.svelte'
    import TitleNixpkgs from './slides/TitleNixpkgs.svelte'
    import TitleNixLanguage from './slides/TitleNixLanguage.svelte'
    import NixLanguage from './slides/NixLanguage.svelte'
    import TitleCommunityProjects from './slides/TitleCommunityProjects.svelte'
    import NixDarwin from './slides/NixDarwin.svelte'
    import HomeManager from './slides/HomeManager.svelte'
    import DesktopManagement from './slides/DesktopManagement.svelte'
    import Agenix from './slides/Agenix.svelte'
    import Devenv from './slides/Devenv.svelte'
    import Configuration from './slides/Configuration.svelte'
    import Neovim from './slides/Neovim.svelte'
    import NixOSRebuild from './slides/NixOSRebuild.svelte'

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
        <History />
        <TheProblem />
        <CoreIdea />
        <TitleNixLanguage />
        <NixLanguage />
        <TitleNixpkgs />
        <PackageGraph />
        <Channels />
        <TitleNixOS />
        <NixOSInstall />
        <Configuration />
        <NixOSRebuild />
        <TitleCommunityProjects />
        <HomeManager />
        <DesktopManagement />
        <NixDarwin />
        <Agenix />
        <Devenv />
        <Neovim />
    </div>
</div>
