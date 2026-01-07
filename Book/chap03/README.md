## Chap03 : 데이터 시각화

---

**사전 준비**

| 항목     | 설명                                                                                                         |
|--------|------------------------------------------------------------------------------------------------------------|
| 설치할 목록 | `pip install matplotlib`, `pip install PyQt5`                                                              |
| 참조 사이트 | [matplotlib](https://matplotlib.org/), [파이썬 시각화 예제](https://partrita.github.io/posts/matplotlib-examples/) |

---

**matplotlib API**
> * `import matplotlib`
> * `import matplotlib.pyplot as plt`

**plt 연관 함수**

| 함수                                             | 설명                                                                                               |
|------------------------------------------------|--------------------------------------------------------------------------------------------------| 
| `axhline(y = 0, xmin = 0, xmax = 1, **kwargs)` | y는 수평선이 그려지는 y축의 좌표 `예시) plt.axhline(y = idx, color = 'c', linewidth = 1, linestyle = 'dashed')` |
| `axvline(x = 0, ymin = 0, ymax = 1, **kwargs)` | `예시) plt.axvline(x = 1, color = 'blue', linewidth = 2, linestyle = 'dotted')`                    |
| `grid(boolean)`                                | 그리드를 표시할 것인지 Boolean 값 지정                                                                        |
| `rcdefaults()`                                 | Matplotlib 스타일에 대한 파라미터를 초기 값으로 돌림                                                               |
| `show()`                                       | 그래프 객체를 보여줌                                                                                      |
| `title(sometitle)`                             | `sometitle` 이라는 문장을 그래프의 제목으로 설정                                                                 |
| `xlabel(str)`                                  | x 축에 `str` 이라는 라벨(문구)를 설정                                                                        |
| `xlim([하한값, 상한값])`                             | x 축의 상한 / 하한 값을 설정                                                                               |
| `xticks()`                                     | x 축의 눈금 라벨에 대한 개수 설정, `예시) plt.xticks(np.arange(1, 11))`                                         |
| `ylabel(str)`                                  | y 축에 `str` 이라는 라벨 설정                                                                             |
| `ylim([하한값, 상한값])`                             | y 축의 상한 / 하한 값을 설정                                                                               |
| `yticks()`                                     | y 축의 눈금 라벨에 대한 개수 설정, `예시) plt.yticks(np.arange(ymin, ymax + 1, 1))`                             |


**이미지로 저장**

| 매개 변수                   | 설명                                                        |
|-------------------------|-----------------------------------------------------------|
| 사용 형식                   | `plt.savefig(filename, dpi = 400, bbox_inches = 'tight')` |
| `fname`                 | 파일 경로나 파이썬의 파일과 유사한 객체를 나타내는 문자열                          |
| `dpi`                   | Figure의 해상도 dpi`(기본 값 : 100)`을 지정                         |
| `facecolor, edge color` | 서브 플룻 바깥 배경 색상, `기본 값 w(흰색)`                              |
| `format`                | 명시적인 파일 포맷`('png', 'pdf', 'svg', ...etc)` 을 지정            |
| `bbox_inches`           | Figure 에서 저장할 부분, 'tight' 는 Figure 의 둘레의 비어 있는 공간 모두 제거   |

---

**그래프 종류**

- 일변량(1개)
  - 연속형
    - 히스토그램(histogram)
    - 상자 수염 그래프(boxplot)
    - 바이올린 그래프(violin)
    - 커널 밀도 그래프(kernel density curve)
  - 범주형
    - 막대 그래프(bar chart)
    - 파이 그래프(pie chart)
- 다변량(>=2)
  - 연속형
    - 산점도(scatter plot)
    - 선 그래프(line)
    - 시계열 그래프
  - 범주형
    - 모자이크 그래프(mosaic graph)
    - Tree Map 그래프