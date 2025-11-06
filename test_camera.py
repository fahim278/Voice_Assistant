import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load model but be very cautious
model = load_model("face_mask_detector.keras")
print("⚠️ AI Model loaded but may be unreliable")

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

def conservative_ai_prediction(face_roi, model):
    """Only trust AI under very specific conditions"""
    img = cv2.resize(face_roi, (224, 224))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) / 255.0
    img = np.expand_dims(img, axis=0)
    
    prediction = model.predict(img, verbose=0)
    ai_confidence = np.max(prediction) * 100
    ai_label = "Mask" if np.argmax(prediction) == 0 else "No Mask"
    
    # Only trust AI if:
    # - It says "No Mask" with >70% confidence, OR
    # - It says "Mask" with >95% confidence (very sure)
    if (ai_label == "No Mask" and ai_confidence > 70) or (ai_label == "Mask" and ai_confidence > 95):
        return ai_label, ai_confidence, "AI"
    else:
        return None, 0, "AI-Unreliable"

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    
    for (x, y, w, h) in faces:
        face_roi = frame[y:y+h, x:x+w]
        
        # Default to rule-based
        label = "No Mask"  # Conservative default
        confidence = 60.0
        method = "Rule-Based"
        color = (0, 0, 255)  # Red for no mask
        
        # Try AI with extreme caution
        ai_label, ai_confidence, ai_method = conservative_ai_prediction(face_roi, model)
        
        if ai_label is not None:
            label = ai_label
            confidence = ai_confidence
            method = ai_method
            color = (0, 255, 0) if label == "Mask" else (0, 0, 255)
        
        # Draw results
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        text = f"{label} ({confidence:.1f}%) [{method}]"
        cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
    
    cv2.imshow("Ultra-Conservative Mask Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()