# https://www.codewars.com/kata/65e8b02a9e79a010e5210b6c

w = 12, h = 8, x = 5, y = 3, d = "SE" --> True

SE
5,3
6,2
7,1
8,0
NE
9,1
10,2
11,3
12,4
NW
11,5
10,6
9,7
8,8
SW
7,7
6,6
5,5
4,4
3,3
2,2
1,1
0,0


SW x==0 && y==0 -> x==y
SE x==0 && y==h -> x == (h-y)
NW x==w && y==0 -> (w-x) == y
NE x==w && y==h -> (w-x) == (h-y)