
# 그리디
# 거스름돈 문제 11/01



#당신은 음식점의 계산을 도와주는 점원이다.

#카운터에는 거스름돈으로 사용할 500원, 100원,50원,10원 짜리 동전이 무한히 존재한다고 가정한다.

#손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러줘야 할 동전의 최소 개수를 구하라. 단 거슬러 줘야 할 돈 N은 항상 10배수이다.




n = 1260

count = 0


tool = [500,100,50,10]


for x in tool:

    count+=n//x

    n%=x


print(count)





