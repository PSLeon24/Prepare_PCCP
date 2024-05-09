# Prepare_PCCP

## Part 2. 문자열 (String)

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


---
## private code
- answer = my_string[:s] + overwrite_string + my_string[s + len(overwrite_string) :] # 슬라이싱 연산의 합
- answer = list(map(int, str(n)[::-1])) # str형 뒤집어서 한번에 int형으로 변환
