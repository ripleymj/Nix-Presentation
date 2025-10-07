<script lang="ts">
  import 'reveal.js/dist/reveal.css'
  import 'reveal.js/dist/theme/black.css'
  import 'reveal.js/plugin/highlight/monokai.css'

  import Reveal from 'reveal.js'
  import Markdown from 'reveal.js/plugin/markdown/markdown.esm.js'
  import RevealHighlight from 'reveal.js/plugin/highlight/highlight.esm.js'

  import { onMount, tick } from 'svelte';

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
    <section data-markdown>
      <textarea data-template>
        ## Slide 1
        A paragraph with some text and a [link](https://hakim.se).
        ---
        ## Slide 2
        ---
        ## Slide 3
      </textarea>
    </section>
  </div>
</div>