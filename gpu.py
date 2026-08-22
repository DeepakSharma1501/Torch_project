import torch

if torch.cuda.is_available():
    device = torch.cuda.current_device()
    gpu_name = torch.cuda.get_device_name(device)
    total_memory_bytes = torch.cuda.get_device_properties(device).total_memory
    total_memory_gb = total_memory_bytes / (1024 ** 3)
    
    print(f"GPU: {gpu_name}")
    print(f"Total VRAM: {total_memory_gb:.2f} GB")
else:
    print("No CUDA GPU detected.")
