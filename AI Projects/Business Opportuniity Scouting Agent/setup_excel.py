import pandas as pd

def create_sample_workbook(file_path: str = "initiatives.xlsx") -> None:
    """
    Generates the initial sample Excel spreadsheet for testing the Business Opportunity Scouting Agent.
    """
    data = {
        "Initiative Name": [
            "Cloud Infrastructure Modernization",
            "Customer Support Automation"
        ],
        "Documentation Link": [
            "https://en.wikipedia.org/wiki/Cloud_computing",
            "https://en.wikipedia.org/wiki/Customer_relationship_management"
        ],
        "Strategic Benefits": ["", ""],
        "Actionable OKR": ["", ""],
        "Status": ["Pending", "Pending"]
    }

    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)
    print(f"Successfully created '{file_path}'!")

if __name__ == "__main__":
    create_sample_workbook()
