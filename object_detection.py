import cv2
from ultralytics import YOLO

font = cv2.FONT_HERSHEY_COMPLEX

img_path = "inference/113.jpg"
model_path = "runs/detect/yolov8_brain_tumor_detection/weights/best.pt"

model = YOLO(model_path)

img = cv2.imread(img_path)

results = model(img)[0]

threshold = 0.5
for result in results.boxes.data.tolist():
    x1, y1, x2, y2, score, class_id = result
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    class_id = int(class_id)
    
    if score > threshold:
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        class_name = results.names[class_id]
        score = score * 100
        text = f"{class_name}: %{score:.2f}"
        cv2.putText(img, text, (x1, y1 - 10), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA)

cv2.imshow('Detected Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()