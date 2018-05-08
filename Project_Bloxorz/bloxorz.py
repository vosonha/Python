
from tkinter import *
import time
"""
# Định nghĩa input đầu vào gồm :
	1. input : ma trận mô phỏng các màng
		Mỗi phần tử được định nghĩa là 1 ô [[ax,ay],[bx,by]]
		Các ô có giá trị : 
			- 'S' : vị trí bắt đầu
			- 'T' : vị trí đích
			-  0  : ô rỗng
			-  1  : ô có gạch
			-  2  : ô này khối trụ không được đứng 
			- 'O' : nếu 1 phần khối trụ nằm trên ô này thì các khối ẩn do ô này quản lý (ô có giá trị 3) sẽ hiện lên, lặp lại lần nữa sẽ ẩn lại
				+  3  : ô có gạch nhưng bị ẩn   
				+  1  : ô hiện gạch
			- 'X' : nếu khối trụ đứng trên ô này thì các khối ẩn của ô này quản lý (ô có giá trị 5) sẽ hiện lên, lặp lại lần nữa sẽ ẩn lại
				+  5  : ô có gạch nhưng bị ẩn   
				+  1  : ô hiện gạch
	2. input_X : mảng lưu vị trí nút điều khiển cầu 'X' và các vị trí nó quản lý
	3. input_O : mảng lưu vị trí nút điều khiển cầu 'O' và các vị trí nó quản lý 
    4. startBloxor : vị trí bắt đầu
    5. targetBloxor : vị trí kết thúc	
"""
# Màng 1
#		    0   1   2   3   4   5   6   7   8   9
input1 = [[ 1 , 1 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], # 0
          [ 1 ,'S', 1 , 1 , 1 , 1 , 0 , 0 , 0 , 0 ], # 1
          [ 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 0 ], # 2
          [ 0 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ], # 3
          [ 0 , 0 , 0 , 0 , 0 , 1 , 1 ,'T', 1 , 1 ], # 4
          [ 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 0 ]] # 5
input1_X = input1_O = []
startBloxor1 = [[1,1],[1,1]]
targetBloxor1 = [[4,7],[4,7]]
# Màng 2
#		    0   1   2   3   4   5   6   7   8   9  10  11  12  13  14
input2 = [[ 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 1 , 0 , 0 , 1 , 1 , 1 ], # 0
          [ 1 , 1 , 1 , 1 , 0 , 0 , 1 , 1 ,'X', 1 , 0 , 0 , 1 ,'T', 1 ], # 1
          [ 1 , 1 ,'O', 1 , 0 , 0 , 1 , 1 , 1 , 1 , 0 , 0 , 1 , 1 , 1 ], # 2
          [ 1 ,'S', 1 , 1 , 0 , 0 , 1 , 1 , 1 , 1 , 0 , 0 , 1 , 1 , 1 ], # 3
          [ 1 , 1 , 1 , 1 , 3 , 3 , 1 , 1 , 1 , 1 , 5 , 5 , 1 , 1 , 1 ], # 4
          [ 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 1 , 0 , 0 , 0 , 0 , 0 ]] # 5
input2_X = [([1,8], [[4,10],[4,11]])]
input2_O = [([2,2], [[4,4],[4,5]])]
startBloxor2 = [[3,1],[3,1]]
targetBloxor2 = [[1,13],[1,13]]
# Màng 3
#		    0   1   2   3   4   5   6   7   8   9  10  11  12  13  14
input3 = [[ 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 0 ], # 0
          [ 1 , 1 , 1 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 1 , 1 , 0 , 0 ], # 1
          [ 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 0 , 1 , 1 , 1 , 1 ], # 2
          [ 0 ,'S', 1 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 ,'T', 1 ], # 3
          [ 1 , 1 , 1 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 1 ], # 4
          [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 ]] # 5
input3_X = input3_O = []     
startBloxor3 = [[3,1],[3,1]]
targetBloxor3 = [[3,13],[3,13]]    
# Màng 4
#		    0   1   2   3   4   5   6   7   8   9  10  11  12  13 
input4 = [[ 0 , 0 , 0 , 2 , 2 , 2 , 2 , 2 , 2 , 2 , 0 , 0 , 0 , 0 ], # 0
          [ 0 , 0 , 0 , 2 , 2 , 2 , 2 , 2 , 2 , 2 , 0 , 0 , 0 , 0 ], # 1
          [ 1 , 1 , 1 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 0 , 0 ], # 2
          [ 1 , 1 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 0 , 0 ], # 3
          [ 1 , 1 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 0 , 0 ], # 4
          [ 1 ,'S', 1 , 0 , 0 , 1 , 1 , 1 , 1 , 2 , 2 , 2 , 2 , 2 ], # 5
          [ 1 , 1 , 1 , 0 , 0 , 1 , 1 , 1 , 1 , 2 , 2 , 2 , 2 , 2 ], # 6
          [ 0 , 0 , 0 , 0 , 0 , 1 ,'T', 1 , 0 , 0 , 2 , 2 , 1 , 2 ], # 7
          [ 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 2 , 2 , 2 , 2 ]] # 8
