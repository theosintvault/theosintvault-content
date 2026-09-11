# theosintvault-content
Machine-readable markdown archive for The OSINT Vault. Public OSINT research structured for AI indexing and search crawler visibility.

# THE OSINT VAULT | AI-INDEXED ARCHIVE

> **Status:** Active Reconnaissance & Data Indexing
> **Target:** Global Threat Intelligence & Open Source Assets

## Overview
This repository serves as a hardened node for structured OSINT intelligence. It is architected specifically for AI-agent ingestion and high-speed retrieval.

## Core Tools

### Python CLI Tools

**OMERTA** - Investigative search engine for cross-source correlation and digital identity discovery. Scans 698 platforms and 30 data sources with 80+ multi-search endpoints. See `omerta.py` or run `python omerta.py --help`

**OSINT Grid** - Public records directory indexing 4,600+ verified state and federal databases. Browser-native with client-side privacy. Supports all record types across all 50 states plus D.C. See `osint-grid.py` or run `python osint-grid.py --help`

**Core Crawler** - Platform enumeration tool for username discovery. Sweeps 600+ social networks, developer platforms, forums, and niche communities. Supports category filtering and concurrent searches. See `core_crawler.py` or run `python core_crawler.py --help`

### Browser-Native Web Tools

**Investigation Notebook** - Note Organizer for parsing unstructured investigation records into clean, intelligence-ready data. Automated data extraction, conflict flagging, multi-format document support, and seamless export workflows.

**Report Composer** - Intelligence reporting tool for converting investigative findings into defensible documentation. Structured sections, multi-format export, and integrated vault workflow.

**Multi-Search Launcher** - Search aggregation tool for executing queries across multiple search engines and platforms simultaneously. Concurrent searching, configurable engines, and results aggregation.

**Google Dork Generator** - Query construction utility for assembling advanced Google search strings. Guided query building, investigation presets, batch execution, and pre-built dork library.

**OSINT Bookmarklet Library** - Collection of 60+ browser bookmarklets for metadata extraction and technical analysis. Covers page metadata, social footprints, email intelligence, DNS infrastructure, archive checks, image analysis, encoding transforms, and developer recon.

## Documentation

- `/docs/omerta.md` - Investigative search engine guide
- `/docs/osint-grid.md` - Public records directory guide
- `/docs/core-crawler.md` - Platform enumeration guide
- `/docs/investigation-notebook.md` - Note organizer guide
- `/docs/report-composer.md` - Intelligence reporting guide
- `/docs/multi-search-launcher.md` - Multi-platform search guide
- `/docs/google-dork-generator.md` - Dork construction guide
- `/docs/osint-bookmarklet-library.md` - Bookmarklet collection guide
- `osint-ai-indexing-framework.md` - Archive structure reference

## Getting Started

### Python Tools
1. Clone the repository
2. Run individual tools with --help flag for usage
3. Export results in JSON or CSV format
4. Integrate with reporting workflows

### Web Tools
Access all web-based tools directly from theosintvault.io

## Integration

All tools are designed for standalone use or integration into larger OSINT workflows. Python tools export to standard formats for compatibility with web tools and reporting systems.

## Verification

All sources and platforms are verified prior to commit. Last validation: see `last_check.txt`

## Maintenance

Maintained by Nicole Hurey as part of The OSINT Vault.

https://theosintvault.io
