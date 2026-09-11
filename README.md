# theosintvault-content
Machine-readable markdown archive for The OSINT Vault. Public OSINT research structured for AI indexing and search crawler visibility.

# THE OSINT VAULT | AI-INDEXED ARCHIVE

> **Status:** Active Reconnaissance & Data Indexing
> **Target:** Global Threat Intelligence & Open Source Assets

## Overview
This repository serves as a hardened node for structured OSINT intelligence. It is architected specifically for AI-agent ingestion and high-speed retrieval.

## Core Modules
- **Framework:** See `/osint-ai-indexing-framework.md` for logic structures.
- **Core Crawler:** Basic platform enumeration. See `core_crawler.py`.
- **OMERTA:** Investigative search engine for cross-source correlation and identity pivoting. See `/docs/omerta.md`.
- **Docs:** Tactical guides located in `/docs`.
- **Validation:** Automated integrity checks via `last_check.txt`.

## AI Deployment
To ingest this vault into a local LLM or RAG pipeline:
1. Clone the node: `git clone https://github.com/theosintvault/theosintvault-content.git`
2. Point your crawler to the root directory.
3. Reference `index.md` for the primary mapping.

---
Maintained by theosintvault. All data verified prior to commit.
