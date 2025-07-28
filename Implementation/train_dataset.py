train_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    rotation_range=20,
    width_shift_range=0.2,
    horizontal_flip=True)

train_generator = train_datagen.flow_from_directory(
    'cats_dogs/PetImages',
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',
    subset='training')

val_generator = train_datagen.flow_from_directory(
    'cats_dogs/PetImages',
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',
    subset='validation')

print(f"Classes: {train_generator.class_indices}")
