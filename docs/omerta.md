# OMERTA: Investigative OSINT Search Engine

OMERTA is a structured intelligence tool for digital identity discovery, cross-source correlation, and investigative pivoting across open-source data.

## Overview

OMERTA performs systematic searches across hundreds of platforms and data sources to correlate fragmented digital identities. Built for investigators, researchers, and intelligence analysts who need repeatable, evidence-based workflows.

## Core Capabilities

### Cross-Identifier Correlation
Links and correlates digital footprints across multiple identifier types:
- Usernames
- Email addresses
- Phone numbers
- Domains
- IP addresses

### Identity Pivoting
Aggregates scattered open-source data to reveal linked profiles, associated records, and actionable investigative leads.

### Platform Coverage
Sweeps 698+ platforms and services using 30 distinct data sources and 80+ multi-search endpoints to surface confirmed hits.

### Structured Research Workflows
Generates repeatable investigations with evidence-based results for documentation and reporting.

## Usage

### Basic Username Sweep
```bash
python omerta.py theosintvault username
```

### Email Correlation
```bash
python omerta.py user@example.com email
```

### Phone Number Lookup
```bash
python omerta.py +1234567890 phone
```

### Domain Investigation
```bash
python omerta.py example.com domain
```

### Export Results
Results automatically export in JSON format for integration with reporting systems and further analysis.

## Platform Categories

### Social Networks
GitHub, Twitter, Instagram, Facebook, LinkedIn, Reddit, TikTok, YouTube, Twitch, Discord

### Professional Services
Crunchbase, Angel List, Product Hunt

### Data Sources
- Whois records
- DNS resolution
- SSL certificate transparency
- Email enumeration
- Phone reverse lookup
- Domain history

## Investigation Workflow

1. Define seed identifier (username, email, domain, etc.)
2. Run correlation scan across all platforms
3. Identify confirmed hits and linked identities
4. Build pivot chains to discover associated profiles
5. Export structured research for reporting

## Output Format

Results include:
- Confirmed platform hits with direct URLs
- Linked identities and associated accounts
- Cross-source correlation metadata
- Evidence chain for investigative documentation

## Integration

OMERTA integrates with the broader OSINT Vault framework for AI indexing and high-speed retrieval of investigative findings.
