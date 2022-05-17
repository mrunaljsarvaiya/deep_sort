# https://jimmy-shen.medium.com/pytorch-freeze-part-of-the-layers-4554105e03a6
# https://pythonguides.com/pytorch-pretrained-model/

import torch.nn as nn

import torchvision.models as models
resnet18 = models.resnet18(pretrained=True)
import pdb; pdb.set_trace()

# Remove last layer
model = nn.Sequential(*list(resnet18.modules())[:-1])

# Freeze layers
# we want to freeze the fc2 layer this time: only train fc1 and fc3
model.fc2.weight.requires_grad = False
model.fc2.bias.requires_grad = False

# passing only those parameters that explicitly requires grad
optimizer = optim.Adam(filter(lambda p: p.requires_grad, model.parameters()))