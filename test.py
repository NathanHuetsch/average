import nifty
import GASP

import numpy as np
import matplotlib.pyplot as plt

import h5py

path = '/home/nhuetsch/Desktop/Data/cremi2012/crop_maskEmb_affs_cremi_val_sample_C.h5'

f = h5py.File(path, 'r')
print(f.keys())
GT = f['GT']
raw = f['raw']
aff_dice = f['affinities_dice']
aff_mask_average = f['affinities_mask_average']
seg_MWS = f['segmentation_MWS']
print(GT.shape)
print(raw.shape)
print(seg_MWS.shape)
print(aff_dice.shape)
print(aff_mask_average.shape)

dice_geometry = np.array([
  [-1, 0, 0],
  [0, -1, 0],
  [0, 0, -1],
  [0, -4, 0],
  [0, 0, -4],
  [0, -4, -4],
  [0, 4, -4],
  [-1, -4, 0],
  [-1, 0, -4],
  [-1, -4, -4],
  [-1, 4, -4],
  [-2, 0, 0],
  [-3, 0, 0],
  [-4, 0, 0],
  [0, -8, -8],
  [0, 8, -8],
  [0, -12, 0],
  [0, 0, -12]
])

mask_average_geometry = np.array([
  [-1, 0, 0],
  [0, -1, 0],
  [0, 0, -1],
  [0, -4, 0],
  [0, 0, -4],
  [0, -4, -4],
  [0, 4, -4],
  [-1, -4, 0],
  [-1, 0, -4],
  [-1, -4, -4],
  [-1, 4, -4],
  [-2, 0, 0],
  [0, -8, -8],
  [0, 8, -8],
  [0, -12, 0],
  [0, 0, -12]
])
