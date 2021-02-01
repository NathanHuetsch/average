import numpy as np
import matplotlib.pyplot as plt
import utility
import matplotlib
matplotlib.use('module://backend_interagg')

# read in data sets
path = '/home/nhuetsch/Desktop/Data/cremi2012/crop_maskEmb_affs_cremi_val_sample_C.h5'
raw, gt, mws_seg = utility.get_cremi_images(path, True)
dice_aff = utility.get_cremi_aff(path, 'dice')
mask_avg_aff = utility.get_cremi_aff(path, 'mask_average')

# read in geometries
dice_geometry = utility.get_dice_geometry()
mask_avg_geometry = utility.get_mask_avg_geometry()

z1, z2, x1, x2, y1, y2 = utility.get_subset(5, 150, 150)
raw_small = raw[z1:z2, x1:x2, y1:y2]
gt_small = gt[z1:z2, x1:x2, y1:y2]
dice_aff_small = dice_aff[:, z1:z2, x1:x2, y1:y2]
mask_avg_aff_small = mask_avg_aff[:, z1:z2, x1:x2, y1:y2]

################
### Sum, True, Dice
################

run_GASP_kwargs = {'linkage_criteria': 'sum',
                   'add_cannot_link_constraints': True}
dic_sum_True = {}
dic_sum_True['segmentation'], dic_sum_True['runtime'], dic_sum_True['nodeData'], dic_sum_True['edgeData'], _ = utility.gasp(dice_geometry, run_GASP_kwargs, dice_aff_small)

ticks = 100
add = np.zeros((ticks))
skip = np.zeros((ticks))
merge = np.zeros((ticks))

actions_done = dic_sum_True['nodeData'][0,5]
step = int(actions_done/ticks)

for i in range(ticks):
    start = i*step
    end = (i+1)*step
    actions = dic_sum_True['nodeData'][start:end, 4]
    skip[i] = len(np.where(actions == 1)[0])
    add[i] = len(np.where(actions == 2)[0])
    merge[i] = len(np.where(actions == 3)[0])

print(actions_done)
x = np.arange(ticks)
plt.scatter(x, add/step, label='AddConstraint')
plt.scatter(x, skip/step, label='Constrained')
plt.scatter(x, merge/step, label='MergeEdges')
plt.xlabel('Interval of size %i' %step)
plt.ylabel('Relative % of action taken')
plt.title('GASP Actions, SumTrue, DiceAff')
plt.legend()
plt.show()

################
### Average, True, Dice
################

run_GASP_kwargs = {'linkage_criteria': 'avg',
                   'add_cannot_link_constraints': True}
dic_avg_True = {}
dic_avg_True['segmentation'], dic_avg_True['runtime'], dic_avg_True['nodeData'], dic_avg_True['edgeData'], _ = utility.gasp(dice_geometry, run_GASP_kwargs, dice_aff_small)

ticks = 100
add = np.zeros((ticks))
skip = np.zeros((ticks))
merge = np.zeros((ticks))

actions_done = dic_avg_True['nodeData'][0,5]
step = int(actions_done/ticks)

for i in range(ticks):
    start = i*step
    end = (i+1)*step
    actions = dic_avg_True['nodeData'][start:end, 4]
    skip[i] = len(np.where(actions == 1)[0])
    add[i] = len(np.where(actions == 2)[0])
    merge[i] = len(np.where(actions == 3)[0])

print(actions_done)
x = np.arange(ticks)
plt.scatter(x, add/step, label='AddConstraint')
plt.scatter(x, skip/step, label='Constrained')
plt.scatter(x, merge/step, label='MergeEdges')
plt.xlabel('Interval of size %i' %step)
plt.ylabel('Relative % of action taken')
plt.title('GASP Actions, AvgTrue, DiceAff')
plt.legend()
plt.show()

################
### Abs_Max, True, Dice
################

run_GASP_kwargs = {'linkage_criteria': 'abs_max',
                   'add_cannot_link_constraints': True}
dic_mws_True = {}
dic_mws_True['segmentation'], dic_mws_True['runtime'], dic_mws_True['nodeData'], dic_mws_True['edgeData'], _ = utility.gasp(dice_geometry, run_GASP_kwargs, dice_aff_small)

ticks = 100
add = np.zeros((ticks))
skip = np.zeros((ticks))
merge = np.zeros((ticks))

actions_done = dic_mws_True['nodeData'][0,5]
step = int(actions_done/ticks)

for i in range(ticks):
    start = i*step
    end = (i+1)*step
    actions = dic_mws_True['nodeData'][start:end, 4]
    skip[i] = len(np.where(actions == 1)[0])
    add[i] = len(np.where(actions == 2)[0])
    merge[i] = len(np.where(actions == 3)[0])

print(actions_done)
x = np.arange(ticks)
plt.scatter(x, add/step, label='AddConstraint')
plt.scatter(x, skip/step, label='Constrained')
plt.scatter(x, merge/step, label='MergeEdges')
plt.xlabel('Interval of size %i' %step)
plt.ylabel('Relative % of action taken')
plt.title('GASP Actions, MWSTrue, DiceAff')
plt.legend()
plt.show()