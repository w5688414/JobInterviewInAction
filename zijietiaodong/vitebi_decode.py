import numpy as np


# def vitebi_decode(hmm_paramter, obs_idx_seq):
#     #取出HMM模型的三个参数
#     A, B , L = hmm_paramter
#     #状态的总个数
#     N = A.shape[0]
#     #获取观测序列的长度
#     T = len(obs_idx_seq)
    
#     #定义[N*T]的矩阵P，用来表示t时刻状态为i的最大概率
#     P = np.zeros((N, T))
#     #定义[N*T]的矩阵D，用来表示t时刻状态为i取得最大概率时t-1时刻的状态
#     D = np.zeros((N, T), dtype=int)
#     #初始化P,D在t=0时刻所对应的概率值和初状态
#     for i in range(N):
#         P[i][0] = L[i] * (B[i, obs_idx_seq[0]])
#         D[i][0] = -1
        
#     #接下来通过一个三层循环对P,D里面的元素进行赋值操作
#     for i in range(1, T):
#         obs_value = obs_idx_seq[i]
#         for j in range(N):
#             pro_list = []
#             for k in range(N):
#                 pro_list.append(P[k, i-1] * A[k, j] * B[j, obs_value])
#             max_value = max(pro_list)
#             max_idx = pro_list.index(max_value)
#             P[j, i] = max_value
#             D[j, i] = max_idx
            
#     #获取P最后一个时刻的最大值，即为最大概率
#     final_max_value = np.max(P, axis=0)[-1]
#     final_max_idx =np.argmax(P, axis=0)[-1]
    
#     #通过finax_max_idx和D倒推出最大概率值所对应的状态序列
#     state_list = []
#     state_list.append(final_max_idx)
#     for i in range(T-1, 0, -1):
#         final_max_idx = D[final_max_idx][i]
#         state_list.append(final_max_idx)
#     final_state_list = []
#     #由于状态是从1开始的，所以要对每一个状态索引加1
#     for i in range(len(state_list) - 1, -1, -1):
#         final_state_list.append(state_list[i]+1)
# 	#print(P)
# 	#print(D)
#     return final_max_value, final_state_list
# if __name__ == "__main__":
#     A = np.array([[0.5, 0.2, 0.3],
#                   [0.3, 0.5, 0.2],
#                   [0.2, 0.3, 0.5]])
#     B = np.array([[0.5, 0.5],
#                   [0.4, 0.6],
#                   [0.7, 0.3]])
#     L = [0.2, 0.4, 0.4]
#     O = ['红', '白', '红']
#     obs_to_idx = {'红':0, '白':1}
#     obs_seq_idx = [obs_to_idx[i] for i in O]
#     max_pro, state_seq = vitebi_decode((A, B, L), obs_seq_idx)
#     print(max_pro)
#     print(state_seq)

import numpy as np
def viterbi(trainsition_probability,emission_probability,pi,obs_seq):
    #转换为矩阵进行运算
    trainsition_probability=np.array(trainsition_probability)
    emission_probability=np.array(emission_probability)
    pi=np.array(pi)
    obs_seq = [0, 2, 3]
    # 最后返回一个Row*Col的矩阵结果
    Row = np.array(trainsition_probability).shape[0]
    Col = len(obs_seq)
    #定义要返回的矩阵
    F=np.zeros((Row,Col))
    #初始状态
    F[:,0]=pi*np.transpose(emission_probability[:,obs_seq[0]])
    for t in range(1,Col):
        list_max=[]
        for n in range(Row):
            list_x=list(np.array(F[:,t-1])*np.transpose(trainsition_probability[:,n]))
            #获取最大概率
            list_p=[]
            for i in list_x:
                list_p.append(i*10000)
            list_max.append(max(list_p)/10000)
        F[:,t]=np.array(list_max)*np.transpose(emission_probability[:,obs_seq[t]])
    return F

if __name__=='__main__':
    #隐藏状态
    invisible=['Sunny','Cloud','Rainy']
    #初始状态
    pi=[0.63,0.17,0.20]
    #转移矩阵
    trainsion_probility=[[0.5,0.375,0.125],[0.25,0.125,0.625],[0.25,0.375,0.375]]
    #发射矩阵
    emission_probility=[[0.6,0.2,0.15,0.05],[0.25,0.25,0.25,0.25],[0.05,0.10,0.35,0.5]]
    #最后显示状态
    obs_seq=[0,2,3]
    #最后返回一个Row*Col的矩阵结果
    F=viterbi(trainsion_probility,emission_probility,pi,obs_seq)
    print(F)
    
