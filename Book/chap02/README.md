## Chap02 : 판다스 패키지

---

**Install Pandas**
> `pip install pandas`

**Editor**
<pre>
Jupyter notebook : pandas 내장되어 있음
Visual Studio Code, pycharm : pandas 내장되어 있지 않음(pip 명령어로 설치)
</pre>

**Series**
<pre>
동일한 데이터 타입을 저장하는 1차원 배열
</pre>

**DataFrame**
<pre>
일반적으로 레이블화 되어있는 2차원 자료 구조, 서로 다른 타입의 여러 컬럼으로 구성되어 있음
</pre>

##### DataFrame 생성
| 인수      | 포맷                         | 설명                                              |
|---------|----------------------------|-------------------------------------------------|
| data    | ndarray / dict / DataFrame | DataFrame 자료, dict은 Series, ndarray, list 포함 가능 |
| index   | index / array-like         | 인덱스(기본 값 : range(n))                            |
| columns | index / array-like         | 열의 제목(기본 값 : range(n))                          |
| dtype   | dtype(기본 값 : None)         | 자료형을 특정하는 경우에 사용, 없으면 자료에서 추정                   |
| copy    | bool(기본 값 : None)          | 자료를 copy 하는지의 여부 지정                             |


**표 출력을 위한 라이브러리 `Tabulate`** 
> `npm install tabulate`

---

**함수 적용과 매핑(apply 함수)**

| 항목               | 설명                                                                                                                                  |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `apply()`        | `사용 예시) f = lambda x : x.max() -x.min()` `print(frame.apply(f))` 각 컬럼마다 (최대 - 최소) 의 결과를 구함, `axis = 1` 옵션이 있으면, 각 행(row) 마다의 연산을 수행 |
| `applymap(func)` | DataFrame의 요소 하나 하나에 각각 동일한 함수를 적용시킴, `사용 예시) format = lambda x : '%.2f 퍼센트' % x` `print(frame.applymap(format))` 모든 요소에 적용         |

---

**데이터 병합(merge 함수)**

| 항목            | 설명                                                                             |
|---------------|--------------------------------------------------------------------------------|
| `left`        | merge 하려는 DataFrame 중 왼쪽에 위치한 DataFrame                                        |
| `right`       | merge 하려는 DataFrame 중 오른쪽에 위치한 DataFrame                                       |
| `how`         | Join의 방법, '`inner` \| `left` \| `left` \| `right` (기본값 : `inner`)              |
| `on`          | 양쪽 DataFrame 에 모두 공존하는 조인하려는 컬럼 이름을 의미                                         |
| `left_on`     | Join 키로 사용할 left DataFrame의 컬럼 이름을 의미                                          |
| `right_on`    | Join 키로 사용할 right DataFrame의 컬럼 이름을 의미                                         |
| `left_index`  | left DataFrame의 색인 로우(다중 색인일 경우의 키)를 조인 키로 사용하고자 하는 경우에 명시                     |
| `right_index` | right DataFrame의 색인 로우(다중 색인일 경우의 키)를 조인 키로 사용하고자 하는 경우에 명시                    |
| `sort`        | 조인 키에 따라 병합된 데이터를 사전 순으로 정렬, 기본 값 : `True`, 대용량 데이ㅓㅌ인 경우 `False`로 설정하면 성능상의 이득 |
| `suffixes`    | 컬럼의 이름이 겹칠 경우 각 컬럼 뒤에 붙일 문자열의 접미사 설정, 기본 값 : `('_x', '_y')`                    |

---

**그룹핑(groupby 함수)**

| 속성/함수                 | 설명                                                                                                                                                 |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| `agg`                 | `groupby` 객체에 직접 사용 가능한 항목들, `min`, `max`, `median`, `mean`, `sum`, `count`, `std`, `var`, `size`, `describe`, `nuique`, `idxmax`, `idxmin` ...etc |
| `get_group(data)`     | 그루핑된 데이터 중에서 값이 `data`인 항목만 추출                                                                                                                     |
| `count()`             | 누락 값은 제외하고, 그룹 내에 `NaN` 값이 아닌 값의 숫자를 반환                                                                                                            |
| `describe()`          | 기초 통계량 정보를 한꺼번에 보여줌, 데이터 수, 평균, 표준 편차, 최소값, 백분위수, 최대 값                                                                                             |
| `first(), last()`     | `NaN` 값이 아닌 값들 중에서 첫 번째 값과 마지막 값을 반환                                                                                                               |
| `mean()`              | `NaN` 값이 아닌 값의 평균 값을 반환                                                                                                                            |
| `median()`            | `NaN` 값이 아닌 값의 산술 중간 값을 반환                                                                                                                         |
| `min(), max`          | `NaN` 값이 아닌 값 중에서 최고 값과 최대 값을 반환                                                                                                                   |
| `ngroups()`           | 그룹의 개수를 반환                                                                                                                                         |
| `quantile(q == 0.25)` | 백분위수 25%                                                                                                                                           |
| `quantile(q == 0.50)` | 백분위수 50%                                                                                                                                           |
| `quantile(q == 0.75)` | 백분위수 75%                                                                                                                                           |
| `prod()`              | `NaN` 값들의 곱을 반환                                                                                                                                    |
| `size()`              | 각 그룹에 대한 자료의 개수(누락 값 포함)                                                                                                                           |
| 'sum()'               | NaN 값이 아닌 값의 합을 반환                                                                                                                                 |
| `std(), var()`        | 편향되지 않은(n - 1을 분모로 하는) 표준 편차와 분산을 구함                                                                                                               |

---

**Pandas로 DataFrame 이용하기**

1. 어떤 형태의 파일인지 확인
   > * `Json` 파일 : `Dictionary`, `List` <br>
   > * `CSV` 파일 : `DataFrame`

2. 데이터 수집(`.json` or `.csv`)
    > * 공공데이터포털(json, csv) <br>
    > * IoT <br>
    > * Database Table Inesrt
 
3. 데이터 가공
    > * 1번에서 수집한 데이터 -> `DataFrame`
    > * 결측값(`null`) -> 다른 값 대체

4. 시각화
    > * `matplotlib` - 차트 만들때 필요한 라이브러리(디자인 X)
    > * `seaborn`