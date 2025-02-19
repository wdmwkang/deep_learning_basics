from dataset.mnist import load_mnist
import sys
import os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정

# 처음 한 번은 몇 분 정도 걸립니다.
(x_train, t_train), (x_test, t_test) = \
    load_mnist(flatten=True, normalize=False)

# 각 데이터의 형상 출력
print(x_train.shape)    # (60000, 784)
print(t_train.shape)    # (60000,)
print(x_test.shape)     # (10000, 784)
print(t_test.shape)     # (10000,)
