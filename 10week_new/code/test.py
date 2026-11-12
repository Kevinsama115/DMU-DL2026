import sys
import torch

print("Python:", sys.executable)
print("PyTorch:", torch.__version__)
print("MPS available:", torch.backends.mps.is_available())
