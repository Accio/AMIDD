# AMIDD Course Website - Claude Instructions

## Project Context

This is the course website for **Applied Mathematics and Informatics in Drug Discovery (AMIDD)**, taught at the University of Basel, Department of Mathematics and Informatics.

- **Schedule:** Fall Semester, Fridays 12:15-14:00
- **Website:** www.AMIDD.ch
- **Technology:** Jekyll static site, GitHub Pages
- **Instructor:** Jitao David Zhang

## Annual Maintenance Pattern

**This site requires a year transition every ~August/September** before the fall semester begins (typically mid-September). The process follows a consistent pattern documented in the Claude memory system.

### When User Requests Year Transition

If the user asks to update the site for a new year (e.g., "update to 2027"), follow the established process:

1. Archive previous year's `README.md` to `archive/README-YYYY.md`
2. Update `README.md` with new year references
3. Update `_config.yml`
4. Create new assets directory with symlinks
5. Test build locally
6. Push changes

### Key Principles

- **Use symlinks** for assets initially - allows immediate functionality while real PDFs are being created
- **Replace Google Form URLs** with placeholder text `[Form URL to be updated]` - don't leave old URLs
- **Check Dies academicus date** - usually late November, affects lecture scheduling
- **Test locally** before pushing - use `make serve` or alternate port if needed

## Project Structure

```
AMIDD/
├── README.md             # Main course page (heavily edited during transitions)
├── _config.yml           # Jekyll config (description needs year update)
├── archive/              # Historical course pages
│   ├── README-2019.md
│   ├── README-2020.md
│   ├── README-2021.md
│   ├── README-2022.md
│   ├── README-2023.md
│   ├── README-2024.md
│   ├── README-2025.md
│   └── ...
├── assets/
│   ├── 2025/            # Previous year materials
│   │   ├── 01/AMIDD-2025-01-Intro.pdf
│   │   └── ...
│   └── 2026/            # Current year (initially symlinks)
├── Makefile             # Build commands
└── CLAUDE.md           # This file
```

## Development Commands

```bash
# Start local development server
make serve

# If port 4000 is in use
bundle exec jekyll serve --port 4001

# Check what's using port 4000
lsof -i :4000
```

## Important Notes

- **Course ID changes yearly**: University of Basel course directory ID must be updated
- **Symlinks work in production**: GitHub Pages correctly handles symlinks in the repo
- **Build time**: ~0.2-0.3 seconds for this small site
- **Assets organized by lecture number**: `assets/YYYY/NN/` where NN is the lecture number

## Contact & Deployment

- **GitHub Repo:** Accio/AMIDD
- **Deployment:** Automatic via GitHub Pages
- **Build Status:** Check GitHub Actions tab after push
- **Deploy Time:** 1-2 minutes after push to main

## Year Transition History

- 2025 → 2026: February 7, 2026 - Full transition with symlinks strategy
