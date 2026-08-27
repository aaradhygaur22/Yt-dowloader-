import yt_dlp
import os

def download_video():
    print("--- YouTube Video Downloader ---")
    url = input("Paste the YouTube URL here: ").strip()
    
    if not url:
        print("No URL provided. Exiting.")
        return

    # 1. Ask the user for their preferred quality
    print("\nSelect Output Quality:")
    print("1. Best Available (Up to 4K)")
    print("2. 1080p")
    print("3. 720p")
    print("4. 480p")
    print("5. Audio Only (MP3)")
    
    choice = input("\nEnter your choice (1-5): ").strip()
    
    # 2. Map the choice to the correct yt-dlp format filter
    if choice == '1':
        format_string = 'bestvideo+bestaudio/best'
    elif choice == '2':
        format_string = 'bestvideo[height<=1080]+bestaudio/best'
    elif choice == '3':
        format_string = 'bestvideo[height<=720]+bestaudio/best'
    elif choice == '4':
        format_string = 'bestvideo[height<=480]+bestaudio/best'
    elif choice == '5':
        format_string = 'bestaudio/best'
    else:
        print("Invalid choice. Defaulting to Best Available (1080p).")
        format_string = 'bestvideo[height<=1080]+bestaudio/best'

    output_folder = 'Downloads'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 3. Setup configuration options
    ydl_opts = {
        'format': format_string,
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
        'quiet': False,
        'no_warnings': True
    }

    # If the user selected "Audio Only", tell FFmpeg to convert it to MP3
    if choice == '5':
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    else:
        # Otherwise, merge video and audio into an MP4 file
        ydl_opts['merge_output_format'] = 'mp4'

    print(f"\nAttempting to download from: {url}")
    print("Fetching video information and downloading... This may take a moment.")
    
    # 4. Execute the download
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
        print(f"\n✅ Success! Saved to the '{output_folder}' folder.")
        
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Note: If you are trying to download high-res video and get an error, make sure FFmpeg is installed.")

if __name__ == "__main__":
    download_video()