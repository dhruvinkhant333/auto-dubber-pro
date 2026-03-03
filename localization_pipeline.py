import asyncio
import edge_tts
from google import genai
from pydub import AudioSegment
import os



# ==========================================
# 1. CONFIGURATION & CUSTOM PATHS
# ==========================================
GEMINI_API_KEY = "AIzaSyDRXzWaWNVxBOqfWoyhptxH0jwhjzUwTYw"
client = genai.Client(api_key=GEMINI_API_KEY)

# 👉 CUSTOM PATH 1: Where do you want the final files saved?
OUTPUT_FOLDER = r"D:\study\coding\ai\code_with_herry\output_files"

# 👉 CUSTOM PATH 2: Where is your background music located?
BACKGROUND_MUSIC_PATH = r"D:\study\coding\ai\code_with_herry\practice\chill_beat.mp3"


# ==========================================
# 2. CONTEXT-AWARE TRANSLATION ENGINE
# ==========================================
def translate_to_hinglish(english_text, topic):
    print(f"\n[1/3] Translating script (Topic: {topic})...")
    
    # UPGRADE: The prompt now accepts a specific topic to adjust the slang
    prompt = (
        "You are an expert YouTube script translator for an Indian audience. "
        "Translate the following English text into casual, high-energy Hinglish. "
        f"The topic of this video is: '{topic}'. "
        "Make sure to use relevant slang and terminology for this specific topic, "
        "keeping technical words in English but using Hindi for the connecting grammar. "
        f"Text to translate: '{english_text}'"
    )
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        print(f"Error during translation: {e}")
        return None

# ==========================================
# 3. TEXT-TO-SPEECH & SUBTITLE ENGINE
# ==========================================
async def generate_audio_and_subs(text, audio_output, srt_output):
    print(f"\n[2/3] Generating realistic audio and subtitles...")
    voice = "hi-IN-MadhurNeural" 
    
    communicate = edge_tts.Communicate(text, voice)
    submaker = edge_tts.SubMaker() # UPGRADE: Initializes the subtitle generator
    
    try:
        # We use a stream instead of .save() so we can capture the text timings
        with open(audio_output, "wb") as audio_file:
            async for chunk in communicate.stream():
                if chunk["type"] == "audio":
                    audio_file.write(chunk["data"])
                elif chunk["type"] in ("WordBoundary", "SentenceBoundary"):
                    submaker.feed(chunk) # Feeds the timing data to the subtitle maker
                    
        # Save the SRT file
        with open(srt_output, "w", encoding="utf-8") as srt_file:
            srt_file.write(submaker.get_srt())
            
        print(f"[Success] Audio saved as: '{audio_output}'")
        print(f"[Success] Subtitles saved as: '{srt_output}'")
    except Exception as e:
        print(f"Error during audio generation: {e}")

# ==========================================
# 4. AUDIO MIXING ENGINE
# ==========================================
def add_background_music(voice_file, bg_music_file, output_file):
    print("\n[3/3] Blending voice with background track...")
    try:
        voice = AudioSegment.from_file(voice_file)
        bg_music = AudioSegment.from_file(bg_music_file)
        
        bg_music = bg_music - 15 
        
        if len(bg_music) < len(voice):
            loop_count = (len(voice) // len(bg_music)) + 1
            bg_music = bg_music * loop_count
            
        bg_music = bg_music[:len(voice)]
        final_audio = voice.overlay(bg_music)
        
        final_audio.export(output_file, format="mp3")
        print(f"[Success] Final track saved as: '{output_file}'")
        
    except FileNotFoundError:
        print(f"[Error] Could not find the background music file: {bg_music_file}")
    except Exception as e:
        print(f"[Error] Mixing failed: {e}")

# ==========================================
# 5. MAIN EXECUTION (The Smart Loop)
# ==========================================
async def main():
    print("=== Ultimate YouTube Shorts Localization Pipeline ===")
    
    VIDEO_TOPIC = "Home Dumbbell Workout" 
    
    # 1. Create the custom output folder if it doesn't exist yet
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    print(f"\n📁 Final files will be saved to: {OUTPUT_FOLDER}")
    
    # 2. THE SMART MUSIC CHECKER
    mix_music = True
    if not os.path.exists(BACKGROUND_MUSIC_PATH):
        print(f"\n⚠️ [Warning] We couldn't find your music file at: {BACKGROUND_MUSIC_PATH}")
        print("🧠 [AI] Asking Gemini for a music suggestion...")
        
        # Ask Gemini for a song suggestion based on the topic
        try:
            prompt = f"In one short sentence, suggest 2 specific genres of royalty-free background music that would perfectly fit a YouTube Short about '{VIDEO_TOPIC}'."
            response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
            print(f"\n💡 [Gemini Suggests]: {response.text.strip()}")
        except:
            print("\n💡 [Suggestion]: Try searching YouTube for an 'Aggressive Phonk Beat' or 'Lo-Fi Chill Track'.")
            
        # Ask the user what they want to do
        user_choice = input("\nDo you want to SKIP adding music and continue anyway? (y/n): ").strip().lower()
        
        if user_choice == 'y':
            print("\n⏩ Skipping background music. Generating voice and subtitles only...")
            mix_music = False
        else:
            print("\n🛑 Program stopped. Go download your music, update the path, and run this again!")
            return # Exits the program entirely
    
    # 3. Your script chunks
    scripts = [
        "What's up guys! Today we are hitting a crazy dumbbell workout at home.",
        "Grab your weights, make sure your form is tight, and let's build some muscle.",
        "Don't forget to like and subscribe for more daily fitness routines!"
    ]
    
    for index, text in enumerate(scripts):
        clip_num = index + 1
        print(f"\n--- Processing Clip {clip_num} ---")
        
        # 4. Save files directly to your custom OUTPUT_FOLDER
        raw_voice_file = os.path.join(OUTPUT_FOLDER, f"clip_{clip_num}_voice.mp3")
        subtitle_file = os.path.join(OUTPUT_FOLDER, f"clip_{clip_num}_subs.srt")
        final_mixed_file = os.path.join(OUTPUT_FOLDER, f"clip_{clip_num}_FINAL.mp3")
        
        # Step 1: Translate
        hinglish_text = translate_to_hinglish(text, VIDEO_TOPIC)
        
        if hinglish_text:
            # Step 2: Generate Voice and Subtitles
            await generate_audio_and_subs(hinglish_text, raw_voice_file, subtitle_file)
            
            # Step 3: Mix Audio (Only runs if you didn't skip!)
            if mix_music:
                add_background_music(raw_voice_file, BACKGROUND_MUSIC_PATH, final_mixed_file)
            
    print("\n✅ === All Clips Processed Successfully! ===")

if __name__ == "__main__":
    asyncio.run(main())