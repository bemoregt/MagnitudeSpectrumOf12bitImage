import numpy as np
import cv2
from matplotlib import pyplot as plt

def display_and_save_fourier_spectrum_of_png_region(img_path, output_path):
    # PNG 이미지를 그레이스케일로 읽어옵니다. 이미지가 12비트라고 가정합니다.
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    
    # 이미지를 float32 타입으로 변환합니다.
    img_float = np.float32(img)
    
    # 2D 푸리에 변환을 수행합니다.
    dft = cv2.dft(img_float, flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    
    # 스펙트럼의 크기를 계산하고 로그 스케일로 변환합니다.
    magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
    
    # 스펙트럼의 값이 12비트 범위에 맞도록 스케일링합니다.
    # 스펙트럼의 최소값과 최대값을 구합니다.
    min_val, max_val = np.min(magnitude_spectrum), np.max(magnitude_spectrum)
    
    # 스펙트럼 값을 0에서 4095 (12비트) 범위로 정규화합니다.
    spectrum_scaled = np.clip((magnitude_spectrum - min_val) / (max_val - min_val) * 4095, 0, 4095).astype(np.uint16)
    
    # 스펙트럼을 디스플레이합니다.
    plt.figure(figsize=(9, 5))
    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(spectrum_scaled, cmap='gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()
    
    # 스펙트럼 결과를 12비트 PNG 파일로 저장합니다.
    cv2.imwrite(output_path, spectrum_scaled)

# 이 함수를 호출할 때는 12비트 이미지를 담은 PNG 파일의 경로와 출력 파일 경로를 'img_path', 'output_path'에 전달합니다.
# 예: display_and_save_fourier_spectrum_of_png_region('path_to_your_12bit_image.png', 'output_spectrum.png')
