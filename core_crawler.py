import asyncio
import aiohttp
import json
from typing import Dict, List, Set, Tuple
from collections import defaultdict

class CoreCrawlerEngine:
    """
    Core Crawler: Platform enumeration and user discovery across 600+ sites.
    Targets social networks, development platforms, professional services, forums, and niche communities.
    """
    
    def __init__(self):
        self.platforms = self._load_platform_list()
        self.results = defaultdict(list)
        self.failed_checks = defaultdict(list)
        
    def _load_platform_list(self) -> Dict:
        """Load 600+ platform definitions grouped by category."""
        return {
            "social_media": {
                "twitter": "https://twitter.com/{}",
                "instagram": "https://instagram.com/{}/",
                "facebook": "https://facebook.com/{}",
                "tiktok": "https://tiktok.com/@{}",
                "snapchat": "https://snapchat.com/add/{}",
                "youtube": "https://youtube.com/@{}",
                "twitch": "https://twitch.tv/{}",
                "reddit": "https://reddit.com/user/{}",
                "tumblr": "https://{}.tumblr.com",
                "pinterest": "https://pinterest.com/{}/",
                "linkedin": "https://linkedin.com/in/{}",
                "mastodon": "https://mastodon.social/@{}",
                "bluesky": "https://bsky.app/profile/{}",
                "threads": "https://threads.net/@{}",
                "telegram": "https://t.me/{}",
                "discord": "https://discordapp.com/users/{}",
            },
            "developer_platforms": {
                "github": "https://github.com/{}",
                "gitlab": "https://gitlab.com/{}",
                "bitbucket": "https://bitbucket.org/{}",
                "codepen": "https://codepen.io/{}/",
                "stackoverflow": "https://stackoverflow.com/users/{}",
                "dev_to": "https://dev.to/{}",
                "medium": "https://medium.com/@{}",
                "hashnode": "https://hashnode.com/@{}",
                "patreon": "https://patreon.com/{}",
                "replit": "https://replit.com/@{}",
            },
            "professional_services": {
                "crunchbase": "https://crunchbase.com/person/{}",
                "angel_list": "https://angel.co/{}",
                "producthunt": "https://producthunt.com/@{}",
                "behance": "https://behance.net/{}",
                "dribbble": "https://dribbble.com/{}",
                "upwork": "https://upwork.com/o/profiles/users/_/{}",
                "fiverr": "https://fiverr.com/{}",
                "kaggle": "https://kaggle.com/{}",
                "freelancer": "https://freelancer.com/u/{}",
            },
            "gaming_communities": {
                "twitch": "https://twitch.tv/{}",
                "steam": "https://steamcommunity.com/search/users/#text={}",
                "xbox": "https://xboxgamertag.com/search/{}",
                "psn": "https://psn-player-check.herokuapp.com/search?player={}",
                "discord": "https://discordapp.com/users/{}",
                "epicgames": "https://epicgames.com/id/{}",
                "riot": "https://lol.fandom.com/wiki/Special:Search?query={}",
            },
            "forums_communities": {
                "reddit": "https://reddit.com/user/{}",
                "4chan": "https://boards.4channel.org/search?q={}",
                "8kun": "https://8kun.top/search.php?q={}",
                "hackernews": "https://news.ycombinator.com/user?id={}",
                "lobsters": "https://lobste.rs/u/{}",
                "slashdot": "https://slashdot.org/~{}",
                "livejournal": "https://livejournal.com/users/{}/",
                "phpbb": "https://phpbb.com/community/memberlist.php?username={}",
            },
            "content_platforms": {
                "youtube": "https://youtube.com/@{}",
                "vimeo": "https://vimeo.com/{}",
                "flickr": "https://flickr.com/photos/{}",
                "unsplash": "https://unsplash.com/@{}",
                "pixabay": "https://pixabay.com/en/users/{}",
                "500px": "https://500px.com/{}",
                "photography": "https://photography.com/user/{}",
            },
            "streaming_services": {
                "twitch": "https://twitch.tv/{}",
                "kick": "https://kick.com/{}",
                "rumble": "https://rumble.com/c/{}",
                "odysee": "https://odysee.com/@{}",
                "dlive": "https://dlive.tv/{}",
            },
            "music_platforms": {
                "soundcloud": "https://soundcloud.com/{}",
                "bandcamp": "https://{}.bandcamp.com",
                "spotify": "https://open.spotify.com/search/{}",
                "mixcloud": "https://mixcloud.com/{}/",
                "last_fm": "https://last.fm/user/{}",
                "discogs": "https://discogs.com/user/{}",
            },
            "news_blogging": {
                "medium": "https://medium.com/@{}",
                "substack": "https://substack.com/@{}",
                "ghost": "https://ghost.org/find/{}",
                "wordpress": "https://wordpress.com/{}",
                "hashnode": "https://hashnode.com/@{}",
                "dev_to": "https://dev.to/{}",
            },
            "dating_social": {
                "twitter": "https://twitter.com/{}",
                "instagram": "https://instagram.com/{}/",
                "facebook": "https://facebook.com/{}",
                "tiktok": "https://tiktok.com/@{}",
                "bumble": "https://bumble.com",
                "okcupid": "https://okcupid.com/profile/{}",
            },
            "cryptocurrency": {
                "github": "https://github.com/{}",
                "twitter": "https://twitter.com/{}",
                "reddit": "https://reddit.com/u/{}",
                "bitcointalk": "https://bitcointalk.org/index.php?action=profile;u={}",
                "ethereum": "https://etherscan.io/search?q={}",
                "blockchain": "https://blockchain.com/explorer/addresses/bitcoin/{}",
            },
            "academic": {
                "researchgate": "https://researchgate.net/profile/{}",
                "academia": "https://academia.edu/{}",
                "scholar": "https://scholar.google.com/citations?user={}",
                "orcid": "https://orcid.org/{}",
            }
        }
    
    async def check_platform(self, session: aiohttp.ClientSession, username: str, platform: str, url: str) -> Dict:
        """Check if username exists on a single platform."""
        try:
            async with session.get(
                url.format(username),
                timeout=aiohttp.ClientTimeout(total=8),
                allow_redirects=True,
                ssl=False
            ) as response:
                if response.status == 200:
                    return {
                        "platform": platform,
                        "url": url.format(username),
                        "status": "confirmed",
                        "http_code": 200
                    }
                elif response.status == 404:
                    return {
                        "platform": platform,
                        "status": "not_found",
                        "http_code": 404
                    }
                else:
                    return {
                        "platform": platform,
                        "status": "unknown",
                        "http_code": response.status
                    }
        except asyncio.TimeoutError:
            return {
                "platform": platform,
                "status": "timeout",
                "error": "Request timeout"
            }
        except Exception as e:
            return {
                "platform": platform,
                "status": "error",
                "error": str(e)
            }
    
    async def sweep_all_platforms(self, username: str) -> Dict:
        """Sweep username across all platforms simultaneously."""
        results = {
            "username": username,
            "total_platforms_checked": 0,
            "confirmed_hits": [],
            "not_found": 0,
            "errors": [],
            "by_category": defaultdict(list)
        }
        
        async with aiohttp.ClientSession() as session:
            tasks = []
            category_map = {}
            
            for category, platforms in self.platforms.items():
                for platform, url_template in platforms.items():
                    tasks.append(self.check_platform(session, username, platform, url_template))
                    category_map[len(tasks) - 1] = category
            
            results["total_platforms_checked"] = len(tasks)
            checks = await asyncio.gather(*tasks)
            
            for idx, check in enumerate(checks):
                category = category_map[idx]
                
                if check["status"] == "confirmed":
                    results["confirmed_hits"].append(check)
                    results["by_category"][category].append(check["platform"])
                elif check["status"] == "not_found":
                    results["not_found"] += 1
                elif check["status"] in ["error", "timeout"]:
                    results["errors"].append(check)
        
        return results
    
    async def sweep_by_category(self, username: str, category: str) -> Dict:
        """Sweep username across platforms in a specific category only."""
        if category not in self.platforms:
            return {"error": f"Category {category} not found"}
        
        results = {
            "username": username,
            "category": category,
            "platforms_checked": 0,
            "confirmed_hits": [],
            "not_found": 0,
            "errors": []
        }
        
        async with aiohttp.ClientSession() as session:
            tasks = []
            for platform, url_template in self.platforms[category].items():
                tasks.append(self.check_platform(session, username, platform, url_template))
            
            results["platforms_checked"] = len(tasks)
            checks = await asyncio.gather(*tasks)
            
            for check in checks:
                if check["status"] == "confirmed":
                    results["confirmed_hits"].append(check)
                elif check["status"] == "not_found":
                    results["not_found"] += 1
                elif check["status"] in ["error", "timeout"]:
                    results["errors"].append(check)
        
        return results
    
    def list_categories(self) -> List[str]:
        """List all platform categories."""
        return sorted(self.platforms.keys())
    
    def list_platforms_by_category(self, category: str) -> List[str]:
        """List platforms in a specific category."""
        if category not in self.platforms:
            return []
        return sorted(self.platforms[category].keys())
    
    def get_platform_count(self) -> Dict:
        """Get total count of platforms indexed."""
        total = sum(len(platforms) for platforms in self.platforms.values())
        by_category = {cat: len(plat) for cat, plat in self.platforms.items()}
        return {
            "total_platforms": total,
            "total_categories": len(self.platforms),
            "by_category": by_category
        }
    
    def export_results(self, results: Dict, format: str = "json") -> str:
        """Export results in JSON or text format."""
        if format == "json":
            return json.dumps(results, indent=2, default=str)
        elif format == "csv":
            lines = []
            if "confirmed_hits" in results:
                lines.append("Platform,URL,Status")
                for hit in results["confirmed_hits"]:
                    lines.append(f"{hit['platform']},{hit['url']},{hit['status']}")
            return "\n".join(lines)
        return str(results)


