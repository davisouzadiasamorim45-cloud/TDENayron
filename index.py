import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.utils import to_categorical

def gerar_tres_espirais(n_pontos, ruido=0.5):
    n = np.sqrt(np.random.rand(n_pontos, 1)) * 780 * (2 * np.pi) / 360
    d1x = -np.cos(n) * n + np.random.rand(n_pontos, 1) * ruido
    d1y = np.sin(n) * n + np.random.rand(n_pontos, 1) * ruido

    dados = np.vstack((
        np.hstack((d1x, d1y)),
        np.hstack((d1x * np.cos(2 * np.pi / 3) - d1y * np.sin(2 * np.pi / 3),
                   d1x * np.sin(2 * np.pi / 3) + d1y * np.cos(2 * np.pi / 3))),
        np.hstack((d1x * np.cos(4 * np.pi / 3) - d1y * np.sin(4 * np.pi / 3),
                   d1x * np.sin(4 * np.pi / 3) + d1y * np.cos(4 * np.pi / 3)))
    ))

    rotulos = np.hstack((
        np.zeros(n_pontos),
        np.ones(n_pontos),
        np.full(n_pontos, 2)
    ))

    return dados, rotulos

# Gerar dados
X, y = gerar_tres_espirais(1000, ruido=0.2)


def plotar_dados(X, y):
    plt.figure(figsize=(6, 6))
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', s=5)
    plt.title('Distribuição das Três Espirais')
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.axis('equal')
    plt.savefig('espirais.png', dpi=300)
    plt.show()

plotar_dados(X, y)


# Normalização
scaler = StandardScaler()
X_norm = scaler.fit_transform(X)

# One-hot encoding dos rótulos
y_cat = to_categorical(y, num_classes=3)

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_norm, y_cat, test_size=0.2, random_state=42)


model = Sequential([
    Input(shape=(2,)),
    Dense(128, activation='tanh'),
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(3, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


history = model.fit(
    X_train, y_train,
    epochs=100,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)


# Plotar histórico de acurácia
plt.plot(history.history['accuracy'], label='Treino')
plt.plot(history.history['val_accuracy'], label='Validação')
plt.title('Acurácia durante o treinamento')
plt.xlabel('Épocas')
plt.ylabel('Acurácia')
plt.legend()
plt.show()
 