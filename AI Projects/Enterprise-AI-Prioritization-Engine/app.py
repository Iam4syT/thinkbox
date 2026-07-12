"""
app.py — Enterprise AI Prioritization & Sustainability Engine
=============================================================
Main Streamlit application entry point.

Orchestrates the UI layout, wires user inputs to the core scoring and
Green AI estimation modules, and renders the consulting analysis framework
as a real-time interactive dashboard.

Run with:
    streamlit run app.py
"""

import streamlit as st
import pandas as pd

from core_engine.scoring_engine import calculate_priority_score, determine_quadrant
from core_engine.green_ai_estimator import (
    estimate_green_ai_impact,
    get_model_options,
    get_sustainability_rating,
)

# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="Enterprise AI Prioritization Engine",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────────────────────
# CUSTOM STYLING
# ─────────────────────────────────────────────────────────────────────────────

st.markdown("""
<style>
    /* Global font and background */
    html, body, [class*="css"] { font-family: 'Segoe UI', sans-serif; }

    /* Header banner */
    .main-header {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        padding: 2rem 2.5rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
    }
    .main-header h1 { color: #ffffff; margin: 0; font-size: 1.9rem; }
    .main-header p  { color: #94a3b8; margin: 0.4rem 0 0; font-size: 1rem; }

    /* Metric cards */
    div[data-testid="metric-container"] {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 1rem;
    }

    /* Section divider */
    hr { border-color: #334155; }

    /* Quadrant result badge */
    .quadrant-badge {
        background: #1e3a5f;
        border-left: 4px solid #3b82f6;
        padding: 0.75rem 1.2rem;
        border-radius: 6px;
        color: #e2e8f0;
        font-size: 1rem;
        font-weight: 600;
        margin: 0.5rem 0 1rem;
    }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# HEADER BANNER
# ─────────────────────────────────────────────────────────────────────────────

st.markdown("""
<div class="main-header">
    <h1>🤖 Enterprise AI Prioritization &amp; Sustainability Engine</h1>
    <p>Stop chasing AI hype. Calculate ROI, Feasibility, and Carbon Footprint before you build.</p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# LAYOUT — Two-column split: inputs LEFT, analysis RIGHT
# ─────────────────────────────────────────────────────────────────────────────

col1, col2 = st.columns([1, 1.3], gap="large")

# ═══════════════════════════════════════════════════════════════════════════════
# LEFT COLUMN — INPUT PANEL
# ═══════════════════════════════════════════════════════════════════════════════

with col1:
    st.header("📋 Use Case Profile")

    use_case_name = st.text_input(
        "Use Case Name",
        placeholder="e.g., Automated Customer Support Bot",
    )
    industry = st.selectbox(
        "Industry Sector",
        ["Financial Services", "Healthcare", "Retail & E-Commerce",
         "Manufacturing", "Public Sector", "Technology", "Other"],
    )

    st.write("---")
    st.subheader("💡 Strategic Value")
    commercial_impact = st.slider(
        "Expected Commercial Impact (Revenue / Cost Savings)",
        min_value=0, max_value=100, value=50,
        help="100 = Game-changing revenue generation or transformational cost reduction.",
    )

    st.subheader("🛠️ Engineering Feasibility")
    engineering_feasibility = st.slider(
        "Engineering Feasibility (Data Readiness & Team Capability)",
        min_value=0, max_value=100, value=50,
        help="100 = Data is clean and available; out-of-the-box solution exists.",
    )

    st.write("---")
    st.subheader("🌿 Green AI Sustainability Inputs")
    model_tier = st.selectbox(
        "Expected AI Model Tier",
        options=get_model_options(),
        help="Model tier determines both cloud cost and carbon footprint.",
    )
    monthly_volume = st.number_input(
        "Estimated Monthly Inference Volume (Total Tokens)",
        min_value=1_000,
        value=5_000_000,
        step=50_000,
        help="Total tokens consumed per month across all users of this use case.",
    )

# ═══════════════════════════════════════════════════════════════════════════════
# RIGHT COLUMN — ANALYSIS RESULTS
# ═══════════════════════════════════════════════════════════════════════════════

with col2:
    st.header("📊 Strategic Analysis Assessment")

    if not use_case_name:
        st.warning("⬅️ Enter a Use Case Name in the left panel to generate the consulting framework analysis.")
    else:
        # ── Core Calculations ──────────────────────────────────────────────────
        final_score = calculate_priority_score(commercial_impact, engineering_feasibility)
        quadrant    = determine_quadrant(commercial_impact, engineering_feasibility)
        est_cost, est_co2 = estimate_green_ai_impact(monthly_volume, model_tier)
        sustainability_rating = get_sustainability_rating(est_co2)

        # ── Priority Score & Quadrant ──────────────────────────────────────────
        m1, m2 = st.columns(2)
        with m1:
            st.metric(label="🏆 Total Priority Score", value=f"{final_score} / 100")
        with m2:
            st.metric(label="📍 Industry Sector", value=industry)

        st.markdown(f'<div class="quadrant-badge">{quadrant}</div>', unsafe_allow_html=True)

        # ── Sustainability Metrics ─────────────────────────────────────────────
        st.write("---")
        st.subheader("🌱 Projected Environmental & Cloud Cost Overhead")

        s1, s2 = st.columns(2)
        with s1:
            st.metric(
                label="☁️ Estimated Azure Token Cost / Mo",
                value=f"${est_cost:,.2f}",
                delta=f"~${est_cost * 12:,.0f} annually",
                delta_color="off",
            )
        with s2:
            st.metric(
                label="🌍 Estimated CO2e Emissions / Mo",
                value=f"{est_co2} kg",
                delta=f"~{round(est_co2 * 12, 2)} kg annually",
                delta_color="off",
            )

        st.info(f"**Sustainability Rating:** {sustainability_rating}")

        # ── Consulting Recommendation ──────────────────────────────────────────
        st.write("---")
        st.subheader("🧠 Consulting Recommendation")
        st.success(
            f"**Use Case:** *{use_case_name}* has been scored **{final_score}/100** and "
            f"classified as a **{quadrant.split('—')[0].strip()}** initiative. "
            f"At {est_co2} kg CO2e/month, verify alignment with your organisation's "
            f"Net-Zero roadmap before committing to build. "
            f"Estimated 12-month cloud spend: **${est_cost * 12:,.0f}**."
        )

        # ── Comparison Table ───────────────────────────────────────────────────
        st.write("---")
        st.subheader("📋 Model Tier Comparison")
        comparison_data = {
            "Model Tier": get_model_options(),
            "Cost / Mo (USD)": [],
            "CO2e / Mo (kg)": [],
            "Annual Cost (USD)": [],
        }
        for tier in get_model_options():
            c, co2 = estimate_green_ai_impact(monthly_volume, tier)
            comparison_data["Cost / Mo (USD)"].append(f"${c:,.2f}")
            comparison_data["CO2e / Mo (kg)"].append(f"{co2}")
            comparison_data["Annual Cost (USD)"].append(f"${c * 12:,.0f}")

        st.dataframe(
            pd.DataFrame(comparison_data),
            use_container_width=True,
            hide_index=True,
        )

# ─────────────────────────────────────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────────────────────────────────────

st.write("---")
st.caption(
    "Enterprise AI Prioritization Engine v1.0 · "
    "Pricing approximated from Azure OpenAI public rate cards · "
    "Carbon metrics based on standard regional data centre emission averages."
)