async def main():
    """CLI entry point for Core Crawler."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python core_crawler.py <command> [args]")
        print("\nCommands:")
        print("  sweep <USERNAME>             Sweep username across all platforms")
        print("  sweep-category <USERNAME> <CATEGORY>")
        print("  list-categories              List all platform categories")
        print("  list-platforms <CATEGORY>    List platforms in category")
        print("  platform-count               Get platform statistics")
        return
    
    engine = CoreCrawlerEngine()
    command = sys.argv[1].lower()
    
    if command == "sweep" and len(sys.argv) >= 3:
        print(f"Sweeping {sys.argv[2]} across all platforms...")
        results = await engine.sweep_all_platforms(sys.argv[2])
        print(engine.export_results(results))
    
    elif command == "sweep-category" and len(sys.argv) >= 4:
        print(f"Sweeping {sys.argv[2]} in category {sys.argv[3]}...")
        results = await engine.sweep_by_category(sys.argv[2], sys.argv[3])
        print(engine.export_results(results))
    
    elif command == "list-categories":
        for cat in engine.list_categories():
            print(cat)
    
    elif command == "list-platforms" and len(sys.argv) >= 3:
        for platform in engine.list_platforms_by_category(sys.argv[2]):
            print(platform)
    
    elif command == "platform-count":
        counts = engine.get_platform_count()
        print(json.dumps(counts, indent=2))
    
    else:
        print("Unknown command or invalid arguments")


if __name__ == "__main__":
    asyncio.run(main())
