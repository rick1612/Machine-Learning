import streamlit as st
import joblib
import re
import time

# ── SKILL LISTS ───────────────────────────────────────────────────────────────
HARD_SKILLS = [
    "Machine Learning", "Deep Learning", "Artificial Intelligence (AI)",
    "Natural Language Processing", "Computer Vision", "Image Processing",
    "Feature Engineering", "Data Engineering", "Data Analysis and Visualization",
    "Statistical Analysis", "Big Data Technologies", "Data Structure",
    "Web Development", "Mobile App Development", "Android App Development",
    "Game Development", "UI/UX Knowledge", "Search Engine Optimization (SEO)",
    "Cybersecurity", "Network Security", "Cryptography",
    "Operating Systems and Networking", "Network Topologies",
    "Cloud Computing", "Computer Network", "Internet of Things (IoT)",
    "Database Development", "System Design", "API Knowledge", "API Testing",
    "Software Quality Assurance", "Performance Testing",
    "Blockchain", "Robotics Knowledge",
    "Graphic Design", "Video Editing & Animation",
]

SOFT_SKILLS = [
    "Problem Solving and Analysis", "Critical Thinking", "Communication",
    "Project Management", "Adaptability", "Interpersonal Skills",
    "Research & Innovation",
]

BAR_COLORS = ["#00C6FF", "#7B2FFF", "#FF6B6B"]
RANK_ICONS = ["🥇", "🥈", "🥉"]

# ── CAREER DESCRIPTIONS ───────────────────────────────────────────────────────
CAREER_DESC = {
    "Artificial Intelligence": "Build intelligent systems, neural networks, and AI-powered applications.",
    "Data Science": "Extract insights from data using statistics, ML, and visualization.",
    "Development": "Create software applications, systems, and digital solutions.",
    "Security": "Protect systems and networks from cyber threats and vulnerabilities.",
    "Software Development and Engineering": "Design and engineer scalable, robust software systems.",
    "User Experience (UX) and User Interface (UI) Design": "Craft intuitive, beautiful digital experiences for users.",
}

# ── PREPROCESS ────────────────────────────────────────────────────────────────
def preprocess(text: str) -> str:
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    stop = {'and','or','the','a','an','in','of','to','is','for','with','on','at','by',
            'as','it','be','this','that','are','was','were','have','has','been','from',
            'not','but','if','so','do','can','will','would','could','should','may',
            'might','my','your','our','their','its','we','they','he','she','you',
            'me','him','her','us','them','what','which','who','how','when','where',
            'why','all','each','any','some','no','also','other','more','very'}
    tokens = [t for t in text.split() if t not in stop and len(t) > 1]
    return ' '.join(tokens)

# ── LOAD MODEL ────────────────────────────────────────────────────────────────
@st.cache_resource
def load_models():
    try:
        vectorizer = joblib.load("model/vectorizer.pkl")
        le         = joblib.load("model/label_encoder.pkl")
        model      = joblib.load("model/model_xgb.pkl")
        return vectorizer, le, model
    except Exception as e:
        return None, None, None

