import pandas as pd
from dotenv import load_dotenv
from scraper import fetch_page_content
from analyzer import analyze_initiative

load_dotenv()

def run_excel_agent(file_path: str = "initiatives.xlsx") -> None:
    """
    Main orchestration loop that reads input Excel workbook, fetches URL content,
    performs AI analysis against strategic goals, and writes results back.
    
    Args:
        file_path (str): Path to the Excel workbook to process.
    """
    print(f"Starting Business Opportunity Scouting Agent...")
    print(f"Loading workbook: {file_path}...")
    try:
        df = pd.read_excel(file_path)
        # Ensure object dtype for text columns so string assignment works cleanly
        for col in ["Strategic Benefits", "Actionable OKR", "Status"]:
            if col in df.columns:
                df[col] = df[col].astype(object)
    except FileNotFoundError:
        print(f"Error: Could not find '{file_path}'. Please run setup_excel.py first.")
        return

    for index, row in df.iterrows():
        name = row["Initiative Name"]
        url = row["Documentation Link"]
        
        print(f"\n[{index + 1}/{len(df)}] Processing: {name}...")
        print(f" -> Scraping URL: {url}")
        
        content = fetch_page_content(url)
        
        if content.startswith("ERROR_FETCHING_URL"):
            print(" -> Scraping failed. Marking row as Error.")
            df.at[index, "Status"] = "Error: Invalid URL or Timeout"
            continue
            
        print(" -> Analyzing alignment against Vision & Mission...")
        result = analyze_initiative(name, content)
        
        # Update the DataFrame with AI-generated insights
        df.at[index, "Strategic Benefits"] = result["benefits"]
        df.at[index, "Actionable OKR"] = result["okr"]
        df.at[index, "Status"] = result["status"]
        print(f" -> Result Status: {result['status']}")
        
    print(f"\nSaving updated workbook back to '{file_path}'...")
    df.to_excel(file_path, index=False)
    print("Done! Open your spreadsheet to view the generated OKRs.")

if __name__ == "__main__":
    run_excel_agent("initiatives.xlsx")
