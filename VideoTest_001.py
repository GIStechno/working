import cv2
import os
import itertools
import time

# Function to display 3x3 grid of videos
def display_videos(video_paths):
    cap_list = [cv2.VideoCapture(video_path) for video_path in video_paths]

    while True:
        frames = []
        for cap in cap_list:
            ret, frame = cap.read()
            if not ret:
                # If the video ends, rewind it
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                ret, frame = cap.read()
            
            frames.append(frame)

        # Ensure all frames have the same dimensions
        frames = [cv2.resize(frame, (frames[0].shape[1], frames[0].shape[0])) for frame in frames]

        # Create a 3x3 grid
        video_grid = cv2.vconcat([cv2.hconcat(frames[:3]), cv2.hconcat(frames[3:6]), cv2.hconcat(frames[6:])])

        cv2.imshow('Video Grid', video_grid)
        cv2.waitKey(1)

        time.sleep(5)  # Display for 5 seconds

    # Release video captures
    for cap in cap_list:
        cap.release()


# Specify the directory path
directory_path = "/Users/user/Desktop/CNN/VideoSample/001/"

# Get a list of video files in the specified directory
video_files = [os.path.join(directory_path, file) for file in os.listdir(directory_path) if file.endswith(".mp4")]

# Display videos in sets of 9
for video_set in itertools.zip_longest(*[iter(video_files)] * 9, fillvalue=None):
    # Filter out any None values (in case the number of videos is not a multiple of 9)
    video_set = list(filter(None, video_set))
    display_videos(video_set)

# Destroy OpenCV windows when the loop ends
cv2.destroyAllWindows()