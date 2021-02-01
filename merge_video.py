import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import utility
import matplotlib
# matplotlib.use('module://backend_interagg')

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

########################

run_GASP_kwargs = {'linkage_criteria': 'avg',
                   'add_cannot_link_constraints': True}
dic_avg_True = {}
dic_avg_True['segmentation'], dic_avg_True['runtime'], \
dic_avg_True['nodeData'], dic_avg_True['edgeData'], dic_avg_True['action'] \
= utility.gasp(dice_geometry, run_GASP_kwargs, dice_aff_small)

nodeOne = dic_avg_True['action'][:,0]
nodeTwo = dic_avg_True['action'][:,1]
edge = dic_avg_True['action'][:,2]
priority = dic_avg_True['action'][:,3]
action = dic_avg_True['action'][:,4]

moves = len(nodeOne)
frames = 1000
movesPerFrame = int(moves/frames)
images = []

for i in range(frames):
    low  = i*movesPerFrame
    high = (i+1)*movesPerFrame

    nodeOne = dic_avg_True['action'][low:high, 0]
    nodeTwo = dic_avg_True['action'][low:high, 1]
    action = dic_avg_True['action'][low:high, 4]