input4_X = input4_O = []
startBloxor4 = [[5,1],[5,1]]
targetBloxor4 = [[7,6],[7,6]]
# Màng 6
#		    0   1   2   3   4   5   6   7   8   9  10  11  12  13  14
input6 = [[ 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 0 , 0 , 0], # 0
          [ 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 0 , 0], # 1
          [ 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 0], # 2
          ['S', 1 , 1 , 1 , 1 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 1], # 3
          [ 0 , 0 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 0 , 0 , 1 , 1 ,'T', 1], # 4
          [ 0 , 0 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1], # 5
          [ 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 0], # 6
          [ 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 0 , 0 , 0], # 7
          [ 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 0 , 0 , 0], # 8
          [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 0 , 0 , 0]] # 9
input6_X = input6_O = []
startBloxor6 = [[3,0],[3,0]]
targetBloxor6 = [[4,13],[4,13]]
# Màng 7
#		    0   1   2   3   4   5   6   7   8   9  10  11  12  13  14
input7 = [[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 1 , 0 , 0 , 0], # 0
          [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 1 , 0 , 0 , 0], # 1
          [ 1 , 1 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 1 , 1 , 1 , 1], # 2
          [ 1 ,'S', 1 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 0 , 0 , 1 , 1 , 1], # 3
          [ 1 , 1 , 1 , 0 , 0 , 0 , 0 , 1 , 1 ,'X', 0 , 0 , 1 ,'T', 1], # 4
          [ 1 , 1 , 1 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 1 , 1 , 1], # 5
          [ 0 , 1 , 1 , 5 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0], # 6
          [ 0 , 0 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0]] # 7
input7_X = [([4,9], [[6,3]])]
input7_O = []
startBloxor7 = [[3,1],[3,1]]
targetBloxor7 = [[4,13],[4,13]]
# Màng 11
#		    0   1   2   3   4   5   6   7   8   9  10  11 
input11 =[[ 0 , 1 , 1 , 1 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], # 0
          [ 0 , 1 ,'T', 1 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], # 1
          [ 0 , 1 , 1 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], # 2
          [ 0 , 1 , 0 , 0 , 0 , 1 , 1 , 1 , 1 , 1 , 1 , 0 ], # 3
          [ 0 , 1 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 1 , 1 , 0 ], # 4
          ['S', 1 , 1 , 1 , 1 , 1 , 1 , 0 , 0 , 1 , 1 , 1 ], # 5
          [ 0 , 0 , 0 , 0 , 0 , 1 , 8 , 0 , 0 , 0 , 0 , 1 ], # 6
          [ 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 1 , 0 , 0 , 1 ], # 7
          [ 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ], # 8
          [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 0 ]] # 9
input11_O = input11_X = []
startBloxor11 = [[5,0],[5,0]]
targetBloxor11 = [[1,2],[1,2]]
# Màng 12
#		    0   1   2   3   4   5   6   7   8   9  10  11  12 
input12 =[[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,'X'], # 0
          [ 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 1 , 1 , 1 ], # 1
          [ 0 , 0 , 0 , 0 , 0 , 1 ,'X', 1 , 1 , 1 , 1 , 1 , 5 ], # 2
          [ 0 , 0 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 0 , 1 , 1 , 0 ], # 3
          [ 0 , 0 , 0 , 1 ,'T', 1 , 5 , 0 , 0 , 0 , 1 , 1 , 0 ], # 4
          [ 0 , 1 , 1 , 1 , 1 , 1 , 0 , 0 , 0 , 1 , 1 , 1 , 1 ], # 5
          [ 1 , 1 ,'S', 1 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 1 ], # 6
          [ 1 , 1 , 1 , 1 , 0 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 0 ], # 7
          [ 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 0 , 0 , 0 ], # 8
          [ 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 0 , 0 , 0 ]] # 9
