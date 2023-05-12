import os
import sys
import cv2

def extract_frames(video_path, output_dir, frame_interval):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    video = cv2.VideoCapture(video_path)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    for frame_number in range(0, total_frames, frame_interval):
        video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ret, frame = video.read()

        if not ret:
            print(f"Error reading frame {frame_number}")
            break

        output_file = os.path.join(output_dir, f"frame_{frame_number}.png")
        cv2.imwrite(output_file, frame)
        print(f"Extracted frame {frame_number} to {output_file}")

    video.release()
    print("Finished extracting frames.")

if __name__ == "__main__":
    video_path, output_dir, fps = sys.argv[1:]
    fps = int(fps)
    extract_frames(video_path, output_dir, fps)
