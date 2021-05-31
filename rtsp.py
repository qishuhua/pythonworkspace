#! /usr/bin/python
# coding=utf-8
import cv2
import time
import datetime

def main1():
	cap = cv2.VideoCapture("rtsp://admin:1qaz2wsx@192.168.10.198:554/h264/ch1/sub/av_stream")
	t = 0
	while True:
		ret, frame = cap.read()
		if time.time() - t > 5:
			t = time.time()
			cv2.imwrite('C:/Users/admin/Documents/98.jpg', frame)  # 存储为图像
		pass
	cap.release()
	cv2.destroyAllWindows()

def main():
	cap = cv2.VideoCapture("rtsp://admin:1qaz2wsx@192.168.10.198:554/h264/ch1/sub/av_stream")
	ret, frame = cap.read()
	cv2.imwrite('C:/Users/admin/Documents/99.jpg', frame)  # 存储为图像
	cap.release()
	cv2.destroyAllWindows()

if __name__=='__main__':
	main()
