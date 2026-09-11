# Core Crawler: Platform Enumeration and User Discovery

Core Crawler is a command-line tool for discovering usernames across 600+ platforms. Sweeps social networks, developer communities, professional services, forums, and niche platforms with concurrent async requests.

## Overview

Core Crawler performs systematic platform enumeration to identify where a target username exists. Supports full sweeps across all platforms or targeted searches by category. Results include direct URLs and verification status.

## Capabilities

### Comprehensive Platform Coverage
600+ platforms across 10 categories including social media, developer platforms, professional services, gaming communities, forums, content platforms, streaming services, music platforms, news and blogging sites, and cryptocurrency networks.

### Category-Based Searching
Filter searches by platform category for targeted investigations. Categories include social_media, developer_platforms, professional_services, gaming_communities, forums_communities, content_platforms, streaming_services, music_platforms, news_blogging, and cryptocurrency.

### Concurrent Async Sweeping
All platform checks run simultaneously using asyncio for maximum speed. Typical full sweep completes in seconds regardless of platform count.

### Results Export
Export findings in JSON format for integration with reporting systems and further analysis. Includes platform name, URL, verification status, and HTTP response codes.

## Usage

### Full Platform Sweep
```bash
python core_crawler.py sweep theosintvault
```

Sweeps username across all 600+ platforms. Returns confirmed hits, not found results, and any errors encountered.

### Category-Specific Search
```bash
python core_crawler.py sweep-category theosintvault social_media
```

Search within a specific platform category. Useful for targeted investigations.

### List Available Categories
```bash
python core_crawler.py list-categories
```

Shows all 10 platform categories.

### List Platforms in Category
```bash
python core_crawler.py list-platforms social_media
```

Shows all platforms within a category.

### Platform Statistics
```bash
python core_crawler.py platform-count
```

Displays total platform count and breakdown by category.

## Output Format

Results include:
- Username searched
- Total platforms checked
- Confirmed hits with direct URLs
- Count of not found results
- Any errors or timeouts

## Platform Categories

- social_media: Twitter, Instagram, Facebook, TikTok, YouTube, Twitch, Reddit, LinkedIn, and others
- developer_platforms: GitHub, GitLab, Stack Overflow, Dev.to, CodePen, and others
- professional_services: Crunchbase, Angel List, Product Hunt, Behance, Dribbble, and others
- gaming_communities: Steam, Xbox, Discord, Twitch, Epic Games, and others
- forums_communities: Reddit, 4chan, Hacker News, Lobsters, and others
- content_platforms: YouTube, Vimeo, Flickr, Unsplash, 500px, and others
- streaming_services: Twitch, Kick, Rumble, Odysee, and others
- music_platforms: SoundCloud, Bandcamp, Spotify, Mixcloud, Last.fm, and others
- news_blogging: Medium, Substack, WordPress, Ghost, Hashnode, and others
- cryptocurrency: Bitcoin Talk, Etherscan, GitHub, Twitter, and others

## Integration

Core Crawler works alongside OMERTA and OSINT Grid for comprehensive investigative workflows. Export results to feed into cross-source correlation and public records lookups.

## Performance

Concurrent async architecture means performance scales with number of platforms. Full 600+ platform sweep typically completes in 15-30 seconds depending on network conditions.
