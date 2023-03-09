
import cv2

from Picture_link_method import Stitcher
imageA = cv2.imread("1.jpg")
imageB = cv2.imread("2.jpg")
save_out = "D:\\pythonProject\\resource\\result\\result.png"
stitcher = Stitcher()
(result, vis) = stitcher.Stitch([imageA, imageB], method=1)
cv2.imwrite(save_out,result)