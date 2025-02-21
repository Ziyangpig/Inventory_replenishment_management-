import numpy as np
from base_lp import solve_subproblem_1, solve_subproblem_2

def calculate_C_h_s_coefficients(w, r, h, s):
    y_coefficients = []
    #TODO: 每个n内部的list的尾部，这里可能需要补全0，使得到T-r，
    dn_coefficients = {n: [] for n in range(0, w + 1)}  # 初始化每个 dq 的系数
    
    # 对于每个 n 从 1 到 w，计算 C_h/s 关于 y 和 dq 的系数
    for n in range(0, w + 1):
        # 初始化 y 和 dq 的系数
        y_coeff = 0
        dq_coeff = {q: 0 for q in range(r, r + w )}  # 每个 dq 的系数初始化为 0
        
        # 第一项: f_n * h * (y - sum(dq))，计算关于 y 和 dq 的系数
        for t in range(r, r + n):
            y_coeff += h  # y 的系数为 h
            for q in range(r, t + 1):
                dq_coeff[q] -= h  # d_q 的系数为 -h
                
        # 第二项: -s * (y - sum(dq))，计算关于 y 和 dq 的系数
        for t in range(r + n, r + w ):
            y_coeff -= s  # y 的系数为 -s
            for q in range(r, t + 1):
                dq_coeff[q] += s  # d_q 的系数为 s
        
        # 存储每个 n 对应的 y 和 dq 的系数
        y_coefficients.append(y_coeff)
        
        dn_coefficients[n] = dq_coeff
    
    return y_coefficients, dn_coefficients


def solve_A2(r, w,T, x, K, c,h,s, delta,sigma):
    # 计算Chs关于y和d的系数
    y_coefficients, dn_coefficients = calculate_C_h_s_coefficients(w, r, h, s)
    # 这里和原论文的省略不完全一样，这里只同时省略了w，以方便两个子问题目标值的直接比较
    alpha = [c + y_coeff for y_coeff in y_coefficients]
    gamma = [K + x * y_coefficients[n] for n in range(0, w + 1)]
    beta = dn_coefficients

    
    subproblem_1_value, optimal_u = solve_subproblem_1(r, w,T, delta, sigma,alpha, beta,gamma)
    subproblem_2_value, _ = solve_subproblem_2(r, w,T, delta, sigma, beta,gamma)
    #TODO: 如果需要目标值，还需要/w
    
    # 比较两个子问题结果，返回最优的目标值和对应的 u
    if subproblem_1_value < subproblem_2_value:
        return subproblem_1_value, optimal_u
    else:
        return subproblem_2_value, 0  # 第二个子问题没有 u 对应

def solve_CBH(T, r, K, c,h ,s, x,d):
    best_solution = float('inf')
    best_w = None
    best_u = None
    best_subproblem_solution = None
    
    for w in range(1, T - r + 2):  # 枚举w的值
        
        # 求解问题 12，即 A2
        A2_solution, optimal_u = solve_A2(r, w, T, x, K, c, h, s, 
        [row[r:] for row in d['delta']], d['sigma'][r:])  # 修改这里以获取每一行的第 r 列之后的所有值
        
        if A2_solution < best_solution:
            best_solution = A2_solution
            best_w = w  # 存储最优的w
            best_u = optimal_u  # 存储最优的u
            best_subproblem_solution = A2_solution  # 存储最优解对应的子问题解
    
    return best_solution, best_w, best_u, best_subproblem_solution

if __name__ == "__main__":
    # 示例参数
    T = 10  
    r = 3   
    K = 5   
    cu = 2  
    x = 1   

    # 求解 CBH 问题
    optimal_value, optimal_w, optimal_u, optimal_subproblem_solution = solve_CBH(T, r, K, cu, x)
    print(f"最优目标值: {optimal_value}")
    print(f"最优w值: {optimal_w}")
    print(f"最优u值: {optimal_u}")
    print(f"最优解对应的子问题解: {optimal_subproblem_solution}")