# ── HOME PAGE CSS ─────────────────────────────────────────────────────────────
HOME_CSS = """
<style>
/* Hero card */
.hero-card {
    background: linear-gradient(135deg, rgba(123,47,255,0.6) 0%, rgba(84,27,125,0.7) 100%);
    backdrop-filter: blur(40px) saturate(180%);
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 28px;
    padding: 44px 40px 36px;
    text-align: center;
    margin-bottom: 32px;
    box-shadow: 0 30px 60px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.15);
    position: relative;
    overflow: hidden;
}
.hero-card::before {
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #007AFF, #7B2FFF, #00C6FF);
    border-radius: 28px 28px 0 0;
}
.hero-icon {
    font-size: 3.5rem;
    margin-bottom: 12px;
    display: block;
    filter: drop-shadow(0 4px 12px rgba(0,198,255,0.4));
}
.hero-title {
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", sans-serif;
    color: #ffffff !important;
    font-size: 2.2rem;
    font-weight: 800;
    margin: 0 0 10px 0;
    line-height: 1.2;
    text-shadow: 0 4px 20px rgba(0,0,0,0.4);
}
.hero-sub {
    color: rgba(255,255,255,0.62) !important;
    font-size: 0.95rem;
    margin: 0;
    letter-spacing: 0.3px;
}

/* Stats row */
.stats-row {
    display: flex;
    gap: 12px;
    margin-bottom: 28px;
}
.stat-card {
    flex: 1;
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 18px;
    padding: 18px 12px;
    text-align: center;
}
.stat-num {
    font-size: 1.6rem;
    font-weight: 800;
    color: #00C6FF !important;
    display: block;
}
.stat-lbl {
    font-size: 0.7rem;
    color: rgba(255,255,255,0.45) !important;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-top: 3px;
}

/* Skill section */
.skill-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 20px;
    padding: 22px 24px;
    margin-bottom: 16px;
}
.skill-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 14px;
}
.skill-header-icon { font-size: 1.2rem; }
.skill-header-text {
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 3px;
    color: rgba(255,255,255,0.55) !important;
    text-transform: uppercase;
}

/* Multiselect overrides */
.stMultiSelect > div > div {
    background: rgba(0,0,0,0.45) !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
    border-radius: 14px !important;
    color: white !important;
}
.stMultiSelect span[data-baseweb="tag"] {
    background: rgba(0,122,255,0.65) !important;
    border-radius: 8px !important;
}
.stMultiSelect input { color: white !important; }

/* Analyze button */
.stButton > button {
    width: 100%;
    border-radius: 18px;
    height: 3.6em;
    background: linear-gradient(90deg, #007AFF 0%, #00C6FF 100%);
    color: white !important;
    font-weight: 700;
    font-size: 1rem;
    border: none;
    letter-spacing: 2px;
    transition: 0.35s all;
    box-shadow: 0 10px 30px rgba(0,122,255,0.45);
    margin-top: 8px;
}
.stButton > button:hover {
    transform: translateY(-3px) scale(1.01);
    box-shadow: 0 18px 40px rgba(0,122,255,0.65);
}

/* Result */
.result-box {
    background: rgba(255,255,255,0.07);
    backdrop-filter: blur(40px);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 26px;
    padding: 32px 36px;
    margin-top: 28px;
    box-shadow: 0 25px 55px rgba(0,0,0,0.5);
    position: relative;
    overflow: hidden;
}
.result-box::before {
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #00C6FF, #7B2FFF, #FF6B6B);
}
.result-header {
    text-align: center;
    margin-bottom: 24px;
}
.result-header-label {
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 4px;
    color: rgba(255,255,255,0.4) !important;
    text-transform: uppercase;
}
.result-header-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: white !important;
    margin-top: 4px;
}
.career-item {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 18px;
    padding: 20px 24px;
    margin-bottom: 12px;
    transition: all 0.2s;
}
.career-item:hover { border-color: rgba(255,255,255,0.22); background: rgba(255,255,255,0.09); }
.career-rank {
    font-size: 0.72rem;
    letter-spacing: 2px;
    color: rgba(255,255,255,0.4) !important;
    margin-bottom: 5px;
    text-transform: uppercase;
}
.career-name {
    font-size: 1.2rem;
    font-weight: 700;
    color: #ffffff !important;
    margin-bottom: 6px;
}
.career-desc {
    font-size: 0.8rem;
    color: rgba(255,255,255,0.45) !important;
    margin-bottom: 12px;
    line-height: 1.5;
}
.bar-bg {
    background: rgba(255,255,255,0.1);
    border-radius: 999px;
    height: 8px;
    width: 100%;
    overflow: hidden;
}
.bar-fill {
    height: 8px;
    border-radius: 999px;
}
.bar-footer {
    display: flex;
    justify-content: space-between;
    margin-top: 6px;
}
.bar-label { font-size: 0.72rem; color: rgba(255,255,255,0.35) !important; }
.pct-text { font-size: 0.85rem; font-weight: 700; }
.result-footer {
    text-align: center;
    font-size: 0.72rem;
    color: rgba(255,255,255,0.25) !important;
    margin-top: 20px;
    margin-bottom: 0;
}
</style>
"""

