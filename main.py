from pytube import YouTube
import os

def show_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(f"Downloaded {percentage_of_completion:.2f}%")

def download_video(url, path):
    try:
        # Create a YouTube object
        yt = YouTube(url)
        yt.register_on_progress_callback(show_progress)

        # Get the highest resolution stream
        video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        # Download the video
        video_stream.download(path)
        print(f"Downloaded: {yt.title}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # URL of the YouTube video
    video_url = "YOUR_VIDEO_URL"

    # Path where you want to save the video
    save_path = "PATH_WHERE_YOU_WANT_TO_SAVE_YOUR_FILE"

    # Download the video
    download_video(video_url, save_path)
