import h5py
import numpy as np
from GASP.segmentation import GaspFromAffinities

def get_cremi_images(path, mws):

    assert type(path) == str
    assert type(mws) == bool

    f = h5py.File(path, 'r')
    gt = np.array(f['GT'])
    raw = np.array(f['raw'])
    if mws:
        mws_seg = np.array(f['segmentation_MWS'])
        return raw, gt, mws_seg
    else:
        return raw, gt


def get_cremi_aff(path, geometry):

    assert type(path) == str
    assert type(geometry) == str
    assert geometry in ["dice", "mask_average"]
    f = h5py.File(path, 'r')

    if geometry == "dice":
        return np.array(f['affinities_dice'], dtype='float32')
    else:
        return np.array(f['affinities_mask_average'], dtype='float32')


def get_dice_geometry():
    return np.array([
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

def get_mask_avg_geometry():
    return np.array([
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


def gasp(geometry, kwargs, aff):
    gasp_instance = GaspFromAffinities(geometry,
                                     superpixel_generator=None,
                                     run_GASP_kwargs=kwargs)
    segmentation, runtime, data = gasp_instance(aff)
    return segmentation, runtime, data[0], data[1], data[2]

def get_subset(z,x,y):
    start_x = np.random.randint(low=0, high=430-x)
    start_y = np.random.randint(low=0, high=480-y)
    start_z = np.random.randint(low=0, high=35-z)

    return start_z, start_z+z, start_x, start_x+x, start_y, start_y+y