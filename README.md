# ✍️ StoryCraft AI
### AI Storytelling & Scriptwriting Assistant

StoryCraft AI is an AI-powered creative writing application that helps users transform their ideas into engaging stories, screenplays, and video scripts. Users can customize the genre, language, length, tone, and target audience to generate content that matches their creative vision.

## ✨ Features

- **Multiple Content Types:** Generate short stories, screenplays, short film scripts, YouTube scripts, Instagram Reel scripts, plot outlines, and character profiles.
- **Genre Customization:** Choose from Fantasy, Thriller, Romance, Comedy, Science Fiction, Drama, Horror, and Adventure.
- **Multilingual Generation:** Create content in English, Tamil, and Tanglish.
- **Flexible Story Settings:** Customize length, tone, characters, and target audience.
- **AI-Powered Generation:** Uses the Google Gemini API to generate creative content.
- **Download Stories:** Download generated content for future use.
- **Interactive Interface:** Built with Streamlit for a simple and user-friendly experience.

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Frontend / UI:** Streamlit
- **AI Integration:** Google Gemini API
- **Libraries:** `google-genai`, `python-dotenv`
- **Version Control:** GitHub

## ⚙️ How It Works

1. Enter a story idea or creative concept.
2. Select the content type, genre, language, length, and tone.
3. Add optional character details and target audience.
4. Click **Generate with AI**.
5. Review the generated content and download it.

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd StoryCraft-AI
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file in the project folder:

```env
GEMINI_API_KEY=your_actual_gemini_api_key
```

Replace the placeholder with your own Gemini API key. Never upload your `.env` file or expose your API key publicly.

### 5. Start the application

```bash
streamlit run app.py
```

## 🔐 Security

- Keep API keys private.
- Store local secrets in `.env`.
- Use Streamlit Cloud Secrets when deploying.
- Never commit `.env` or other files containing credentials.

## 🌐 Live Demo

Add your deployed Streamlit application URL here.

## 👩‍💻 Developer

Developed as an AI-powered creative writing project to explore Python application development, generative AI integration, and interactive web applications.

## 🔮 Future Enhancements

- AI-generated character and scene illustrations.
- Save and manage multiple stories.
- Export scripts to PDF and DOCX.
- Voice-based storytelling and idea input.
- Improved screenplay formatting and story continuity.

---

*Turn your imagination into stories with StoryCraft AI.*