# ── RENDER HOMEPAGE ───────────────────────────────────────────────────────────
def render():
    st.markdown(HOME_CSS, unsafe_allow_html=True)
    vectorizer, le, model = load_models()

    # Hero card
    st.markdown("""
        <div class="hero-card">
            <span class="hero-icon">🎓</span>
            <h1 class="hero-title">Computer Science Student<br>Career Prediction</h1>
            <p class="hero-sub">Select your skills and discover your best-fit tech career path</p>
        </div>
    """, unsafe_allow_html=True)

    # Stats
    st.markdown("""
        <div class="stats-row">
            <div class="stat-card">
                <span class="stat-num">4,076</span>
                <span class="stat-lbl">Training Data</span>
            </div>
            <div class="stat-card">
                <span class="stat-num">6</span>
                <span class="stat-lbl">Career Paths</span>
            </div>
            <div class="stat-card">
                <span class="stat-num">95.71%</span>
                <span class="stat-lbl">Accuracy</span>
            </div>
            <div class="stat-card">
                <span class="stat-num">4</span>
                <span class="stat-lbl">ML Models</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    if vectorizer is None:
        st.error("⚠️ Model files not found. Pastikan folder `model/` ada dan berisi `vectorizer.pkl`, `label_encoder.pkl`, `model_xgb.pkl`.")
        return

    # Hard Skills
    st.markdown("""
        <div class="skill-card">
            <div class="skill-header">
                <span class="skill-header-icon">💻</span>
                <span class="skill-header-text">Hard Skills</span>
            </div>
    """, unsafe_allow_html=True)
    hard_selected = st.multiselect(
        label="hard_skills",
        options=HARD_SKILLS,
        placeholder="Select your technical skills...",
        label_visibility="collapsed",
    )
    if hard_selected:
        st.markdown(f"<p style='color:rgba(0,198,255,0.7);font-size:0.8rem;margin-top:6px;'>✅ {len(hard_selected)} technical skill(s) selected</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Soft Skills
    st.markdown("""
        <div class="skill-card">
            <div class="skill-header">
                <span class="skill-header-icon">🧠</span>
                <span class="skill-header-text">Soft Skills</span>
            </div>
    """, unsafe_allow_html=True)
    soft_selected = st.multiselect(
        label="soft_skills",
        options=SOFT_SKILLS,
        placeholder="Select your soft skills...",
        label_visibility="collapsed",
    )
    if soft_selected:
        st.markdown(f"<p style='color:rgba(123,47,255,0.9);font-size:0.8rem;margin-top:6px;'>✅ {len(soft_selected)} soft skill(s) selected</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Analyze Button
    if st.button("🔍  START ANALYSIS"):
        if not hard_selected:
            st.warning("⚠️ Please select at least 1 Hard Skill.")
            return
        if not soft_selected:
            st.warning("⚠️ Please select at least 1 Soft Skill.")
            return

        with st.spinner("Analyzing your career profile..."):
            time.sleep(0.8)
            all_skills  = hard_selected + soft_selected
            skills_text = preprocess(" ".join(all_skills))
            X_vec       = vectorizer.transform([skills_text])
            probas      = model.predict_proba(X_vec)[0]
            top3_idx    = probas.argsort()[::-1][:3]
            top3        = [(str(le.classes_[i]), float(probas[i])) for i in top3_idx]

        # Build result cards
        cards_html = ""
        for rank, (role, prob) in enumerate(top3):
            pct      = prob * 100
            color    = BAR_COLORS[rank]
            icon     = RANK_ICONS[rank]
            lbl      = ["TOP MATCH", "2ND MATCH", "3RD MATCH"][rank]
            desc     = CAREER_DESC.get(role, "An exciting career path in the tech industry.")

            cards_html += f"""
            <div class="career-item">
                <div class="career-rank">{icon} &nbsp;{lbl}</div>
                <div class="career-name">{role}</div>
                <div class="career-desc">{desc}</div>
                <div class="bar-bg">
                    <div class="bar-fill" style="width:{pct:.1f}%; background: linear-gradient(90deg, {color}, {color}99);"></div>
                </div>
                <div class="bar-footer">
                    <span class="bar-label">Confidence Score</span>
                    <span class="pct-text" style="color:{color};">{pct:.1f}%</span>
                </div>
            </div>
            """

        skills_shown = ", ".join(hard_selected[:4])
        if len(hard_selected) > 4:
            skills_shown += f" +{len(hard_selected)-4} more"

        st.markdown(f"""
            <div class="result-box">
                <div class="result-header">
                    <div class="result-header-label">AI Career Analysis</div>
                    <div class="result-header-title">Your Identified Career Pathways</div>
                </div>
                {cards_html}
            <p class="result-footer">
                Based on: {skills_shown} &nbsp;·&nbsp; Powered by XGBoost &nbsp;·&nbsp; Trained on 4,076 CS student profiles
            </p>
            </div>
        """, unsafe_allow_html=True)