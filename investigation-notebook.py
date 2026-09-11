import json
import re
from typing import Dict, List, Set, Tuple
from collections import defaultdict
from datetime import datetime

class InvestigationNotebook:
    """
    Investigation Notebook: Note Organizer and Data Extraction
    Parses unstructured investigation records into clean, intelligence-ready data.
    """
    
    def __init__(self):
        self.entities = defaultdict(list)
        self.timelines = []
        self.financial_markers = []
        self.property_references = []
        self.litigation_notes = []
        self.sources = []
        self.conflicts = []
        self.duplicates = []
        
    def _extract_entities(self, text: str) -> Dict:
        """Extract key entities from text: names, emails, phones, domains, URLs."""
        entities = {
            "names": [],
            "emails": [],
            "phones": [],
            "domains": [],
            "urls": [],
            "ip_addresses": [],
            "social_handles": []
        }
        
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        entities["emails"] = list(set(re.findall(email_pattern, text)))
        
        phone_pattern = r'(\+?1?[-.\s]?)?\(?[0-9]{3}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}'
        entities["phones"] = list(set(re.findall(phone_pattern, text)))
        
        domain_pattern = r'(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,}'
        entities["domains"] = list(set(re.findall(domain_pattern, text.lower())))
        
        url_pattern = r'https?://[^\s]+'
        entities["urls"] = list(set(re.findall(url_pattern, text)))
        
        ip_pattern = r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
        entities["ip_addresses"] = list(set(re.findall(ip_pattern, text)))
        
        handle_pattern = r'@[a-zA-Z0-9_]{1,15}'
        entities["social_handles"] = list(set(re.findall(handle_pattern, text)))
        
        return entities
    
    def _extract_dates(self, text: str) -> List[Dict]:
        """Extract dates and timeline events from text."""
        timeline = []
        date_patterns = [
            (r'\d{1,2}/\d{1,2}/\d{4}', 'MM/DD/YYYY'),
            (r'\d{4}-\d{1,2}-\d{1,2}', 'YYYY-MM-DD'),
            (r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4}', 'Full Date'),
        ]
        
        for pattern, format_type in date_patterns:
            matches = re.findall(pattern, text)
            for match in matches:
                timeline.append({
                    "date": match,
                    "format": format_type,
                    "context": self._get_context(text, match)
                })
        
        return timeline
    
    def _extract_financial_markers(self, text: str) -> List[Dict]:
        """Extract financial references: amounts, accounts, transactions."""
        markers = []
        
        amount_pattern = r'\$[0-9]{1,3}(?:,[0-9]{3})*(?:\.[0-9]{2})?'
        amounts = re.findall(amount_pattern, text)
        for amount in amounts:
            markers.append({
                "type": "monetary_amount",
                "value": amount,
                "context": self._get_context(text, amount)
            })
        
        account_pattern = r'(?:account|acct|acc)\s*(?:number|#)?\s*[:\-]?\s*([0-9*X]{8,})'
        accounts = re.findall(account_pattern, text, re.IGNORECASE)
        for account in accounts:
            markers.append({
                "type": "account_reference",
                "value": account,
                "context": self._get_context(text, account)
            })
        
        return markers
    
    def _extract_property_references(self, text: str) -> List[Dict]:
        """Extract property and location references."""
        properties = []
        
        address_pattern = r'\d+\s+[A-Za-z\s]+(?:Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Lane|Ln|Drive|Dr|Court|Ct|Circle|Cir|Way|Place|Pl|Park|Parkway|Pkwy)'
        addresses = re.findall(address_pattern, text)
        for address in set(addresses):
            properties.append({
                "type": "street_address",
                "value": address,
                "context": self._get_context(text, address)
            })
        
        zip_pattern = r'\d{5}(?:-\d{4})?'
        zips = re.findall(zip_pattern, text)
        for zip_code in set(zips):
            properties.append({
                "type": "postal_code",
                "value": zip_code
            })
        
        return properties
    
    def _detect_conflicts(self, extracted_data: Dict) -> List[Dict]:
        """Identify conflicting or duplicate information."""
        conflicts = []
        
        if "emails" in extracted_data:
            emails = extracted_data["emails"]
            if len(emails) != len(set(emails)):
                conflicts.append({
                    "type": "duplicate_email",
                    "values": [e for e in emails if emails.count(e) > 1],
                    "severity": "low"
                })
        
        if "domains" in extracted_data:
            domains = extracted_data["domains"]
            if len(domains) != len(set(domains)):
                conflicts.append({
                    "type": "duplicate_domain",
                    "values": [d for d in domains if domains.count(d) > 1],
                    "severity": "low"
                })
        
        return conflicts
    
    def _get_context(self, text: str, match: str, context_length: int = 50) -> str:
        """Extract surrounding context for a matched string."""
        idx = text.find(match)
        if idx == -1:
            return ""
        start = max(0, idx - context_length)
        end = min(len(text), idx + len(match) + context_length)
        return text[start:end].strip()
    
    def process_text(self, text: str, case_id: str = None) -> Dict:
        """Process raw text and extract all structured data."""
        result = {
            "case_id": case_id or f"case_{datetime.now().timestamp()}",
            "processed_at": datetime.now().isoformat(),
            "extracted_data": {}
        }
        
        entities = self._extract_entities(text)
        timelines = self._extract_dates(text)
        financial = self._extract_financial_markers(text)
        properties = self._extract_property_references(text)
        conflicts = self._detect_conflicts(entities)
        
        result["extracted_data"]["entities"] = entities
        result["extracted_data"]["timelines"] = timelines
        result["extracted_data"]["financial_markers"] = financial
        result["extracted_data"]["property_references"] = properties
        result["extracted_data"]["conflicts"] = conflicts
        
        return result
    
    def process_document(self, filename: str, file_type: str) -> Dict:
        """Process uploaded document (PDF, DOCX, DOC, TXT, RTF)."""
        supported_types = ["pdf", "docx", "doc", "txt", "rtf"]
        
        if file_type.lower() not in supported_types:
            return {"error": f"Unsupported file type: {file_type}"}
        
        result = {
            "filename": filename,
            "file_type": file_type,
            "processing_status": "pending",
            "extracted_content": None
        }
        
        return result
    
    def flag_duplicates(self, case_data: Dict) -> List[Dict]:
        """Scan for overlapping entity details and flag potential duplicates."""
        duplicates = []
        
        if "extracted_data" in case_data:
            data = case_data["extracted_data"]
            
            if "entities" in data:
                for entity_type, entities in data["entities"].items():
                    unique_count = len(set(entities))
                    total_count = len(entities)
                    if unique_count < total_count:
                        duplicates.append({
                            "type": f"duplicate_{entity_type}",
                            "count": total_count - unique_count,
                            "examples": list(set([e for e in entities if entities.count(e) > 1]))
                        })
        
        return duplicates
    
    def export_structured_notes(self, case_data: Dict, format: str = "json") -> str:
        """Export structured notes in JSON, TXT, or other formats."""
        if format == "json":
            return json.dumps(case_data, indent=2, default=str)
        
        elif format == "txt":
            lines = []
            lines.append(f"Case ID: {case_data.get('case_id', 'Unknown')}")
            lines.append(f"Processed: {case_data.get('processed_at', 'Unknown')}")
            lines.append("")
            
            if "extracted_data" in case_data:
                data = case_data["extracted_data"]
                
                if "entities" in data:
                    lines.append("EXTRACTED ENTITIES")
                    lines.append("=" * 50)
                    for entity_type, entities in data["entities"].items():
                        if entities:
                            lines.append(f"\n{entity_type.upper()}:")
                            for e in entities:
                                lines.append(f"  - {e}")
                
                if "timelines" in data and data["timelines"]:
                    lines.append("\n\nTIMELINE EVENTS")
                    lines.append("=" * 50)
                    for event in data["timelines"]:
                        lines.append(f"  {event['date']}: {event.get('context', '')[:100]}")
                
                if "financial_markers" in data and data["financial_markers"]:
                    lines.append("\n\nFINANCIAL MARKERS")
                    lines.append("=" * 50)
                    for marker in data["financial_markers"]:
                        lines.append(f"  {marker['type']}: {marker['value']}")
                
                if "conflicts" in data and data["conflicts"]:
                    lines.append("\n\nCONFLICTS AND DUPLICATES")
                    lines.append("=" * 50)
                    for conflict in data["conflicts"]:
                        lines.append(f"  {conflict['type']}: {conflict.get('values', '')}")
            
            return "\n".join(lines)
        
        return str(case_data)


def main():
    """CLI entry point for Investigation Notebook."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python investigation-notebook.py <command> [args]")
        print("\nCommands:")
        print("  process-text <FILENAME>      Process raw text file")
        print("  process-document <FILENAME>  Process document (PDF, DOCX, etc)")
        print("  export <CASE_ID> <FORMAT>   Export structured notes")
        return
    
    notebook = InvestigationNotebook()
    command = sys.argv[1].lower()
    
    if command == "process-text" and len(sys.argv) >= 3:
        try:
            with open(sys.argv[2], 'r') as f:
                text = f.read()
            result = notebook.process_text(text, case_id=sys.argv[2])
            print(json.dumps(result, indent=2, default=str))
        except FileNotFoundError:
            print(f"File not found: {sys.argv[2]}")
    
    elif command == "process-document" and len(sys.argv) >= 3:
        filename = sys.argv[2]
        file_type = sys.argv[3] if len(sys.argv) > 3 else filename.split('.')[-1]
        result = notebook.process_document(filename, file_type)
        print(json.dumps(result, indent=2, default=str))
    
    else:
        print("Unknown command or invalid arguments")


if __name__ == "__main__":
    main()
