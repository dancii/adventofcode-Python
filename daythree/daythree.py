#!/usr/bin/python
triangles = open('input.txt').read().strip().split('\n')

def main():
    valid_triangles_count = 0
    for triangle in triangles:
        triangle = filter(None,triangle.split(' '))
        if triangle_inequality_theorem(triangle) == True:
            valid_triangles_count+=1
    print valid_triangles_count

def main2():
    valid_triangles_count = 0
    for x in range(0, len(triangles)-2, 3):
        a_triangle = filter(None,triangles[x].split(' '))
        b_triangle = filter(None,triangles[x+1].split(' '))
        c_triangle = filter(None,triangles[x+2].split(' '))

        first_col_triangle = []
        first_col_triangle.append(a_triangle[0])
        first_col_triangle.append(b_triangle[0])
        first_col_triangle.append(c_triangle[0])

        sec_col_triangle = []
        sec_col_triangle.append(a_triangle[1])
        sec_col_triangle.append(b_triangle[1])
        sec_col_triangle.append(c_triangle[1])

        third_col_triangle = []
        third_col_triangle.append(a_triangle[2])
        third_col_triangle.append(b_triangle[2])
        third_col_triangle.append(c_triangle[2])

        if triangle_inequality_theorem(first_col_triangle) == True:
            valid_triangles_count+=1
        if triangle_inequality_theorem(sec_col_triangle) == True:
            valid_triangles_count+=1
        if triangle_inequality_theorem(third_col_triangle) == True:
            valid_triangles_count+=1
    print(valid_triangles_count)
        # for btriangle in range(1, len(triangles)-2):
        #     for ctriangle in range(2, len(triangles)-1):

def triangle_inequality_theorem(triangle):
    passes_count = 0
    a = int(triangle[0])
    b = int(triangle[1])
    c = int(triangle[2])
    if a + b > c:
        passes_count+=1
    if a + c > b:
        passes_count+=1
    if b + c > a:
        passes_count+=1
    if passes_count == 3:
        return True
    return False

main2()
