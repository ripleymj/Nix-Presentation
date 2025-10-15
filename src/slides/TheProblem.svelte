<script>
    import PythonLogo from '/python.svg'
</script>

<section>
    <section style="text-align: left;">
        <h3>The Problem</h3>
        <p style="font-size: 20pt;">
            <strong>"It works on my machine."</strong> Nix aims to end 'dependency hell' by ensuring
            every build is isolated and reproducible.
        </p>
    </section>
    <section data-auto-animate>
        <div class="venv">
            <img class="python-logo" src={PythonLogo} alt="Python Logo" />
            <pre><code data-trim class="language-python">
# my_awesome_program.py

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
col_means = np.mean(a, axis=0)

print("Array:\n", a)
print("Column means:", col_means)
            </code></pre>
        </div>
    </section>
    <section data-auto-animate>
        <div class="venv">
            <img class="python-logo" src={PythonLogo} alt="Python Logo" />
            <pre data-id="venv-animation"><code data-trim>
$ python -m venv .venv
$ source .venv/bin/activate
            </code></pre>
        </div>
    </section>
    <section data-auto-animate>
        <div class="venv">
            <img class="python-logo" src={PythonLogo} alt="Python Logo" />
            <pre data-id="venv-animation"><code data-trim>
$ python -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip install numpy
            </code></pre>
        </div>
    </section>
</section>

<style>
    .venv {
        display: grid;
        min-height: 200px;
        grid-template-rows: 1fr;
        grid-template-columns: 1fr 2fr;
        justify-items: center;
        align-items: center;
    }
</style>
