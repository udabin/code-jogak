import torch
import torch.nn.functional as f

# preferred와 non-preferred 응답의 로그 확률
# -1.5와 -1.5은 예시로 임의로 설정된 로그 확률 값
# 학습 과정에서 모델은 각 응답에 대해 로그 확률(log probability) 값을 출력
# 이 값들은 모델의 예측 결과에 의해 실제 학습 시에는 동적으로 변경됨
log_probs_preferred = torch.tensor([-1.5], requires_grad=True)    # 선호되는 응답의 로그 확률
log_probs_non_preferred = torch.tensor([-1.5], requires_grad=True) # 비선호되는 응답의 로그 확률

def dpo_loss(log_probs_preferred, log_probs_non_preferred):

    # 선호도 차이를 계산하고 시그모이드 적용 후 음의 로그를 취함
    diff = log_probs_preferred - log_probs_non_preferred
    loss = -torch.log(torch.sigmoid(diff))
    return loss

# DPO 손실 계산
loss = dpo_loss(log_probs_preferred, log_probs_non_preferred)
print("DPO Loss:", loss.item())

# 역전파 수행 (학습 시 사용)
loss.backward()