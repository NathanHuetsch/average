import numpy as np
import matplotlib.pyplot as plt

'''
# read in the gasp statistics from file
one = np.load('gasp_statistics_15.npz', allow_pickle=True)['dict'].item()

# get the statistics for the sum
Sum_True_Dice_Edge = one['sumTrueDiceEdge']
Sum_True_Dice_Node = one['sumTrueDiceNode']
Sum_False_Dice_Edge = one['sumFalseDiceEdge']
Sum_False_Dice_Node = one['sumFalseDiceNode']

# get the statistics for the avg
Avg_True_Dice_Edge = one['avgTrueDiceEdge']
Avg_True_Dice_Node = one['avgTrueDiceNode']
Avg_False_Dice_Edge = one['avgFalseDiceEdge']
Avg_False_Dice_Node = one['avgFalseDiceNode']

# get the statistics for the abs_max
AbsMax_True_Dice_Edge = one['abs_maxTrueDiceEdge']
AbsMax_True_Dice_Node = one['abs_maxTrueDiceNode']
AbsMax_False_Dice_Edge = one['abs_maxFalseDiceEdge']
AbsMax_False_Dice_Node = one['abs_maxFalseDiceNode']

# plot the edge weights of the resulting contraction graph
fig, axs = plt.subplots(nrows=3, ncols=2,
                                    figsize=(20, 8))
plt.subplots_adjust(hspace=0.5)

xaxis = np.arange(0, Sum_True_Dice_Edge.shape[0])
axs[0,0].scatter(xaxis, Sum_True_Dice_Edge[:, 2])
axs[0,0].set_xlabel('Edge')
axs[0,0].set_ylabel('Weight')
axs[0,0].set_ylim(-1,1)
axs[0,0].set_title('SumTrueDice', size=10)

xaxis = np.arange(0, Sum_False_Dice_Edge.shape[0])
axs[0,1].scatter(xaxis, Sum_False_Dice_Edge[:, 2])
axs[0,1].set_xlabel('Edge')
axs[0,1].set_ylabel('Weight')
axs[0,1].set_ylim(-1,1)
axs[0,1].set_title('SumFalseDice', size=10)

xaxis = np.arange(0, Avg_True_Dice_Edge.shape[0])
axs[1,0].scatter(xaxis, Avg_True_Dice_Edge[:, 2])
axs[1,0].set_xlabel('Edge')
axs[1,0].set_ylabel('Weight')
axs[1,0].set_ylim(-1,1)
axs[1,0].set_title('AvgTrueDice', size=10)

xaxis = np.arange(0, Avg_False_Dice_Edge.shape[0])
axs[1,1].scatter(xaxis, Avg_False_Dice_Edge[:, 2])
axs[1,1].set_xlabel('Edge')
axs[1,1].set_ylabel('Weight')
axs[1,1].set_ylim(-1,1)
axs[1,1].set_title('AvgFalseDice', size=10)

xaxis = np.arange(0, AbsMax_True_Dice_Edge.shape[0])
axs[2,0].scatter(xaxis, AbsMax_True_Dice_Edge[:, 2])
axs[2,0].set_xlabel('Edge')
axs[2,0].set_ylabel('Weight')
axs[2,0].set_ylim(-1,1)
axs[2,0].set_title('AbsMaxTrueDice', size=10)

xaxis = np.arange(0, AbsMax_False_Dice_Edge.shape[0])
axs[2,1].scatter(xaxis, AbsMax_False_Dice_Edge[:, 2])
axs[2,1].set_xlabel('Edge')
axs[2,1].set_ylabel('Weight')
axs[2,1].set_ylim(-1,1)
axs[2,1].set_title('AbsMaxFalseDice', size=10)

fig.suptitle('Resulting Edge Weights')
plt.show()

'''

positives_Sum_True = np.zeros((20))
positives_Sum_False = np.zeros((20))
positives_Avg_True = np.zeros((20))
positives_Avg_False = np.zeros((20))
positives_AbsMax_True = np.zeros((20))
positives_AbsMax_False = np.zeros((20))

total_Sum_True = np.zeros((20))
total_Sum_False = np.zeros((20))
total_Avg_True = np.zeros((20))
total_Avg_False = np.zeros((20))
total_AbsMax_True = np.zeros((20))
total_AbsMax_False = np.zeros((20))

meanWeight_positives_Sum_True = np.zeros((20))
meanWeight_positives_Sum_False = np.zeros((20))
meanWeight_positives_Avg_True = np.zeros((20))
meanWeight_positives_Avg_False = np.zeros((20))

