# code-jogak

이 레포지토리는 딥러닝 및 머신러닝에서 자주 사용되는 핵심 수학적 계산 또는 논문 내 수식 구현 코드를 정리해두는 개인 프로젝트 공간입니다.  
실험적 검증보다는 수식의 구조와 동작을 빠르게 이해하고 확인할 수 있도록 간단한 예제와 함께 작성되었습니다.


## 현재 포함된 코드

### 1. `dpo-loss.py`
- DPO 손실 함수를 PyTorch로 구현
- 선호 응답과 비선호 응답 간의 로그 확률 차이를 시그모이드와 음의 로그로 변환하여 손실로 계산
- 역전파(gradient backpropagation)를 포함해 학습 실험에 바로 사용 가능  

```
DPO Loss: 0.6931
```

### 2. `kl-divergence.py`
- KL Divergence 계산 함수 구현
- 두 확률 분포 간의 거리 측정을 위한 기본 수식 구현
- 수치 안정성을 위해 epsilon 사용  

```
KL Divergence: 0.0853
```

### 3. `timing_decorator.py`
- 함수 실행 시간을 측정하는 데코레이터 유틸리티
- 디버깅이나 성능 확인 시 함수 단위의 실행 시간을 로깅할 수 있음
- `logging` 모듈과 사용자 정의 로거를 함께 사용해 유연한 출력 지원  

```
@timefn: some_function took 0.0142 seconds
```


## 사용 목적
- 논문 수식 구현 연습
- 모델 평가 메트릭 계산 이해
- 코드 스니펫 활용을 위한 수학 함수/유틸리티 라이브러리 구축
- 디버깅 또는 성능 측정을 위한 보조 기능 제공


## 향후 추가 예정
- Cross-Entropy, Entropy, JS Divergence 등 정보이론 기반 지표
- PPO, REINFORCE 등 강화학습 손실 함수
- Attention score, Cosine similarity 등 논문 내 계산 수식
- 유용한 디버깅/개발 유틸리티 (예: 파라미터 개수 계산기 등)


## 프로젝트 구조
```
code-jogak/
├── dpo-loss.py            # DPO Loss 계산
├── kl-divergence.py       # KL Divergence 계산
├── timing_decorator.py    # 함수 실행 시간 측정 데코레이터
└── README.md              # 설명 문서
```


## 작성 목적
본 저장소는 개인적으로 논문을 구현하거나 수식 기반 계산을 실험할 때 자주 참조하기 위해 구성되었습니다.  
학습용으로 활용할 수 있도록 최소한의 의존성과 간단한 구조를 지향합니다.
