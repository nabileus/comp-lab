import os
import subprocess
import shutil

# Create a 'frame' folder in the current directory
frame_folder = 'frames'

os.makedirs('gifs', exist_ok=True)
os.makedirs('comp', exist_ok=True)

# Get a list of video files with .mp4 and .webm extensions in the current directory
video_files = [filename for filename in os.listdir() if filename.endswith((".mp4", ".webm"))]

for video_filename in video_files:
    # Use ffmpeg to extract frames from the video
    
    os.makedirs(frame_folder, exist_ok=True)

    frame_rate = 10
    delay = round(100 / frame_rate, 2)
    ffmpeg_cmd = f"ffmpeg -i {video_filename} -r {frame_rate} {frame_folder}/frame_%04d.png"
    subprocess.run(ffmpeg_cmd, shell=True)

    # Set the gif filename to be the video filename without the extension
    video_filename_without_extension = os.path.splitext(video_filename)[0]
    gif_filename = f"{video_filename_without_extension}.gif"

    # Use ImageMagick to convert the frames to a GIF
    imagemagick_cmd = f"convert -delay {delay} -loop 0 {frame_folder}/frame_*.png gifs/{gif_filename}"
    subprocess.run(imagemagick_cmd, shell=True)

    print(f"Frames extracted and converted to '{gif_filename}' for {video_filename}")

    # Compression
    print(f"Compression Started for {gif_filename}")

    comp_name = f"{video_filename_without_extension}-comp.gif"
    comp_cmd = f"convert gifs/{gif_filename} -resize 50% -layers Optimize -colors 128  -fuzz 2% -dither FloydSteinberg -coalesce -layers Optimize comp/{comp_name}"
    subprocess.run(comp_cmd, shell=True)

    print(f"Compression Finished for {gif_filename}")

    # Delete the 'frame' folder
    shutil.rmtree(frame_folder)
    print(f"'{frame_folder}' folder and frames deleted for {video_filename}")
