<script lang="ts">
    import * as d3 from 'd3'
    import { onMount } from 'svelte'

    type PackageStat = {
        name: string
        color: string
        packages: number
        freshPackages: number
    }

    let queuedRepositories: PackageStat[] = []
    let repositories: PackageStat[] = []
    export let width: number = 800
    export let height: number = 500
    export let marginTop: number = 30
    export let marginRight: number = 80
    export let marginBottom: number = 50
    export let marginLeft: number = 70

    let gx: SVGGElement, gy: SVGGElement

    $: innerWidth = width - marginLeft - marginRight
    $: innerHeight = height - marginTop - marginBottom
    $: x = d3
        .scaleLinear([0, Math.max(...repositories.map((d) => d.packages))], [0, innerWidth])
        .nice()

    $: y = d3
        .scaleLinear([0, Math.max(...repositories.map((d) => d.freshPackages))], [innerHeight, 0])
        .nice()

    // render axes with transitions
    $: if (gx && repositories.length > 0) {
        const t = d3.transition().duration(750).ease(d3.easeCubicInOut)
        d3.select(gx).transition(t).call(d3.axisBottom(x))
    }

    $: if (gy && repositories.length > 0) {
        const t = d3.transition().duration(750).ease(d3.easeCubicInOut)
        d3.select(gy).transition(t).call(d3.axisLeft(y))
    }

    onMount(async () => {
        const nixpkgsOrAUR = (pkg: PackageStat) =>
            pkg.name.startsWith('nixpkgs') || pkg.name === 'AUR'

        const res = await d3.csv<PackageStat, string>('packages.csv', d3.autoType)
        repositories = res.filter((pkg) => !nixpkgsOrAUR(pkg))
        queuedRepositories = res.filter(nixpkgsOrAUR).sort((a, b) => {
            if (a.name === 'AUR' && b.name !== 'AUR') return -1
            if (b.name === 'AUR' && a.name !== 'AUR') return 1
            return b.packages - a.packages
        })
    })

    let highlightedRepos: Set<string> = new Set()
    let grayRepos: boolean = false

    function* animations(): Generator<() => void> {
        yield () => {
            grayRepos = true
            highlightedRepos.add('ubuntu')
            highlightedRepos = highlightedRepos
        }
        yield () => {
            highlightedRepos.add('debian')
            highlightedRepos = highlightedRepos
        }
        yield () => {
            highlightedRepos.add('fedora')
            highlightedRepos = highlightedRepos
        }
        yield () => {
            highlightedRepos.add('alpine')
            highlightedRepos = highlightedRepos
        }

        grayRepos = false
        highlightedRepos.clear()
        highlightedRepos = highlightedRepos

        while (queuedRepositories.length > 0) {
            const nextPkg = queuedRepositories.shift()!
            yield () => {
                highlightedRepos.add(nextPkg.name.toLowerCase().split(' ')[0])
                highlightedRepos = highlightedRepos
                repositories = [...repositories, nextPkg]
            }
        }
    }

    const animate = animations()
</script>

<section
    role="presentation"
    on:mouseup={() => {
        const fun = animate.next()
        if (!fun.done) fun.value()
    }}
>
    <strong>Packages</strong>
    <svg {width} {height}>
        <g transform="translate({marginLeft},{marginTop})">
            <g bind:this={gx} transform="translate(0,{innerHeight})" fill="white">
                <text fill="white" text-anchor="middle" x={innerWidth / 2} y="40">Packages</text>
            </g>
            <g bind:this={gy} x={-innerHeight / 2} y={-50} fill="white" text-anchor="middle">
                <text
                    transform="rotate(-90)"
                    fill="white"
                    text-anchor="middle"
                    x={-innerHeight / 2}
                    y={-50}>Fresh Packages</text
                >
            </g>
            {#each repositories as { name, color, packages, freshPackages } (name)}
                {@const highlight = highlightedRepos.has(name.toLowerCase().split(' ')[0])}
                <circle
                    fill={!grayRepos || highlight ? color : '#666666'}
                    cx={x(packages)}
                    cy={y(freshPackages)}
                    r="5"
                />
                {#if highlight}
                    <text fill="white" x={x(packages) + 7} y={y(freshPackages)} font-size="8"
                        >{name}</text
                    >
                {/if}
            {/each}
        </g>
    </svg>
</section>

<style>
    circle {
        transition: all 750ms ease-in-out;
    }
</style>
