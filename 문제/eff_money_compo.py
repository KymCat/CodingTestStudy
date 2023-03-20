'''
input
3 10
1
2
3

output
4

첫째 줄에 서로 다른 가치의 동전의 종류 수를 나타내는 정수 N과,
만들려는 가치의 합을 의미하는 정수 M이 공백으로 구분되어 주어집니다. (1 ≤ N ≤ 100, 1 ≤ M ≤ 10,000)
이후의 N개의 줄에는 각 화폐의 가치가 주어집니다. 화폐의 가치는 10,000보다 작거나 같은 자연수입니다.

첫째 줄에 가치 M을 만드는 최소 동전의 개수를 출력합니다.
만약 가치 M을 만드는 것이 불가능하다면 -1을 출력합니다.
'''

n,m = map(int, input().split())
array = []
for _ in range(n) :
    array.append(int(input()))

# M의 범위가 10,000이기에 10,001은 존재 할수 없는 수
# 존재 할수 없는 수를 넣어 만들수 없는 경우를 표시
d = [10001] * (m + 1)
d[0] = 0

# 점화식 a(i) = min( a(i), a(i-k)+1 )
# a(i)는 i원을 구성 하는 화폐 개수, k는 화폐 단위(array 값들)
'''
i가 15원, k가 5원 동전 이라고 가정하자. 
결국 15원은 10원 + 5원(k)로 나타낼수 있기에 
a(i-k)+1, 즉 a(10원 - 5원(k)) + 1(5원(k) 1개)라는 식이 탄생한다.
'''

for i in range(n) :
    for j in range(array[i],m+1) :
        d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001 : # 만들 수 없다면...
    print("-1")
else : print(d[m])
