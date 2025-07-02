# Dental Diseases Classification
<p align="justify">The task involves classifying dental and oral cavity images into seven disease categories using a deep learning model (CNN Architecture). These diseases often present visually distinguishable symptoms but can be misidentified without expert knowledge. Automation via image classification enhances diagnostic speed and accessibility.</p>

## Preprocessing
Image normalization and augmentation was implemented.
### Augmentation Results
![image](https://github.com/user-attachments/assets/ec1e5766-3aab-42f6-9570-ed62bedd19ed)

## Model Architecture
- Input Layer: (256, 256, 3) RGB dental images
- Conv Layers: Three convolutional blocks with increasing filter depth (32 → 64 → 128), each followed by max pooling for spatial reduction.
- Flatten → Dense: Transforms feature maps to a 1D vector then processes with a hidden layer.
- Dropout (0.3): Regularization to reduce overfitting.
- Output Layer: Softmax for multi-class classification (7 classes).

## Results
Accuracy is 90%

