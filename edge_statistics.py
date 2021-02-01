# import nifty
# import GASP
# from GASP.segmentation import GaspFromAffinities, WatershedOnDistanceTransformFromAffinities
import numpy as np
import matplotlib.pyplot as plt
import utility
from segmfriends.utils.various import cremi_score
import matplotlib
matplotlib.use('module://backend_interagg')

# read in data sets
path = '/home/nhuetsch/Desktop/Data/cremi2012/crop_maskEmb_affs_cremi_val_sample_C.h5'
raw, gt, mws_seg = utility.get_cremi_images(path, True)
dice_aff = utility.get_cremi_aff(path, 'dice')
mask_avg_aff = utility.get_cremi_aff(path, 'mask_average')

# read in geometries
dice_geometry = utility.get_dice_geometry()
mask_average_geometry = utility.get_mask_avg_geometry()

z1, z2, x1, x2, y1, y2 = utility.get_subset(5, 50, 50)
raw_small = raw[z1:z2, x1:x2, y1:y2]
gt_small = gt[z1:z2, x1:x2, y1:y2]
dice_aff_small = dice_aff[:, z1:z2, x1:x2, y1:y2]
mask_avg_aff_small = mask_avg_aff[:, z1:z2, x1:x2, y1:y2]


run_GASP_kwargs = {'linkage_criteria': 'sum',
                   'add_cannot_link_constraints': True}
dic_sum_True = {}

segmentation, runtime, nodeData, edgeData,_ = utility.gasp(dice_geometry, run_GASP_kwargs, dice_aff_small)
dic_sum_True['score'] = cremi_score(gt_small, segmentation)
dic_sum_True['runtime'] = runtime

dic_sum_True['positive'] = np.where(edgeData[:, 2] > 0)[0]
dic_sum_True['lifted'] = np.where(edgeData[:, 4] != 0)[0]
dic_sum_True['constrained'] = np.where(edgeData[:, 5] != 0)[0]
dic_sum_True['positive+lifted'] = np.intersect1d(dic_sum_True['positive'], dic_sum_True['lifted'])
dic_sum_True['positive+constrained'] = np.intersect1d(dic_sum_True['constrained'], dic_sum_True['positive'])
dic_sum_True['constrained+lifted'] = np.intersect1d(dic_sum_True['constrained'], dic_sum_True['lifted'])
dic_sum_True['positive+constrained+lifted'] = np.intersect1d(
                                                dic_sum_True['positive+constrained'], dic_sum_True['lifted'])



run_GASP_kwargs = {'linkage_criteria': 'avg',
                   'add_cannot_link_constraints': True}
dic_avg_True = {}

segmentation, runtime, nodeData, edgeData, _ = utility.gasp(dice_geometry, run_GASP_kwargs, dice_aff_small)
dic_avg_True['score'] = cremi_score(gt_small, segmentation)
dic_avg_True['runtime'] = runtime

dic_avg_True['positive'] = np.where(edgeData[:, 2] > 0)[0]
dic_avg_True['lifted'] = np.where(edgeData[:, 4] != 0)[0]
dic_avg_True['constrained'] = np.where(edgeData[:, 5] != 0)[0]
dic_avg_True['positive+lifted'] = np.intersect1d(dic_avg_True['positive'], dic_avg_True['lifted'])
dic_avg_True['positive+constrained'] = np.intersect1d(dic_avg_True['constrained'], dic_avg_True['positive'])
dic_avg_True['constrained+lifted'] = np.intersect1d(dic_avg_True['constrained'], dic_avg_True['lifted'])
dic_avg_True['positive+constrained+lifted'] = np.intersect1d(
                                                dic_avg_True['positive+constrained'], dic_avg_True['lifted'])

'''
print('---------------------------------------------------')
print('sum')
for key in dic_sum_True.keys():
    if key == 'score' or key == 'runtime':
        continue
    print(key, len(dic_sum_True[key]))
print('---------------------------------------------------')
print('avg')
for key in dic_avg_True.keys():
    if key == 'score' or key == 'runtime':
        continue
    print(key, len(dic_avg_True[key]))
print('---------------------------------------------------')
print('Cremi Scores')
print('Sum, True', dic_sum_True['score'])
print('Avg, True', dic_avg_True['score'])
print('---------------------------------------------------')
'''

