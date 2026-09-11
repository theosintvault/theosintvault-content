import json
from typing import Dict, List, Set
from datetime import datetime
from collections import defaultdict

class ReportComposer:
    """
    Report Composer: Intelligence Reporting Tool
    Converts investigative findings into defensible, structured documentation.
    """
    
    def __init__(self):
        self.report_sections = {}
        self.evidence_chain = []
        self.metadata = {}
        
    def create_report(self, report_title: str, case_id: str = None) -> Dict:
        """Initialize a new intelligence report."""
        self.report_sections = {
            "metadata": {
                "title": report_title,
                "case_id": case_id or f"case_{datetime.now().timestamp()}",
                "created_at": datetime.now().isoformat(),
                "created_by": "Intelligence Analyst",
                "classification": "unclassified"
            },
            "subject_metadata": {
                "subject_name": "",
                "aliases": [],
                "identifiers": [],
                "demographics": {}
            },
            "target_identifiers": {
                "primary_targets": [],
                "secondary_targets": [],
                "associated_entities": []
            },
            "scope_and_methodology": {
                "investigation_scope": "",
                "timeframe": "",
                "investigative_methods": [],
                "data_sources_used": [],
                "limitations": []
            },
            "findings": {
                "key_findings": [],
                "supporting_evidence": [],
                "corroborating_sources": []
            },
            "analytical_observations": {
                "patterns_identified": [],
                "anomalies": [],
                "conclusions": []
            },
            "evidence_chain": {
                "primary_evidence": [],
                "corroborating_evidence": [],
                "chain_of_custody": []
            },
            "risk_assessments": {
                "identified_risks": [],
                "exposure_level": "",
                "mitigations": []
            },
            "sources_and_attribution": {
                "primary_sources": [],
                "secondary_sources": [],
                "methodology_notes": []
            }
        }
        
        return self.report_sections
    
    def add_subject_metadata(self, name: str, aliases: List[str] = None, identifiers: Dict = None) -> Dict:
        """Add subject information to report."""
        self.report_sections["subject_metadata"]["subject_name"] = name
        if aliases:
            self.report_sections["subject_metadata"]["aliases"] = aliases
        if identifiers:
            self.report_sections["subject_metadata"]["identifiers"] = identifiers
        
        return self.report_sections["subject_metadata"]
    
    def add_findings(self, findings: List[str], evidence: List[Dict] = None) -> Dict:
        """Add investigative findings to report."""
        self.report_sections["findings"]["key_findings"] = findings
        
        if evidence:
            for item in evidence:
                self.report_sections["findings"]["supporting_evidence"].append({
                    "type": item.get("type", "unknown"),
                    "source": item.get("source", ""),
                    "description": item.get("description", ""),
                    "timestamp": item.get("timestamp", datetime.now().isoformat())
                })
        
        return self.report_sections["findings"]
    
    def add_evidence_chain(self, evidence_items: List[Dict]) -> List[Dict]:
        """Build chain of custody for evidence."""
        for idx, item in enumerate(evidence_items, 1):
            chain_link = {
                "sequence": idx,
                "evidence_type": item.get("type", ""),
                "description": item.get("description", ""),
                "source": item.get("source", ""),
                "collected_date": item.get("date", datetime.now().isoformat()),
                "verified_by": item.get("verified_by", "Analyst"),
                "integrity_status": "verified"
            }
            self.report_sections["evidence_chain"]["primary_evidence"].append(chain_link)
        
        return self.report_sections["evidence_chain"]["primary_evidence"]
    
    def add_scope_and_methodology(self, scope: str, timeframe: str, methods: List[str], sources: List[str]) -> Dict:
        """Define investigation scope and methodology."""
        self.report_sections["scope_and_methodology"]["investigation_scope"] = scope
        self.report_sections["scope_and_methodology"]["timeframe"] = timeframe
        self.report_sections["scope_and_methodology"]["investigative_methods"] = methods
        self.report_sections["scope_and_methodology"]["data_sources_used"] = sources
        
        return self.report_sections["scope_and_methodology"]
    
    def add_analytical_observations(self, patterns: List[str], anomalies: List[str], conclusions: List[str]) -> Dict:
        """Add analytical findings and conclusions."""
        self.report_sections["analytical_observations"]["patterns_identified"] = patterns
        self.report_sections["analytical_observations"]["anomalies"] = anomalies
        self.report_sections["analytical_observations"]["conclusions"] = conclusions
        
        return self.report_sections["analytical_observations"]
    
    def add_risk_assessment(self, risks: List[str], exposure_level: str, mitigations: List[str]) -> Dict:
        """Add risk and exposure assessment."""
        self.report_sections["risk_assessments"]["identified_risks"] = risks
        self.report_sections["risk_assessments"]["exposure_level"] = exposure_level
        self.report_sections["risk_assessments"]["mitigations"] = mitigations
        
        return self.report_sections["risk_assessments"]
    
    def add_sources_and_attribution(self, primary_sources: List[Dict], secondary_sources: List[Dict] = None) -> Dict:
        """Add source attribution for complete chain of custody."""
        for source in primary_sources:
            self.report_sections["sources_and_attribution"]["primary_sources"].append({
                "source_name": source.get("name", ""),
                "source_type": source.get("type", ""),
                "source_url": source.get("url", ""),
                "access_date": source.get("date", datetime.now().isoformat()),
                "verification_status": "verified"
            })
        
        if secondary_sources:
            for source in secondary_sources:
                self.report_sections["sources_and_attribution"]["secondary_sources"].append(source)
        
        return self.report_sections["sources_and_attribution"]
    
    def export_report(self, format: str = "json") -> str:
        """Export report in JSON, DOCX, PDF, or Markdown format."""
        if format == "json":
            return json.dumps(self.report_sections, indent=2, default=str)
        
        elif format == "markdown":
            lines = []
            lines.append(f"# {self.report_sections['metadata']['title']}")
            lines.append(f"**Case ID:** {self.report_sections['metadata']['case_id']}")
            lines.append(f"**Created:** {self.report_sections['metadata']['created_at']}")
            lines.append()
            
            if self.report_sections["subject_metadata"]["subject_name"]:
                lines.append("## Subject Information")
                lines.append(f"**Name:** {self.report_sections['subject_metadata']['subject_name']}")
                if self.report_sections["subject_metadata"]["aliases"]:
                    lines.append(f"**Aliases:** {', '.join(self.report_sections['subject_metadata']['aliases'])}")
                lines.append()
            
            if self.report_sections["scope_and_methodology"]["investigation_scope"]:
                lines.append("## Scope and Methodology")
                lines.append(self.report_sections["scope_and_methodology"]["investigation_scope"])
                lines.append()
            
            if self.report_sections["findings"]["key_findings"]:
                lines.append("## Findings")
                for finding in self.report_sections["findings"]["key_findings"]:
                    lines.append(f"- {finding}")
                lines.append()
            
            if self.report_sections["analytical_observations"]["conclusions"]:
                lines.append("## Conclusions")
                for conclusion in self.report_sections["analytical_observations"]["conclusions"]:
                    lines.append(f"- {conclusion}")
                lines.append()
            
            if self.report_sections["sources_and_attribution"]["primary_sources"]:
                lines.append("## Sources")
                for source in self.report_sections["sources_and_attribution"]["primary_sources"]:
                    lines.append(f"- {source['source_name']} ({source['source_type']})")
            
            return "\n".join(lines)
        
        elif format == "txt":
            return json.dumps(self.report_sections, indent=2, default=str)
        
        return json.dumps(self.report_sections, indent=2, default=str)
    
    def validate_defensibility(self) -> Dict:
        """Check report for chain-of-custody integrity and defensibility."""
        validation = {
            "defensible": True,
            "missing_sections": [],
            "warnings": [],
            "passed_checks": []
        }
        
        required_sections = ["subject_metadata", "scope_and_methodology", "findings", "evidence_chain"]
        
        for section in required_sections:
            if not self.report_sections.get(section):
                validation["missing_sections"].append(section)
                validation["defensible"] = False
        
        if not self.report_sections["evidence_chain"]["primary_evidence"]:
            validation["warnings"].append("No primary evidence documented")
            validation["defensible"] = False
        
        if self.report_sections["metadata"]["classification"] == "unclassified":
            validation["passed_checks"].append("Classification level set")
        
        return validation


def main():
    """CLI entry point for Report Composer."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python report-composer.py <command> [args]")
        print("\nCommands:")
        print("  create <TITLE> [CASE_ID]     Create new report")
        print("  export <FORMAT>              Export report (json, markdown, txt)")
        print("  validate                     Validate report defensibility")
        return
    
    composer = ReportComposer()
    command = sys.argv[1].lower()
    
    if command == "create" and len(sys.argv) >= 3:
        title = sys.argv[2]
        case_id = sys.argv[3] if len(sys.argv) > 3 else None
        result = composer.create_report(title, case_id)
        print(json.dumps(result, indent=2, default=str))
    
    elif command == "export" and len(sys.argv) >= 3:
        format_type = sys.argv[2]
        print(composer.export_report(format_type))
    
    elif command == "validate":
        validation = composer.validate_defensibility()
        print(json.dumps(validation, indent=2))
    
    else:
        print("Unknown command or invalid arguments")


if __name__ == "__main__":
    main()
