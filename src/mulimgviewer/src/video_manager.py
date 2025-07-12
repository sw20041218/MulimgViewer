import cv2
from PIL import Image

class VideoManager:
    def __init__(self, video_path):
        self.cap = cv2.VideoCapture(video_path)
        if not self.cap.isOpened():
            raise ValueError("无法打开视频文件")
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.current_frame_index = 0

    # def get_next_frame(self):
    #     if not self.cap.isOpened():
    #         return None
    #     ret, frame = self.cap.read()
    #     if not ret:
    #         return None
    #     self.current_frame_index += 1

    #     # 转换为 PIL.Image 对象
    #     frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #     return Image.fromarray(frame_rgb)
    def get_next_frame(self):
        if not self.cap.isOpened():
            return None

        ret, frame = self.cap.read()
        if not ret:
            return None

        # ✅ 从 OpenCV 获取实际帧编号
        self.current_frame_index = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES)) - 1

        # 转换为 PIL.Image
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return Image.fromarray(frame_rgb)

    # def get_frame(self, index):
    #     if not self.cap.isOpened():
    #         return None
    #     self.cap.set(cv2.CAP_PROP_POS_FRAMES, index)
    #     return self.get_next_frame()
    def get_frame(self, index):
        if not self.cap.isOpened():
            return None

        self.cap.set(cv2.CAP_PROP_POS_FRAMES, index)
        ret, frame = self.cap.read()
        if not ret:
            return None

        self.current_frame_index = index  # ✅ 明确设置当前帧号！

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return Image.fromarray(frame_rgb)

    def release(self):
        if self.cap.isOpened():
            self.cap.release()
