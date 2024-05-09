# Prepare_PCCP

## Part 2. 문자열 (String)
- .islower() & .isupper(): 대문자인지 모두 소문자인지 확인하여 boolean type으로 return
- ord(): string to ascii
- chr(): ascii to string

## Part 3. 선형 배열 (Linear Arrays)
- 선형 배열: 데이터들이 선 (line) 처럼 일렬로 늘어선 형태 ~ Python에서는 List(주의, Linked List와는 구별해야 함)
- Python 리스트에 활용할 수 있는 연산들
  - 원소 덧붙이기: .append()
  - 원소 하나를 꺼내기: .pop()
- 리스트의 길이에 비례해서 실행 시간이 걸리는 연산들 ~ 원소를 삽입하거나 삭제하면 나머지 원소들을 전부 이동시켜야 하기 때문
  - 원소 삽입하기: .insert()
  - 원소 삭제하기: .remove()
  - 원소 삭제하기: del ListName[index]
- 추가 다른 연산
  - 원소 탐색하기: .index()

## Part 6. 알고리즘의 복잡도 (Comlexity of Algorithms)
- 복잡도(Complexity)
  - 시간 복잡도(Time Complexity): 문제의 크기와 이를 해결하는 데 걸리는 시간 사이의 관계
    - 평균 시간 복잡도(Average Time Complexity): 임의의 입력 패턴을 가정했을 때 소요되는 시간의 평균
    - 최악 시간 복잡도(Worst-case Time Complexity): 가장 긴 시간을 소요하게 만드는 입력에 따라 소요되는 시간
  - 공간 복잡도(Space Complexity): 문제의 크기와 이를 해결하는 데 필요한 메모리 공간 사이의 관계
- big-O notation: O(1) → O(logn) → O(N) → O(nlogn) → O(n^2) → O(n^3) → O(2^x) → O(n!)
  - e.g., O(n): n개의 무작위로 나열된 수에서 최댓값을 찾기 위해 선형 탐색 알고리즘을 적용
  - e.g., O(logn): n개의 크기 순으로 정렬된 수에서 특정 값을 찾기 위해 이진 탐색 알고리즘을 적용
  - e.g., O(nlogn): 병합 정렬(merge sort)
    - 정렬 문제에 대해 O(nlogn)보다 낮은 복잡도를 갖는 알고리즘은 존재할 수 없음이 증명되어 있음
  - e.g., O(n^2): 삽입 정렬(insertion sort)

---
## private code
- answer = my_string[:s] + overwrite_string + my_string[s + len(overwrite_string) :] # 슬라이싱 연산의 합
- answer = list(map(int, str(n)[::-1])) # str형 뒤집어서 한번에 int형으로 변환
