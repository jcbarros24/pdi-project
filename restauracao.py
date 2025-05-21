import cv2
import matplotlib.pyplot as plt

img_ruido = cv2.imread('imagens/ruido3.jpeg', cv2.IMREAD_GRAYSCALE)

if img_ruido is None:
    print("Erro ao carregar a imagem.")
    exit()

img_mediana = cv2.medianBlur(img_ruido, 5)

img_gaussiano = cv2.GaussianBlur(img_ruido, (5, 5), sigmaX=1)

img_bilateral = cv2.bilateralFilter(img_ruido, d=9, sigmaColor=75, sigmaSpace=75)

img_iterativa = cv2.medianBlur(img_ruido, 3)
img_iterativa = cv2.medianBlur(img_iterativa, 3)
img_iterativa = cv2.medianBlur(img_iterativa, 3)

plt.figure(figsize=(16, 8))

plt.subplot(2, 3, 1)
plt.title("Imagem com Ruído")
plt.imshow(img_ruido, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.title("Mediana (5x5)")
plt.imshow(img_mediana, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.title("Gaussiano (5x5)")
plt.imshow(img_gaussiano, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.title("Bilateral")
plt.imshow(img_bilateral, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.title("Iterativo Mediana")
plt.imshow(img_iterativa, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()