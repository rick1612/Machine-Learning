import streamlit as st

WORKFLOW_CSS = """
<style>
/* Page header */
.wf-page-header {
    background: linear-gradient(135deg, rgba(123,47,255,0.5) 0%, rgba(84,27,125,0.6) 100%);
    backdrop-filter: blur(40px);
    border: 1px solid rgba(255,255,255,0.18);
    border-radius: 24px;
    padding: 36px 40px;
    text-align: center;
    margin-bottom: 36px;
    position: relative;
    overflow: hidden;
}
.wf-page-header::before {
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0; height: 3px;
    background: linear-gradient(90deg, #007AFF, #7B2FFF, #00C6FF, #FF6B6B);
    border-radius: 24px 24px 0 0;
}
.wf-page-title {
    font-size: 1.9rem;
    font-weight: 800;
    color: white !important;
    margin: 0 0 8px 0;
}
.wf-page-sub {
    font-size: 0.9rem;
    color: rgba(255,255,255,0.55) !important;
    margin: 0;
}

/* Flow container */
.flow-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0;
    padding: 0 8px;
}

/* Step node */
.step-node {
    width: 100%;
    max-width: 1000px;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.14);
    border-radius: 20px;
    padding: 24px 28px;
    position: relative;
    transition: all 0.25s;
}
.step-node:hover {
    background: rgba(255,255,255,0.1);
    border-color: rgba(255,255,255,0.25);
    transform: translateY(-2px);
    box-shadow: 0 15px 35px rgba(0,0,0,0.35);
}
.step-node.accent-blue  { border-left: 4px solid #007AFF; }
.step-node.accent-cyan  { border-left: 4px solid #00C6FF; }
.step-node.accent-purple{ border-left: 4px solid #7B2FFF; }
.step-node.accent-green { border-left: 4px solid #30D158; }
.step-node.accent-orange{ border-left: 4px solid #FF9F0A; }
.step-node.accent-red   { border-left: 4px solid #FF6B6B; }
.step-node.accent-teal  { border-left: 4px solid #5AC8FA; }

.step-header {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 14px;
}
.step-icon {
    width: 44px; height: 44px;
    border-radius: 13px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.3rem;
    flex-shrink: 0;
}
.step-icon.bg-blue   { background: rgba(0,122,255,0.25); }
.step-icon.bg-cyan   { background: rgba(0,198,255,0.25); }
.step-icon.bg-purple { background: rgba(123,47,255,0.25); }
.step-icon.bg-green  { background: rgba(48,209,88,0.25); }
.step-icon.bg-orange { background: rgba(255,159,10,0.25); }
.step-icon.bg-red    { background: rgba(255,107,107,0.25); }
.step-icon.bg-teal   { background: rgba(90,200,250,0.25); }

.step-meta { flex: 1; }
.step-badge {
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    margin-bottom: 3px;
}
.step-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: white !important;
    margin: 0;
}

/* Sub items */
.sub-items {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 6px;
}
.sub-chip {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 999px;
    padding: 6px 14px;
    font-size: 0.8rem;
    color: rgba(255,255,255,0.8) !important;
    display: flex;
    align-items: center;
    gap: 7px;
}
.sub-chip .chip-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    flex-shrink: 0;
}

/* Description */
.step-desc {
    font-size: 0.82rem;
    color: rgba(255,255,255,0.5) !important;
    margin-top: 10px;
    line-height: 1.6;
    padding-top: 12px;
    border-top: 1px solid rgba(255,255,255,0.07);
}

/* Arrow connector */
.arrow-connector {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0;
    padding: 4px 0;
    width: 100%;
    max-width: 1000px;
}
.arrow-line {
    width: 2px;
    height: 22px;
    background: linear-gradient(180deg, rgba(255,255,255,0.15), rgba(255,255,255,0.4));
}
.arrow-head {
    width: 0; height: 0;
    border-left: 7px solid transparent;
    border-right: 7px solid transparent;
    border-top: 9px solid rgba(255,255,255,0.4);
}

/* Model comparison table */
.model-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 12px;
}
.model-table th {
    font-size: 0.7rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: rgba(255,255,255,0.4) !important;
    padding: 8px 12px;
    text-align: left;
    border-bottom: 1px solid rgba(255,255,255,0.08);
}
.model-table td {
    font-size: 0.83rem;
    color: rgba(255,255,255,0.8) !important;
    padding: 10px 12px;
    border-bottom: 1px solid rgba(255,255,255,0.05);
    vertical-align: top;
}
.model-table tr:last-child td { border-bottom: none; }
.model-table tr:hover td { background: rgba(255,255,255,0.03); }
.badge-pill {
    display: inline-block;
    background: rgba(0,122,255,0.25);
    border: 1px solid rgba(0,122,255,0.4);
    border-radius: 999px;
    padding: 2px 10px;
    font-size: 0.72rem;
    color: #00C6FF !important;
}
.badge-pill.green  { background: rgba(48,209,88,0.2); border-color: rgba(48,209,88,0.4); color: #30D158 !important; }
.badge-pill.orange { background: rgba(255,159,10,0.2); border-color: rgba(255,159,10,0.4); color: #FF9F0A !important; }
.badge-pill.purple { background: rgba(123,47,255,0.2); border-color: rgba(123,47,255,0.4); color: #BF5AF2 !important; }

/* Metric cards */
.metrics-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 10px;
}
.metric-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 14px;
    padding: 14px 16px;
}
.metric-name {
    font-size: 0.78rem;
    font-weight: 700;
    color: rgba(255,255,255,0.7) !important;
    margin-bottom: 3px;
}
.metric-def {
    font-size: 0.72rem;
    color: rgba(255,255,255,0.38) !important;
    line-height: 1.5;
}
.metric-val {
    font-size: 1rem;
    font-weight: 800;
    margin-top: 6px;
}

/* Interpretability chips */
.interp-chips {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 10px;
}
.interp-chip {
    flex: 1;
    min-width: 160px;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 14px;
    padding: 16px;
}
.interp-chip-title {
    font-size: 0.85rem;
    font-weight: 700;
    color: white !important;
    margin-bottom: 5px;
}
.interp-chip-desc {
    font-size: 0.75rem;
    color: rgba(255,255,255,0.4) !important;
    line-height: 1.5;
}
</style>
"""

