Here is your perfectly formatted and assembled `README.md` file.

I cleaned up the broken code blocks, removed my previous conversational text, fixed the heading hierarchy (so it outlines perfectly in GitHub), and completed the Quick Setup section that got cut off in your copy-paste.

Just copy this entire block and paste it directly into your `README.md` file!

---

```markdown
# 🎙️ Auto-Dubber Pro: AI YouTube Shorts Localizer

An automated, end-to-end Python pipeline that localizes English YouTube Shorts for an Indian audience. This tool uses Large Language Models (LLMs) to translate English scripts into context-aware Hinglish, generates high-fidelity neural text-to-speech, creates automatic subtitle timings, and mixes the final vocal track with background music.

## ⚙️ Prerequisites
Before running this on a new machine, ensure you have the following installed:
1. **Python 3.11 or 3.12** (Avoid Python 3.14+ to ensure maximum AI package compatibility).
2. **FFmpeg**: Required for `pydub` to process `.mp3` files.
   * *Windows Quick Install*: Download the latest Windows `.zip` build from `gyan.dev`. Extract it, open the `bin` folder, and drop `ffmpeg.exe` and `ffprobe.exe` directly into your virtual environment's `Scripts` folder (`.venv\Scripts\`).

## 🚀 Quick Setup Instructions
If you are deploying this code on a new computer, follow these exact steps:

1. **Create a Virtual Environment:**
   ```bash
   python -m venv .venv

```

2. **Activate the Environment:**
* Windows: `.\.venv\Scripts\activate`
* Mac/Linux: `source .venv/bin/activate`


3. **Install all Dependencies:**
```bash
pip install -r requirements.txt

```



---

## 📖 Beginner's Guide: How to Use the Auto-Dubber Pro

Welcome! This program takes your English video scripts and automatically turns them into ready-to-upload Hinglish audio tracks with perfectly synced background music and subtitles.

You do not need to be a coding expert to use this. You only need to change a few lines of text at the very top and very bottom of the code.

### Step 1: The Setup (Getting your files ready)

Before you run the code, you need two things inside your project folder:

1. **The Code:** Your `localization_pipeline.py` file.
2. **The Music:** Download a copyright-free background song (like a phonk beat or chill lofi track). Save it in the exact same folder as your code and name it `chill_beat.mp3`. *(If your song has a different name, that is okay, we will tell the code its name in Step 3!)*

### Step 2: Connect the "Brain" (The API Key)

The program needs permission to use Google's AI to translate your script.

1. Open the code in your editor (like VS Code).
2. Look near the very top (around Line 10) for this:
`GEMINI_API_KEY = "YOUR_API_KEY_HERE"`
3. Delete `YOUR_API_KEY_HERE` and paste your actual Google API key inside the quotation marks.

### Step 3: The Control Center (Customizing your Video)

Scroll all the way down to the bottom of the code to the `async def main():` section. This is your control center. Here are the 3 features you can change for every new video:

* **Feature 1: The Topic (Context-Aware AI)**
Look for `VIDEO_TOPIC = "Home Dumbbell Workout"`. Change the text inside the quotes to match whatever your video is about.
*Why?* If you type `"GTA V Gameplay"`, the AI will translate your script using gamer slang. If you type `"F1 Racing"`, it will use racing terms.
* **Feature 2: The Background Music**
Look for `BACKGROUND_BEAT = "chill_beat.mp3"`. If your music file is named something else (like `epic_music.mp3`), change it here so the program knows which file to mix with your voice.
* **Feature 3: Your Script (The Bulk Processor)**
Look for the `scripts = [ ... ]` section. This is where you type what you want the AI voice to say.
* Replace the English sentences with your own script.
* Keep each sentence or paragraph inside its own set of quotation marks `""` and separate them with a comma `,`.
* *Why?* The program processes the video in "chunks." For every line you write, it will generate a separate, clean audio clip.



### Step 4: Run the Program

Once your script is typed in, simply hit the **Run** (Play) button in VS Code, or type `python localization_pipeline.py` in your terminal.

Sit back and watch the terminal. It will tell you exactly what it is doing: translating, generating audio, and mixing the beat.

---

## 🧩 How the Functions Work

### `main()`

* **What it does:** This is the execution loop. It iterates through your array of script chunks, feeding them through the translation, dubbing, and mixing functions sequentially.

---

## 📂 Output Files Explained

When you run the script, it generates specific files for every line of text in your script array. Here is what they are and how to use them:

### 🎵 The Audio File (`clip_X_voice.mp3` / `clip_X_FINAL.mp3`)

* **What it is:** This is the standard audio file containing your generated AI voiceover. If you enabled background music mixing, you will also see a `_FINAL.mp3` version which has the voice and music already blended perfectly together.
* **When and Where to use it:** Drag and drop this file directly into the audio timeline of your video editing software (like Premiere Pro, CapCut, DaVinci Resolve, or VN Editor) to serve as the main voice track for your YouTube Short.

### 📝 The Subtitle File (`clip_X_subs.srt`)

* **What it is:** An SRT (SubRip Subtitle) file. It is a plain-text file that contains the exact words spoken in the audio, along with exact, millisecond-perfect timestamp codes telling the video editor exactly when to display each word on the screen.
* **When and Where to use it:** * **In your Editor:** Drag this file directly into your Premiere Pro or CapCut timeline, and it will automatically generate perfectly synced, customizable text captions on your video.
* **On YouTube:** When uploading your video to YouTube Studio, you can choose to upload this `.srt` file in the "Subtitles" section to instantly provide perfectly accurate closed captions for your audience.



---

## 💡 Bonus Feature: Changing the Voice

By default, the script uses a high-quality Indian Male voice (`hi-IN-MadhurNeural`). Want a female voice instead?

1. Open the Python script.
2. Scroll to the middle of the code to the `generate_audio_and_subs` function.
3. Find this exact line: `voice = "hi-IN-MadhurNeural"`
4. Change it to: `voice = "hi-IN-SwaraNeural"`

### 🌍 How to Access More Voices (US, UK, and more!)

This tool isn't just limited to Hinglish! The `edge-tts` engine has hundreds of premium voices from all over the world built right in.

If you want to see the complete list of every voice available:

1. Open your terminal (ensure your virtual environment is active).
2. Run this exact command:
```bash
edge-tts --list-voices

```


3. Hit Enter, and it will print out a massive list of voices. You will see options like:
* `en-US-ChristopherNeural` (US English, Male)
* `en-GB-SoniaNeural` (UK English, Female)
* `en-AU-NatashaNeural` (Australian English, Female)


4. Just copy the exact name of the voice you want and paste it into the `voice = "..."` line in your script!

---

## 👨‍💻 Author Info

* **Developed by:** leo
* **Role:** AI & Data Science Student
* **Version:** 1.0.0
