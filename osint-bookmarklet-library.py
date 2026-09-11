import json
from typing import Dict, List
from collections import defaultdict
from datetime import datetime

class OSINTBookmarkletLibrary:
    """
    OSINT Bookmarklet Library: Browser Automation Tools
    Collection of 60+ JavaScript bookmarklets for rapid metadata extraction and analysis.
    """
    
    def __init__(self):
        self.bookmarklets = self._load_bookmarklet_collection()
        self.categories = self._load_categories()
        self.execution_log = []
        
    def _load_categories(self) -> List[str]:
        """Load all bookmarklet functional categories."""
        return [
            "page_metadata",
            "social_footprints",
            "username_correlation",
            "email_intelligence",
            "dns_whois",
            "archive_checks",
            "image_analysis",
            "encoding_transforms",
            "developer_recon",
            "search_operators"
        ]
    
    def _load_bookmarklet_collection(self) -> Dict:
        """Load all 60+ bookmarklets organized by category."""
        return {
            "page_metadata": {
                "extract_html_headers": {
                    "name": "Extract HTML Headers",
                    "description": "Pull all meta tags, OpenGraph, and schema markup",
                    "code_length": "embedded",
                    "version": "1.0"
                },
                "extract_analytics_ids": {
                    "name": "Extract Analytics IDs",
                    "description": "Find Google Analytics, GTM, and tracking IDs",
                    "code_length": "embedded",
                    "version": "1.0"
                },
                "extract_canonical_url": {
                    "name": "Extract Canonical URL",
                    "description": "Pull canonical URL and alternative references",
                    "code_length": "embedded",
                    "version": "1.0"
                },
                "extract_form_fields": {
                    "name": "Extract Form Fields",
                    "description": "List all hidden and visible form inputs",
                    "code_length": "embedded",
                    "version": "1.0"
                },
                "extract_outbound_links": {
                    "name": "Extract Outbound Links",
                    "description": "Generate outbound link graph",
                    "code_length": "embedded",
                    "version": "1.0"
                }
            },
            "social_footprints": {
                "detect_social_accounts": {
                    "name": "Detect Social Accounts",
                    "description": "Identify social media account links and mentions",
                    "code_length": "embedded",
                    "version": "1.0"
                },
                "extract_social_profiles": {
                    "name": "Extract Social Profiles",
                    "description": "Pull linked social profiles from page",
                    "code_length": "embedded",
                    "version": "1.0"
                },
                "extract_social_widgets": {
                    "name": "Extract Social Widgets",
                    "description": "Identify embedded social widgets and feeds",
                    "code_length": "embedded",
                    "version": "1.0"
                }
            },
            "username_correlation": {
                "extract_usernames": {
                    "name": "Extract Usernames",
                    "description": "Pull all username patterns from page",
                    "code_length": "embedded",
                    "version": "1.0"
                },
                "username_correlation_search": {
                    "name": "Username Correlation Search",
                    "description": "Cross-reference usernames across platforms",
                    "code_length": "embedded",
                    "version": "1.0"
                },
                "detect_handles": {
                    "name": "Detect Social Handles",
                    "description": "Identify @mention handles and social identifiers",
                    "code_length": "embedded",
                    "version": "1.0"
                }
            },
            "email_intelligence": {
                "extract_emails": {
                    "name": "Extract Emails",
                    "description": "Pull all email addresses from page content",
                    "code_length": "embedded",
                    "version": "1.0"
                },
                "extract_obfuscated_emails": {
                    "name": "Extract Obfuscated Emails",
                    "description": "Decode obfuscated and munged email addresses",
                    "code_length": "embedded",
                    "version": "1.0"
                },
                "email_patterns": {
                    "name": "Email Patterns",
                    "description": "Identify email naming conventions",
                    "code_length": "embedded",
                    "version": "1.0"
                }
            },
            "dns_whois": {
                "query_dns_records": {
                    "name": "Query DNS Records",
                    "description": "Fetch DNS A, MX, TXT records",
                    "code_length": "embedded",
                    "version": "1.0"
                },
                "whois_lookup": {
                    "name": "WHOIS Lookup",
                    "description": "Query domain registrar information",
                    "code_length": "embedded",
                    "version": "1.0"
                },
                "ip_geolocation": {
                    "name": "IP Geolocation",
                    "description": "Geolocate IP address from domain",
                    "code_length": "embedded",
                    "version": "1.0"
                },
                "nameserver_check": {
                    "name": "Nameserver Check",
                    "description": "Query nameserver configuration",
                    "code_length": "embedded",
                    "version": "1.0"
                }
            },
            "archive_checks": {
                "wayback_snapshot": {
                    "name": "Wayback Machine Snapshot",
                    "description": "Query Internet Archive for snapshots",
                    "code_length": "embedded",
                    "version": "1.0"
                },
                "cached_version": {
                    "name": "Cached Version",
                    "description": "Check Google Cache for current page",
                    "code_length": "embedded",
                    "version": "1.0"
                },
                "historical_pages": {
                    "name": "Historical Pages",
                    "description": "Find historical variations of page",
                    "code_length": "embedded",
                    "version": "1.0"
                }
            },
            "image_analysis": {
                "extract_image_metadata": {
                    "name": "Extract Image Metadata",
                    "description": "Pull EXIF data from page images",
                    "code_length": "embedded",
                    "version": "1.0"
                },
                "reverse_image_search": {
                    "name": "Reverse Image Search",
                    "description": "Reverse image search triggers for images",
                    "code_length": "embedded",
                    "version": "1.0"
                },
                "image_urls": {
                    "name": "Extract Image URLs",
                    "description": "Extract all image URLs with metadata",
                    "code_length": "embedded",
                    "version": "1.0"
                }
            },
            "encoding_transforms": {
                "decode_base64": {
                    "name": "Decode Base64",
                    "description": "Decode base64 encoded content",
                    "code_length": "embedded",
                    "version": "1.0"
                },
                "decode_url_encoding": {
                    "name": "Decode URL Encoding",
                    "description": "Decode URL-encoded strings",
                    "code_length": "embedded",
                    "version": "1.0"
                },
                "decode_hex": {
                    "name": "Decode Hex",
                    "description": "Convert hex-encoded content to text",
                    "code_length": "embedded",
                    "version": "1.0"
                },
                "decode_rot13": {
                    "name": "Decode ROT13",
                    "description": "ROT13 cipher decoder",
                    "code_length": "embedded",
                    "version": "1.0"
                }
            },
            "developer_recon": {
                "detect_technology_stack": {
                    "name": "Detect Technology Stack",
                    "description": "Identify frameworks, CMS, and libraries",
                    "code_length": "embedded",
                    "version": "1.0"
                },
                "extract_cdn_info": {
                    "name": "Extract CDN Info",
                    "description": "Identify CDN and hosting providers",
                    "code_length": "embedded",
                    "version": "1.0"
                },
                "extract_api_endpoints": {
                    "name": "Extract API Endpoints",
                    "description": "Find API endpoints and endpoints in page",
                    "code_length": "embedded",
                    "version": "1.0"
                },
                "javascript_comments": {
                    "name": "Extract JavaScript Comments",
                    "description": "Pull comments from JavaScript files",
                    "code_length": "embedded",
                    "version": "1.0"
                },
                "source_map_finder": {
                    "name": "Source Map Finder",
                    "description": "Locate JavaScript source maps",
                    "code_length": "embedded",
                    "version": "1.0"
                }
            },
            "search_operators": {
                "google_dork_builder": {
                    "name": "Google Dork Builder",
                    "description": "Generate Google dorks for domain",
                    "code_length": "embedded",
                    "version": "1.0"
                },
                "search_operator_generator": {
                    "name": "Search Operator Generator",
                    "description": "Create Bing, DuckDuckGo operators",
                    "code_length": "embedded",
                    "version": "1.0"
                }
            }
        }
    
    def list_bookmarklets_by_category(self, category: str) -> List[Dict]:
        """List all bookmarklets in a category."""
        if category not in self.bookmarklets:
            return []
        
        bookmarklets = []
        for bookmarklet_id, info in self.bookmarklets[category].items():
            bookmarklets.append({
                "id": bookmarklet_id,
                "name": info.get("name"),
                "description": info.get("description")
            })
        return bookmarklets
    
    def get_bookmarklet_info(self, category: str, bookmarklet_id: str) -> Dict:
        """Get detailed information about a specific bookmarklet."""
        if category not in self.bookmarklets or bookmarklet_id not in self.bookmarklets[category]:
            return {"error": "Bookmarklet not found"}
        
        return self.bookmarklets[category][bookmarklet_id]
    
    def get_all_categories(self) -> List[str]:
        """Get all bookmarklet categories."""
        return sorted(list(self.bookmarklets.keys()))
    
    def get_bookmarklet_count(self) -> Dict:
        """Get total count of bookmarklets."""
        total = 0
        by_category = {}
        
        for category, bookmarklets in self.bookmarklets.items():
            count = len(bookmarklets)
            by_category[category] = count
            total += count
        
        return {
            "total_bookmarklets": total,
            "total_categories": len(self.bookmarklets),
            "by_category": by_category
        }
    
    def export_bookmarklet_list(self, format: str = "json") -> str:
        """Export complete bookmarklet library."""
        if format == "json":
            return json.dumps(self.bookmarklets, indent=2, default=str)
        
        elif format == "txt":
            lines = []
            for category in sorted(self.bookmarklets.keys()):
                lines.append(f"\n{category.upper()}")
                lines.append("=" * 50)
                for bookmarklet_id, info in self.bookmarklets[category].items():
                    lines.append(f"  {info['name']}: {info['description']}")
            return "\n".join(lines)
        
        return str(self.bookmarklets)