input12_X = [([2,6], [[2,12]]), ([0,12], [[4,6]])]
input12_O = []
startBloxor12 = [[6,2],[6,2]]
targetBloxor12 = [[4,4],[4,4]]
# Màng 13
#		    0   1   2   3   4   5   6   7   8   9  10  11  12  13 
input13 =[[ 1 , 1 , 1 , 2 , 1 , 1 , 1 , 1 , 2 , 1 , 1 , 1 , 1 , 0 ], # 0
          [ 1 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 0 ], # 1
          [ 1 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 ], # 2
          [ 1 , 1 , 1 , 0 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 1 ,'S', 1 ], # 3
          [ 1 , 1 , 1 , 2 , 2 , 2 , 1 ,'T', 1 , 0 , 0 , 1 , 1 , 1 ], # 4
          [ 1 , 1 , 1 , 0 , 0 , 2 , 1 , 1 , 1 , 0 , 0 , 1 , 0 , 0 ], # 5
          [ 0 , 0 , 1 , 0 , 0 , 2 , 2 , 2 , 2 , 2 , 1 , 1 , 0 , 0 ], # 6
          [ 0 , 0 , 1 , 1 , 1 , 2 , 2 , 1 , 2 , 2 , 2 , 0 , 0 , 0 ], # 7
          [ 0 , 0 , 0 , 1 , 1 , 2 , 2 , 2 , 2 , 2 , 2 , 0 , 0 , 0 ], # 8
          [ 0 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 0 ]] # 9
input13_X = input13_O = []
startBloxor13 = [[3,12],[3,12]]
targetBloxor13 = [[4,7],[4,7]]
# Màng 14
#		    0   1   2   3   4   5   6   7   8   9  10  11  12  13 
input14 =[[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 0 ], # 0
          [ 0 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 0 ], # 1
          [ 1 , 5 , 5 , 1 ,'S', 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ], # 2
          [ 1 , 5 , 5 , 1 , 1 , 1 , 0 , 0 , 0 , 0 , 0 , 0 ,'X', 1 ], # 3
          [ 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 ], # 4
          [ 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 ], # 5
          [ 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 1 , 1 , 1 ], # 6
          [ 1 , 1 , 1 , 1 , 1 , 0 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 0 ], # 7
          [ 0 , 1 , 1 ,'T', 1 , 0 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 0 ], # 8
          [ 0 , 0 , 1 , 1 , 1 , 0 , 0 , 0 , 1 , 1 , 1 , 1 , 1 ,'X']] # 9
input14_X = [([3,12], [[2,1],[2,2]]), ([9,13], [[3,1],[3,2]])]
input14_O = []
startBloxor14 = [[2,4],[2,4]]
targetBloxor14 = [[8,3],[8,3]]
# Màng 17 chưa đc
#		    0   1   2   3   4   5   6   7   8   9  10  11  12  13  14
input17 =[[ 1 , 1 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], # 0
          [ 1 ,'S', 1 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 0 , 0 , 1 , 1 , 1 ], # 1
          [ 1 , 1 , 1 , 0 , 0 , 0 , 0 , 5 , 1 , 1 , 1 , 1 , 1 ,'T', 1 ], # 2
          [ 1 , 1 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,'X','X', 1 ], # 3
          [ 1 , 1 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], # 4
          [ 1 , 1 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], # 5
          [ 1 , 1 , 1 , 0 , 0 , 0 , 5 , 1 , 1 , 1 , 1 , 1 ,'X', 0 , 0 ], # 6
          [ 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 5 , 0 , 0 , 1 , 1 , 0 , 0 ], # 7
          [ 1 ,'O', 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 0 , 0 ], # 8
          [ 1 , 1 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 ,'X', 0 , 0 ]] # 9
input17_X = [([6,12], [[2,7]]), ([9,12], [[3,1]])]
input17_O = [([8,1],[[7,8]])]
startBloxor17 = [[1,1],[1,1]]
targetBloxor17 = [[2,13],[2,13]]
# Màng 18
#		    0   1   2   3   4   5   6   7   8   9  10  11  12  13  14
input18 =[[ 0 , 0 , 0 , 0 , 0 , 0 , 0 ,'O', 0 , 0 , 0 , 0 , 0 , 0 , 0 ], # 0
          [ 1 , 1 , 8 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], # 1
          [ 1 , 1 , 1 , 1 , 1 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], # 2
          [ 1 , 8 ,'S', 1 , 1 , 1 , 1 , 1 , 3 , 3 , 1 , 1 , 3 , 3 , 1 ], # 3
          [ 1 , 1 , 1 , 1 , 1 , 5 , 0 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 0 ], # 4
          [ 1 , 1 , 8 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 0 ], # 5
          [ 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,'O', 0 , 0 , 1 , 1 , 1 , 0 ], # 6
          [ 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 ,'T', 1 , 0 ], # 7
          [ 1 , 3 , 3 ,'X', 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 1 , 0 ]] # 8
