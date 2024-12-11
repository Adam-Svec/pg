#!/usr/bin/env python3
import sys
import subprocess
import os
import platform

def sanitize_filename(name):
    """Create a safe filename from video title."""
    if not name:
        name = "youtube_audio"
    # Remove special characters and replace spaces
    return "".join(c if c.isalnum() or c in [' ', '_', '-'] else '_' for c in name).rstrip()

def install(package, upgrade=False):
    """
    Install or upgrade a Python package with robust error handling.
    
    :param package: Name of the package to install
    :param upgrade: Whether to upgrade the package
    :return: True if installation was successful, False otherwise
    """
    try:
        pip_cmd = [sys.executable, "-m", "pip"]
        
        # Ensure pip is up to date
        subprocess.check_call(pip_cmd + ["install", "--upgrade", "pip"])
        
        # Prepare install command
        if upgrade:
            install_cmd = pip_cmd + ["install", "--upgrade"]
        else:
            install_cmd = pip_cmd + ["install"]
        
        # Add package name
        install_cmd.append(package)
        
        # Run installation
        subprocess.check_call(install_cmd)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package}: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error installing {package}: {e}")
        return False

def check_system_dependencies():
    """
    Check and install system-level dependencies.
    """
    system = platform.system()
    
    if system == "Linux":
        # Attempt to install FFmpeg on Linux
        try:
            subprocess.check_call(["which", "ffmpeg"])
        except subprocess.CalledProcessError:
            print("FFmpeg not found. Attempting to install...")
            try:
                # Try package managers
                subprocess.check_call(["sudo", "apt-get", "update"])
                subprocess.check_call(["sudo", "apt-get", "install", "-y", "ffmpeg"])
            except Exception as e:
                print(f"Could not install FFmpeg: {e}")
                print("Please install FFmpeg manually.")

def setup_transcription_environment():
    """
    Set up the environment for YouTube audio transcription.
    Installs necessary Python packages with robust error handling.
    """
    # List of packages to install
    packages = [
        "pytube",
        "yt-dlp",  # Replacing youtube_dl with yt-dlp
        "openai-whisper",
        "setuptools",
        "wheel",
        "deep_translator"
    ]
    
    # Check system dependencies first
    check_system_dependencies()
    
    # Install packages
    for package in packages:
        if not install(package):
            print(f"Failed to install {package}. Attempting alternative installation...")
            
            # Try with pip directly if subprocess method fails
            try:
                import pip
                pip.main(["install", package])
            except Exception as e:
                print(f"Alternative installation for {package} failed: {e}")

def download_audio_from_youtube(url, out_dir=".", file_name=None):
    """
    Robust YouTube audio download function with multiple download methods.
    
    :param url: YouTube video URL
    :param out_dir: Output directory for downloaded audio
    :param file_name: Optional custom filename
    :return: Path to downloaded audio file
    """
    # Try multiple download methods
    download_methods = [
        # Method 1: yt-dlp (more robust than youtube_dl)
        lambda: _download_with_ytdlp(url, out_dir, file_name),
        
        # Method 2: pytube (if yt-dlp fails)
        lambda: _download_with_pytube(url, out_dir, file_name)
    ]

    for method in download_methods:
        try:
            downloaded_file = method()
            if downloaded_file and os.path.exists(downloaded_file):
                return downloaded_file
        except Exception as e:
            print(f"Download method failed: {e}")
    
    raise RuntimeError("Could not download audio from the provided YouTube URL")

def _download_with_pytube(url, out_dir, file_name=None):
    """Download audio using pytube."""
    from pytube import YouTube
    
    yt = YouTube(url)
    video_title = sanitize_filename(yt.title)
    
    if not file_name:
        file_name = os.path.join(out_dir, f"{video_title}_audio.mp4")
    
    # Select highest quality audio stream
    audio_stream = (yt.streams
                    .filter(only_audio=True)
                    .order_by('abr')
                    .desc()
                    .first())
    
    return audio_stream.download(output_path=out_dir, filename=os.path.basename(file_name))

def _download_with_ytdlp(url, out_dir, file_name=None):
    """Download audio using yt-dlp as a fallback."""
    import yt_dlp
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(out_dir, '%(title)s.%(ext)s'),
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_title = sanitize_filename(info_dict.get('title', 'youtube_audio'))
        file_name = os.path.join(out_dir, f"{video_title}.mp3")
        return file_name

