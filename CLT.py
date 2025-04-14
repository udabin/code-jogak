import torch
import torch.nn as nn
import torch.nn.functional as F

class CLT(nn.Module):
    """
    Cross-Layer Transcoder: transforms hidden state from layer l to layer k
    """
    def __init__(self, hidden_size):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(hidden_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, hidden_size)
        )

    def forward(self, h_l):
        return self.net(h_l)