import cv2
import numpy as np
import utils

def score(input_path='examples/1.jpg'):
    src = 255 - cv2.imread(input_path,0)
    scores = []

    h,w = src.shape
    small_dimention = min(h,w)
    src = src[:small_dimention, :small_dimention]

    # Rotate the image around in a circle
    angle = 0
    ang_score = []
    while angle <= 360:
        # Rotate the source image
        img = utils.rotate(src, angle)    
        # Crop the center 1/3rd of the image (roi is filled with text)
        h,w = img.shape
        buffer = min(h, w) - int(min(h,w)/1.5)
        #roi = img.copy()
        roi = img[int(h/2-buffer):int(h/2+buffer), int(w/2-buffer):int(w/2+buffer)]
        # Create background to draw transform on
        bg = np.zeros((buffer*2, buffer*2), np.uint8)
        # Threshold image
        _, roi = cv2.threshold(roi, 140, 255, cv2.THRESH_BINARY)
        # Compute the sums of the rows
        row_sums = utils.sum_rows(roi)
        # High score --> Zebra stripes
        score = np.count_nonzero(row_sums)
        if sum(row_sums) < 100000: scores.append(angle)
        # k = display_data(roi, row_sums, buffer)
        # if k == 27: break
        # Increment angle and try again
        angle += .5
        ang_score.append((score, angle))
        # print(score, angle)

    # Rotate the source image
    temp1 = min([i for i, j in ang_score])
    temp2 = dict(ang_score)[temp1]+180

    img = utils.rotate(cv2.imread(input_path), temp2)
    out_path = '/'.join(['output', input_path.split('/')[-1]])
    
    cv2.imwrite(out_path, img)

if __name__ == '__main__':
    score(input_path='examples/1.jpg')
    score(input_path='examples/2.jpg')
    score(input_path='examples/3.jpg')
    score(input_path='examples/4.jpg')
    score(input_path='examples/5.jpg')
    score(input_path='examples/6.jpg')
    score(input_path='examples/7.jpg')
    score(input_path='examples/8.jpg')
    score(input_path='examples/10.jpg')
    score(input_path='examples/11.jpg')
    score(input_path='examples/12.jpg')
    score(input_path='examples/13.jpg')
