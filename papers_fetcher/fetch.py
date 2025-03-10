import requests
import xml.etree.ElementTree as ET
from typing import List, Dict

PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

def fetch_pubmed_papers(query: str, max_results: int = 20) -> List[str]:
    """Fetch PubMed paper IDs based on the given query."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }
    response = requests.get(PUBMED_API_URL, params=params)
    response.raise_for_status()
    data = response.json()

    return data["esearchresult"]["idlist"]

def get_paper_details(pmids: List[str]) -> List[Dict]:
    """Fetch detailed metadata for PubMed papers."""
    params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "xml"
    }
    response = requests.get(PUBMED_FETCH_URL, params=params)
    response.raise_for_status()
    
    papers = []
    root = ET.fromstring(response.text)
    
    for article in root.findall(".//PubmedArticle"):
        pmid = article.find(".//PMID").text
        title = article.find(".//ArticleTitle").text
        pub_date = article.find(".//PubDate/Year")
        pub_date = pub_date.text if pub_date is not None else "Unknown"
        
        authors = []
        affiliations = []
        emails = []
        
        for author in article.findall(".//Author"):
            lastname = author.find("LastName")
            firstname = author.find("ForeName")
            aff = author.find("AffiliationInfo/Affiliation")

            name = f"{firstname.text} {lastname.text}" if firstname is not None and lastname is not None else "Unknown"
            affiliation = aff.text if aff is not None else "Unknown"

            if affiliation and "@" in affiliation:
                emails.append(affiliation.split()[-1])  # Extract email if present
            
            authors.append(name)
            affiliations.append(affiliation)

        papers.append({
            "PubmedID": pmid,
            "Title": title,
            "Publication Date": pub_date,
            "Authors": authors,
            "Affiliations": affiliations,
            "Emails": emails
        })
    
    return papers
