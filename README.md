# YouTube Video Downloader

A simple command-line YouTube downloader built with Python and `yt-dlp`.

You can download videos in different qualities or extract the audio as an MP3. No complicated setup, no GUI, just run the script, paste a URL, choose your quality, and you're good to go.

> Use this tool only for content you have permission to download and in accordance with YouTube's Terms of Service and applicable laws.

## What can it do?

* Download the best available quality, including up to 4K when available
* Download up to 1080p
* Download up to 720p
* Download up to 480p
* Download audio as MP3
* Automatically create a `Downloads` folder
* Automatically merge video and audio using FFmpeg
* Keep downloaded files organized in one folder

## Project Structure

```text
youtube-downloader/
│
├── downloader.py
├── requirements.txt
├── README.md
└── Downloads/
```

You can name the Python file whatever you want. In the examples below, I'll assume it is called `downloader.py`.

---

# 1. What you need

You only need three things:

1. Python
2. `yt-dlp`
3. FFmpeg

Don't worry if you've never used Python before. The setup is pretty straightforward.

---

# 2. Install Python

## Windows

Download Python from the official Python website:

https://www.python.org/downloads/

During installation, make sure you check:

```text
Add Python to PATH
```

Then finish the installation.

To check if it worked, open Command Prompt and run:

```bash
python --version
```

You should see something similar to:

```text
Python 3.13.x
```

## Linux

Most Linux distributions already include Python.

Check with:

```bash
python3 --version
```

If Python isn't installed, use your distribution's package manager.

For Fedora:

```bash
sudo dnf install python3
```

For Ubuntu/Debian:

```bash
sudo apt install python3
```

## macOS

Check whether Python is installed:

```bash
python3 --version
```

If you need it, download it from:

https://www.python.org/downloads/macos/

---

# 3. Download this project

If you downloaded the project as a ZIP:

1. Extract the ZIP file.
2. Open the extracted folder.
3. You should see the Python file.

If you're using Git:

```bash
git clone YOUR_REPOSITORY_URL
cd youtube-downloader
```

---

# 4. Install yt-dlp

Open a terminal inside the project folder.

Run:

```bash
pip install yt-dlp
```

If that doesn't work on Linux/macOS, try:

```bash
pip3 install yt-dlp
```

You can also use:

```bash
python -m pip install yt-dlp
```

or on Linux:

```bash
python3 -m pip install yt-dlp
```

---

# 5. Install FFmpeg

FFmpeg is important because YouTube often provides video and audio as separate streams.

For example:

```text
Video: 1080p
Audio: separate audio stream
```

FFmpeg combines them into one playable video file.

It is also required to convert audio to MP3.

## Windows

Download FFmpeg from:

https://ffmpeg.org/download.html

After installing it, make sure FFmpeg is added to your system PATH.

Check it with:

```bash
ffmpeg -version
```

If you see FFmpeg information, you're set.

## Fedora

Run:

```bash
sudo dnf install ffmpeg
```

Then check:

```bash
ffmpeg -version
```

## Ubuntu/Debian

Run:

```bash
sudo apt update
sudo apt install ffmpeg
```

Then:

```bash
ffmpeg -version
```

## macOS

If you use Homebrew:

```bash
brew install ffmpeg
```

Then:

```bash
ffmpeg -version
```

---

# 6. Install everything from requirements.txt

If the project contains a `requirements.txt` file, you can install the dependencies in one command.

```bash
pip install -r requirements.txt
```

A basic `requirements.txt` for this project can contain:

```text
yt-dlp
```

You still need to install FFmpeg separately because it is a system program rather than a Python package.

---

# 7. Run the downloader

Open your terminal inside the project folder.

Run:

### Windows

```bash
python downloader.py
```

### Linux/macOS

```bash
python3 downloader.py
```

You should see:

```text
--- YouTube Video Downloader ---

Paste the YouTube URL here:
```

Paste your YouTube URL and press Enter.

Then you'll get:

```text
Select Output Quality:

1. Best Available (Up to 4K)
2. 1080p
3. 720p
4. 480p
5. Audio Only (MP3)

Enter your choice (1-5):
```

Enter the number you want.

For example:

```text
Enter your choice (1-5): 2
```

The downloader will start processing the video.

---

# 8. Where are my downloads?

By default, the program creates a folder called:

```text
Downloads
```

inside the same folder where you run the Python script.

For example:

```text
youtube-downloader/
│
├── downloader.py
├── requirements.txt
├── README.md
└── Downloads/
    └── My Video.mp4
```

You don't have to create the `Downloads` folder yourself.

The program does this automatically:

```python
output_folder = 'Downloads'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
```

---

# 9. How to change the download folder

This is probably the most useful thing to customize.

Find this line in the Python code:

```python
output_folder = 'Downloads'
```

Change it to whatever folder you want.

## Example: Desktop

```python
output_folder = 'Desktop'
```

This creates:

```text
Desktop/
```

inside the project directory.

### Important

If you want to save to a specific location on your computer, you can provide the full path.

For example on Linux:

```python
output_folder = '/home/yourusername/Videos'
```

On Windows:

```python
output_folder = r'C:\Users\YourName\Videos'
```

The `r` before the Windows path is useful because Windows paths contain backslashes.

You can also use forward slashes:

```python
output_folder = 'C:/Users/YourName/Videos'
```

---

# 10. Change the folder name only

If you simply want the downloader to use a folder called `Videos` instead of `Downloads`:

Change:

```python
output_folder = 'Downloads'
```

to:

```python
output_folder = 'Videos'
```

