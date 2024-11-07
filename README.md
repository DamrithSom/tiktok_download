TikTok Video Downloader
TikTok Video Downloader is a Python application designed to download TikTok videos in bulk. Simply provide a text file containing TikTok video URLs, and the app will download each video to your local directory. The application features a user-friendly GUI built with customtkinter.

Features
Select a text file with TikTok video URLs.
Download multiple videos at once.
View real-time status updates in a scrollable message log.
Dark-themed, modern GUI with easy navigation.
Prerequisites
Python 3.x
Chrome browser installed (required by pyktok)
Installation
Clone this repository:

bash
Copy code
git clone https://github.com/yourusername/tiktok-video-downloader.git
cd tiktok-video-downloader
Install the required Python packages. You can do this in two ways:

Option A: Install packages individually
bash
Copy code
pip install pyktok beautifulsoup4 browser-cookie3 numpy pandas requests selenium streamlit
Option B: Use requirements.txt
Alternatively, use the requirements.txt file for a one-step installation:

bash
Copy code
pip install -r requirements.txt
Make sure to save this file as requirements.txt:

plaintext
Copy code
pyktok
beautifulsoup4
browser-cookie3
numpy
pandas
requests
selenium
streamlit
Usage
Run the Application: Start the app by running:

bash
Copy code
python main.py
Browse for File:

Click "Browse Files" to select a text file containing TikTok video URLs. Each URL should be on a separate line.
Download Videos:

Click "Download" to start the download process. Progress messages will appear in the message log panel, and a popup will indicate when all videos have been downloaded.
License
© 2024 Damrith Som. All rights reserved.
