import os
import subprocess

# Base paths
test_dir = "data/test/sora_mp4/" # Directory contains videos
frame_dir = "frame/1_fake/"
optical_dir = "optical_result/1_fake/"
mop_path = "checkpoints/optical.pth"
mor_path = "checkpoints/original.pth"
threshold = "0.1"

# Ensure directories exist
assert os.path.isdir(test_dir), f"Directory not found: {test_dir}"

mp4_files = [f for f in os.listdir(test_dir) if f.endswith(".mp4")]

# Run the command for each file
for mp4_file in mp4_files:
    video_path = os.path.join(test_dir, mp4_file)
    video_name = os.path.splitext(mp4_file)[0]

    folder_original_path = os.path.join(frame_dir, video_name)
    folder_optical_flow_path = os.path.join(optical_dir, video_name)

    command = [
        "python", "demo.py",
        "--path", video_path,
        "--folder_original_path", folder_original_path,
        "--folder_optical_flow_path", folder_optical_flow_path,
        "-mop", mop_path,
        "-mor", mor_path,
        "-t", threshold,
    ]

    print("Running:", " ".join(command))
    subprocess.run(command)
