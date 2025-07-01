import cv2

def preprocess_image(input_path: str, output_path: str):
    # Read image
    image = cv2.imread(input_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Resize to fixed size (e.g., 300x300)
    resized = cv2.resize(gray, (300, 300))

    # Save processed image
    cv2.imwrite(output_path, resized)

    return output_path
