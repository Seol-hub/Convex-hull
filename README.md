## 볼록 껍질(Convex hull)은 2차원 유클리드 좌표에서 어떤 점들의 집합으로 만든 다각형이 다른 모든 점들을 모두 포함하는 점들의 집합을 말합니다.

<img src="https://mblogthumb-phinf.pstatic.net/MjAxOTA0MTFfMTg5/MDAxNTU0OTQ5MjMzODQ5.CtMxrQN8bfUvY5_ha9NLlkf4d0kTzFBp0L7szfGk8mQg.iGJwFYkKHn1ZEBotjx2B6AMb3xiLk218GqVDuulWG6Yg.PNG.pyw0564/image.png?type=w800">

위와 같은 11개의 좌표가 있다면 볼록 껍질(이하, 컨벡스 헐)은 아래와 같이 됩니다.

​<img src="https://mblogthumb-phinf.pstatic.net/MjAxOTA0MTFfMTYx/MDAxNTU0OTQ5NzU2NzIx.amhJnmEz-lbxhJZTkQR_aNrhaaDci7seaIkjyCHFSn4g.1cRTb0Lzd4r5ipZE6h0SyThCvZV8EfBEYGx8vA105mIg.PNG.pyw0564/image.png?type=w800">

총 7개의 점의 집합으로 컨벡스 헐을 나타낼 수 있습니다.

컨벡스 헐을 구하는 방법은 분할 정복과 그라함 스캔(Graham scan)등 이 있습니다.
둘다 O(NlogN)에 수행이 가능하지만,
그라함 스캔이 쉽고 간편하므로 여기서는 그라함 스캔을 설명합니다.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/GrahamScanDemo.gif/200px-GrahamScanDemo.gif">

## Graham scan

y좌표가 가장 크거나 가장 작은 점, x좌표가 가장 크거나 가장 작은 점 중 아무거나 골라도 됩니다.
좌표들이 주어졌을 때, 제일 왼쪽 점은 컨벡스헐에 포함됩니다.
마찬가지로 제일 아래쪽, 오른쪽, 위쪽에 있는 점도 컨벡스헐에 포함됩니다.
위의 그라함 스캔은 제일 아래의 점을 기준정점으로 잡은 것입니다.

<img src="https://mblogthumb-phinf.pstatic.net/MjAxOTA0MTFfNTQg/MDAxNTU0OTUxMjU2MDY2.EM9T6kLCJOaG74eGZnA2qKtBRH5yhj-_BmD3dWiUDOsg.lw7jEPhLqOm7GvpEVdPLZT8wgZRnw20dSLhYyJFNXI0g.PNG.pyw0564/SE-e2518b2e-7be5-42c5-a309-80fa48357f52.png?type=w800">

위 그림에서 0이 시작점입니다. 제일 왼쪽점을 기준 정점으로 합니다.
0을 제외한 나머지의 점들을 0에 대한 기울기를 계산하여 오름차순으로 정렬합니다.
기울기의 오름차순이므로 위의 사진처럼 되는데,
이렇게 만드는 컨벡스 헐은 반시계 방향이므로 ccw도 반시계 방향으로 검사합니다.
ccw(Counter Clockwise)란 세 점이 주어졌을 때 방향을 알 수 있는(넓이를 알 수 있는) 함수 입니다.
이는 두 벡터의 외적으로 구할 수 있습니다.

아무튼 0부터 스택에 넣고 스택의 크기가 2 이상일 때, 컨벡스 헐 검사를 합니다.

<img src="https://mblogthumb-phinf.pstatic.net/MjAxOTA0MTFfMTY0/MDAxNTU0OTUxMjI2Nzc3.UgP7Cfi-9MyC2EVDfR1zD2fxR7l_ddgn_fPS9EtFnXEg.MElhu4BBqsyLMX8rDoJY4MaM1vwiEMbCdWSyEuCPJqAg.PNG.pyw0564/image.png?type=w800">

2의 차례일 때 ccw(0,1,2)를 확인합니다. 반시계방향이므로 스택에 넣어줍니다.

<img src="https://mblogthumb-phinf.pstatic.net/MjAxOTA0MTFfNzMg/MDAxNTU0OTUxMTk5Mjgy.8hA4xgoK4pjq8mCvi_4-iCvHVJltEJZAetxioeERs28g.YRpb-_bUDNyMfiJLSJmWffeqRTHxKZMkUqbV9Mrqibsg.PNG.pyw0564/image.png?type=w800">

3번째 점일때 ccw(1,2,3)을 확인하니 시계방향입니다. 이때 2의 점은 오목하게 들어가는 부분이므로
컨벡스헐에 포함되지 않음이 자명합니다. 그러므로 2를 스택에서 뺀 후,
ccw(0,1,3)을 확인합니다. 반시계 이므로 3을 넣습니다.

<img src="https://mblogthumb-phinf.pstatic.net/MjAxOTA0MTFfMjUz/MDAxNTU0OTUxMjk5ODc3.5j_jpF-LbtkP2PlHrES4gExc54kQNwyh6x2qpSwSXiYg.tkzdELTmEpbA5hzfdhJGcgEK-PzrOiT3ZgWsKF-OVEog.PNG.pyw0564/image.png?type=w800">

마찬가지로 6까지 계속 스택에 들어가다가 ccw(5,6,7)이 시계 방향이 됩니다.

<img src="https://mblogthumb-phinf.pstatic.net/MjAxOTA0MTFfMjUg/MDAxNTU0OTUxMzE5MDc0.3s-ON0-5w8JBaHpKes5O1XQqVYIIhVDgUPlF8l3FhaIg.Fvt3yW89ci6JJGvPUhatli9jWkwkI5AT8rtnxQwrZk0g.PNG.pyw0564/image.png?type=w800">

반시계 방향이 나올 때 까지 스택을 비우게 됩니다. 모든 점에 대해서 수행하면 컨벡스 헐이 완성됩니다.
그라함 스캔의 시간복잡도는 O(N)에 수행이 됩니다.
스택에 들어가는 점은 한번만 들어가고 스택에서 나온 점은 컨벡스헐에서 제외되므로
다시 들어가지 못하게 됩니다. 그러므로 O(N+N) = O(N) 입니다.
처음 기준 점을 구하는데 O(NlogN), 기울기를 정렬하는데 O(NlogN), 그라함 스캔 O(N)이므로
총 시간복잡도 O(NlogN)입니다.

코드에서는 간단히 컨벡스헐을 이루는 꼭짓점들의 개수를 출력하고 있지만,
꼭짓점들의 좌표를 출력하려면 스택에 존재하는 인덱스 값들에 대한 수열 A의 값을 출력하면 됩니다.