weight_important_constraint_Sum_True = np.zeros((20))
weight_important_constraint_Sum_False = np.zeros((20))
weight_important_constraint_Avg_True = np.zeros((20))
weight_important_constraint_Avg_False = np.zeros((20))

aff_important_constraint_Sum_True = np.zeros((20))
aff_important_constraint_Sum_False = np.zeros((20))
aff_important_constraint_Avg_True = np.zeros((20))
aff_important_constraint_Avg_False = np.zeros((20))

for i in range(20):

    file = 'gasp_statistics_' + str(i) + '.npz'
    one = np.load(file, allow_pickle=True)['dict'].item()

    Sum_True_Dice_Edge = one['sumTrueDiceEdge']
    Sum_False_Dice_Edge = one['sumFalseDiceEdge']
    Avg_True_Dice_Edge = one['avgTrueDiceEdge']
    Avg_False_Dice_Edge = one['avgFalseDiceEdge']
    AbsMax_True_Dice_Edge = one['abs_maxTrueDiceEdge']
    AbsMax_False_Dice_Edge = one['abs_maxFalseDiceEdge']

    positives_Sum_True[i] = np.sum(Sum_True_Dice_Edge[:, 2] > 0)
    positives_Sum_False[i] = np.sum(Sum_False_Dice_Edge[:, 2] > 0)
    positives_Avg_True[i] = np.sum(Avg_True_Dice_Edge[:, 2] > 0)
    positives_Avg_False[i] = np.sum(Avg_False_Dice_Edge[:, 2] > 0)
    positives_AbsMax_True[i] = np.sum(AbsMax_True_Dice_Edge[:, 2] > 0)
    positives_AbsMax_False[i] = np.sum(AbsMax_False_Dice_Edge[:, 2] > 0)

    total_Sum_True[i] = np.sum(Sum_True_Dice_Edge.shape[0])
    total_Sum_False[i] = np.sum(Sum_False_Dice_Edge.shape[0])
    total_Avg_True[i] = np.sum(Avg_True_Dice_Edge.shape[0])
    total_Avg_False[i] = np.sum(Avg_False_Dice_Edge.shape[0])
    total_AbsMax_True[i] = np.sum(AbsMax_True_Dice_Edge.shape[0])
    total_AbsMax_False[i] = np.sum(AbsMax_False_Dice_Edge.shape[0])

    weights_positives_Sum_True = Sum_True_Dice_Edge[:,3][Sum_True_Dice_Edge[:, 2] > 0]
    weights_positives_Sum_False = Sum_False_Dice_Edge[:,3][Sum_False_Dice_Edge[:, 2] > 0]
    weights_positives_Avg_True = Avg_True_Dice_Edge[:, 3][Avg_True_Dice_Edge[:, 2] > 0]
    weights_positives_Avg_False = Avg_False_Dice_Edge[:, 3][Avg_False_Dice_Edge[:, 2] > 0]

    meanWeight_positives_Sum_True[i] = np.mean(weights_positives_Sum_True)
    meanWeight_positives_Sum_False[i] = np.mean(weights_positives_Sum_False)
    meanWeight_positives_Avg_True[i] = np.mean(weights_positives_Avg_True)
    meanWeight_positives_Avg_False[i] = np.mean(weights_positives_Avg_False)

    index_Sum_True = np.argmax(weights_positives_Sum_True)
    index_Sum_False = np.argmax(weights_positives_Sum_False)
    index_Avg_True = np.argmax(weights_positives_Avg_True)
    index_Avg_False = np.argmax(weights_positives_Avg_False)

    weight_important_constraint_Sum_True[i] = weights_positives_Sum_True[index_Sum_True]
    weight_important_constraint_Sum_False[i] = weights_positives_Sum_False[index_Sum_False]
    weight_important_constraint_Avg_True[i] = weights_positives_Avg_True[index_Avg_True]
    weight_important_constraint_Avg_False[i] = weights_positives_Avg_False[index_Avg_False]

    aff_important_constraint_Sum_True[i] = Sum_True_Dice_Edge[:,2][Sum_True_Dice_Edge[:, 2] > 0][index_Sum_True]
    aff_important_constraint_Sum_False[i] = Sum_False_Dice_Edge[:,2][Sum_False_Dice_Edge[:, 2] > 0][index_Sum_False]
    aff_important_constraint_Avg_True[i] = Avg_True_Dice_Edge[:,2][Avg_True_Dice_Edge[:, 2] > 0][index_Avg_True]
    aff_important_constraint_Avg_False[i] = Avg_False_Dice_Edge[:,2][Avg_False_Dice_Edge[:, 2] > 0][index_Avg_False]

    print(Avg_True_Dice_Edge[:,2:][Avg_True_Dice_Edge[:, 2] > 0][index_Avg_True])

