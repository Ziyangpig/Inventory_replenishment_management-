from lookahead_heur import solve_CBH
def rolling_cycle_implementation(T, r_initial, K, c, h,s,x,d):
    # 假设 r_initial 是第一个周期的起始期
    r = r_initial  # 第一个周期的起始期
    W, U = [],[]
    while r <= T:
        # 求解当前周期的 CBH 问题
        optimal_obj,optimal_w, optimal_u,_ = solve_CBH(T, r, K, c, h,s,x,d)
        
        # 打印或存储当前周期的最优决策
        print(f"Cycle starting at period {r}: Optimal w = {optimal_w}, Optimal S = {optimal_S}")
        
        # 更新下一个周期的起始期为 r + w + 1
        r = r + optimal_w   # 下一个周期的起始期
        # TODO: 真实d 
        x = x + optimal_u - sum(d['real'][r:r+optimal_w+1]) 
        
        W.append(optimal_w)
        U.append(optimal_u)
    return W,S

if __name__ == "__main__":
    # 假设 CBH_solver 是一个已经定义好的函数，用于求解 CBH 问题
    T = 10  # 假设总周期数为 10
    r_initial = 1  # 第一个周期的起始期为 1
    K = 25  
    c = 2  
    h = 1  
    s = 6  
    x0 = 0
    d = {'real': [3, 5, 3, 4, 2, 6, 3, 3, 4, 8],
         'delta': [[1, 2, 1, 0, 0, 0, 0, 0, 0, 0],[0,0,0,1,2,1,0,0,0,0],[0,0,0,0,0,0,1,2,1,1]],
         'sigma': [15,12,20]
         }

    W,S = rolling_cycle_implementation(T, r_initial, K, c, h,s,x0,d)