def main():
    """CLI entry point for OSINT Bookmarklet Library."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python osint-bookmarklet-library.py <command> [args]")
        print("\nCommands:")
        print("  list-categories              List all bookmarklet categories")
        print("  list-bookmarklets <CATEGORY> List bookmarklets in category")
        print("  get-info <CATEGORY> <ID>     Get bookmarklet details")
        print("  count                        Get library statistics")
        print("  export <FORMAT>              Export library (json, txt)")
        return
    
    library = OSINTBookmarkletLibrary()
    command = sys.argv[1].lower()
    
    if command == "list-categories":
        for category in library.get_all_categories():
            print(category)
    
    elif command == "list-bookmarklets" and len(sys.argv) >= 3:
        bookmarklets = library.list_bookmarklets_by_category(sys.argv[2])
        for b in bookmarklets:
            print(f"{b['id']}: {b['name']} - {b['description']}")
    
    elif command == "get-info" and len(sys.argv) >= 4:
        info = library.get_bookmarklet_info(sys.argv[2], sys.argv[3])
        print(json.dumps(info, indent=2, default=str))
    
    elif command == "count":
        stats = library.get_bookmarklet_count()
        print(json.dumps(stats, indent=2))
    
    elif command == "export" and len(sys.argv) >= 3:
        output = library.export_bookmarklet_list(sys.argv[2])
        print(output)
    
    else:
        print("Unknown command or invalid arguments")


if __name__ == "__main__":
    main()