That's it.

---

# 11. Choosing video quality

The downloader gives you five options.

### 1. Best Available

```text
1. Best Available (Up to 4K)
```

Downloads the highest quality available.

If the video is available in 4K, it can download 4K.

If the video is only available in 1080p, you'll get 1080p.

### 2. 1080p

```text
2. 1080p
```

Downloads the best quality available up to 1080p.

### 3. 720p

```text
3. 720p
```

Downloads the best quality available up to 720p.

### 4. 480p

```text
4. 480p
```

Downloads the best quality available up to 480p.

### 5. MP3

```text
5. Audio Only (MP3)
```

Downloads the audio and converts it to MP3 at 192 kbps.

---

# 12. How the quality system works

You don't have to understand this to use the program

# Yt-dowloader-

A simple Python-based video downloader using yt-dlp and FFmpeg. Download videos in different qualities or extract audio as MP3 with an easy command-line interface.

, but if you're curious:

For 1080p, the program uses:

```python
bestvideo[height<=1080]+bestaudio/best
```

This tells `yt-dlp`:

```text
Find the best video stream up to 1080p
+
Find the best audio stream
```

FFmpeg then combines them into one video file.

This is why FFmpeg is needed for many high-quality downloads.

---

# 13. Changing the default quality

If you enter an invalid option, the program currently defaults to 1080p.

This part:

```python
else:
    print("Invalid choice. Defaulting to Best Available (1080p).")
    format_string = 'bestvideo[height<=1080]+bestaudio/best'
```

can be changed if you want a different default.

For example, to default to 720p:

```python
format_string = 'bestvideo[height<=720]+bestaudio/best'
```

---

# 14. Changing the MP3 quality

The current audio setting is:

```python
'preferredquality': '192',
```

So the output is approximately:

```text
192 kbps MP3
```

You can change it to:

```python
'preferredquality': '128',
```

or:

```python
'preferredquality': '320',
```

Higher bitrate generally means a larger file.

---

# 15. Common problems

## `No module named yt_dlp`

You haven't installed `yt-dlp`.

Run:

```bash
pip install yt-dlp
```

or:

```bash
python3 -m pip install yt-dlp
```

---

## `ffmpeg is not installed`

Install FFmpeg and make sure it is available from your terminal.

Check:

```bash
ffmpeg -version
```

If the command isn't recognized, FFmpeg probably isn't correctly installed or isn't in your PATH.

---

## Video downloads but doesn't play correctly

Make sure FFmpeg is installed.

High-quality YouTube videos can have separate video and audio streams, so FFmpeg is used to merge them.

---

## The URL doesn't work

Make sure you copied the complete YouTube URL.

For example:

```text
https://www.youtube.com/watch?v=xxxxxxxxxxx
```

Also make sure the video is publicly accessible and that you have permission to download it.

---

## The program closes immediately

Don't double-click the `.py` file.

Instead, open a terminal in the project folder and run:

```bash
python downloader.py
```

That way, you can actually see any error messages.

---

# 16. Updating yt-dlp

YouTube changes frequently, so keeping `yt-dlp` updated is a good idea.

Run:

```bash
pip install -U yt-dlp
```

or:

```bash
python3 -m pip install -U yt-dlp
```

If downloads suddenly stop working, updating `yt-dlp` should be one of the first things you try.

---

# 17. Quick setup

If you're comfortable with the terminal, the whole setup is basically:

```bash
git clone YOUR_REPOSITORY_URL
cd youtube-downloader

pip install -r requirements.txt

python downloader.py
```

Make sure FFmpeg is installed separately.

---

# 18. For non-technical users

If you've never coded before, here's the short version:

### Step 1

Install Python.

### Step 2

Install FFmpeg.

### Step 3

Open the project folder.

### Step 4

Open a terminal in that folder.

### Step 5

Install the Python dependency:

```bash
pip install yt-dlp
```

### Step 6

Start the program:

```bash
python downloader.py
```

### Step 7

Paste a YouTube URL.

### Step 8

Choose your quality.

### Step 9

Find your video inside the `Downloads` folder.

That's literally it.

---

# 19. Customization

The main settings are near the middle of the Python file.

### Download location

```python
output_folder = 'Downloads'
```

### Output filename

Currently:

```python
'outtmpl': f'{output_folder}/%(title)s.%(ext)s'
```

This means the file will be saved using the video's title.

For example:

```text
Downloads/
└── My Awesome Video.mp4
```

You can customize the filename template if you want.

For example:

```python
'outtmpl': f'{output_folder}/%(title)s - %(id)s.%(ext)s'
```

would produce something like:

```text
My Awesome Video - abc123xyz.mp4
```

---

# 20. Disclaimer

This project is intended for educational and personal use.

Downloading copyrighted content without permission may violate copyright law or the platform's terms. Make sure you have the necessary rights or permission before downloading content.

The developer is not responsible for how this software is used.

---

# 21. Tech Stack

* Python
* yt-dlp
* FFmpeg

Simple stack. Does one job and does it without pretending to be a full-blown application.

---

# 22. License

Add your preferred license here.

For example, if you're using the MIT License:

```text
MIT License
```

---

## That's it

No account system.
No database.
No unnecessary UI.
Paste URL → choose quality → download.

If something breaks, check the **Common Problems** section first. In most cases, it's either `yt-dlp` or FFmpeg needing an update.

# Yt-dowloader-

A simple Python-based video downloader using yt-dlp and FFmpeg. Download videos in different qualities or extract audio as MP3 with an easy command-line interface.
