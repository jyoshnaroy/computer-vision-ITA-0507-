import cv2
cap = cv2.VideoCapture("sample.mp4")
frames = []
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

height, width, layers = frames[0].shape
fps = 30  
out = cv2.VideoWriter(
    "reverse_sample.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (width, height)
)
for frame in reversed(frames):
    out.write(frame)
out.release()

print("Reverse video created successfully as reverse_sample.mp4")
