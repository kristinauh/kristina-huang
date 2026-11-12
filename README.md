# K's Project Room

A 3D room of my projects, built with three.js. Live at https://kristinauh.github.io/kristina-huang/

- `src/` is the source page (the same page as the private claude.ai artifact, which is the source of truth).
- `build.py` makes the public copy at the repo root: `python3 build.py [projects.json]`.
  The optional json is an export of the artifact's `projects` collection; only projects with `public: true` are published.
