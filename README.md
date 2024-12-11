# doc_scanner
**PROBLEM DESCRIPTION:**
This project simulates document scanning by applying perspective transformations, edge detection, and brightness/contrast adjustments. 
**REQUIREMENTS:**
LIBRARIES:
    	OpenCV (cv2): For image manipulation and computer vision tasks such as resizing, contour detection, edge detection, and applying transformations.
    	NumPy: For numerical operations, particularly working with arrays and matrices.
    	Imutils: A library to simplify common image processing tasks, such as the perspective transformation.
    
**OpenCV**: Provides extensive tools for image processing.
    1.	cv2.imread():  Reads an image from file.
    2.	cv2.imshow():  Displays an image in a window.
    3.	cv2.resize():  Resizes an image to a new size.
    4.	cv2.cvtColor():  Converts an image between different color spaces (e.g., BGR to grayscale).
    5.	cv2.GaussianBlur():  Applies Gaussian blurring to smooth the image.
    6.	cv2.Canny():  Performs edge detection using the Canny edge detection algorithm.
    7.	cv2.findContours():  Finds contours in a binary image.
    8.	cv2.drawContours():  Draws contours on an image.
    9.	cv2.addWeighted(): Adjusts the brightness and contrast of an image.
    10.	cv2.imwrite(): Saves an image to disk.
    11.	cv2.detailEnhance():Enhances the details in an image.
    12.	cv2.dilate() : Performs dilation to thicken edges in the image
    13.	cv2.morphologyEx():Applies morphological transformations (e.g., closing).
    14.	cv2.arcLength(): Calculates the perimeter of a contour.
    15.	cv2.approxPolyDP(): Approximates a contour shape to a polygon

**NumPy**: Used for numerical operations on arrays.
    1.	np.array(): Converts images to arrays.
    2.	np.squeeze(): Removes single-dimensional entries from an array (e.g., used to process contours).
    3.	np.ones(): Creates an array filled with ones, used for morphological transformations (e.g., dilation).
    
**Imutils**: Provides the function four_point_transform() to perform perspective transformation.
    1.	four_point_transform(): This function is used to transform the perspective of the input image based on four points (typically corners of the document or sign).
    
**ALGORITHM**:
    1. Load and Show the Original Image
    2. Resize the Image
    3. Enhance Details: Apply filters to make small details in the image clearer.
    4. Convert to Grayscale: Change the image to black-and-white (grayscale) for easier processing.
    5. Smooth the Image: Blur the image slightly to reduce noise and unnecessary details.
    6. Detect Edges: Use an edge detection tool to find the outline of objects in the image.
    7. Find the Document: Search for shapes in the image (using contours). Identify the biggest 4-sided shape (the document).
    8. Transform the Perspective: Warp the document into a top-down view to make it look straight.
    9. Adjust Brightness and Contrast: Create versions of the image with improved brightness and contrast.
    10. Save the Final Images: The top-down scanned document. Images with adjusted brightness and contrast.
    11. Display Results: Show the resized, edge-detected, and final scanned images.

**INPUT**:

    	Image file: ‘05.jpg’

**OUTPUT**:

    	INTERMEDIATE OUTPUTS:
        1.	Resized image.
        2.	Edge-detected image.
        3.	Contour-drawn image.
    	FINAL OUTPUTS:
        1.	Scanned document image.
        2.	Adjusted images with brightness and contrast variations.
The processed images are saved in the specified output directory with the following files:

**scanned_image.jpg: A scanned, perspective-transformed version of the document.
magic_image.jpg: A brightness-enhanced version.
magic_image_c1.jpg: A contrast-enhanced version.
magic_image_c2.jpg: A version enhanced with both brightness and contrast.**
