import cv2
import numpy as np
import argparse

# 配置图片存放参数
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())


# 读取图片
img = cv2.imread(args['image'])

# 照片提亮
alpha = 2
beta = 20
new_img = np.zeros(img.shape, img.dtype)
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        for c in range(img.shape[2]):
            new_img[y, x, c] = np.clip(alpha * img[y, x, c] + beta, 0, 255)
img_copy = new_img.copy()
img_gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
_, img_thresh = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY_INV)

# 配置HSV
target_color = ['green', 'red', 'blue', 'purple', 'yellow']

color_dist = {'red': {'Lower': np.array([0, 112, 120]), 'Upper': np.array([9, 184, 205])},
              'blue': {'Lower': np.array([87, 28, 66]), 'Upper': np.array([122, 146, 134])},
              'green': {'Lower': np.array([40, 25, 75]), 'Upper': np.array([82, 97, 203])},
              'purple': {'Lower': np.array([121, 26, 125]), 'Upper': np.array([178, 71, 210])},
              'yellow': {'Lower': np.array([18, 134, 183]), 'Upper': np.array([25, 222, 255])},
              }

# 高斯模糊
img_gaussian = cv2.GaussianBlur(new_img, (5, 5), 0)

# 转换为HSV图像
img_hsv = cv2.cvtColor(img_gaussian, cv2.COLOR_BGR2HSV)

# 腐蚀操作
img_hsv = cv2.erode(img_hsv, None, iterations=2)

# 找匹配
color_dict = {}
for i, color in enumerate(target_color):
    inRange_hsv = cv2.inRange(img_hsv, color_dist[color]['Lower'], color_dist[color]['Upper'])
    cnts = cv2.findContours(inRange_hsv.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    c = max(cnts, key=cv2.contourArea)
    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)
    cv2.drawContours(img_copy, [np.int0(box)], -1, (0, 255, 255), 2)
    cv2.putText(img_copy, color, (np.int0(box)[1][0]-5, np.int0(box)[1][1]),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
cv2.imshow('image', img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
