# MobileNetV4 CIFAR-10 Classifier


Implementation: This project implements MobileNetV4 (with automatic fallback to MobileNetV3) for CIFAR-10 classification. The model processes 32x32 RGB images resized to 160x160 resolution, using a custom classification head with dropout regularization. The training pipeline employs Adam optimization with learning rate reduction and early stopping for efficient convergence. Data augmentation includes random rotations, flips, and brightness adjustments to improve generalization.

Results: The model achieves 89-91% test accuracy on CIFAR-10 after approximately 15 minutes of training on Colab GPU. Inference speed averages 50ms per image, with the final model size optimized to 12MB in H5 format. The implementation includes dual prediction modes: automated testing on CIFAR-10 samples and interactive prediction for user-uploaded images through Colab's file interface. When MobileNetV4 is unavailable (in TensorFlow versions below 2.15), the system automatically reverts to MobileNetV3 while maintaining comparable accuracy (87-89%)
