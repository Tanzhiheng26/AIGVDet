import os
import subprocess

# Base paths
test_dir = "frame/0_real/" # Directory contains directories of frames
optical_dir = "optical_result/0_real/"
mop_path = "checkpoints/optical.pth"
mor_path = "checkpoints/original.pth"
threshold = "0.1"

# Ensure directories exist
assert os.path.isdir(test_dir), f"Directory not found: {test_dir}"
frame_folders = [f for f in os.listdir(test_dir) if os.path.isdir(os.path.join(test_dir, f))]

# Run the command for each folder
for folder in frame_folders:
    folder_original_path = os.path.join(test_dir, folder)
    folder_optical_flow_path = os.path.join(optical_dir, folder)

    command = [
        "python", "demo.py",
        "--folder_original_path", folder_original_path,
        "--folder_optical_flow_path", folder_optical_flow_path,
        "-mop", mop_path,
        "-mor", mor_path,
        "-t", threshold,
    ]

    print("Running:", " ".join(command))
    subprocess.run(command)
