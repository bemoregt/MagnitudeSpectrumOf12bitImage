# Magnitude Spectrum of 12-bit Images

이 저장소는 12비트 이미지의 푸리에 변환 및 진폭 스펙트럼(Magnitude Spectrum)을 계산하고 시각화하는 도구를 제공합니다.

## 기능

- 12비트 PNG 이미지 파일 읽기
- 2D 푸리에 변환(FFT) 수행
- 진폭 스펙트럼 계산 및 로그 스케일로 변환
- 12비트(0-4095) 범위로 스케일링된 스펙트럼 시각화
- 입력 이미지와 스펙트럼 결과를 병렬로 표시
- 결과 스펙트럼을 12비트 PNG 파일로 저장

## 코드 설명

`magnitude_spectrum.py` 파일은 다음과 같은 과정으로 이미지의 진폭 스펙트럼을 계산합니다:

1. 12비트 PNG 이미지를 그레이스케일로 읽어옵니다.
2. 이미지를 float32 타입으로 변환합니다.
3. OpenCV의 `cv2.dft` 함수를 사용하여 2D 푸리에 변환을 수행합니다.
4. 저주파 성분을 이미지 중앙으로 이동시키기 위해 `np.fft.fftshift`를 적용합니다.
5. 복소수 결과에서 진폭 스펙트럼을 계산하고 로그 스케일로 변환합니다.
6. 스펙트럼 값을 12비트 범위(0-4095)로 정규화합니다.
7. 입력 이미지와 진폭 스펙트럼을 시각화합니다.
8. 결과 스펙트럼을 12비트 PNG 파일로 저장합니다.

## 사용 방법

```python
from magnitude_spectrum import display_and_save_fourier_spectrum_of_png_region

# 함수 호출 예시
display_and_save_fourier_spectrum_of_png_region('input_12bit_image.png', 'output_spectrum.png')
```

## 필요 라이브러리

- NumPy
- OpenCV (cv2)
- Matplotlib

## 설치 방법

```bash
pip install numpy opencv-python matplotlib
```

## 활용 사례

- 이미지 주파수 특성 분석
- 이미지 필터링 및 처리를 위한 주파수 영역 특성 파악
- 이미지의 노이즈 패턴 식별
- 이미지 품질 평가

## 라이센스

MIT

## 기여

이슈 및 풀 리퀘스트를 통한 기여를 환영합니다.
