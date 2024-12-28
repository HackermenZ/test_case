# import sys
# from typing import List, Tuple

# def generate_points(xc: int, yc: int, k: int) -> List[Tuple[int, int]]:
#     points = set()
#     dx = [-1, 0, 1]
#     dy = [-1, 0, 1]
    
#     x, y = xc, yc
#     points.add((x, y))
    
#     while len(points) < k:
#         for i in range(3):
#             for j in range(3):
#                 new_x = x + dx[i]
#                 new_y = y + dy[j]
#                 if -10**9 <= new_x <= 10**9 and -10**9 <= new_y <= 10**9:
#                     points.add((new_x, new_y))
#                     if len(points) == k:
#                         return list(points)
        
#         # If we couldn't find enough points in the immediate vicinity,
#         # we'll expand our search area
#         x += 1
#         if x > 10**9:
#             x = -10**9
#             y += 1
#         if y > 10**9:
#             y = -10**9

#     return list(points)

# def main():
#     t = int(input())
#     for _ in range(t):
#         xc, yc, k = map(int, input().split())
#         points = generate_points(xc, yc, k)
#         for x, y in points:
#             print(x, y)

# if __name__ == "__main__":
#     main()
code=[1,2,3]
print(help(code.insert))