input18_X = [([8,3], [[4,5]])]
input18_O = [([0,7],[[3,8],[3,9]]), ([6,8],[[3,12],[3,13],[8,1],[8,2]])]
startBloxor18 = [[3,2],[3,2]]
targetBloxor18 = [[7,12],[7,12]]
# Màng 21
#		    0   1   2   3   4   5   6   7   8   9  10  11  12  13  14
input21 =[[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 0 , 0 ], # 0
          [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 0 , 0 , 0 ], # 1
          [ 1 , 1 , 0 , 0 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 0 , 0 , 0 , 0 ], # 2
          [ 1 ,'S', 1 , 1 , 1 , 1 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 ], # 3
          [ 1 , 1 , 1 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 1 , 1 , 1 ], # 4
          [ 0 , 1 , 1 , 0 , 0 , 0 , 0 , 0 ,'X', 1 , 1 , 1 , 1 ,'T', 1 ], # 5
          [ 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 ,'X', 1 , 0 , 0 , 1 , 1 , 1 ], # 6
          [ 0 , 0 , 1 , 1 , 1 , 5 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 0 , 0 ], # 7
          [ 0 , 0 , 0 , 1 , 1 , 1 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 0 , 0 ], # 8
          [ 0 , 0 , 0 , 5 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 0 , 0 , 0 , 0 ]] # 9
input21_X = [([5,8], [[9,3]]), ([6,8], [[7,5]])]
input21_O = []
startBloxor21 = [[3,1],[3,1]]
targetBloxor21 = [[5,13],[5,13]]

def getNumeric(prompt):
		while True:
			response = input(prompt)
			try:
				return int(response)
			except ValueError:
				print("Please enter a number!")

def choice_State():
	#while True:
			print("---------Please enter number 0 to Exit!-----------")
			n = getNumeric("Enter a number state (1->33) = ")
			if n >=1 and n <= 33 :
				print("--------------State %d-------------" % n)
			if n == 1:
				Bloxorz(input1, input1_X, input1_O, startBloxor1, targetBloxor1)
			elif n == 2:
				Bloxorz(input2, input2_X, input2_O, startBloxor2, targetBloxor2)
			elif n == 3:
				Bloxorz(input3, input3_X, input3_O, startBloxor3, targetBloxor3)
			elif n == 4:
				Bloxorz(input4, input4_X, input4_O, startBloxor4, targetBloxor4)
			elif n == 6:
				Bloxorz(input6, input6_X, input6_O, startBloxor6, targetBloxor6)
			elif n == 7:
				Bloxorz(input7, input7_X, input7_O, startBloxor7, targetBloxor7)
			elif n == 11:
				Bloxorz(input11, input11_X, input11_O, startBloxor11, targetBloxor11)
			elif n == 12:
				Bloxorz(input12, input12_X, input12_O, startBloxor12, targetBloxor12)
			elif n == 13:
				Bloxorz(input13, input13_X, input13_O, startBloxor13, targetBloxor13)
			elif n == 14:
				Bloxorz(input14, input14_X, input14_O, startBloxor14, targetBloxor14)
			elif n == 18:
				Bloxorz(input18, input18_X, input18_O, startBloxor18, targetBloxor18)
			elif n == 21:
				Bloxorz(input21, input21_X, input21_O, startBloxor21, targetBloxor21)
			else:
				return

def print_input(input1):
	for temp in range(len(input1)):
		for temp1 in range(len(input1[0])):
			print(str(input1[temp][temp1]), end = "   ")
		print("\n")

