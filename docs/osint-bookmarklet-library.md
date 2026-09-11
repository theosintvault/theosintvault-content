# OSINT Bookmarklet Library

The OSINT Bookmarklet Library is a collection of browser-native scripts designed to speed up metadata extraction, technical analysis, and investigative pivots. Built and maintained by Nicole Hurey as part of The OSINT Vault, the library equips researchers with over 60 zero-installation tools that run directly inside any standard web browser.

Instead of installing questionable extensions or leaving a target page to run external lookups, investigators can drag individual bookmarklets to their browser toolbar to execute instant, targeted actions on demand.

## Core Capabilities and Features

### Comprehensive Investigative Categories
Features dedicated scripts across ten distinct functional areas, including page metadata, social media footprints, username correlation, email intelligence, DNS and WHOIS infrastructure, archive checks, image analysis, encoding transforms, developer recon, and search operator generators.

### Rapid Metadata Extraction
Pulls hidden HTML metadata, Open Graph fields, schema markup, Google Analytics IDs, hidden form fields, and outbound link graphs in seconds without opening developer tools.

### Strict Client-Side Privacy
Executes all code locally inside the browser DOM. The scripts do not track users, inject third-party analytics, or send collected target data to external servers.

### Instant Workflow Integration
Works directly alongside other core Vault tools, allowing investigators to quickly gather technical indicators on a page and pass findings straight into the Note Organizer or Report Composer.

### Transparent Codebase
Maintains lightweight, fully inspectable JavaScript snippets so security teams and researchers can review every script's behavior before execution on sensitive systems.

## Bookmarklet Categories

### Page Metadata
Extracts HTML headers, meta tags, Open Graph data, schema markup, and canonical URL references.

### Social Media Footprints
Identifies social media accounts, linked profiles, and embedded social widgets on target pages.

### Username and Email Correlation
Cross-references usernames and email addresses across the page for entity linking and pattern analysis.

### Email Intelligence
Extracts email addresses, obfuscated contacts, and email patterns from visible content.

### DNS and WHOIS Infrastructure
Queries DNS records, WHOIS data, IP geolocation, and nameserver information for target domains.

### Archive and Historical Records
Checks Internet Archive snapshots, cached versions, and historical page variations.

### Image Analysis
Extracts image metadata, EXIF data, reverse image search triggers, and embedded visual indicators.

### Encoding and Obfuscation Transforms
Decodes base64, URL encoding, hex, and other encoded content embedded in pages.

### Developer Reconnaissance
Identifies technology stacks, frameworks, CDNs, analytics platforms, and development tools used by target sites.

### Search Operator Generators
Creates dorks, advanced queries, and search strings formatted for Google, Bing, and specialized platforms.

## Installation

Drag individual bookmarklets from the library directly into your browser toolbar. No installation process, no extensions, no permissions required.

## Usage

Navigate to any target page and click the relevant bookmarklet. Results display inline or in a new tab depending on the specific script.

## Integration Points

Bookmarklet findings feed directly into:
- Investigation Notebook for organized case data
- Report Composer for evidence documentation
- Multi-Search Launcher for follow-up searches
- Google Dork Generator for refined queries

## Access

https://theosintvault.io/osint-bookmarklet-library

## Security and Transparency

Every bookmarklet is open source and fully inspectable. All code executes locally within your browser. No external calls, no data collection, no behavioral tracking.
