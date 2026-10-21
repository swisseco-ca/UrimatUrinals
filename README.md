# UrimatUrinals.ca
Bilingual first-stage website for Swiss Eco Media. Hosted with OpenAI Sites; source also maintained in swisseco-ca/UrimatUrinals.

Run `python3 build.py` to generate English and French HTML. Static deployment directory: `dist`.

## Implemented
English/French homepage, original responsive styling, editable operating-cost calculator, FAQ, verified telephone link and local-only project brief download.

## Before public launch
Replace noindex/robots restrictions after review; finish product/industry/local pages, image inventory and five logo options; connect a verified lead endpoint; approve privacy language; prepare redirects from existing URLs; verify custom-domain DNS and HTTPS. Do not represent the project planner as a submitted inquiry.

## Assets
`dist/assets/urimat-eco.png`: existing URIMAT Eco product image from the user's urimaturinals.ca website, originally https://static.tildacdn.com/tild6537-3562-4034-b933-636237356664/Urinal_-_Eco.png . Reused for the same owner's redesign. Confirm manufacturer image permission before broader reuse.

## Deployment
Sites uses its managed source repository for publication. GitHub is a separate source copy, not an automatically connected deployment pipeline. Keep both copies synchronized when editing.

## Phase 2 private draft
Product overview and Eco pages, how-it-works diagram, maintenance and consumables guidance, planning resources, and five industry page pairs are implemented in `phase2.py`. The homepage links to the new content. All 30 English/French pages retain noindex and reciprocal page-specific language switches. Five original SVG companion-logo concepts are available at `/en/review/logos/` and `/fr/revision/logos/`; none has been selected or applied.

No customer installation story is claimed without evidence. See [asset inventory](docs/ASSET-INVENTORY.md) for sources and permission gaps and [backlog](docs/BACKLOG.md) for remaining Phase 2 approvals and later work.

## Local development and checks
Requires Python 3; no third-party build dependencies. Run from the repository root:

```sh
python3 build.py
python3 -m unittest discover -s tests -v
python3 -m http.server 8000 --bind 127.0.0.1 --directory dist
```

The builder regenerates HTML/CSS and logo concepts; `dist/app.js` and the product PNG are retained source assets, so do not delete `dist` before building. Structural checks validate local links/assets/fragments, translated pairs and private indexing directives. Browser acceptance checks should also cover mobile/desktop overflow, keyboard navigation, loaded imagery, calculator validation and actual planner downloads.

The hosting project ID in `.openai/hosting.json` is the new private draft. Preserve the earlier project's `www.urimaturinals.ca` domain and DNS. A GitHub push does not publish this draft to OpenAI Sites.
