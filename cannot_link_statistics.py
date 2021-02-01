import numpy as np
import utility
import time

# read in data sets
path = '/home/nhuetsch/Desktop/Data/cremi2012/crop_maskEmb_affs_cremi_val_sample_C.h5'
raw, gt, mws_seg = utility.get_cremi_images(path, True)
dice_aff = utility.get_cremi_aff(path, 'dice')
mask_avg_aff = utility.get_cremi_aff(path, 'mask_average')

# read in geometries
dice_geometry = utility.get_dice_geometry()
mask_average_geometry = utility.get_mask_avg_geometry()

iterations = 10

# collect statistics:
# dim0 : iteration -> Random dataset
# dim1 : linkage_criteria -> [0]:'sum' , [1]:'avg', [2]:'abs_max'
# dim2 : add_cannot_link -> [0]:True , [1]:False
# dim3 : aff_geometry -> [0]'dice , [1]:mask_avg
# dim4 : data -> [0]:nodesFinal , [1]:edgesFinal , [2]:positives (edges with positive weight in contracted graph)



for iter in range(iterations):
    start = time.time()
    z1, z2, x1, x2, y1, y2 = utility.get_subset(10, 250, 250)
    raw_small, gt_small = raw[z1:z2, x1:x2, y1:y2], gt[z1:z2, x1:x2, y1:y2]
    dice_aff_small = dice_aff[:, z1:z2, x1:x2, y1:y2]
    mask_avg_aff_small = mask_avg_aff[:, z1:z2, x1:x2, y1:y2]

    statistics = {}
    for c, linkage_criteria in enumerate(['sum', 'avg', 'abs_max']):
        for l, add_cannot_link_constraints in enumerate([True, False]):

            run_GASP_kwargs = {'linkage_criteria': linkage_criteria,
                               'add_cannot_link_constraints': add_cannot_link_constraints}

            segmentation, runtime, nodeData, edgeData, action = utility.gasp(dice_geometry, run_GASP_kwargs, dice_aff_small)

            EdgeName = linkage_criteria + str(add_cannot_link_constraints) + 'Dice' + 'Edge'
            NodeName = linkage_criteria + str(add_cannot_link_constraints) + 'Dice' + 'Node'
            ActionName = linkage_criteria + str(add_cannot_link_constraints) + 'Dice' + 'Action'
            statistics[EdgeName] = edgeData
            statistics[NodeName] = nodeData
            statistics[ActionName] = action

            segmentation, runtime, nodeData, edgeData, action = utility.gasp(mask_average_geometry, run_GASP_kwargs, mask_avg_aff_small)

            EdgeName = linkage_criteria + str(add_cannot_link_constraints) + 'Mask' + 'Edge'
            NodeName = linkage_criteria + str(add_cannot_link_constraints) + 'Mask' + 'Node'
            ActionName = linkage_criteria + str(add_cannot_link_constraints) + 'Mask' + 'Action'
            statistics[EdgeName] = edgeData
            statistics[NodeName] = nodeData
            statistics[ActionName] = action


    filename='gasp_statistics_'+str(iter)
    np.savez(filename, dict=statistics)
    end = time.time()
    print(end-start)
