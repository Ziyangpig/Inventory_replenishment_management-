# Robust Inventory Management: A Cycle-Based Approach 算法实现
本项目复现了Robust Inventory Management: A Cycle-Based Approach中提出的算法，文章链接：https://pubsonline.informs.org/doi/10.1287/msom.2022.1168  
补充材料链接：https://doi.org/10.1287/msom.2022.1168

## 问题基本设定
- 单商品、单仓库，有限离散horizon
- 考虑lost-sales 和 backlogging两种模型，并拓展到具有提前期的情况（a positive lead time）
- 需求不确定性：box uncertainty 和 polyhedral uncertainty
- 决策每个订货周期的长度和订货量


## 算法框架
- 该文章提出了一种one-cycle heuristic + rollng implementation的方法，用于解决robust inventory management问题。
- one-cycle heuristic 减少了每次优化需要决策的整数变量的空间，并通过枚举法避免了直接求解MIP问题
- 通过demand uncertatinty的强对偶性，以及成本函数的凸性，将原问题转换为求解有限个LP问题
- 该算法在实践上具有高度可操作性，求解速率较快

## 原文章摘要
Problem definition: We study the robust formulation of an inventory model with positive fixed ordering costs, where the unfulfilled demand is either backlogged or lost, the lead time is allowed to be positive, the demand is potentially intertemporally correlated, and the information about the demand distribution is limited. Methodology/results: We propose a robust cycle-based policy that manages inventory by dividing the planning horizon into nonoverlapping inventory cycles, where an order is placed at the beginning of each cycle. Our policy selects the lengths and order quantities for all inventory cycles to minimize the worst-case total cost incurred over the planning horizon. When the uncertain demand belongs to a general polyhedral uncertainty set, the decisions in our policy can be computed by solving linear programs (LPs) for the backlogging model with any lead time and the lost-sales model with zero lead time; however, the number of LPs that need to be solved grows exponentially in the length of the planning horizon. In the special case where the uncertain demand belongs to a box uncertainty set, the decisions in our policy can be computed using a dynamic programming (DP) recursion whose complexity grows polynomially in the length of the planning horizon. We also propose a one-cycle look-ahead heuristic to handle large problem instances with a general polyhedral uncertainty set. This heuristic can be applied for both the backlogging and lost-sales models with any lead time, and it only requires solving LPs whose number grows quadratically in the length of the planning horizon. Results from extensive computational experiments clearly show that both a rolling-cycle implementation of our policy and the one-cycle look-ahead heuristic have very strong empirical performance. Managerial implications: Our robust cycle-based policy and the one-cycle look-ahead heuristic are conceptually simple and can accommodate multiple realistic features in inventory management problems. They provide a very effective approach to robust inventory management, especially in the lost-sales setting.