history = model.fit(
    train_generator,
    epochs=10,
    validation_data=val_generator)

# Save model
model.save('cats_dogs_mobilenet.h5')
