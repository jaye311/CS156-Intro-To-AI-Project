import kagglehub

# Download latest version
path = kagglehub.dataset_download("enrique4/activity-recognition-with-accelerometer-and-sound")

print("Path to dataset files:", path)
