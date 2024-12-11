import numpy as np
import cv2


from imutils.perspective import four_point_transform

# Load the original image
img_orig = cv2.imread('05.jpg')
cv2.namedWindow('original', cv2.WINDOW_NORMAL)
cv2.imshow('original', img_orig)
cv2.waitKey()
cv2.destroyAllWindows()

# Resizing function
def resizer(image, width=500):
    h, w, c = image.shape
    height = int((h / w) * width)
    size = (width, height)
    image = cv2.resize(image, (width, height))
    return image, size

# Document scanner function
def document_scanner(image):
    img_re, size = resizer(image)
    detail = cv2.detailEnhance(img_re, sigma_s=20, sigma_r=0.15)
    gray = cv2.cvtColor(detail, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Edge detection
    edge_image = cv2.Canny(blur, 75, 200)

    # Morphological transformations
    kernel = np.ones((5, 5), np.uint8)
    dilate = cv2.dilate(edge_image, kernel, iterations=1)
    closing = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)

    # Find contours
    contours, hire = cv2.findContours(closing, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    for contour in contours:
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

        if len(approx) == 4:
            four_points = np.squeeze(approx)
            break

    cv2.drawContours(img_re, [four_points], -1, (0, 255, 0), 3)

    # Find four points for the original image
    multiplier = image.shape[1] / size[0]
    four_points_orig = four_points * multiplier
    four_points_orig = four_points_orig.astype(int)

    # Perform perspective transform
    wrap_image = four_point_transform(image, four_points_orig)
    
    return wrap_image, four_points_orig, img_re, closing

# Apply brightness and contrast adjustments
def apply_brightness_contrast(input_img, brightness=0, contrast=0):
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow) / 255
        gamma_b = shadow
        buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
    else:
        buf = input_img.copy()

    if contrast != 0:
        f = 131 * (contrast + 127) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127 * (1 - f)
        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)

    return buf

# Test document scanner function
img = cv2.imread('05.jpg')
wrpimg, points, cnt_img, edgeimg = document_scanner(img)
cv2.imshow('original', img)
cv2.imshow('resize', cnt_img)
cv2.imshow('edge', edgeimg)
cv2.imshow('wrap', wrpimg)
cv2.waitKey()
cv2.destroyAllWindows()

# Adjust brightness and contrast
rgb = cv2.cvtColor(wrpimg, cv2.COLOR_BGR2RGB)
magic_image = apply_brightness_contrast(rgb, 120, 0)
magic_image_c1 = apply_brightness_contrast(rgb, 0, 40)
magic_image_c2 = apply_brightness_contrast(rgb, 50, 40)


# Save the final processed images
cv2.imwrite('scanned_image.jpg', wrpimg)  # Save the scanned (perspective transformed) image
cv2.imwrite('magic_image.jpg', cv2.cvtColor(magic_image, cv2.COLOR_RGB2BGR))  # Save the image with adjusted brightness and contrast
cv2.imwrite('magic_image_c1.jpg', cv2.cvtColor(magic_image_c1, cv2.COLOR_RGB2BGR))  # Save the image with contrast adjustment
cv2.imwrite('magic_image_c2.jpg', cv2.cvtColor(magic_image_c2, cv2.COLOR_RGB2BGR))  # Save the image with both brightness and contrast adjustment
