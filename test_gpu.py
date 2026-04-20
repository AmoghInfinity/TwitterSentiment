import torch

print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))

x = torch.rand(3, 3).to("cuda")
print(x)