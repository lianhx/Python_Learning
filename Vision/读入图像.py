import cv2


# 读取图像，解决imread不能读取中文路径的问题
# def cv_imread(file_path):
#     cv_img = cv.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
#     return cv_img

img = cv2.imread('Vision/src/messi5.jpg')
cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF
if k == 27:  # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):  # wait for 's' key to save and exit
    cv2.imwrite('Vision/src/messigray.png', img)
    cv2.destroyAllWindows()
