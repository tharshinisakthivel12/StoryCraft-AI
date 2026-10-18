import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

st.set_page_config(
    page_title="StoryCraft AI",
    page_icon="✍️",
    layout="wide"
)

st.markdown("""
<style>
.storycraft-hero {
    padding: 2.5rem 2.2rem;
    margin-bottom: 1.8rem;
    border: 1px solid rgba(167,139,250,.28);
    border-radius: 24px;
    background: linear-gradient(120deg, rgba(124,58,237,.22), rgba(59,130,246,.12), rgba(20,22,40,.65));
    box-shadow: 0 12px 40px rgba(0,0,0,.16);
}
.storycraft-badge {
    color: #c4b5fd;
    font-size: .75rem;
    font-weight: 700;
    letter-spacing: 2.5px;
    margin-bottom: 1rem;
}
.storycraft-hero h1 {
    font-size: clamp(2.6rem, 6vw, 4rem);
    font-weight: 800;
    letter-spacing: -2px;
    margin: 0;
    color: #ffffff;
}
.storycraft-hero h1 span {
    background: linear-gradient(90deg, #c4b5fd, #93c5fd);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.storycraft-tagline {
    font-size: 1.2rem;
    font-weight: 600;
    margin: 1rem 0 .35rem;
    color: #f0edff;
}
.storycraft-description {
    color: #bfc3df;
    line-height: 1.7;
    margin-bottom: 0;
}

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background: radial-gradient(ellipse at top left, #25204b 0%, #111322 48%, #0b0d17 100%);
    color: #f4f3ff;
    font-family: 'Inter', sans-serif;
}
.block-container {
    max-width: 1120px;
    padding-top: 2rem;
    padding-bottom: 4rem;
    animation: storyEnter .7s ease-out;
}
@keyframes storyEnter {
    from { opacity: 0; transform: translateY(12px); }
    to { opacity: 1; transform: translateY(0); }
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #191a30, #10121f);
    border-right: 1px solid rgba(167,139,250,.2);
}
.stButton > button, .stDownloadButton > button {
    background: linear-gradient(100deg, #7c3aed, #4f46e5);
    color: white;
    border: 1px solid rgba(196,181,253,.35);
    border-radius: 12px;
    font-weight: 600;
    transition: transform .2s ease, box-shadow .2s ease, filter .2s ease;
}
.stButton > button:hover, .stDownloadButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(124,58,237,.3);
    filter: brightness(1.12);
}
.stTextArea textarea, .stTextInput input,
[data-baseweb="select"] > div {
    background-color: #191b30 !important;
    color: #f4f3ff !important;
    border-color: rgba(167,139,250,.3) !important;
    border-radius: 10px !important;
}
h1, h2, h3, p, label { color: #f0efff; }
@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: .01ms !important;
        transition-duration: .01ms !important;
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="storycraft-hero">
    <div class="storycraft-badge">? YOUR CREATIVE STUDIO</div>
    <h1>StoryCraft <span>AI</span></h1>
    <p class="storycraft-tagline">Every great story starts with an idea.</p>
    <p class="storycraft-description">
        Turn your imagination into captivating stories, screenplays and video scripts.
    </p>
</div>
""", unsafe_allow_html=True)

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None

with st.sidebar:
    st.header("Story Settings")
    task = st.selectbox(
        "What do you want to create?",
        ["Short Story", "Screenplay", "Short Film Script",
         "YouTube Script", "Instagram Reel Script",
         "Plot Outline", "Character Profiles"]
    )
    genre = st.selectbox(
        "Genre",
        ["Fantasy", "Thriller", "Romance", "Comedy",
         "Science Fiction", "Drama", "Horror", "Adventure"]
    )
    language = st.selectbox("Language", ["English", "Tamil", "Tanglish"])
    length = st.selectbox("Length", ["Short", "Medium", "Long"])
    tone = st.selectbox(
        "Tone",
        ["Emotional", "Funny", "Suspenseful", "Inspirational",
         "Dark", "Realistic", "Imaginative"]
    )

idea = st.text_area(
    "Your story idea",
    placeholder="Example: A student discovers an AI that can predict the future...",
    height=150
)

characters = st.text_input(
    "Main characters (optional)",
    placeholder="Example: Meera, a curious engineering student"
)

audience = st.selectbox(
    "Target audience",
    ["Children", "Teenagers", "Young Adults", "General Audience"]
)

if st.button("Generate with AI", type="primary", use_container_width=True):
    if not idea.strip():
        st.warning("Please enter your story idea.")
    elif not client:
        st.error("Gemini API key missing. Please check your .env file.")
    else:
        prompt = f"""
You are StoryCraft AI, a professional creative writer.

Create a complete {task}.
Story idea: {idea}
Genre: {genre}
Language: {language}
Length: {length}
Tone: {tone}
Target audience: {audience}
Characters: {characters or "Create suitable characters"}

Requirements:
- Add a compelling title and engaging opening.
- Make the plot coherent and characters believable.
- Use natural dialogue and meaningful details.
- Give the story a satisfying ending.
- For screenplays, include scene headings, action and dialogue.
- For video scripts, include a hook, scenes and a strong ending.
- Write the actual content, not instructions.
"""

        try:
            with st.spinner("StoryCraft AI is creating your content..."):
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )
                result = response.text

            st.session_state["generated_story"] = result

        except Exception as e:
            error_text = str(e)

            if "503" in error_text or "UNAVAILABLE" in error_text:
                st.warning(
                    "Gemini is temporarily busy. Please wait 30?60 seconds "
                    "and click Generate with AI again. Your story idea is still available."
                )
            elif "429" in error_text or "RESOURCE_EXHAUSTED" in error_text:
                st.warning(
                    "Gemini API rate limit reached. Please wait before trying again."
                )
            else:
                st.error(f"Generation failed: {type(e).__name__}")
                st.caption(error_text)

if st.session_state.get("generated_story"):
    st.divider()
    st.header("Your Creation")
    st.markdown(st.session_state["generated_story"])
    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            "Download your creation",
            data=st.session_state["generated_story"],
            file_name="storycraft_creation.txt",
            mime="text/plain",
            use_container_width=True
        )

    with col2:
        st.code(st.session_state["generated_story"], language=None)

