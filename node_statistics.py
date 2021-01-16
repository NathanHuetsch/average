import nifty
import GASP
from GASP.segmentation import GaspFromAffinities, WatershedOnDistanceTransformFromAffinities
import numpy as np
import matplotlib.pyplot as plt
import utility

path = '/home/nhuetsch/Desktop/Data/cremi2012/crop_maskEmb_affs_cremi_val_sample_C.h5'
raw, gt, mws_seg = utility.get_cremi_images(path, True)
dice_aff = utility.get_cremi_aff(path, 'dice')
mask_avg_aff = utility.get_cremi_aff(path, 'mask_average')

dice_geometry = utility.get_dice_geometry()
mask_average_geometry = utility.get_mask_avg_geometry()

run_GASP_kwargs = {'linkage_criteria': 'average',
                   'add_cannot_link_constraints': False}


gasp_instance = GaspFromAffinities(dice_geometry ,
                                   superpixel_generator=None,
                                   run_GASP_kwargs=run_GASP_kwargs)
print('go')

raw_small, gt_small= raw[:25,:300,:300], gt[:25,:300,:300]
dice_aff_small = dice_aff[:,:25,:300,:300]
mask_avg_aff_small = mask_avg_aff[:,:25,:300,:300]

segmentation, runtime, data = gasp_instance(dice_aff_small)
segments=len(np.unique(segmentation))
NodeData = data[0]
EdgeData = data[1]



xaxis = np.arange(0,300*300*25)[:-segments]
fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=4, sharex=True,
                                    figsize=(14, 8))

ax0.plot(xaxis, NodeData[:-segments,0])
ax0.set_title('maxNodeSize')
ax0.set_xlabel('Iteration')
ax0.set_xticks([0,1000000,2000000])

ax1.plot(xaxis, NodeData[:-segments,1])
ax1.set_title('maxCostInPQ')
ax1.set_xlabel('Iteration')
ax1.set_xticks([0,1000000,2000000])

ax2.plot(xaxis, NodeData[:-segments,2])
ax2.set_title('meanNodeSize')
ax2.set_xlabel('Iteration')
ax2.set_xticks([0,1000000,2000000])

ax3.plot(xaxis, NodeData[:-segments,3])
ax3.set_title('Variance')
ax3.set_xlabel('Iteration')
ax3.set_xticks([0,1000000,2000000])

fig.suptitle('Average, False, Dice, [:25,:300,:300]')
plt.show()

print(runtime)
print('go')
gasp_instance = GaspFromAffinities(mask_average_geometry ,
                                   superpixel_generator=None,
                                   run_GASP_kwargs=run_GASP_kwargs)
segmentation, runtime, data = gasp_instance(mask_avg_aff_small)
segments=len(np.unique(segmentation))
NodeData = data[0]
EdgeData = data[1]



xaxis = np.arange(0,300*300*25)[:-segments]
fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=4, sharex=True,
                                    figsize=(14, 8))

ax0.plot(xaxis, NodeData[:-segments,0])
ax0.set_title('maxNodeSize')
ax0.set_xlabel('Iteration')
ax0.set_xticks([0,1000000,2000000])

ax1.plot(xaxis, NodeData[:-segments,1])
ax1.set_title('maxCostInPQ')
ax1.set_xlabel('Iteration')
ax1.set_xticks([0,1000000,2000000])

ax2.plot(xaxis, NodeData[:-segments,2])
ax2.set_title('meanNodeSize')
ax2.set_xlabel('Iteration')
ax2.set_xticks([0,1000000,2000000])

ax3.plot(xaxis, NodeData[:-segments,3])
ax3.set_title('Variance')
ax3.set_xlabel('Iteration')
ax3.set_xticks([0,1000000,2000000])

fig.suptitle('Average, False, Mask_Avg, [:25,:300,:300]')
plt.show()

print(runtime)