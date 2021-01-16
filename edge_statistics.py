# import nifty
# import GASP
# from GASP.segmentation import GaspFromAffinities, WatershedOnDistanceTransformFromAffinities
import numpy as np
import matplotlib.pyplot as plt
import utility

# read in data sets
path = '/home/nhuetsch/Desktop/Data/cremi2012/crop_maskEmb_affs_cremi_val_sample_C.h5'
raw, gt, mws_seg = utility.get_cremi_images(path, True)
dice_aff = utility.get_cremi_aff(path, 'dice')
mask_avg_aff = utility.get_cremi_aff(path, 'mask_average')

# read in geometries
dice_geometry = utility.get_dice_geometry()
mask_average_geometry = utility.get_mask_avg_geometry()

# subset of the data
z1, z2, x1, x2, y1, y2 = utility.get_subset(15, 300, 300)
raw_small, gt_small = raw[z1:z2, x1:x2, y1:y2], gt[z1:z2, x1:x2, y1:y2]
dice_aff_small = dice_aff[:, z1:z2, x1:x2, y1:y2]
mask_avg_aff_small = mask_avg_aff[:, z1:z2, x1:x2, y1:y2]


# Run GASPS

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