def transcribe_audio(file_path, model_size="base", generate_text=True, generate_srt=True):
    """
    Transcribe audio using OpenAI Whisper.
    
    :param file_path: Path to the audio file
    :param model_size: Size of Whisper model (tiny, base, small, medium, large)
    :param generate_text: Generate .txt transcript
    :param generate_srt: Generate .srt subtitles
    :return: Transcription result dictionary
    """
    import torch
    import whisper
    from pathlib import Path
    from whisper.utils import get_writer

    # Determine device
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")

    # Load Whisper model
    model = whisper.load_model(model_size).to(device)

    # Print transcription details
    print("\n=======================")
    print(f"🤖 Whisper Model: {model_size}")
    print(f"📁 Audio File: {file_path}")
    print("=======================")

    # Transcribe audio
    print("\n==> Transcribing audio")
    result = model.transcribe(file_path, verbose=False)

    # Get file paths
    file_path = Path(file_path)
    output_directory = file_path.parent

    # Generate text file
    if generate_text:
        print(f"\n==> Creating .txt file")
        txt_path = file_path.with_suffix(".txt")
        with open(txt_path, "w", encoding="utf-8") as txt:
            txt.write(result["text"])
        print(f"Text transcript saved to: {txt_path}")

    # Generate SRT subtitles
    if generate_srt:
        print(f"\n==> Creating .srt file")
        srt_writer = get_writer("srt", output_directory)
        srt_writer(result, str(file_path.stem))
        print(f"SRT subtitles saved to: {output_directory}/{file_path.stem}.srt")

    print("\n✨ Transcription Complete!")
    print("=======================")
    return result

def translate_whisper_result(result, target_language='en'):
    """
    Translate the transcription result using Google Translate API.
    
    :param result: Whisper transcription result
    :param target_language: Target language code (default is English)
    :return: Translated text
    """
    try:
        from deep_translator import GoogleTranslator
        
        # Translate the entire text
        translator = GoogleTranslator(source='auto', target=target_language)
        translated_text = translator.translate(result['text'])
        
        # If segments exist, attempt to translate each segment
        if 'segments' in result:
            translated_segments = []
            for segment in result['segments']:
                try:
                    translated_segment = translator.translate(segment['text'])
                    translated_segments.append({
                        **segment,
                        'text': translated_segment
                    })
                except Exception as e:
                    print(f"Error translating segment: {e}")
                    translated_segments.append(segment)
            
            result['translated_segments'] = translated_segments
        
        result['translated_text'] = translated_text
        return result
    
    except ImportError:
        print("Deep Translator not found. Installing...")
        install('deep_translator')
        return translate_whisper_result(result, target_language)
    except Exception as e:
        print(f"Translation error: {e}")
        return result

def process_audio_translation(audio_file, model_size="base", source_language=None, target_language='en'):
    """
    Comprehensive audio processing function with optional translation.
    
    :param audio_file: Path to the audio file
    :param model_size: Whisper model size
    :param source_language: Source language hint for Whisper (optional)
    :param target_language: Target language for translation
    :return: Processed transcription result
    """
    # Transcribe audio
    transcription_result = transcribe_audio(
        audio_file, 
        model_size=model_size,
        generate_text=True, 
        generate_srt=True
    )
    
    # Add source language hint if provided
    if source_language:
        transcription_result['detected_language'] = source_language
    
    # Translate if target language is different
    if target_language and target_language.lower() != 'none':
        try:
            transcription_result = translate_whisper_result(
                transcription_result, 
                target_language
            )
        except Exception as e:
            print(f"Translation failed: {e}")
    
    return transcription_result

def generate_audio_report(result):
    """
    Generate a comprehensive report from the transcription result.
    
    :param result: Transcription result dictionary
    :return: Formatted report as string
    """
    report = "🎙️ Audio Transcription Report 🎙️\n"
    report += "=" * 40 + "\n\n"
    
    # Basic info
    report += f"📝 Original Text Length: {len(result.get('text', ''))} characters\n"
    
    # Language detection
    if 'detected_language' in result:
        report += f"🌐 Detected Language: {result['detected_language']}\n"
    
    # Translation info
    if 'translated_text' in result:
        report += f"🌍 Translated Text Length: {len(result['translated_text'])} characters\n"
        report += f"🔤 Translated Language: {result.get('target_language', 'Not specified')}\n"
    
    # Segment analysis
    if 'segments' in result:
        segment_count = len(result['segments'])
        total_segment_duration = sum(seg['end'] - seg['start'] for seg in result['segments'])
        
        report += f"\n📊 Segment Analysis:\n"
        report += f"   Total Segments: {segment_count}\n"
        report += f"   Total Speech Duration: {total_segment_duration:.2f} seconds\n"
    
    # Confidence and timing
    report += "\n🔍 Transcription Details:\n"
    report += f"   Model Size: {result.get('model_size', 'Unknown')}\n"
    report += f"   Timestamp: {result.get('timestamp', 'Not available')}\n"
    
    return report

def main():
    # Prompt user to input YouTube URL
    youtube_url = input("Please enter the YouTube URL to transcribe: ")
    
    # Set up environment
    setup_transcription_environment()
    
    try:
        # Download audio
        audio_file = download_audio_from_youtube(youtube_url)
        
        # Process audio with comprehensive options
        result = process_audio_translation(
            audio_file, 
            model_size="base",      # You can change model size here
            source_language=None,   # Optionally specify source language
            target_language='en'    # Translation target language
        )
        
        # Generate and print report
        report = generate_audio_report(result)
        print(report)
        
        # Optional: Save full result to JSON for further analysis
        import json
        with open('transcription_result.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() dssdsds