plt.scatter(np.arange(20), positives_Sum_True/total_Sum_True, label='sum')
plt.scatter(np.arange(20), positives_Avg_True/total_Avg_True, label='avg')
plt.scatter(np.arange(20), positives_AbsMax_True/total_AbsMax_True, label='absMax')
plt.xticks(np.arange(20))
plt.xlabel('Experiment')
plt.ylabel('% of edges with positive weight')
plt.title('True')
plt.legend()
plt.show()

plt.scatter(np.arange(20), positives_Sum_False/total_Sum_False, label='sum')
plt.scatter(np.arange(20), positives_Avg_False/total_Avg_False, label='avg')
plt.scatter(np.arange(20), positives_AbsMax_False/total_AbsMax_False, label='absMax')
plt.xticks(np.arange(20))
plt.xlabel('Experiment')
plt.ylabel('% of edges with positive weight')
plt.title('False')
plt.legend()
plt.show()

plt.scatter(np.arange(20), total_Sum_True, label='sum')
plt.scatter(np.arange(20), total_Avg_True, label='avg')
plt.scatter(np.arange(20), total_AbsMax_True, label='absMax')
plt.xticks(np.arange(20))
plt.xlabel('Experiment')
plt.ylabel('Edges total in contracted graph')
plt.title('True')
plt.legend()
plt.show()

plt.scatter(np.arange(20), total_Sum_False, label='sum')
plt.scatter(np.arange(20), total_Avg_False, label='avg')
plt.scatter(np.arange(20), total_AbsMax_False, label='absMax')
plt.xticks(np.arange(20))
plt.xlabel('Experiment')
plt.ylabel('Edges total in contracted graph')
plt.title('False')
plt.legend()
plt.show()

plt.scatter(np.arange(20), meanWeight_positives_Sum_True, label='sum')
plt.scatter(np.arange(20), meanWeight_positives_Avg_True, label='avg')
plt.xticks(np.arange(20))
plt.xlabel('Experiment')
plt.ylabel('Mean weight of positive Edges')
plt.title('True')
plt.legend()
plt.show()

plt.scatter(np.arange(20), meanWeight_positives_Sum_False, label='sum')
plt.scatter(np.arange(20), meanWeight_positives_Avg_False, label='avg')
plt.xticks(np.arange(20))
plt.xlabel('Experiment')
plt.ylabel('Mean weight of positive Edges')
plt.title('False')
plt.legend()
plt.show()

plt.scatter(np.arange(20), weight_important_constraint_Sum_True, label='sum')
plt.scatter(np.arange(20), weight_important_constraint_Avg_True, label='avg')
plt.xticks(np.arange(20))
plt.xlabel('Experiment')
plt.ylabel('Weight off important constraint')
plt.title('True')
plt.legend()
plt.show()

plt.scatter(np.arange(20), weight_important_constraint_Sum_False, label='sum')
plt.scatter(np.arange(20), weight_important_constraint_Avg_False, label='avg')
plt.xticks(np.arange(20))
plt.xlabel('Experiment')
plt.ylabel('Weight off important constraint')
plt.title('False')
plt.legend()
plt.show()

plt.scatter(np.arange(20), aff_important_constraint_Sum_True, label='sum')
plt.scatter(np.arange(20), aff_important_constraint_Avg_True, label='avg')
plt.xticks(np.arange(20))
plt.xlabel('Experiment')
plt.ylabel('Affinity off important constraint')
plt.title('True')
plt.legend()
plt.ylim((0,1))
plt.show()

plt.scatter(np.arange(20), aff_important_constraint_Sum_False, label='sum')
plt.scatter(np.arange(20), aff_important_constraint_Avg_False, label='avg')
plt.xticks(np.arange(20))
plt.xlabel('Experiment')
plt.ylabel('Affinity off important constraint')
plt.title('False')
plt.legend()
plt.show()







'''
print("Positive Edges:")
print('Sum_True: ', positives_Sum_True)
print('Sum_False: ', positives_Sum_False)
print('Avg_True: ', positives_Avg_True)
print('Avg_False: ', positives_Avg_False)
print('AbsMax_True: ', positives_AbsMax_True)
print('AbsMax_False: ', positives_AbsMax_False)
'''