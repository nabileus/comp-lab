import os
import subprocess
import shutil

# Ask for the video filename
video_filename = input("Enter the video filename: ")

# Create a 'frame' folder in the current directory
frame_folder = 'frames'
os.makedirs(frame_folder, exist_ok=True)

# Use ffmpeg to extract frames from the video

frame_rate = int(input("Enter frame rate:"))
delay = round(100 / frame_rate, 2)
ffmpeg_cmd = f"ffmpeg -i {video_filename} -r {frame_rate} {frame_folder}/frame_%04d.png"
subprocess.run(ffmpeg_cmd, shell=True)

# Use ImageMagick to convert the frames to a GIF
video_filename_without_extension = os.path.splitext(video_filename)[0]
gif_filename = f"{video_filename_without_extension}.gif"
imagemagick_cmd = f"convert -delay {delay} -loop 0 {frame_folder}/frame_*.png {gif_filename}"
subprocess.run(imagemagick_cmd, shell=True)

print(f"Frames extracted and converted to '{gif_filename}'")

#compression
print(f"Compression Started")

comp_name = f"{video_filename_without_extension}-comp.gif"
comp_cmd = f"convert {gif_filename} -resize 50% -layers Optimize -colors 128 -fuzz 2% -dither FloydSteinberg -coalesce -layers Optimize {comp_name}"
subprocess.run(comp_cmd, shell=True)

print(f"Compression Finished")

# Delete the 'frame' folder
shutil.rmtree(frame_folder)
print(f"'{frame_folder}' folder and frames deleted.")
