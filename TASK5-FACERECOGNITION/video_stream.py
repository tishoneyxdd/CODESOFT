import cv2
from PIL import Image, ImageTk
from detector import detect_faces, draw_faces

def start_video_stream(video_label):
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    video_capture = cv2.VideoCapture(0)

    if not video_capture.isOpened():
        print("Error: Unable to access the camera.")
        return

    def update_frame():
        ret, frame = video_capture.read()
        if not ret:
            print("Error: Unable to read from camera.")
            return

        faces = detect_faces(frame, face_cascade)
        frame = draw_faces(frame, faces)

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = ImageTk.PhotoImage(Image.fromarray(rgb_frame))
        video_label.configure(image=image)
        video_label.image = image

        video_label.after(10, update_frame)

    update_frame()

    return video_capture
