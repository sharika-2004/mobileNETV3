from google.colab import files
import cv2

def upload_and_predict():
    uploaded = files.upload()
    for filename in uploaded.keys():
        
        img = cv2.imdecode(np.fromstring(uploaded[filename], np.uint8), cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (224, 224)) / 255.0

        
        pred = model.predict(np.expand_dims(img, axis=0))[0][0]
        label = "Dog" if pred > 0.5 else "Cat"

        
        plt.figure(figsize=(6, 6))
        plt.imshow(img)
        plt.title(f"Prediction: {label}\nConfidence: {max(pred, 1-pred):.2%}")
        plt.axis('off')
        plt.show()

        return label, float(pred)
print("Upload a cat or dog image:")
pred_class, confidence = upload_and_predict()
print(f"\nFinal Prediction: {pred_class} ({confidence:.2%} confidence)")
