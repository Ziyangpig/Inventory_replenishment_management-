import gurobipy as gp
from gurobipy import GRB
from gurobipy import quicksum
def solve_subproblem_1(r, w,T, delta, sigma,alpha, beta,gamma):
    """
    delta:p*T-r+1
    sigma:p
    约束中的max原问题：变量d个数为T-r+1，约束数量每个n对应p
    则对偶问题：变量每个vn均有p个，约束数量为T-r+1，只是beta长度不够的后面几个补全为0，
    """
    p = len(sigma)
    model = gp.Model("subproblem1")
    z = model.addVar(name="z")
    u = model.addVar(lb=0,name="u")
    v = {} 
    for n in range(w+1):
        v[n] = [model.addVar(lb=0,name=f"v_{i}") for i in range( p)]
    
    model.setObjective(z, GRB.MINIMIZE)
    # 添加其他必要的约束
    for n in range(w+1):
        model.addConstr(z >= gamma[n] + alpha[n]*u +
                        quicksum(sigma[i]*v[n][i] for i in range(p)))
                        
        #TODO: 对偶约束 

        # 补全0
        right_side_values = [beta[n][i+r] if i < w else 0 for i in range(T-r+1)]

        # 添加约束
        for i in range(T-r+1):
            model.addConstr(quicksum(delta[j][i] * v[n][j]for j in range(p))  
                             == right_side_values[i])

    model.optimize()
    optimal_u = u.getAttr("x")
    optimal_z = z.getAttr("x")
    return optimal_z, optimal_u
def solve_subproblem_2(r, w,T, delta, sigma, beta,gamma):
    """
    等价于1，将u替换成0即可
    """
    p = len(sigma)
    model = gp.Model("subproblem2")
    z = model.addVar(name="z")

    v = {} 
    for n in range(w+1):
        v[n] = [model.addVar(lb=0,name=f"v_{i}") for i in range( p)]
    
    model.setObjective(z, GRB.MINIMIZE)
    # 添加其他必要的约束
    for n in range(w+1):
        model.addConstr(z >= gamma[n] +
                        quicksum(sigma[i]*v[n][i] for i in range(p)))
                        
        #TODO: 对偶约束 

        # 补全0
        right_side_values = [beta[n][i+r] if i < w else 0 for i in range(T-r+1)]

        # 添加约束
        for i in range(T-r+1):
            model.addConstr(quicksum(delta[j][i] * v[n][j]for j in range(p))  
                             == right_side_values[i])

    model.optimize()
    optimal_z = z.getAttr("x")
    return optimal_z, 0