wrongs = edgeData[dic_avg_True['positive+constrained']]
#print(wrongs)
for edge in wrongs:
    print(edge[0])
    print(edge[1])
    print(np.sum(segmentation==edge[0]))
    print(np.sum(segmentation==edge[1]))
    print(np.where(segmentation==edge[0]))
    break
# Run GASPS
'''
fig, axs = plt.subplots(nrows=2, ncols=2,
                                    figsize=(16, 8))

run_GASP_kwargs = {'linkage_criteria': 'sum',
                   'add_cannot_link_constraints': False}

segmentation, runtime, nodeData, edgeData = utility.gasp(dice_geometry, run_GASP_kwargs, dice_aff_small)

nodesFinal = len(np.unique(segmentation))
edgesFinal = edgeData.shape[0]
positives_sum_False = np.sum(edgeData[:, 2] > 0)


xaxis = np.arange(0, edgesFinal)
axs[0,0].scatter(xaxis, edgeData[:, 2])
axs[0,0].set_xlabel('Edge')
axs[0,0].set_ylabel('Weight')
axs[0,0].set_ylim(-1,1)
axs[0,0].set_title(run_GASP_kwargs, size=10)

run_GASP_kwargs = {'linkage_criteria': 'sum',
                   'add_cannot_link_constraints': True}

segmentation, runtime, nodeData, edgeData = utility.gasp(dice_geometry, run_GASP_kwargs, dice_aff_small)

nodesFinal = len(np.unique(segmentation))
edgesFinal = edgeData.shape[0]
positives_sum_True = np.sum(edgeData[:, 2] > 0)

xaxis = np.arange(0, edgesFinal)
axs[0,1].scatter(xaxis, edgeData[:, 2])
axs[0,1].set_xlabel('Edge')
axs[0,1].set_ylabel('Weight')
axs[0,1].set_ylim(-1,1)
axs[0,1].set_title(run_GASP_kwargs, size=10)

run_GASP_kwargs = {'linkage_criteria': 'average',
                   'add_cannot_link_constraints': False}

segmentation, runtime, nodeData, edgeData = utility.gasp(dice_geometry, run_GASP_kwargs, dice_aff_small)

nodesFinal = len(np.unique(segmentation))
edgesFinal = edgeData.shape[0]
positives_avg_False = np.sum(edgeData[:, 2] > 0)

xaxis = np.arange(0, edgesFinal)
axs[1,0].scatter(xaxis, edgeData[:, 2])
axs[1,0].set_xlabel('Edge')
axs[1,0].set_ylabel('Weight')
axs[1,0].set_title(run_GASP_kwargs, size=10)

run_GASP_kwargs = {'linkage_criteria': 'average',
                   'add_cannot_link_constraints': True}

segmentation, runtime, nodeData, edgeData = utility.gasp(dice_geometry, run_GASP_kwargs, dice_aff_small)

nodesFinal = len(np.unique(segmentation))
edgesFinal = edgeData.shape[0]
positives_avg_True = np.sum(edgeData[:, 2] > 0)

xaxis = np.arange(0, edgesFinal)
axs[1,1].scatter(xaxis, edgeData[:, 2])
axs[1,1].set_xlabel('Edge')
axs[1,1].set_ylabel('Weight')
axs[1,1].set_title(run_GASP_kwargs, size=10)

fig.suptitle('dice affinity, dataset size [15,300,300]')
plt.show()


print('positives_sum_False: ', positives_sum_False)
print('positives_sum_True: ', positives_sum_True)
print('positives_avg_False: ', positives_avg_False)
print('positives_avg_True: ', positives_avg_True)

'''
'''
run_GASP_kwargs = {'linkage_criteria': 'sum',
                   'add_cannot_link_constraints': False}

segmentation, runtime, nodeData, edgeData = utility.gasp(dice_geometry, run_GASP_kwargs, dice_aff_small)
score_sum_False = cremi_score(gt_small, segmentation)

ind = np.where(edgeData[:,2]>0)[0]
lifted_sum_False = len(ind)
assert(edgeData[:,4][ind].all() == np.ones((lifted_sum_False)).all())


run_GASP_kwargs = {'linkage_criteria': 'avg',
                   'add_cannot_link_constraints': False}

segmentation, runtime, nodeData, edgeData = utility.gasp(dice_geometry, run_GASP_kwargs, dice_aff_small)
score_avg_False = cremi_score(gt_small, segmentation)

ind = np.where(edgeData[:,2]>0)[0]
lifted_avg_False = len(ind)
assert(edgeData[:,4][ind].all() == np.ones((lifted_avg_False)).all())
'''