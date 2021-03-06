'''
배열은 다수의 데이터를 그룹핑해서 효율적으로 관리할 수 있는 데이터 스트럭쳐입니다. 
배열의 가장 큰 특징은 인덱스가 있다는 것입니다. 만약 인덱스를 알고 있다면 인덱스를 이용해서 데이터를 가져올 수 있습니다. 
인덱스를 이용한 데이터의 조회는 매우 빠르게 처리 됩니다. 하지만 인덱스를 이용해서 데이터를 가져오려면 데이터에 대한 인덱스의 값이 고정되어야 합니다. 
자연스럽게 어떤 엘리먼트가 삭제되면 삭제된 상태를 빈 공간으로 남겨둬야 합니다. 이것은 메모리의 낭비를 초래합니다. 
또한 배열에 데이터가 있는지 없는지를 체크하는 로직이 필요하다는 의미이기도 합니다.

리스트는 배열이 가지고 있는 인덱스라는 장점을 버리고 대신 빈틈없는 데이터의 적재라는 장점을 취한 데이터 스트럭쳐라고 할 수 있습니다. 
'''
# 리스트의 슬라이싱
kospi_top10 = ['삼성전자', 'SK하이닉스', '현대차', '한국전력',
               '아모레퍼시픽', '제일모직', '삼성전자우', '삼성생명', 'NAVER', '현대모비스']
kospi_top5 = kospi_top10[0:5]
print(kospi_top5)
print(kospi_top10[5:10])
print(kospi_top10[5:9])
print(kospi_top10[5:-1])
