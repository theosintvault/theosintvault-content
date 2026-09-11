# Google Dork Generator

The Google Dork Generator is a browser-native query construction utility built to streamline targeted web search operations. Designed and maintained by Nicole Hurey as part of The OSINT Vault, the builder simplifies advanced Google dorking by assembling precision search strings that uncover hidden assets without manual syntax errors.

Instead of trying to remember complex operator combinations or making formatting mistakes that break search logic, researchers can stack targeted rules to quickly reach exposed files, hidden administrative portals, and indexed infrastructure.

## Core Capabilities and Features

### Guided Query Construction
Supports 11 advanced search operators and 13 specific file types to isolate target domains, file structures, cached pages, and keyword proximity.

### Investigation Presets
Features one-click configurations tailored to common research needs, including infrastructure reconnaissance, admin panel discovery, document extraction, credential searches, cloud storage scans, and personnel lookups.

### Batch Query Execution
Generates multiple tactical query variations at once, opening filetype, title, and infrastructure variants simultaneously to map target surface areas rapidly.

### Pre-Built Dork Library
Includes 28 verified example queries across six operational categories for fast, repeatable searches.

### Client-Side Data Privacy
Assembles queries entirely within the browser. Search targets, keywords, and domain parameters are never sent to external servers or logged anywhere outside local storage.

### Integrated Vault Workflow
Connects directly to the Multi-Search Launcher, Bookmarklet Library, and Report Composer to form a seamless, defensible collection chain.

## Supported Operators

- site: (domain restriction)
- filetype: (specific file formats)
- intitle: (page title matching)
- inurl: (URL path matching)
- intext: (page content matching)
- cache: (cached versions)
- link: (pages linking to target)
- related: (similar pages)
- OR / AND / NOT (boolean logic)
- Quotes (exact phrase matching)
- Wildcards (pattern matching)

## Supported File Types

PDF, DOCX, XLSX, PPTX, TXT, CSV, SQL, LOG, CONFIG, JSON, XML, BAK, ZIP

## Investigation Presets

- Infrastructure reconnaissance
- Administrative panel discovery
- Document exposure scans
- Credential and auth leak searches
- Cloud storage enumeration
- Personnel information gathering

## Access

https://theosintvault.io/google-dork-generator

## Query Privacy

Dorks are constructed locally in your browser and executed through Google from your IP. No dork history, no logging, no external query tracking beyond Google's standard search logs.
