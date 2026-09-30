import streamlit as st

# ── PAGE CONFIG ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Career AI · CS Prediction",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ── GLOBAL CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* Background */
.stApp {
    background: linear-gradient(125deg, #0f0c29, #541b7d, #252a5e, #7a0bc0, #16213e);
    background-size: 300% 300%;
    animation: vibrant-flow 12s ease infinite;
    color: white !important;
}
@keyframes vibrant-flow {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
.stApp::before {
    content: "";
    position: fixed;
    top: -50%; left: -50%; width: 200%; height: 200%;
    background: repeating-radial-gradient(
        circle at center,
        rgba(255,255,255,0.07) 0px, transparent 1px, transparent 25px
    );
    z-index: 0;
    animation: wave-pulse 8s linear infinite;
    pointer-events: none;
}
@keyframes wave-pulse {
    0%   { transform: scale(1) rotate(0deg); opacity: 0.4; }
    50%  { transform: scale(1.05) rotate(2deg); opacity: 0.7; }
    100% { transform: scale(1) rotate(0deg); opacity: 0.4; }
}
.block-container {
    padding-top: 2rem !important;
    position: relative;
    z-index: 10;
    max-width: 760px !important;
    margin-left: auto !important;
    margin-right: auto !important;
    left: 0 !important;
    right: 0 !important;
    transition: all 0.3s ease !important;
}

/* Paksa main content selalu center */
.main .block-container {
    position: relative !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    float: none !important;
}

/* Reset saat sidebar terbuka */
[data-testid="stSidebar"][aria-expanded="true"] ~ .main .block-container {
    left: 50% !important;
    transform: translateX(-50%) !important;
}

/* Reset saat sidebar tertutup */
[data-testid="stSidebar"][aria-expanded="false"] ~ .main .block-container {
    left: 50% !important;
    transform: translateX(-50%) !important;
}

/* ── HEADER: sembunyikan kontennya tapi BUKAN tombol sidebar ── */
header {
    background: transparent !important;
}
header > div:first-child {
    visibility: hidden !important;
}
/* Pastikan tombol sidebar tetap visible */
header button,
header [data-testid="stSidebarCollapsedControl"],
header [data-testid="collapsedControl"] {
    visibility: visible !important;
    display: flex !important;
    opacity: 1 !important;
    pointer-events: all !important;
    z-index: 999999 !important;
    color: white !important;
}

footer { visibility: hidden; }

/* Decorative shapes */
.shape { position: fixed; opacity: 0.09; z-index: 0; pointer-events: none; }
.c1 { width: 580px; height: 580px; border: 4px solid #007AFF; border-radius: 50%; top: -160px; left: -270px; }
.s1 { width: 420px; height: 420px; border: 2px solid #ffffff; bottom: 4%; right: -160px; transform: rotate(35deg); }
.c2 { width: 240px; height: 240px; border: 2px solid #7B2FFF; border-radius: 50%; bottom: 18%; left: -70px; }

/* ── SIDEBAR ─────────────────────────────────────────────────────────────── */
[data-testid="stSidebar"] {
    background: rgba(10, 8, 30, 0.88) !important;
    backdrop-filter: blur(35px) saturate(180%) !important;
    border-right: 1px solid rgba(255,255,255,0.09) !important;
    min-width: 230px !important;
    max-width: 240px !important;
}
[data-testid="stSidebar"] * { color: white !important; }
[data-testid="stSidebarNav"] { display: none !important; }

/* Sidebar logo */
.sb-logo {
    text-align: center;
    padding: 32px 20px 24px;
    border-bottom: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 18px;
}
.sb-logo-icon { font-size: 3rem; display: block; margin-bottom: 10px; }
.sb-logo-title {
    font-size: 0.88rem;
    font-weight: 800;
    color: white !important;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin: 0 0 4px;
}
.sb-logo-sub {
    font-size: 0.65rem;
    color: rgba(255,255,255,0.35) !important;
    letter-spacing: 2px;
    text-transform: uppercase;
}
.sb-version {
    display: inline-block;
    background: rgba(0,198,255,0.15);
    border: 1px solid rgba(0,198,255,0.3);
    border-radius: 999px;
    padding: 2px 10px;
    font-size: 0.6rem;
    color: #00C6FF !important;
    margin-top: 8px;
    letter-spacing: 1px;
}

/* Nav section label */
.sb-section {
    font-size: 0.6rem;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: rgba(255,255,255,0.25) !important;
    padding: 0 20px;
    margin-bottom: 8px;
}

/* Radio → custom nav buttons */
div[data-testid="stRadio"] > div {
    display: flex !important;
    flex-direction: column !important;
    align-items: stretch !important;
    gap: 8px !important;
}
div[data-testid="stRadio"] > div > label {
    display: flex !important;
    align-items: center !important;
    width: 100% !important;
    min-height: 48px !important;
    margin: 0 !important;
    gap: 11px !important;
    padding: 14px 18px !important;
    border-radius: 14px !important;
    border: none !important;
    box-shadow: inset 0 0 0 2px transparent !important;
    background: transparent !important;
    font-size: 0.92rem !important;
    font-weight: 600 !important;
    color: rgba(255,255,255,0.55) !important;
    cursor: pointer !important;
    transition: background 0.22s, color 0.22s, box-shadow 0.22s !important;
    box-sizing: border-box !important;
}
div[data-testid="stRadio"] > div > label:hover {
    background: rgba(0,122,255,0.15) !important;
    box-shadow:
        inset 0 0 0 2px rgba(0,122,255,0.35),
        inset 4px 0 0 0 rgba(0,122,255,0.6) !important;
    color: white !important;
}
div[data-testid="stRadio"] > div > label:has(input:checked) {
    background: rgba(0,122,255,0.25) !important;
    box-shadow:
        inset 0 0 0 2px rgba(0,122,255,0.55),
        inset 5px 0 0 0 #007AFF !important;
    color: white !important;
}
div[data-testid="stRadio"] > div > label > div:first-child {
    display: none !important;
}

/* Sidebar divider */
.sb-divider {
    border: none;
    border-top: 1px solid rgba(255,255,255,0.07);
    margin: 16px 20px;
}

/* Sidebar info card */
.sb-info {
    margin: 0 10px;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 14px;
    padding: 14px 16px;
}
.sb-info-label {
    font-size: 0.62rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: rgba(255,255,255,0.25) !important;
    margin-bottom: 8px;
}
.sb-info-row {
    display: flex;
    justify-content: space-between;
    font-size: 0.75rem;
    margin-bottom: 5px;
    color: rgba(255,255,255,0.55) !important;
}
.sb-info-val { color: #00C6FF !important; font-weight: 600; }

.sb-footer {
    position: relative !important;
    margin-top: 40px !important;
    padding: 16px 0 !important;
    text-align: center;
    font-size: 0.62rem;
    color: rgba(255,255,255,0.18) !important;
    line-height: 1.8;
}
</style>
<div class="shape c1"></div>
<div class="shape s1"></div>
<div class="shape c2"></div>
""", unsafe_allow_html=True)


# ── SIDEBAR CONTENT ───────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
        <div class="sb-logo">
            <span class="sb-logo-icon">🎓</span>
            <div class="sb-logo-title">Career AI</div>
            <div class="sb-logo-sub">CS Career Predictor</div>
            <span class="sb-version">v1.0 · XGBoost</span>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sb-section">Navigation</div>', unsafe_allow_html=True)

    page = st.radio(
        label="nav",
        options=["🏠   Home", "⚙️   ML Workflow"],
        label_visibility="collapsed",
    )

    st.markdown('<hr class="sb-divider">', unsafe_allow_html=True)

    st.markdown("""
        <div class="sb-info">
            <div class="sb-info-label">Model Info</div>
            <div class="sb-info-row">
                <span>Algorithm</span>
                <span class="sb-info-val">XGBoost</span>
            </div>
            <div class="sb-info-row">
                <span>Accuracy</span>
                <span class="sb-info-val">95.71%</span>
            </div>
            <div class="sb-info-row">
                <span>Classes</span>
                <span class="sb-info-val">6 Careers</span>
            </div>
            <div class="sb-info-row">
                <span>Training Data</span>
                <span class="sb-info-val">4,076</span>
            </div>
            <div class="sb-info-row">
                <span>Features</span>
                <span class="sb-info-val">5,000 TF-IDF</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="sb-footer">
            Built with Streamlit &amp; scikit-learn<br>
            CS Career Prediction System - 2026
        </div>
    """, unsafe_allow_html=True)


# ── PAGE ROUTING ──────────────────────────────────────────────────────────────
if "Home" in page:
    import homepage
    homepage.render()
else:
    import workflow
    workflow.render()