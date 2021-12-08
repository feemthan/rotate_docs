import cv2
def rotate(img, angle):
    rows,cols,*_ = img.shape
    M = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1)
    dst = cv2.warpAffine(img,M,(cols,rows))
    return dst

def sum_rows(img):
    # Create a list to store the row sums
    row_sums = []
    # Iterate through the rows
    for r in range(img.shape[0]-1):
        # Sum the row
        row_sum = sum(sum(img[r:r+1,:]))
        # Add the sum to the list
        row_sums.append(row_sum)
    # Normalize range to (0,255)
    row_sums = (row_sums/max(row_sums)) * 255
    # Return
    return row_sums