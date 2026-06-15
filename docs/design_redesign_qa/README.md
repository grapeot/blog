# Signal Redesign QA Screenshots

Generated with Playwright against local `output/` after `make html`.

Viewports:

| Prefix | Size |
|---|---|
| `desktop_*` | 1440 x 1100 |
| `mobile_*` | 390 x 1100 |

Pages covered: home, Chinese article, English article, archives, Chinese tag page, about page, plus `mobile_nav_open.png`.

Programmatic checks run with the screenshots:

| Check | Result |
|---|---|
| Horizontal overflow across sampled desktop/mobile pages | Passed |
| Mobile nav opens | Passed |
| Page JS errors during sampled screenshot capture | Passed |

Note: the Kit embed is a fixed slide-in popup. Full-page screenshots can show it in the stitched capture area, but the page-level overflow check passes and the newsletter remains Chinese-only by test contract.
