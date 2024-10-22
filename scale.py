import cv2
import numpy as np

# pemanggilan  gambar 
img = cv2.imread(r"C:\Users\USER\Downloads\WhatsApp Image 2024-09-24 at 20.18.34.jpeg")

# Mengubah ukuran gambar menjadi 500 x 500 piksel
resized_img = cv2.resize(img, (500, 500))

# Mendapatkan dimensi gambar yang sudah diubah ukurannya
height, width, channels = resized_img.shape

# Membuat matriks kosong untuk menyimpan nilai RGB
rgb_matrix = np.zeros((height, width, channels), dtype=np.uint8)

# Mengisi matriks RGB dengan nilai dari gambar yang sudah diubah ukurannya
for y in range(height):
    for x in range(width):
        rgb_matrix[y, x] = resized_img[y, x]

# Menampilkan matriks RGB
print("Matriks RGB:")
print(rgb_matrix)

# Mengubah gambar menjadi grayscale
gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

# Menampilkan matriks grayscale
print("\nMatriks Grayscale:")
print(gray_img)

# Menampilkan gambar grayscale
cv2.imshow('Grayscale Image', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()