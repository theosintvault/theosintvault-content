import asyncio
import aiohttp
import json
from typing import Dict, List, Set
from collections import defaultdict
from datetime import datetime

class MultiSearchLauncher:
    """
    Multi-Search Launcher: Search Aggregation Tool
    Executes investigative queries across multiple search engines simultaneously.
    """
    
    def __init__(self):
        self.search_engines = self._load_search_engines()
        self.results = defaultdict(list)
        self.search_history = []
        
    def _load_search_engines(self) -> Dict:
        """Load configured search engines and platforms."""
        return {
            "general": {
                "google": {
                    "url": "https://www.google.com/search",
                    "param": "q",
                    "type": "general_search"
                },
                "bing": {
                    "url": "https://www.bing.com/search",
                    "param": "q",
                    "type": "general_search"
                },
                "duckduckgo": {
                    "url": "https://duckduckgo.com/",
                    "param": "q",
                    "type": "general_search"
                },
                "yandex": {
                    "url": "https://yandex.com/search",
                    "param": "text",
                    "type": "general_search"
                }
            },
            "specialized": {
                "github": {
                    "url": "https://github.com/search",
                    "param": "q",
                    "type": "code_search"
                },
                "shodan": {
                    "url": "https://www.shodan.io/search",
                    "param": "query",
                    "type": "infrastructure"
                },
                "censys": {
                    "url": "https://search.censys.io/search",
                    "param": "q",
                    "type": "infrastructure"
                },
                "have_i_been_pwned": {
                    "url": "https://haveibeenpwned.com/",
                    "param": "query",
                    "type": "breach_search"
                }
            },
            "archives": {
                "wayback_machine": {
                    "url": "https://web.archive.org/web/*/",
                    "param": "url",
                    "type": "historical"
                },
                "google_cache": {
                    "url": "https://webcache.googleusercontent.com/",
                    "param": "url",
                    "type": "historical"
                }
            },
            "social": {
                "twitter_search": {
                    "url": "https://twitter.com/search",
                    "param": "q",
                    "type": "social_media"
                },
                "reddit": {
                    "url": "https://www.reddit.com/search",
                    "param": "q",
                    "type": "social_media"
                }
            }
        }
    
    async def search_engine(self, session: aiohttp.ClientSession, engine_name: str, query: str, engine_config: Dict) -> Dict:
        """Execute search on a single engine."""
        try:
            params = {engine_config["param"]: query}
            
            async with session.get(
                engine_config["url"],
                params=params,
                timeout=aiohttp.ClientTimeout(total=10),
                allow_redirects=True
            ) as response:
                return {
                    "engine": engine_name,
                    "status": "success" if response.status == 200 else "failed",
                    "http_code": response.status,
                    "url": str(response.url),
                    "timestamp": datetime.now().isoformat()
                }
        except asyncio.TimeoutError:
            return {
                "engine": engine_name,
                "status": "timeout",
                "error": "Request timeout",
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return {
                "engine": engine_name,
                "status": "error",
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    async def launch_multi_search(self, query: str, categories: List[str] = None) -> Dict:
        """Launch search across multiple engines simultaneously."""
        result = {
            "query": query,
            "launched_at": datetime.now().isoformat(),
            "total_engines": 0,
            "successful_searches": 0,
            "failed_searches": 0,
            "results": defaultdict(list)
        }
        
        async with aiohttp.ClientSession() as session:
            tasks = []
            engine_map = {}
            
            for category, engines in self.search_engines.items():
                if categories and category not in categories:
                    continue
                
                for engine_name, config in engines.items():
                    tasks.append(self.search_engine(session, engine_name, query, config))
                    engine_map[len(tasks) - 1] = category
            
            result["total_engines"] = len(tasks)
            searches = await asyncio.gather(*tasks)
            
            for idx, search_result in enumerate(searches):
                category = engine_map[idx]
                result["results"][category].append(search_result)
                
                if search_result["status"] == "success":
                    result["successful_searches"] += 1
                else:
                    result["failed_searches"] += 1
        
        self.search_history.append(result)
        return result
    
    def launch_batch_searches(self, queries: List[str], categories: List[str] = None) -> List[Dict]:
        """Queue multiple queries for sequential execution."""
        batch_results = []
        
        for query in queries:
            result = asyncio.run(self.launch_multi_search(query, categories))
            batch_results.append(result)
        
        return batch_results
    
    def list_search_categories(self) -> List[str]:
        """List available search categories."""
        return sorted(self.search_engines.keys())
    
    def list_engines_by_category(self, category: str) -> List[str]:
        """List engines within a category."""
        if category not in self.search_engines:
            return []
        return sorted(self.search_engines[category].keys())
    
    def get_search_stats(self) -> Dict:
        """Get statistics about search operations."""
        total_searches = len(self.search_history)
        total_successful = sum(1 for s in self.search_history if s["successful_searches"] > 0)
        
        return {
            "total_searches_executed": total_searches,
            "successful_operations": total_successful,
            "failure_rate": (total_searches - total_successful) / total_searches if total_searches > 0 else 0,
            "total_engines_queried": sum(s["total_engines"] for s in self.search_history)
        }
    
    def export_results(self, format: str = "json") -> str:
        """Export search results in JSON or CSV format."""
        if format == "json":
            return json.dumps(self.results, indent=2, default=str)
        
        elif format == "csv":
            lines = ["Engine,Status,HTTP_Code,Timestamp"]
            for category, results in self.results.items():
                for result in results:
                    lines.append(f"{result.get('engine','')},{result.get('status','')},{result.get('http_code','')},{result.get('timestamp','')}")
            return "\n".join(lines)
        
        return str(self.results)


def main():
    """CLI entry point for Multi-Search Launcher."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python multi-search-launcher.py <command> [args]")
        print("\nCommands:")
        print("  search <QUERY>               Launch multi-search")
        print("  batch <FILE>                 Execute batch searches from file")
        print("  list-categories              List search categories")
        print("  list-engines <CATEGORY>      List engines in category")
        print("  stats                        Get search statistics")
        return
    
    launcher = MultiSearchLauncher()
    command = sys.argv[1].lower()
    
    if command == "search" and len(sys.argv) >= 3:
        query = sys.argv[2]
        result = asyncio.run(launcher.launch_multi_search(query))
        print(json.dumps(result, indent=2, default=str))
    
    elif command == "list-categories":
        for category in launcher.list_search_categories():
            print(category)
    
    elif command == "list-engines" and len(sys.argv) >= 3:
        for engine in launcher.list_engines_by_category(sys.argv[2]):
            print(engine)
    
    elif command == "stats":
        stats = launcher.get_search_stats()
        print(json.dumps(stats, indent=2))
    
    else:
        print("Unknown command or invalid arguments")


if __name__ == "__main__":
    main()
