def predict_pet(img_path):
    img = tf.keras.utils.load_img(img_path, target_size=(224, 224))
    x = tf.keras.utils.img_to_array(img)/255.
    x = np.expand_dims(x, axis=0)
    pred = model.predict(x)[0][0]
    return "Dog" if pred > 0.5 else "Cat", pred
  test_images = [
    'cats_dogs/PetImages/Cat/6779.jpg',
    'cats_dogs/PetImages/Dog/10292.jpg'
]

plt.figure(figsize=(10, 4))
for i, img_path in enumerate(test_images):
    pred, conf = predict_pet(img_path)
    plt.subplot(1, 2, i+1)
    plt.imshow(plt.imread(img_path))
    plt.title(f"Pred: {pred}\nConf: {conf:.2%}")
    plt.axis('off')
plt.tight_layout()
plt.show()
