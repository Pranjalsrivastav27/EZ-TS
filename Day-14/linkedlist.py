# # class Node:
# #     def __init__(self,data):
# #         self.data=data
# #         self.next=None
# # class Linkedlist:
# #     def __init__(self):
# #         self.start=None
# #         self.temp=None
# #     def create_list(self):
# #         for i in range(10):
# #             new_node=Node(i)
# #             if self.start is None:
# #                 self.start=new_node
# #                 self.temp=self.start
# #             else:
# #                 self.temp.next=new_node
# #                 temp=temp.next
# #         return self.start
# #     def print_list(self):
# #         self.temp=self.start
# #         while self.temp:
# #             print(self.temp.data,end=" ")
# #             self.temp=self.temp.next 
# #         print()
# # obj=Linkedlist()
# # start=obj.create_list()
# # obj.print_list()
# # obj.print_list()



        
# # A recursive solution for subset sum
# # problem


# # Returns true if there is a subset
# # of set[] with sun equal to given sum
# def isSubsetSum(set, n, sum):

# 	# Base Cases
# 	if (sum == 0):
# 		return True
# 	if (n == 0):
# 		return False

# 	# If last element is greater than
# 	# sum, then ignore it
# 	if (set[n - 1] > sum):
# 		return isSubsetSum(set, n - 1, sum)

# 	# Else, check if sum can be obtained
# 	# by any of the following
# 	# (a) including the last element
# 	# (b) excluding the last element
# 	return isSubsetSum(
# 		set, n-1, sum) or isSubsetSum(
# 		set, n-1, sum-set[n-1])


# # Driver code
# if __name__ == '__main__':
# 	set = [3, 34, 4, 12, 5, 2]
# 	sum = 9
# 	n = len(set)
# 	print(isSubsetSum(set, n, sum))

# # This code is contributed by Nikita Tiwari.

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# def fu(c):
#     d=c.split()
#     for i in d:
#         print(i,end=" ")
# v=input()
# fu(v)
# a=[1,2,3]
# for i in a:
#     b=i**3
#     print((i,b),end=" ")
a=[[1,2,3],[4,5,6]]
b=[[1,2,3],[4,5,6]]
res=[[0,0,0],
     [0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        res[i][j]=a[i][j]-b[i][j]
for i in res:
    print(i,end=" ")
    