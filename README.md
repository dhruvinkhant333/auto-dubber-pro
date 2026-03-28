# 🎙️ Auto Dubber Pro
### AI-Powered YouTube Shorts Localization Pipeline

Auto Dubber Pro is a fully automated Python pipeline that takes English video scripts and localizes them for an Indian audience. It uses **Google Gemini AI** for context-aware Hinglish translation, **Microsoft Edge TTS** for neural voice generation, auto-generates **SRT subtitle files**, and blends everything with background music — all in one run.

---

## ✨ What It Does

| Step | What Happens |
|---|---|
| 1️⃣ Translate | Gemini AI translates English scripts into natural, topic-aware Hinglish |
| 2️⃣ Voice | Edge TTS generates realistic Hindi neural audio (hi-IN-MadhurNeural) |
| 3️⃣ Subtitles | Auto-generates perfectly timed `.srt` subtitle files |
| 4️⃣ Mix | Blends the voice with background music using pydub |

---

## 🛠️ Tech Stack

- **Google Gemini 2.5 Flash** — Context-aware translation engine
- **Microsoft Edge TTS** — Neural text-to-speech (100+ voices)
- **pydub** — Audio mixing and processing
- **asyncio** — Async audio streaming for real-time subtitle timing
- **ffmpeg** — Backend audio processing

---

## ⚙️ Installation

### 1. Clone the repo
```bash
git clone https://github.com/dhruvinkhant333/auto-dubber-pro.git
cd auto-dubber-pro
```

### 2. Create a virtual environment
```bash
python -m venv .venv

# Activate — Windows
.\.venv\Scripts\activate

# Activate — Mac/Linux
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg (required for pydub)
- Download from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/)
- Extract and place `ffmpeg.exe` + `ffprobe.exe` in your `.venv\Scripts\` folder

---

## 🔑 Setup

Open `main.py` and update these 3 things at the top:

```python
# Your Google Gemini API Key
GEMINI_API_KEY = "your_api_key_here"

# Where output files should be saved
OUTPUT_FOLDER = r"C:\your\output\folder"

# Path to your background music file
BACKGROUND_MUSIC_PATH = r"C:\your\music\chill_beat.mp3"
```

> ⚠️ Never push your API key to GitHub. Use a `.env` file and add it to `.gitignore`

---

## 🚀 Usage

### Step 1 — Set your video topic and scripts

Scroll to `async def main()` and update:

```python
VIDEO_TOPIC = "Home Dumbbell Workout"  # Change to your video topic

scripts = [
    "What's up guys! Today we are hitting a crazy dumbbell workout at home.",
    "Grab your weights, make sure your form is tight, and let's build some muscle.",
    "Don't forget to like and subscribe for more daily fitness routines!"
]
```

The `VIDEO_TOPIC` makes Gemini use the right slang — `"GTA V Gameplay"` gives gamer terms, `"F1 Racing"` gives racing terms, etc.

### Step 2 — Run

```bash
python main.py
```

---

## 📂 Output Files

For every line in your `scripts` array, the tool generates:

| File | Description |
|---|---|
| `clip_1_voice.mp3` | Raw AI voice audio |
| `clip_1_subs.srt` | Perfectly timed subtitle file |
| `clip_1_FINAL.mp3` | Voice mixed with background music |

**How to use them:**
- Drop `_FINAL.mp3` into CapCut, Premiere Pro, or DaVinci Resolve as your audio track
- Import `_subs.srt` into your editor or upload directly to YouTube Studio for auto-captions

---

## 🎤 Changing the Voice

Default voice is `hi-IN-MadhurNeural` (Indian Male). To change it, find this line in `generate_audio_and_subs()`:

```python
voice = "hi-IN-MadhurNeural"
```

Some alternatives:
- `hi-IN-SwaraNeural` — Indian Female
- `en-US-ChristopherNeural` — US English Male
- `en-GB-SoniaNeural` — UK English Female

To see all 400+ available voices:
```bash
edge-tts --list-voices
```

---

## 🧩 Project Structure

```
auto-dubber-pro/
│
├── main.py               # Full pipeline script
├── requirements.txt      # Python dependencies
├── .gitignore            # Excludes .env and output files
└── README.md
```

---

## 📋 Requirements

```
google-genai
edge-tts
pydub
```

---

## 👨‍💻 About

**Dhruvin Khant** — BE Student | AI & Data Science | GEC Rajkot  
Built as a personal AI project to explore LLM APIs, TTS systems, and audio processing.

---

## 📄 License

MIT License — free to use and modify.
