import json
from typing import Dict, List, Set
from collections import defaultdict
from datetime import datetime

class GoogleDorkGenerator:
    """
    Google Dork Generator: Query Construction Utility
    Assembles precision search strings for advanced web intelligence.
    """
    
    def __init__(self):
        self.operators = self._load_operators()
        self.file_types = self._load_file_types()
        self.presets = self._load_investigation_presets()
        self.dork_library = self._load_dork_library()
        self.generated_queries = []
        
    def _load_operators(self) -> Dict:
        """Load advanced search operators."""
        return {
            "site": {
                "description": "Restrict search to specific domain",
                "syntax": "site:example.com",
                "example": "vulnerability site:example.com"
            },
            "filetype": {
                "description": "Search for specific file types",
                "syntax": "filetype:pdf",
                "example": "budget filetype:xlsx"
            },
            "intitle": {
                "description": "Search terms in page title",
                "syntax": "intitle:admin",
                "example": "intitle:admin panel"
            },
            "inurl": {
                "description": "Search terms in URL path",
                "syntax": "inurl:admin",
                "example": "inurl:backup inurl:database"
            },
            "intext": {
                "description": "Search terms in page content",
                "syntax": "intext:secret",
                "example": "intext:API key"
            },
            "cache": {
                "description": "View cached version of page",
                "syntax": "cache:example.com",
                "example": "cache:example.com/private"
            },
            "link": {
                "description": "Find pages linking to target",
                "syntax": "link:example.com",
                "example": "link:example.com"
            },
            "related": {
                "description": "Find similar pages",
                "syntax": "related:example.com",
                "example": "related:competitor.com"
            },
            "OR": {
                "description": "Boolean OR operator",
                "syntax": "term1 OR term2",
                "example": "admin OR administrator"
            },
            "AND": {
                "description": "Boolean AND operator",
                "syntax": "term1 AND term2",
                "example": "password AND database"
            },
            "NOT": {
                "description": "Exclude terms from search",
                "syntax": "-term",
                "example": "admin -login"
            }
        }
    
    def _load_file_types(self) -> List[str]:
        """Load supported file types for search."""
        return [
            "pdf", "docx", "xlsx", "pptx", "txt", "csv", "sql", "log",
            "config", "json", "xml", "bak", "zip"
        ]
    
    def _load_investigation_presets(self) -> Dict:
        """Load pre-built dork templates for common investigations."""
        return {
            "infrastructure_recon": {
                "description": "Reconnaissance of target infrastructure",
                "template": "site:{domain} inurl:admin OR inurl:panel OR inurl:dashboard",
                "category": "infrastructure"
            },
            "admin_discovery": {
                "description": "Find administrative interfaces",
                "template": "intitle:admin OR intitle:administrator inurl:login site:{domain}",
                "category": "admin_panel"
            },
            "document_exposure": {
                "description": "Locate exposed documents",
                "template": "site:{domain} filetype:pdf OR filetype:xlsx OR filetype:docx",
                "category": "documents"
            },
            "credential_search": {
                "description": "Search for exposed credentials",
                "template": "site:{domain} intext:password OR intext:API key OR intext:token",
                "category": "credentials"
            },
            "cloud_storage": {
                "description": "Enumerate cloud storage exposures",
                "template": "site:s3.amazonaws.com OR site:storage.googleapis.com {domain}",
                "category": "cloud"
            },
            "personnel_lookup": {
                "description": "Gather personnel information",
                "template": 'site:linkedin.com/in {domain} OR site:github.com {domain}',
                "category": "personnel"
            }
        }
    
    def _load_dork_library(self) -> List[Dict]:
        """Load verified example dorks."""
        return [
            {
                "category": "admin_panels",
                "dork": "intitle:admin panel",
                "description": "Generic admin panel discovery"
            },
            {
                "category": "admin_panels",
                "dork": "intitle:cpanel inurl:login",
                "description": "cPanel login discovery"
            },
            {
                "category": "databases",
                "dork": "inurl:phpmyadmin login",
                "description": "phpMyAdmin exposure"
            },
            {
                "category": "databases",
                "dork": "filetype:sql intext:password",
                "description": "Exposed SQL databases with credentials"
            },
            {
                "category": "documents",
                "dork": "filetype:pdf inurl:internal",
                "description": "Internal documents"
            },
            {
                "category": "credentials",
                "dork": "intext:username OR intext:login filetype:txt",
                "description": "Credential files"
            },
            {
                "category": "backup_files",
                "dork": "filetype:bak OR filetype:backup",
                "description": "Backup file discovery"
            },
            {
                "category": "configuration",
                "dork": "filetype:config inurl:database",
                "description": "Configuration files with database info"
            },
            {
                "category": "api_endpoints",
                "dork": "inurl:api OR inurl:v1 OR inurl:v2 intext:API key",
                "description": "Exposed API endpoints"
            },
            {
                "category": "infrastructure",
                "dork": "inurl:status OR inurl:health intext:server",
                "description": "Server status and health endpoints"
            }
        ]
    
    def build_dork(self, operators_list: List[Dict]) -> str:
        """Construct custom dork from operator list."""
        query_parts = []
        
        for op in operators_list:
            op_type = op.get("type")
            value = op.get("value")
            
            if op_type == "site":
                query_parts.append(f"site:{value}")
            elif op_type == "filetype":
                query_parts.append(f"filetype:{value}")
            elif op_type == "intitle":
                query_parts.append(f"intitle:{value}")
            elif op_type == "inurl":
                query_parts.append(f"inurl:{value}")
            elif op_type == "intext":
                query_parts.append(f"intext:{value}")
            elif op_type == "link":
                query_parts.append(f"link:{value}")
            elif op_type == "boolean":
                query_parts.append(value)
        
        dork = " ".join(query_parts)
        self.generated_queries.append({
            "dork": dork,
            "created_at": datetime.now().isoformat()
        })
        
        return dork
    
    def apply_preset(self, preset_name: str, domain: str) -> str:
        """Apply investigation preset to domain."""
        if preset_name not in self.presets:
            return f"Error: Preset {preset_name} not found"
        
        template = self.presets[preset_name]["template"]
        dork = template.format(domain=domain)
        
        self.generated_queries.append({
            "dork": dork,
            "preset": preset_name,
            "domain": domain,
            "created_at": datetime.now().isoformat()
        })
        
        return dork
    
    def generate_batch_variants(self, base_dork: str, variations: List[str]) -> List[str]:
        """Generate multiple query variations from base dork."""
        variants = []
        
        for variant in variations:
            new_dork = base_dork.replace("{variant}", variant)
            variants.append(new_dork)
            self.generated_queries.append({
                "dork": new_dork,
                "base_dork": base_dork,
                "variant": variant,
                "created_at": datetime.now().isoformat()
            })
        
        return variants
    
    def get_dorks_by_category(self, category: str) -> List[Dict]:
        """Retrieve dorks from library by category."""
        return [d for d in self.dork_library if d["category"] == category]
    
    def list_preset_categories(self) -> List[str]:
        """List all investigation preset categories."""
        categories = set()
        for preset_info in self.presets.values():
            categories.add(preset_info.get("category", "uncategorized"))
        return sorted(list(categories))
    
    def export_generated_queries(self, format: str = "json") -> str:
        """Export all generated queries."""
        if format == "json":
            return json.dumps(self.generated_queries, indent=2, default=str)
        
        elif format == "txt":
            lines = []
            for query in self.generated_queries:
                lines.append(query["dork"])
            return "\n".join(lines)
        
        return str(self.generated_queries)