class Bloxorz:
	def __init__(self, input1, input_X, input_O, startBloxor, targetBloxor):
		self.input_temp = input1
		self.input = input1
		self.numrows = len(input1)
		self.numcols = len(input1[0])
		self.input_X = input_X
		self.input_O = input_O
		self.startBloxor = startBloxor
		self.targetBloxor = targetBloxor
		self.flag = False
		self.choice()
		
	def choice(self):
		#while True:
			self.flag = False
			self.input = self.input_temp
			print("Input : ")
			print_input(self.input)
			print("Start :",self.startBloxor)
			print("Target :",self.targetBloxor)
			print("Algorithm choice :")
			print("1. DFS")
			print("2. BFS")
			print("3. Best First Search")
			print("4. Exit")
			n = getNumeric("Enter a number (1->4) = ")
			if n == 1:
				self.solve_dfs()
			elif n == 2:
				self.solve_bfs()
			elif n == 3:
				self.solve_best_first_search()
			elif n == 4:
				return

	def solve_dfs(self):
		# Hàm xử lý DFS
		print("--------------------------DFS-------------------------")
		# stack lưu các vị trí có thể di chuyển tiếp theo từ top của stack (pop()) vào đầu stack
		stack = [(self.startBloxor,[self.startBloxor])]
		# visited lưu các vị trí đã đi qua
		visited = []
		visited_O_X = []
		while stack:
			# vertex : vị trí xét, path : đường dẫn từ vị trí đầu tới nó
			# lấy vị trí top
			(vertex, path) = stack.pop()
			visited.append(vertex)
			ax = vertex[0][0]
			ay = vertex[0][1]
			bx = vertex[1][0]
			by = vertex[1][1]
			# Kiểm tra có nằm trên nút điều khiển
			if self.check_O_X(ax, ay, bx, by):
				stack = []
				visited = []
				if self.input[ax][ay] == 'O':
					visited_O_X.append([[ax,ay],[ax,ay]])
					visited_O_X.append([[ax-1,ay],[ax,ay]])
					visited_O_X.append([[ax,ay],[ax+1,ay]])
					visited_O_X.append([[ax,ay-1],[ax,ay]])
					visited_O_X.append([[ax,ay],[ax,ay+1]])
				elif self.input[bx][by] == 'O':
					visited_O_X.append([[bx,by],[bx,by]])
					visited_O_X.append([[bx-1,by],[bx,by]])
					visited_O_X.append([[bx,by],[bx+1,by]])
					visited_O_X.append([[bx,by-1],[bx,by]])
					visited_O_X.append([[bx,by],[bx,by+1]])
				else:
					visited_O_X.append(vertex)
			isState = self.is_state(vertex)  # trạng thái của khối
			if self.add_vertex_and_check_flag(isState, stack, path, visited, visited_O_X, vertex, ax, ay, bx, by):
				# Xuất ra output
				print(path)
				grapphic(self.input, path, self.targetBloxor, self.input_X, self.input_O)
				return
		print("No path to the destination!")

	def solve_bfs(self):
		# Hàm xử lý BFS
		print("--------------------------BFS-------------------------")
		# queue : lưu các vị trí có thể di chuyển tiếp từ phần tử đầu (pop(0)) vào cuối queue
		queue = [(self.startBloxor,[self.startBloxor])]
		# visited lưu các vị trí đã đi qua
		visited = []
		visited_O_X = []
		while queue:
			# vertex : vị trí xét, path : đường dẫn từ vị trí đầu tới nó
			(vertex, path) = queue.pop(0)
			visited.append(vertex)
			ax = vertex[0][0]
			ay = vertex[0][1]
			bx = vertex[1][0]
			by = vertex[1][1]
			# Kiểm tra có nằm trên nút điều khiển
			if self.check_O_X(ax, ay, bx, by):
				queue = []
				visited = []
				if self.input[ax][ay] == 'O':
					visited_O_X.append([[ax,ay],[ax,ay]])
					visited_O_X.append([[ax-1,ay],[ax,ay]])
					visited_O_X.append([[ax,ay],[ax+1,ay]])
					visited_O_X.append([[ax,ay-1],[ax,ay]])
					visited_O_X.append([[ax,ay],[ax,ay+1]])
				elif self.input[bx][by] == 'O':
					visited_O_X.append([[bx,by],[bx,by]])
					visited_O_X.append([[bx-1,by],[bx,by]])
					visited_O_X.append([[bx,by],[bx+1,by]])
					visited_O_X.append([[bx,by-1],[bx,by]])
					visited_O_X.append([[bx,by],[bx,by+1]])
				else:
					visited_O_X.append(vertex)
			# Trạng thái của khối trụ
			isState = self.is_state(vertex)
			if self.add_vertex_and_check_flag(isState, queue, path, visited, visited_O_X, vertex, ax, ay, bx, by):
				# Xuất ra output
				print(path)
				grapphic(self.input, path, self.targetBloxor, self.input_X, self.input_O)
				return
		print("No path to the destination!")

	def solve_best_first_search(self):
		# Hàm xử lý Hill climing
		print("--Best First Search--")
		

	def check_O_X(self, ax, ay, bx, by):
		# Kiểm tra trường hợp nút điều khiển cầu 'O' và 'X'
		if self.input[ax][ay] == 'O' or self.input[bx][by] == 'O':
			for temp in range(len(self.input_O)):
				if self.input_O[temp][0] == [ax, ay] or self.input_O[temp][0] == [bx,by]:
					for temp1 in range(len(self.input_O[temp][1])):
						if self.input[ self.input_O[temp][1][temp1][0] ][ self.input_O[temp][1][temp1][1] ] != 1:
							self.input[ self.input_O[temp][1][temp1][0] ][ self.input_O[temp][1][temp1][1] ] = 1
						else:
							self.input[ self.input_O[temp][1][temp1][0] ][ self.input_O[temp][1][temp1][1] ] = 3
			return True
		if self.input[ax][ay] == self.input[bx][by] == 'X':
			for temp in range(len(self.input_X)):
				if self.input_X[temp][0] == [ax, ay]:
					for temp1 in range(len(self.input_X[temp][1])):
						if self.input[ self.input_X[temp][1][temp1][0] ][ self.input_X[temp][1][temp1][1] ] != 1:
							self.input[ self.input_X[temp][1][temp1][0] ][ self.input_X[temp][1][temp1][1] ] = 1
						else:
							self.input[ self.input_X[temp][1][temp1][0] ][ self.input_X[temp][1][temp1][1] ] = 5
			return True

	def is_state(self, vertex):
		# Kiểm tra trạng thái của khối trụ
		temp = (vertex[1][0]-vertex[0][0], vertex[1][1]-vertex[0][1])
		if temp == (0,0):
			return "isStanding"
		elif temp == (0,1):
			return "isHorizontal"
		elif temp == (1,0):
			return "isVertical"
		else:
			return "Invalid bloxor"

	def add_vertex_and_check_flag(self, isState, stack, path, visited, visited_O_X, vertex, ax, ay, bx, by):
		# Hàm thêm các vị trí có thể di chuyển tiếp vào stack or queue
		# Nếu tới vị trí đích thì in kết quả và return True
		# Nếu chưa tới vị trí đích thì return False
		if isState == "isStanding":
			# Di chuyển lên : ax - 2, bx - 1
			self.move_up_down(stack, path, visited, visited_O_X, ax, ay, bx, by, -2, -1)
			if self.check_flag(path):
				return True
			# Di chuyển xuống : ax + 1, bx + 2
			self.move_up_down(stack, path, visited, visited_O_X, ax, ay, bx, by, 1, 2)
			if self.check_flag(path):
				return True
			# Di chuyển qua phải : ay + 1, by +2
			self.move_right_left(stack, path, visited, visited_O_X, ax, ay, bx, by, 1, 2)
			if self.check_flag(path):
				return True
			# Di chuyển qua trái : ay - 2, by - 1
			self.move_right_left(stack, path, visited, visited_O_X, ax ,ay, bx, by, -2, -1)
			if self.check_flag(path):
				return True
		elif isState == "isHorizontal":
			# Di chuyển lên : ax - 1, bx - 1
			self.move_up_down(stack, path, visited, visited_O_X, ax, ay, bx, by, -1, -1)
			if self.check_flag(path):
				return True
			# Di chuyển xuống : ax + 1, bx + 1
			self.move_up_down(stack, path, visited, visited_O_X, ax, ay, bx, by, 1, 1)
			if self.check_flag(path):
				return True
			# Di chuyển qua phải : ay + 2, by +1
			self.move_right_left(stack, path, visited, visited_O_X, ax, ay, bx, by, 2, 1)
			if self.check_flag(path):
				return True
			# Di chuyển qua trái : ay - 1, by - 2
			self.move_right_left(stack, path, visited, visited_O_X, ax, ay, bx, by, -1, -2)
			if self.check_flag(path):
				return True
		elif isState == "isVertical":
			# Di chuyển lên : ax - 1, bx - 2
			self.move_up_down(stack, path, visited, visited_O_X, ax, ay, bx, by, -1, -2)
			if self.check_flag(path):
				return True
			# Di chuyển xuống : ax + 2, bx + 1
			self.move_up_down(stack, path, visited, visited_O_X, ax, ay, bx, by, 2, 1)
			if self.check_flag(path):
				return True
			# Di chuyển qua phải : ay + 1, by +1
			self.move_right_left(stack, path, visited, visited_O_X, ax, ay, bx, by, 1, 1)
			if self.check_flag(path):
				return True
			# Di chuyển qua trái : ay - 1, by - 1
			self.move_right_left(stack, path, visited, visited_O_X, ax, ay, bx, by, -1, -1)
			if self.check_flag(path):
				return True
		else:
			return print(isState)
		return False

	def move_up_down(self, stack, path, visited, visited_O_X, ax, ay, bx, by, x1, x2):
		# Di chuyển lên hoặc xuống
		ax, bx = self.shiftX(ax, bx, x1, x2)
		# Kiểm tra vị trí
		if self.check_state(ax, ay, bx, by):
			if [[ax,ay],[bx,by]] not in visited:
				if [[ax,ay],[bx,by]] not in visited_O_X:
					if [[ax,ay],[bx,by]] == self.targetBloxor:
						# Nếu đã tới đích thì gán flag = True và return
						self.flag = True
						return
					# Add vị trí hợp lệ và đường dẫn tới nó vào stack 
					stack.append(([[ax,ay],[bx,by]], path + [[[ax,ay],[bx,by]]]))

	def move_right_left(self, stack, path, visited, visited_O_X, ax, ay, bx, by, y1, y2):
		# Di chuyển qua trái hoặc phải
		ay, by = self.shiftY(ay, by, y1, y2)
		# Kiểm tra vị trí
		if self.check_state(ax, ay, bx, by):
			if [[ax,ay],[bx,by]] not in visited:
				if [[ax,ay],[bx,by]] not in visited_O_X:
					if [[ax,ay],[bx,by]] == self.targetBloxor:
						# Nếu đã tới đích thì gán flag = True và return
						self.flag = True
						return
					# Add vị trí hợp lệ và đường dẫn tới nó vào stack 
					stack.append(([[ax,ay],[bx,by]], path + [[[ax,ay],[bx,by]]]))

	def shiftX(self, ax, bx, x1, x2):
		# Move up and down
		ax += x1
		bx += x2
		return ax, bx

	def shiftY(self, ay, by, y1, y2):
		# Move right and left
		ay += y1
		by += y2
		return ay, by

	def check_state(self, ax, ay, bx, by):
			# kiểm tra vị trí mới nằm trên ô hợp lệ
		if ax >= 0 and ax < self.numrows and bx >= 0 and bx < self.numrows and ay >= 0 and ay < self.numcols and by >= 0 and by < self.numcols:
		 	if (self.input[ax][ay] == self.input[bx][by] == 1) or (self.input[ax][ay] == self.input[bx][by] == 'T') or (self.input[ax][ay] == 1 and self.input[bx][by] == 'T') or (self.input[ax][ay] == 'T' and self.input[bx][by] == 1) or (self.input[ax][ay] == 1 and self.input[bx][by] == 'S') or (self.input[ax][ay] == 'S' and self.input[bx][by] == 1):
		 		return True
		 	# Kiểm tra trường hợp khối trụ không được đứng trên ô '2'
		 	elif (self.input[ax][ay] == self.input[bx][by] == 2) and ((bx-ax) != (by-ay)) or (self.input[ax][ay] == 1 and self.input[bx][by] == 2) or (self.input[ax][ay] == 2 and self.input[bx][by] == 1):
		 		return True
		 	# Kiểm tra trường hợp nút điều khiển cầu
		 	elif (self.input[ax][ay] == self.input[bx][by] == 'X') or (self.input[ax][ay] == 1 and self.input[bx][by] == 'X') or (self.input[ax][ay] == 'X' and self.input[bx][by] == 1):
		 		return True
		 	if (self.input[ax][ay] == self.input[bx][by] == 'O') or (self.input[ax][ay] == 1 and self.input[bx][by] == 'O') or (self.input[ax][ay] == 'O' and self.input[bx][by] == 1):
		 		return True
		 		
		else:
			return False

	def check_flag(self, path):
		# Nếu đã tới đích thì in đường đi...
		if self.flag == True:
			# Lưu vị trí đích vào path
			path.append(self.targetBloxor)
			return True
