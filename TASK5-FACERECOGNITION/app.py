import tkinter as tk
import cv2
from video_stream import start_video_stream

def main():
    root = tk.Tk()
    root.title("Live Face Detection")
    root.geometry("800x600")
    root.resizable(False, False)

    video_label = tk.Label(root)
    video_label.pack(expand=True, fill=tk.BOTH)

    start_button = tk.Button(
        root,
        text="Start Detection",
        command=lambda: start_video_stream(video_label)
    )
    start_button.pack(pady=10)
    def on_closing():
        if "video_capture" in locals():
            video_capture.release()
        root.destroy()
        cv2.destroyAllWindows()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()
