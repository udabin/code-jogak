import torch

def kl_divergence(P, Q):

    # P와 Q가 0인 경우 로그 연산 시 문제가 발생하므로, 작은 값을 추가 (수치적 안정성을 위해 필요)
    epsilon = 1e-10
    P = P + epsilon
    Q = Q + epsilon
    
    # KL Divergence 수식을 적용
    kl_div = P * torch.log(P / Q)
    
    # 모든 요소에 대해 합산하여 최종 KL Divergence 계산
    return torch.sum(kl_div)

# 예제
P = torch.tensor([0.4, 0.4, 0.2])  # 실제 분포
Q = torch.tensor([0.5, 0.3, 0.2])  # 모델의 예측 분포

# KL Divergence 계산
kl_div = kl_divergence(P, Q)
print("KL Divergence:", kl_div.item())