"""
# Hàm vẽ đồ họa mô phỏng game
# Định nghĩa :
	- gray: ô gạch
	- brown: khối trụ
	- green: đích
	- pink: nút điều khiển O
	- yellow: nút điều khiển X
	- orange: ô gạch không được đứng
"""
def grapphic(input1, path, targetBloxor, input_X, input_O):
	root = Tk()
	root.title('Graphic')
	canvas = Canvas(root, width = 1350, height = 800, bg='white')
	canvas.pack()

	for i in range(len(input1)):
		for j in range(len(input1[i])):
			if input1[i][j] == 'S':
				canvas.create_rectangle(5 + (j*50),5 +(i*50),55+(j*50) ,55 +(i*50),fill='brown')		
			elif input1[i][j] == 'T':
				canvas.create_rectangle(5 + (j*50),5 +(i*50),55+(j*50) ,55 +(i*50),fill='green')
			elif input1[i][j] == 'O' or input1[i][j] == 8:
				canvas.create_rectangle(5 + (j*50),5 +(i*50),55+(j*50) ,55 +(i*50),fill='pink')
			elif input1[i][j] == 'X':
				canvas.create_rectangle(5 + (j*50),5 +(i*50),55+(j*50) ,55 +(i*50),fill='yellow')
			elif input1[i][j] == 1: 
				canvas.create_rectangle(5 + (j*50),5 +(i*50),55+(j*50) ,55 +(i*50),fill='gray')
			elif input1[i][j] == 2: 
				canvas.create_rectangle(5 + (j*50),5 +(i*50),55+(j*50) ,55 +(i*50),fill='orange')
	# Xét các ô cầu
	for i in range(len(input_O)):
		for j in range(len(input_O[i][1])):
			canvas.create_rectangle(5 + (input_O[i][1][j][1]*50),5 +(input_O[i][1][j][0]*50),55+(input_O[i][1][j][1]*50) ,55 +(input_O[i][1][j][0]*50),fill='white')
	for i in range(len(input_X)):
		for j in range(len(input_X[i][1])):
			canvas.create_rectangle(5 + (input_X[i][1][j][1]*50),5 +(input_X[i][1][j][0]*50),55+(input_X[i][1][j][1]*50) ,55 +(input_X[i][1][j][0]*50),fill='white')
	# In đường đi step-by-step
	for i in range(len(path)):
		canvas.create_rectangle(5 + (path[i][0][1]*50),5 +(path[i][0][0]*50),55+(path[i][0][1]*50) ,55 +(path[i][0][0]*50),fill='brown')	
		canvas.create_rectangle(5 + (path[i][1][1]*50),5 +(path[i][1][0]*50),55+(path[i][1][1]*50) ,55 +(path[i][1][0]*50),fill='brown')
		
		# Xét đi tới nút điều khiển thì hiện cầu
		if input1[path[i][0][0]][path[i][0][1]] == 'O' or input1[path[i][1][0]][path[i][1][1]] == 'O':
			for temp in range(len(input_O)):
				if input_O[temp][0] == [path[i][0][0],path[i][0][1]] or input_O[temp][0] == [path[i][1][0],path[i][1][1]]:
					for temp1 in range(len(input_O[temp][1])):
						canvas.create_rectangle(5 + (input_O[temp][1][temp1][1]*50),5 +(input_O[temp][1][temp1][0]*50),55+(input_O[temp][1][temp1][1]*50) ,55 +(input_O[temp][1][temp1][0]*50),fill='gray')
		if input1[path[i][0][0]][path[i][0][1]] == input1[path[i][1][0]][path[i][1][1]] == 'X':
			for temp in range(len(input_X)):
				if input_X[temp][0] == [path[i][0][0],path[i][0][1]] or input_X[temp][0] == [path[i][1][0],path[i][1][1]]:
					for temp1 in range(len(input_X[temp][1])):
						canvas.create_rectangle(5 + (input_X[temp][1][temp1][1]*50),5 +(input_X[temp][1][temp1][0]*50),55+(input_X[temp][1][temp1][1]*50) ,55 +(input_X[temp][1][temp1][0]*50),fill='gray')	
		root.update()
		time.sleep(0.5)
		if i != len(path) - 1:
			canvas.create_rectangle(5 + (path[i][0][1]*50),5 +(path[i][0][0]*50),55+(path[i][0][1]*50) ,55 +(path[i][0][0]*50),fill='gray')
			canvas.create_rectangle(5 + (path[i][1][1]*50),5 +(path[i][1][0]*50),55+(path[i][1][1]*50) ,55 +(path[i][1][0]*50),fill='gray')
		if path[i][0] == targetBloxor[0] or path[i][1] == targetBloxor[0]:
			canvas.create_rectangle(5 + (targetBloxor[0][1]*50),5 +(targetBloxor[0][0]*50),55+(targetBloxor[0][1]*50) ,55 +(targetBloxor[0][0]*50),fill='green')
		if input1[path[i][0][0]][path[i][0][1]] == 2:
			canvas.create_rectangle(5 + (path[i][0][1]*50),5 +(path[i][0][0]*50),55+(path[i][0][1]*50) ,55 +(path[i][0][0]*50),fill='orange')
		if input1[path[i][1][0]][path[i][1][1]] == 2:
			canvas.create_rectangle(5 + (path[i][1][1]*50),5 +(path[i][1][0]*50),55+(path[i][1][1]*50) ,55 +(path[i][1][0]*50),fill='orange')
		if input1[path[i][0][0]][path[i][0][1]] == 'O':
			canvas.create_rectangle(5 + (path[i][0][1]*50),5 +(path[i][0][0]*50),55+(path[i][0][1]*50) ,55 +(path[i][0][0]*50),fill='pink')
		if input1[path[i][1][0]][path[i][1][1]] == 'O':
			canvas.create_rectangle(5 + (path[i][1][1]*50),5 +(path[i][1][0]*50),55+(path[i][1][1]*50) ,55 +(path[i][1][0]*50),fill='pink')
		if input1[path[i][0][0]][path[i][0][1]] == 'X':
			canvas.create_rectangle(5 + (path[i][0][1]*50),5 +(path[i][0][0]*50),55+(path[i][0][1]*50) ,55 +(path[i][0][0]*50),fill='yellow')
		if input1[path[i][1][0]][path[i][1][1]] == 'X':
			canvas.create_rectangle(5 + (path[i][1][1]*50),5 +(path[i][1][0]*50),55+(path[i][1][1]*50) ,55 +(path[i][1][0]*50),fill='yellow')
	root.mainloop()

choice_State()