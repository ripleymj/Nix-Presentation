<section>
    <section style="text-align: left;">
        <h3>Channels?</h3>
        <ul style="font-size: 20pt;">
            <li>
                The nix package repository, <a
                    href="https://github.com/NixOS/nixpkgs"
                    target="_blank">nixpkgs</a
                >, is a simple GitHub repository
            </li>
            <li>
                A "channel" refers to a specific, "verified" commit of nixpkgs. Simply put, its a
                version of the repository
            </li>
            <li>
                There are two general categories of channels, <strong>stable</strong> and
                <strong>unstable</strong>
            </li>
        </ul>
    </section>
    <section id="stable-vs-unstable">
        <div style="text-align: left;">
            <h4 style="color: var(--nix-dark-blue);">Stable</h4>
            <ul style="font-size: 16pt;">
                <li>Bi-yearly release (e.g. nixos-24.11, nixos-25.05)</li>
                <li>Largely focused on bug fixes and security vulnerabilities</li>
                <li>Similar to Ubuntu releases like Ubuntu 25.04, Ubuntu 25.10, etc.</li>
            </ul>
        </div>
        <strong>VS</strong>
        <div id="unstable" dir="rtl">
            <h4 style="color: var(--nix-light-blue);">Unstable</h4>
            <ul style="font-size: 16pt;">
                <li>Rolling release</li>
                <li>Provides latest tested packages</li>
                <li>Similar to the AUR</li>
                <li>Single continuously update channel (e.g. nixos-unstable, nixpkgs-unstable)</li>
            </ul>
        </div>
    </section>
</section>

<style>
    #stable-vs-unstable {
        display: grid !important;
        grid-template-rows: 1fr;
        grid-template-columns: 1fr min-content 1fr;
        gap: 3rem;
        align-items: center;
    }
    li {
        margin-bottom: 8px;
    }
    #unstable,
    #unstable ul {
        text-align: right !important;
    }
</style>
