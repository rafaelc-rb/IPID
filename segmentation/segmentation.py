import cv2
import numpy as np

# Carregue a imagem
imagem = cv2.imread('miranha.jpeg')

# Converta a imagem para o espaço de cores HSV
hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# Defina o intervalo de cores do Homem-Aranha
vermelho_baixo = np.array([0, 100, 100])
vermelho_alto = np.array([10, 255, 255])

# Crie uma máscara para a cor vermelha
mascara = cv2.inRange(hsv, vermelho_baixo, vermelho_alto)

# Aplique a máscara à imagem
resultado = cv2.bitwise_and(imagem, imagem, mask=mascara)

# Mostre a imagem original e a imagem segmentada
cv2.imshow('Imagem Original', imagem)
cv2.imshow('Imagem Segmentada', resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()
