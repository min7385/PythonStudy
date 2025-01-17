import joblib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

# 데이터 로드 및 스케일링
df = pd.read_excel("./AAPL_20100101_20241010.xlsx", engine="openpyxl")
print(df.describe())
scaler = MinMaxScaler(feature_range=(0, 1))
df['Close'] = scaler.fit_transform(df['Close'].values.reshape(-1, 1))
joblib.dump(scaler, 'scaler.save')  # 나중에 사용하기 위해 저장

# 시퀀스 데이터 생성 x: 1~50일, y: 51일
seq_len = 50
data_len = len(df['Close'].values)
all_len = seq_len + 1
sequence = []
for i in range(data_len - all_len):
    sequence.append(df['Close'][i:i + all_len])
ndarry_seq = np.array(sequence)

# 학습 및 테스트 데이터 분리
train_size = int(round(ndarry_seq.shape[0] * 0.9))
train_data = ndarry_seq[:train_size, :]
test_data = ndarry_seq[train_size:, :]  # 수정된 부분

x_train = train_data[:, :-1]
y_train = train_data[:, -1]
x_test = test_data[:, :-1]
y_test = test_data[:, -1]  # 올바르게 설정됨

# 데이터 차원 재조정
x_train_reshape = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
x_test_reshape = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

# RNN 모델 생성
model = Sequential()
model.add(LSTM(128, return_sequences=True, input_shape=(seq_len, 1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(1, activation='linear'))
model.compile(loss='mse', optimizer='adam')

# 모델 학습
model.fit(x_train_reshape, y_train, validation_data=(x_test_reshape, y_test), batch_size=50, epochs=50)
model.save("AAPL.h5")

# 시각화
pred = model.predict(x_test_reshape)
plt.plot(y_test, label='True')
plt.plot(pred, label='Predicted')
plt.legend()
plt.show()
