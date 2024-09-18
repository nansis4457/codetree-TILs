n = int(input())
cnt = 'A'

# 알파벳을 삼각형 모양으로 출력합니다.
for i in range(n):
    # i만큼 공백을 출력
    for j in range(i):
        print(' ', end=" ")
    # i + 1만큼 알파벳을 출력
    for _ in range(n-i):
        print(cnt, end=" ")
        cnt = chr(ord(cnt) + 1)
        # 알파벳이 Z를 넘으면 A로 돌아갑니다.
        if ord(cnt) > ord('Z'):
            cnt = 'A'
    
    # 한 줄 출력 후 줄바꿈
    print()