def main():
    """CLI entry point for Google Dork Generator."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python google-dork-generator.py <command> [args]")
        print("\nCommands:")
        print("  list-presets                 List investigation presets")
        print("  list-operators               List available operators")
        print("  apply-preset <PRESET> <DOMAIN>")
        print("  list-dorks <CATEGORY>       List dorks by category")
        print("  export <FORMAT>              Export generated queries")
        return
    
    generator = GoogleDorkGenerator()
    command = sys.argv[1].lower()
    
    if command == "list-presets":
        for preset_name, info in generator.presets.items():
            print(f"{preset_name}: {info['description']}")
    
    elif command == "list-operators":
        for op_name, op_info in generator.operators.items():
            print(f"{op_name}: {op_info['description']}")
    
    elif command == "apply-preset" and len(sys.argv) >= 4:
        dork = generator.apply_preset(sys.argv[2], sys.argv[3])
        print(dork)
    
    elif command == "list-dorks" and len(sys.argv) >= 3:
        dorks = generator.get_dorks_by_category(sys.argv[2])
        for dork in dorks:
            print(f"{dork['dork']} - {dork['description']}")
    
    elif command == "export" and len(sys.argv) >= 3:
        output = generator.export_generated_queries(sys.argv[2])
        print(output)
    
    else:
        print("Unknown command or invalid arguments")


if __name__ == "__main__":
    main()
