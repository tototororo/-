def routes(start,end,city,n):                                             ##경로 구하는 함수
    route = [[start]]                                                      ##출발지 저장
    start_in = city.index(start)                                           ##도시 인덱스 구하기
    while end not in route[-1]:                                           ##도시에 도착하지 않는다면 탐색
        route.append([])                                                         
        route[-1] = [city[i] for i in range(len(city))if n[start_in][i] == 1]    ##리스트 내포를 이용하여 이웃도시 리스트 생성               
        for x in range(len(city)):                                                ##출발지 탐색경로제외
            n[x][start_in] = 0
        if route[-1] != []:                                                        ##막다른길이 아닐경우 출발지 갱신하여 재 탐색
            start_in = city.index(route[-1][-1])
        else :                                                                    ##막다른길일경우 탐색 종료 
            route[-1].append("경로없음")
            break 
    return route
###################################################################################################################
def points(road,city):                         #경로로 가중치 구하는 함수, 많이 배운 최대값 구하는 매커니즘
    n2 = [[0,0.3,0,0,0,0,0], [0.25,0,0,0.33,0,0,0],[0,0,0,0,0,0.12,0], [0,0.12,0.05,0,0,0,0.46], [0,0,0,0.09,0,0,0.11],[0,0,0.65,0,0,0,0.07], [0,0,0,0,0,0.11,0]]
    st = gg = 0
    for g in road[-1]:
        star= city.index(g)
        gg+= n2[st][city.index(g)]
        st = star
    return gg
######################################################################################################################
#변수선언
road = []                                                                       ##경로
poin= 10,1                                                                      ## 가중치
cit = ["서울","대전","대구","부산","시흥","안산","원주"]                        ##도시와 도로
n1 = [[0,1,0,0,0,0,0], [1,0,0,1,0,0,0],[1,0,0,0,0,1,0],[0,1,1,0,0,0,1],[0,0,0,1,0,0,1],[0,0,1,0,0,0,1],[0,0,0,0,1,1,0]]
nn = []                                                                          ##다음경로를 위한 복사본
for n in n1:                                                                    ##딥카피를 위한 작업
    nn.append(list(n))
star = input("출발지 입력:")
en = input("도착지 입력:")
z = 1                                                                            ##경로가 밀렸을때 순서를 당기기위한용도
route_c = [10]                                                                   ##갈림길 나오는 도시가 변경됐음을 알기위한 용도
################################################################################################
for i in range(10):                                         
    route = routes(star,en,cit,n1)                                 ##경로 구하는 함수
    road.append([])                                           ##출력전 경로 다듬기
    road[-1] = [route[i][-1]for i in range(len(route))]      ##리스트내포를 이용해 출력할 리스트 가공
    road[-1][-1] = en
    if road[-1] not in road[:-1] and en in route[-1] :                           ##찾은 경로가 중복되지 않을경우 출력
        print(f"경로 {i+z}. {road[-1]}") 
        gg = points(road,cit)                                    ## 경로의 가중치 계산
        if gg < poin[0]:   
            poin = gg,(i+z)
    else:
        z -= 1
    for i in route :                                        ##다음 경로찾기전 작업
        s=0
        if len(i) > 1 :                                      ##갈림길이 나왔을경우 
            route_c.append(route.index(i))                   ##갈림길이 시작되는 도시를 기억
            rename = cit.index(i[-1])                    #갈림길중하나의 인덱스
            rename2 = cit.index(i[-2])
            cl = cit.index(route[route.index(i)-1][-1])  #갈림길에 도착할수없도록 전 도시에서 길을막음
            nn[cl][rename] = 0                           
            n1.clear()                                  ##함수에 넣기전 갈림길 블락처리 하기위해 초기화후 딥카피
            for n in nn:
                n1.append(list(n))  
            break
    if route[-1][-1] == "경로없음":                      ##막다른 길일경우 우회할수 있게함
        nn[cl][rename] = 1
        nn[cl][rename2] = 0
        n1.clear()
        for n in nn:
            n1.append(list(n))
print(f"[최적경로] 경로{poin[1]}번 가중치:{poin[0]:0.2f}")         ##최소 가중치 출력
