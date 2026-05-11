import streamlit as st

# Page config
st.set_page_config(
    page_title="Rehan Shafique — Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&display=swap');
    
    * { font-family: 'Syne', sans-serif; }
    
    .main { background-color: #05080f; color: #f0ece4; }
    
    .hero-name {
        font-size: 64px;
        font-weight: 800;
        background: linear-gradient(135deg, #c9a84c, #e8c97a);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1;
        margin-bottom: 8px;
    }
    .hero-role {
        font-size: 22px;
        color: #7a7f8e;
        font-style: italic;
        margin-bottom: 16px;
    }
    .hero-desc {
        font-size: 16px;
        color: rgba(240,236,228,0.7);
        line-height: 1.7;
        max-width: 600px;
    }
    .gold-badge {
        display: inline-block;
        background: rgba(201,168,76,0.1);
        border: 1px solid rgba(201,168,76,0.3);
        color: #c9a84c;
        padding: 6px 16px;
        border-radius: 2px;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        margin-bottom: 20px;
    }
    .section-title {
        font-size: 40px;
        font-weight: 700;
        color: #f0ece4;
        margin-bottom: 8px;
    }
    .section-label {
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: #c9a84c;
        margin-bottom: 4px;
    }
    .skill-card {
        background: #0c1220;
        border: 1px solid rgba(255,255,255,0.07);
        border-left: 3px solid #c9a84c;
        padding: 20px 24px;
        border-radius: 2px;
        margin-bottom: 12px;
    }
    .skill-card h4 { color: #f0ece4; font-size: 16px; margin-bottom: 6px; }
    .skill-card p  { color: #7a7f8e; font-size: 13px; margin: 0; }
    .project-card {
        background: #0c1220;
        border: 1px solid rgba(255,255,255,0.07);
        padding: 28px 32px;
        border-radius: 2px;
        margin-bottom: 12px;
        border-top: 2px solid #c9a84c;
    }
    .project-card h3 { color: #f0ece4; font-size: 22px; margin-bottom: 8px; }
    .project-card p  { color: rgba(240,236,228,0.65); font-size: 14px; line-height: 1.7; }
    .live-badge {
        display: inline-block;
        background: rgba(45,143,95,0.15);
        border: 1px solid rgba(45,143,95,0.4);
        color: #2d8f5f;
        padding: 3px 10px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 600;
        margin-bottom: 10px;
    }
    .tech-tag {
        display: inline-block;
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.1);
        color: #7a7f8e;
        padding: 4px 10px;
        border-radius: 2px;
        font-size: 11px;
        margin: 3px 3px 3px 0;
    }
    .stat-card {
        background: #0c1220;
        border: 1px solid rgba(255,255,255,0.07);
        padding: 24px;
        text-align: center;
        border-radius: 2px;
    }
    .stat-num { font-size: 42px; font-weight: 700; color: #c9a84c; line-height: 1; }
    .stat-lbl { font-size: 11px; color: #7a7f8e; letter-spacing: 0.1em; text-transform: uppercase; margin-top: 4px; }
    .divider { border: none; border-top: 1px solid rgba(255,255,255,0.07); margin: 40px 0; }
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ── HERO ──
st.markdown('<div class="gold-badge">● Available for Work</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-name">Rehan Shafique</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-role">Python Developer & Bioinformatics Researcher</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-desc">I build intelligent digital solutions at the intersection of computer science and biology. Full-stack web engineer, AI enthusiast, and problem solver based in Faisalabad, Pakistan.</div>', unsafe_allow_html=True)

st.markdown("")
col1, col2, col3 = st.columns([1,1,4])
with col1:
    st.link_button("🔬 Live AI App", "https://skincancerpredictions.streamlit.app/")
with col2:
    st.link_button("💼 LinkedIn", "https://linkedin.com/in/rehan-shafique")

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── STATS ──
st.markdown('<div class="section-label">At a Glance</div>', unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown('<div class="stat-card"><div class="stat-num">500+</div><div class="stat-lbl">Connections</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="stat-card"><div class="stat-num">85%</div><div class="stat-lbl">AI Accuracy</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="stat-card"><div class="stat-num">3+</div><div class="stat-lbl">Years Coding</div></div>', unsafe_allow_html=True)
with c4:
    st.markdown('<div class="stat-card"><div class="stat-num">∞</div><div class="stat-lbl">Problems Solved</div></div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── ABOUT ──
st.markdown('<div class="section-label">About Me</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Turning ideas into reality</div>', unsafe_allow_html=True)
st.markdown("""
<div style="color:rgba(240,236,228,0.7);font-size:15px;line-height:1.8;max-width:700px;">
I am a <strong style="color:#f0ece4;">Computer Science student</strong> at the University of Agriculture, Faisalabad, 
with a unique focus on both software engineering and bioinformatics. I sit at a rare intersection — where code meets life sciences.<br><br>
As a <strong style="color:#f0ece4;">freelance developer</strong>, I have built real-world web applications, automation tools, 
and AI-powered systems that solve genuine problems. I believe great software is not just functional — it is elegant, scalable, and meaningful.
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── SKILLS ──
st.markdown('<div class="section-label">Expertise</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">What I bring to the table</div>', unsafe_allow_html=True)

col_a, col_b = st.columns(2)
with col_a:
    st.markdown("""
    <div class="skill-card">
        <h4>🐍 Python Development</h4>
        <p>Scripting, automation, data pipelines, and backend logic built with clean Python code.</p>
        <div style="margin-top:10px;">
            <span class="tech-tag">Python</span><span class="tech-tag">Django</span>
            <span class="tech-tag">Flask</span><span class="tech-tag">Automation</span>
        </div>
    </div>
    <div class="skill-card">
        <h4>🌐 Full-Stack Web</h4>
        <p>End-to-end web applications from responsive UI to robust backend APIs and databases.</p>
        <div style="margin-top:10px;">
            <span class="tech-tag">HTML/CSS</span><span class="tech-tag">JavaScript</span>
            <span class="tech-tag">REST APIs</span><span class="tech-tag">SQL</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
with col_b:
    st.markdown("""
    <div class="skill-card">
        <h4>🧬 Bioinformatics</h4>
        <p>Genomic data analysis, sequence alignment, and computational pipelines for life sciences.</p>
        <div style="margin-top:10px;">
            <span class="tech-tag">Genomics</span><span class="tech-tag">BLAST</span>
            <span class="tech-tag">Pipelines</span><span class="tech-tag">Data Analysis</span>
        </div>
    </div>
    <div class="skill-card">
        <h4>🤖 Deep Learning</h4>
        <p>Building and deploying AI models for real-world medical and scientific classification tasks.</p>
        <div style="margin-top:10px;">
            <span class="tech-tag">CNN</span><span class="tech-tag">TensorFlow</span>
            <span class="tech-tag">Keras</span><span class="tech-tag">OpenCV</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── PROJECTS ──
st.markdown('<div class="section-label">Projects</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Selected Work</div>', unsafe_allow_html=True)

st.markdown("""
<div class="project-card">
    <div class="live-badge">● Live App</div>
    <h3>Skin Cancer Detection AI System</h3>
    <p>
        An AI-powered web application that detects malignant vs benign skin lesions from dermoscopic 
        images using a Convolutional Neural Network (CNN) achieving <strong style="color:#c9a84c;">85%+ accuracy</strong>. 
        Deployed live on Streamlit and accessible worldwide.
    </p>
    <div style="margin-top:14px;">
        <span class="tech-tag">Python</span><span class="tech-tag">CNN</span>
        <span class="tech-tag">TensorFlow</span><span class="tech-tag">Streamlit</span>
        <span class="tech-tag">OpenCV</span><span class="tech-tag">Deep Learning</span>
    </div>
</div>
""", unsafe_allow_html=True)
st.link_button("🔗 View Live App →", "https://skincancerpredictions.streamlit.app/")

st.markdown("""
<div class="project-card" style="margin-top:12px;">
    <h3>Full-Stack Web Development</h3>
    <p>
        Designed and delivered multiple full-stack web applications for freelance clients across diverse 
        industries — focusing on clean architecture, performance, and long-term maintainability.
    </p>
    <div style="margin-top:14px;">
        <span class="tech-tag">Python</span><span class="tech-tag">Django</span>
        <span class="tech-tag">JavaScript</span><span class="tech-tag">REST APIs</span><span class="tech-tag">SQL</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── CONTACT ──
st.markdown('<div class="section-label">Contact</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Let\'s work together</div>', unsafe_allow_html=True)
st.markdown("""
<div style="color:rgba(240,236,228,0.6);font-size:15px;line-height:1.7;margin-bottom:24px;">
I am open to freelance projects, research collaborations, full-time opportunities, and meaningful connections.<br>
📍 Faisalabad, Pakistan &nbsp;·&nbsp; 🌐 Available Worldwide (Remote)
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns([1,1,4])
with c1:
    st.link_button("💼 LinkedIn", "https://linkedin.com/in/rehan-shafique")
with c2:
    st.link_button("📧 Email Me", "mailto:rehan@email.com")

st.markdown("""
<div style="text-align:center;color:#7a7f8e;font-size:12px;margin-top:60px;padding-top:20px;border-top:1px solid rgba(255,255,255,0.07);">
    © 2026 Rehan Shafique · Faisalabad, Pakistan · Open to Work
</div>
""", unsafe_allow_html=True)
