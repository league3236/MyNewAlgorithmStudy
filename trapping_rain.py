def trapping_rain(buildings):

    trapped_rain = 0 #갇힌 물
    current_tallest = 0 #현재 최고 높이 빌딩
    total_tallest = max(buildings) #빌딩 전체 중, 최고 높이

    for index in range(0, len(buildings)-1):
        # 첫 인덱스와 마지막 인덱스는 물이 찰 수 없다.
        # 첫 인덱스는 current_tallest를 지정해주고, 마지막 인덱스는 제외 len(buildings) - 1

        if (buildings[index] >= current_tallest) and (buildings[index] != total_tallest):
            current_tallest = buildings[index]

        if buildings[index] < current_tallest:
            trapped_rain += current_tallest - buildings[index]

        if (buildings[index] == total_tallest) and (index != len(buildings)-1):
            next_highest = max(buildings[index+1:])
            for i in range(index+1, len(buildings)-1):
                trapped_rain += next_highest - buildings[i]

            return trapped_rain

    return trapped_rain
        

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))