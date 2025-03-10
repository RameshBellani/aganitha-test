from typing import List, Tuple

NON_ACADEMIC_KEYWORDS = ["Pharma", "Biotech", "Inc", "Ltd", "Corporation", "Company", "LLC"]

def identify_non_academic_authors(authors: List[str], affiliations: List[str]) -> List[Tuple[str, str]]:
    """Identify authors affiliated with pharmaceutical or biotech companies."""
    non_academic_authors = []
    
    for name, affiliation in zip(authors, affiliations):
        if any(keyword in affiliation for keyword in NON_ACADEMIC_KEYWORDS):
            non_academic_authors.append((name, affiliation))
    
    return non_academic_authors
