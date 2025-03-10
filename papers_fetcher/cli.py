import argparse
from papers_fetcher.fetch import fetch_pubmed_papers, get_paper_details
from papers_fetcher.filter import identify_non_academic_authors
from papers_fetcher.export import export_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers and filter non-academic authors.")
    parser.add_argument("query", type=str, help="PubMed search query")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("-f", "--file", type=str, help="Filename to save results (CSV)")

    args = parser.parse_args()

    pmids = fetch_pubmed_papers(args.query)
    papers = get_paper_details(pmids)

    filtered_papers = []
    
    for paper in papers:
        non_academic_authors = identify_non_academic_authors(paper["Authors"], paper["Affiliations"])
        if non_academic_authors:
            filtered_papers.append({
                "PubmedID": paper["PubmedID"],
                "Title": paper["Title"],
                "Publication Date": paper["Publication Date"],
                "Non-academic Author(s)": ", ".join([x[0] for x in non_academic_authors]),
                "Company Affiliation(s)": ", ".join([x[1] for x in non_academic_authors]),
                "Corresponding Author Email": ", ".join(paper["Emails"])
            })

    if args.file:
        export_to_csv(filtered_papers, args.file)
    else:
        for paper in filtered_papers:
            print(paper)

if __name__ == "__main__":
    main()
 