def arrow():
    return """
    <div class="arrow-connector">
        <div class="arrow-line"></div>
        <div class="arrow-head"></div>
    </div>
    """

def render():
    st.markdown(WORKFLOW_CSS, unsafe_allow_html=True)

    # Page header
    st.markdown("""
        <div class="wf-page-header">
            <h1 class="wf-page-title">⚙️ Machine Learning Workflow</h1>
            <p class="wf-page-sub">End-to-end pipeline for career prediction - from raw data to interpretable AI</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="flow-wrapper">', unsafe_allow_html=True)

    # ── Step 1: Dataset ───────────────────────────────────────────────────────
    st.markdown(f"""
        <div class="step-node accent-blue">
            <div class="step-header">
                <div class="step-icon bg-blue">🗄️</div>
                <div class="step-meta">
                    <div class="step-badge" style="color:#007AFF;">Step 1</div>
                    <div class="step-title">Dataset</div>
                </div>
            </div>
            <div class="sub-items">
                <div class="sub-chip"><div class="chip-dot" style="background:#007AFF;"></div>4,076 student skill records</div>
                <div class="sub-chip"><div class="chip-dot" style="background:#007AFF;"></div>6 career categories</div>
                <div class="sub-chip"><div class="chip-dot" style="background:#007AFF;"></div>2 columns: Skill, Career</div>
                <div class="sub-chip"><div class="chip-dot" style="background:#007AFF;"></div>CS / IT domain</div>
            </div>
            <div class="step-desc">
                Raw dataset berisi daftar skill mahasiswa CS (hard + soft skills) beserta label karir yang sesuai.
                Format: comma-separated skills per baris. Data bersih, tanpa missing values.
            </div>
        </div>
        {arrow()}
    """, unsafe_allow_html=True)

    # ── Step 2: Text Preprocessing ────────────────────────────────────────────
    st.markdown(f"""
        <div class="step-node accent-cyan">
            <div class="step-header">
                <div class="step-icon bg-cyan">🔤</div>
                <div class="step-meta">
                    <div class="step-badge" style="color:#00C6FF;">Step 2</div>
                    <div class="step-title">Text Preprocessing</div>
                </div>
            </div>
            <div class="sub-items">
                <div class="sub-chip"><div class="chip-dot" style="background:#00C6FF;"></div>① Lowercase</div>
                <div class="sub-chip"><div class="chip-dot" style="background:#00C6FF;"></div>② Punctuation Removal</div>
                <div class="sub-chip"><div class="chip-dot" style="background:#00C6FF;"></div>③ Tokenization</div>
                <div class="sub-chip"><div class="chip-dot" style="background:#00C6FF;"></div>④ Stopword Removal</div>
            </div>
            <div class="step-desc">
                <b style="color:rgba(255,255,255,0.75);">Lowercase</b> — normalisasi kapitalisasi agar "Python" = "python".<br>
                <b style="color:rgba(255,255,255,0.75);">Punctuation removal</b> — regex <code style="color:#00C6FF;">[^a-z\s]</code> menghapus simbol & angka.<br>
                <b style="color:rgba(255,255,255,0.75);">Tokenization</b> — split teks menjadi token kata per kata.<br>
                <b style="color:rgba(255,255,255,0.75);">Stopword removal</b> — hapus kata umum (and, or, the, ...) yang tidak informatif.
            </div>
        </div>
        {arrow()}
    """, unsafe_allow_html=True)

    # ── Step 3: TF-IDF ───────────────────────────────────────────────────────
    st.markdown(f"""
        <div class="step-node accent-purple">
            <div class="step-header">
                <div class="step-icon bg-purple">📊</div>
                <div class="step-meta">
                    <div class="step-badge" style="color:#7B2FFF;">Step 3</div>
                    <div class="step-title">TF-IDF Vectorization</div>
                </div>
            </div>
            <div class="sub-items">
                <div class="sub-chip"><div class="chip-dot" style="background:#7B2FFF;"></div>max_features = 5,000</div>
                <div class="sub-chip"><div class="chip-dot" style="background:#7B2FFF;"></div>ngram_range = (1, 2)</div>
                <div class="sub-chip"><div class="chip-dot" style="background:#7B2FFF;"></div>sublinear_tf = True</div>
                <div class="sub-chip"><div class="chip-dot" style="background:#7B2FFF;"></div>Sparse Matrix Output</div>
            </div>
            <div class="step-desc">
                Term Frequency–Inverse Document Frequency mengubah teks menjadi vektor numerik.
                <b style="color:rgba(255,255,255,0.7);">Unigram + bigram</b> menangkap frasa seperti "machine learning".
                <b style="color:rgba(255,255,255,0.7);">sublinear_tf</b> = log(1+tf) meredam dominasi kata yang sangat sering muncul.
                Output: sparse matrix (4076 × 5000).
            </div>
        </div>
        {arrow()}
    """, unsafe_allow_html=True)

    # ── Step 4: Train-Test Split ──────────────────────────────────────────────
    st.markdown(f"""
        <div class="step-node accent-green">
            <div class="step-header">
                <div class="step-icon bg-green">✂️</div>
                <div class="step-meta">
                    <div class="step-badge" style="color:#30D158;">Step 4</div>
                    <div class="step-title">Train-Test Split</div>
                </div>
            </div>
            <div class="sub-items">
                <div class="sub-chip"><div class="chip-dot" style="background:#30D158;"></div>80% Train → 3,260 samples</div>
                <div class="sub-chip"><div class="chip-dot" style="background:#30D158;"></div>20% Test → 816 samples</div>
                <div class="sub-chip"><div class="chip-dot" style="background:#30D158;"></div>Stratified Sampling</div>
                <div class="sub-chip"><div class="chip-dot" style="background:#30D158;"></div>random_state = 42</div>
            </div>
            <div class="step-desc">
                Stratified split memastikan proporsi setiap kelas karir tetap seimbang di train dan test set,
                sehingga evaluasi tidak bias terhadap kelas mayoritas (Development: 1,148 samples).
            </div>
        </div>
        {arrow()}
    """, unsafe_allow_html=True)

    # ── Step 5: Model Training ────────────────────────────────────────────────
    st.markdown("""
        <div class="step-node accent-orange">
            <div class="step-header">
                <div class="step-icon bg-orange">🤖</div>
                <div class="step-meta">
                    <div class="step-badge" style="color:#FF9F0A;">Step 5</div>
                    <div class="step-title">Model Training</div>
                </div>
            </div>
            <table class="model-table">
                <tr>
                    <th>Model</th>
                    <th>Key Parameters</th>
                    <th>Accuracy</th>
                    <th>Kelebihan</th>
                </tr>
                <tr>
                    <td><b style="color:white;">Naive Bayes</b></td>
                    <td><code style="color:#FF9F0A;font-size:0.75rem;">alpha=0.1</code></td>
                    <td><span class="badge-pill">92.28%</span></td>
                    <td>Cepat, baseline yang kuat</td>
                </tr>
                <tr>
                    <td><b style="color:white;">Logistic Regression</b></td>
                    <td><code style="color:#FF9F0A;font-size:0.75rem;">C=5, max_iter=1000</code></td>
                    <td><span class="badge-pill">94.73%</span></td>
                    <td>Akurasi tinggi, interpretable</td>
                </tr>
                <tr>
                    <td><b style="color:white;">Linear SVM</b></td>
                    <td><code style="color:#FF9F0A;font-size:0.75rem;">C=1.0, max_iter=2000</code></td>
                    <td><span class="badge-pill">94.12%</span></td>
                    <td>Robust terhadap high-dim data</td>
                </tr>
                <tr>
                    <td><b style="color:white;">XGBoost</b></td>
                    <td><code style="color:#FF9F0A;font-size:0.75rem;">n_est=300, depth=6, lr=0.1</code></td>
                    <td><span class="badge-pill green">95.71%</span></td>
                    <td>Akurasi tertinggi, ensemble model</td>
                </tr>
            </table>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(arrow(), unsafe_allow_html=True)

    # ── Step 6: Evaluation ───────────────────────────────────────────────────
    st.markdown(f"""
        <div class="step-node accent-red">
            <div class="step-header">
                <div class="step-icon bg-red">📈</div>
                <div class="step-meta">
                    <div class="step-badge" style="color:#FF6B6B;">Step 6</div>
                    <div class="step-title">Evaluation</div>
                </div>
            </div>
            <div class="metrics-grid">
                <div class="metric-card">
                    <div class="metric-name">🎯 Accuracy</div>
                    <div class="metric-def">Proporsi prediksi benar dari total prediksi keseluruhan.</div>
                    <div class="metric-val" style="color:#00C6FF;">95.71%</div>
                </div>
                <div class="metric-card">
                    <div class="metric-name">🔍 Precision</div>
                    <div class="metric-def">Dari semua yang diprediksi kelas X, berapa yang benar-benar kelas X.</div>
                    <div class="metric-val" style="color:#30D158;">96.53%</div>
                </div>
                <div class="metric-card">
                    <div class="metric-name">📡 Recall</div>
                    <div class="metric-def">Dari semua data kelas X, berapa yang berhasil terdeteksi.</div>
                    <div class="metric-val" style="color:#FF9F0A;">95.94%</div>
                </div>
                <div class="metric-card">
                    <div class="metric-name">⚖️ Macro F1-Score</div>
                    <div class="metric-def">Rata-rata F1 per kelas tanpa mempertimbangkan ketidakseimbangan data.</div>
                    <div class="metric-val" style="color:#BF5AF2;">96.20%</div>
                </div>
            </div>
            <div class="step-desc">
                <b style="color:rgba(255,255,255,0.7);">Confusion Matrix</b> — matriks N×N yang menunjukkan prediksi benar/salah
                untuk setiap kombinasi kelas. Berguna mengidentifikasi kelas mana yang sering tertukar.
            </div>
        </div>
        {arrow()}
    """, unsafe_allow_html=True)

    # ── Step 7: Interpretability ─────────────────────────────────────────────
    st.markdown(f"""
        <div class="step-node accent-teal">
            <div class="step-header">
                <div class="step-icon bg-teal">🔬</div>
                <div class="step-meta">
                    <div class="step-badge" style="color:#5AC8FA;">Step 7</div>
                    <div class="step-title">Interpretability</div>
                </div>
            </div>
            <div class="interp-chips">
                <div class="interp-chip">
                    <div class="interp-chip-title">🌊 SHAP Values</div>
                    <div class="interp-chip-desc">
                        SHAP digunakan untuk membantu memahami alasan di balik prediksi model. Metode ini menunjukkan fitur atau skill 
                        mana yang paling berpengaruh terhadap rekomendasi karir yang dihasilkan oleh model XGBoost menggunakan 
                        <code style="color:#5AC8FA;">TreeExplainer</code>.
                    </div>
                </div>
                <div class="interp-chip">
                    <div class="interp-chip-title">🏷️ Top Important Words</div>
                    <div class="interp-chip-desc">
                        Visualisasi 15 kata/fitur TF-IDF dengan bobot koefisien tertinggi per kelas
                        karir, diambil langsung dari <code style="color:#5AC8FA;">coef_</code> Logistic Regression.
                        Mudah diinterpretasi tanpa library tambahan.
                    </div>
                </div>
            </div>
            <div class="step-desc">
                Interpretability penting agar prediksi model dapat dipercaya dan dijelaskan kepada
                mahasiswa — bukan sekadar "black box". Memungkinkan verifikasi apakah model
                belajar pola yang memang masuk akal secara domain.
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)  # close flow-wrapper

    # Summary footer
    st.markdown("""
        <div style="
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 18px;
            padding: 24px 28px;
            margin-top: 28px;
            text-align: center;
        ">
            <div style="font-size:0.72rem; letter-spacing:3px; text-transform:uppercase;
                        color:rgba(255,255,255,0.35); margin-bottom:10px;">Pipeline Summary</div>
            <div style="font-size:0.88rem; color:rgba(255,255,255,0.6); line-height:1.8;">
                Dataset (4,076 records)
                &nbsp;→&nbsp; Text Preprocessing
                &nbsp;→&nbsp; TF-IDF (5K features)
                &nbsp;→&nbsp; Split 80:20
                &nbsp;→&nbsp; 4 Models Trained
                &nbsp;→&nbsp; Best: <span style="color:#30D158; font-weight:700;">XGBoost 95.71%</span>
                &nbsp;→&nbsp; SHAP + Top Words
            </div>
        </div>
    """, unsafe_allow_html=True)