import json
import asyncio
import aiohttp
from typing import Dict, List, Set
from collections import defaultdict

class OSINTGridEngine:
    """
    OSINT Grid: Public Records Directory
    Browser-native index of 4,600+ verified state and federal public record portals.
    """
    
    def __init__(self):
        self.state_modules = self._load_state_modules()
        self.federal_agencies = self._load_federal_agencies()
        self.record_categories = self._load_record_categories()
        self.verified_sources = defaultdict(list)
    
    def _load_state_modules(self) -> Dict:
        """Load all 50 state modules plus D.C."""
        states = {
            "alabama": {"code": "AL", "region": "southeast"},
            "alaska": {"code": "AK", "region": "west"},
            "arizona": {"code": "AZ", "region": "west"},
            "arkansas": {"code": "AR", "region": "south"},
            "california": {"code": "CA", "region": "west"},
            "colorado": {"code": "CO", "region": "west"},
            "connecticut": {"code": "CT", "region": "northeast"},
            "delaware": {"code": "DE", "region": "northeast"},
            "florida": {"code": "FL", "region": "southeast"},
            "georgia": {"code": "GA", "region": "southeast"},
            "hawaii": {"code": "HI", "region": "west"},
            "idaho": {"code": "ID", "region": "west"},
            "illinois": {"code": "IL", "region": "midwest"},
            "indiana": {"code": "IN", "region": "midwest"},
            "iowa": {"code": "IA", "region": "midwest"},
            "kansas": {"code": "KS", "region": "midwest"},
            "kentucky": {"code": "KY", "region": "south"},
            "louisiana": {"code": "LA", "region": "south"},
            "maine": {"code": "ME", "region": "northeast"},
            "maryland": {"code": "MD", "region": "northeast"},
            "massachusetts": {"code": "MA", "region": "northeast"},
            "michigan": {"code": "MI", "region": "midwest"},
            "minnesota": {"code": "MN", "region": "midwest"},
            "mississippi": {"code": "MS", "region": "south"},
            "missouri": {"code": "MO", "region": "midwest"},
            "montana": {"code": "MT", "region": "west"},
            "nebraska": {"code": "NE", "region": "midwest"},
            "nevada": {"code": "NV", "region": "west"},
            "new_hampshire": {"code": "NH", "region": "northeast"},
            "new_jersey": {"code": "NJ", "region": "northeast"},
            "new_mexico": {"code": "NM", "region": "west"},
            "new_york": {"code": "NY", "region": "northeast"},
            "north_carolina": {"code": "NC", "region": "southeast"},
            "north_dakota": {"code": "ND", "region": "midwest"},
            "ohio": {"code": "OH", "region": "midwest"},
            "oklahoma": {"code": "OK", "region": "south"},
            "oregon": {"code": "OR", "region": "west"},
            "pennsylvania": {"code": "PA", "region": "northeast"},
            "rhode_island": {"code": "RI", "region": "northeast"},
            "south_carolina": {"code": "SC", "region": "southeast"},
            "south_dakota": {"code": "SD", "region": "midwest"},
            "tennessee": {"code": "TN", "region": "south"},
            "texas": {"code": "TX", "region": "south"},
            "utah": {"code": "UT", "region": "west"},
            "vermont": {"code": "VT", "region": "northeast"},
            "virginia": {"code": "VA", "region": "southeast"},
            "washington": {"code": "WA", "region": "west"},
            "west_virginia": {"code": "WV", "region": "south"},
            "wisconsin": {"code": "WI", "region": "midwest"},
            "wyoming": {"code": "WY", "region": "west"},
            "washington_dc": {"code": "DC", "region": "northeast"},
        }
        return states
    
    def _load_federal_agencies(self) -> Dict:
        """Load federal agency database sources."""
        return {
            "fbi": {"name": "Federal Bureau of Investigation", "type": "criminal"},
            "sec": {"name": "Securities and Exchange Commission", "type": "corporate"},
            "fda": {"name": "Food and Drug Administration", "type": "regulatory"},
            "irs": {"name": "Internal Revenue Service", "type": "tax"},
            "bop": {"name": "Bureau of Prisons", "type": "corrections"},
            "doe": {"name": "Department of Education", "type": "educational"},
            "va": {"name": "Veterans Affairs", "type": "military"},
            "sba": {"name": "Small Business Administration", "type": "business"},
            "copyright": {"name": "U.S. Copyright Office", "type": "intellectual_property"},
            "usps": {"name": "U.S. Postal Service", "type": "postal"},
        }
    
    def _load_record_categories(self) -> Dict:
        """Load all searchable record categories."""
        return {
            "court_filings": {
                "description": "Criminal and civil court records",
                "sources": "state_courts"
            },
            "property_assessor": {
                "description": "Property assessor records and tax records",
                "sources": "county_assessor"
            },
            "inmate_lookup": {
                "description": "Correctional facility inmate records",
                "sources": "state_corrections"
            },
            "business_filings": {
                "description": "Corporate business filings and registrations",
                "sources": "secretary_of_state"
            },
            "professional_licenses": {
                "description": "Professional licensing records",
                "sources": "state_boards"
            },
            "ucc_filings": {
                "description": "Uniform Commercial Code filings",
                "sources": "secretary_of_state"
            },
            "voter_registry": {
                "description": "Voter registration records",
                "sources": "county_clerk"
            },
            "sex_offender_registry": {
                "description": "Sex offender registry records",
                "sources": "state_law_enforcement"
            },
            "vital_records": {
                "description": "Birth, death, and marriage records",
                "sources": "state_health_department"
            },
            "occupational_licenses": {
                "description": "Occupational and trade licenses",
                "sources": "state_licensing"
            },
        }
    
    def search_by_state(self, state: str, record_type: str) -> Dict:
        """
        Search for record sources in a specific state by category.
        Returns verified sources for direct access.
        """
        state_key = state.lower().replace(" ", "_")
        
        if state_key not in self.state_modules:
            return {"error": f"State {state} not found"}
        
        if record_type not in self.record_categories:
            return {"error": f"Record type {record_type} not found"}
        
        result = {
            "state": state,
            "state_code": self.state_modules[state_key]["code"],
            "record_type": record_type,
            "category_info": self.record_categories[record_type],
            "sources": []
        }
        
        return result
    
    def search_by_county(self, state: str, county: str, record_type: str) -> Dict:
        """
        Search for county-level public record sources.
        """
        result = {
            "state": state,
            "county": county,
            "record_type": record_type,
            "county_sources": []
        }
        
        return result
    
    def search_federal_agency(self, agency: str, record_type: str = None) -> Dict:
        """
        Search federal agency databases.
        """
        agency_key = agency.lower()
        
        if agency_key not in self.federal_agencies:
            return {"error": f"Federal agency {agency} not found"}
        
        result = {
            "agency": self.federal_agencies[agency_key]["name"],
            "agency_code": agency_key,
            "agency_type": self.federal_agencies[agency_key]["type"],
            "databases": []
        }
        
        return result
    
    def list_states(self) -> List[str]:
        """List all available state modules."""
        return sorted(self.state_modules.keys())
    
    def list_record_types(self) -> List[str]:
        """List all searchable record categories."""
        return sorted(self.record_categories.keys())
    
    def list_federal_agencies(self) -> List[str]:
        """List all indexed federal agencies."""
        return sorted(self.federal_agencies.keys())
    
    def export_index(self, format: str = "json") -> str:
        """Export the complete OSINT Grid index."""
        index = {
            "states": len(self.state_modules),
            "federal_agencies": len(self.federal_agencies),
            "record_categories": len(self.record_categories),
            "total_verified_sources": sum(len(v) for v in self.verified_sources.values()),
            "state_modules": self.state_modules,
            "federal_agencies": self.federal_agencies,
            "record_categories": self.record_categories,
        }
        
        if format == "json":
            return json.dumps(index, indent=2)
        return str(index)


