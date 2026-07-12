# Convolutional Neural Networks (CNN)

**Status:** Not started  
**Milestone:** Deep learning  
**Related exercise:** [cnn_conv2d](../../exercises/pytorch/cnn_conv2d/)

## Intuition

A **convolution** slides a small learnable filter over spatial input (image,
sequence) to detect local patterns (edges, textures). **Pooling** downsamples.
CNNs exploit locality and translation structure before global pooling / FC layers.

## Formal definition

2D convolution (single channel, schematic):

\[
(Y * K)_{i,j} = \sum_{m}\sum_{n} Y_{i+m,j+n} \cdot K_{m,n}
\]

PyTorch: `nn.Conv2d(in_channels, out_channels, kernel_size, stride, padding)`.

## Why it matters in machine learning

- Foundation for vision models (ResNet, etc.)
- 1D convolutions used in audio and sometimes text
- Conceptual contrast with full attention (local vs global)

## Minimal implementation

```python
conv = torch.nn.Conv2d(1, 8, kernel_size=3, padding=1)
out = conv(image_tensor)  # (N, 8, H, W)
```

## Experiment

Apply Sobel edge filters vs learned conv1 on MNIST digit.

## What I still do not understand

- Receptive field growth with depth
- When CNNs are still preferred over ViT for small data
