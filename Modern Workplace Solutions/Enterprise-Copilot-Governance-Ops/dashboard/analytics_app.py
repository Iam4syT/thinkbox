import matplotlib.pyplot as plt

def generate_powerbi_mock_data(df):
    """
    Structures the audit data and exports a clean visualization, demonstrating 
    the core data visualization competencies required for corporate reporting.
    """
    print("\n[PowerBI Sync Engine] Synthesizing tenant metrics for stakeholder presentation...")
    
    # Calculate executive-level operational KPIs
    total_scanned = len(df)
    critical_risks = len(df[df['ATS_Risk_Score'] > 80])
    compliance_percentage = ((total_scanned - critical_risks) / total_scanned) * 100
    
    print(f"--- Executive KPI Summary ---")
    print(f"• Total Data Estates Scanned: {total_scanned}")
    print(f"• Governance Anomalies Flagged: {critical_risks}")
    print(f"• Baseline Copilot Readiness Score: {compliance_percentage:.1f}%\n")
    
    # Generate an analytical plot mimicking a PowerBI dashboard component
    plt.figure(figsize=(8, 4.5))
    
    # Color condition: Red for high exposure risks (>80), green for compliant assets
    colors = ['#E74C3C' if score > 80 else '#2ECC71' for score in df['ATS_Risk_Score']]
    
    plt.bar(df['file_name'], df['ATS_Risk_Score'], color=colors, width=0.4)
    plt.title('M365 Data Source Risk Index (Pre-Copilot Deployment)', fontsize=11, fontweight='bold')
    plt.xlabel('Tenant Files / Assets', fontsize=9)
    plt.ylabel('Exposure Risk Score', fontsize=9)
    plt.xticks(rotation=15, ha='right', fontsize=8)
    plt.ylim(0, 110)
    plt.tight_layout()
    
    # Export visualization artifact
    plt.savefig('copilot_readiness_telemetry.png', dpi=150)
    print("[PowerBI Sync Engine] Telemetry graphic exported successfully as 'copilot_readiness_telemetry.png'.")