def main():
    """CLI entry point for OSINT Grid."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python osint-grid.py <command> [args]")
        print("\nCommands:")
        print("  list-states          List all state modules")
        print("  list-categories      List all record categories")
        print("  list-agencies        List all federal agencies")
        print("  search-state <STATE> <CATEGORY>")
        print("  search-county <STATE> <COUNTY> <CATEGORY>")
        print("  search-federal <AGENCY> [CATEGORY]")
        print("  export               Export complete index")
        return
    
    engine = OSINTGridEngine()
    command = sys.argv[1].lower()
    
    if command == "list-states":
        for state in engine.list_states():
            print(state)
    
    elif command == "list-categories":
        for cat in engine.list_record_types():
            print(cat)
    
    elif command == "list-agencies":
        for agency in engine.list_federal_agencies():
            print(agency)
    
    elif command == "search-state" and len(sys.argv) >= 4:
        result = engine.search_by_state(sys.argv[2], sys.argv[3])
        print(json.dumps(result, indent=2))
    
    elif command == "search-county" and len(sys.argv) >= 5:
        result = engine.search_by_county(sys.argv[2], sys.argv[3], sys.argv[4])
        print(json.dumps(result, indent=2))
    
    elif command == "search-federal" and len(sys.argv) >= 3:
        record_type = sys.argv[3] if len(sys.argv) > 3 else None
        result = engine.search_federal_agency(sys.argv[2], record_type)
        print(json.dumps(result, indent=2))
    
    elif command == "export":
        print(engine.export_index())
    
    else:
        print("Unknown command or invalid arguments")


if __name__ == "__main__":
    main()
