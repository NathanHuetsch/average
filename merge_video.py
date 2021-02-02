import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import utility
import matplotlib
# matplotlib.use('module://backend_interagg')

data_folder = '/home/nhuetsch/Desktop/Data/average/'
number_of_experiments = 3
paths_of_experiments = []
for i in range(number_of_experiments):
    path = data_folder + 'gasp_statistics_' + str(i) + '.npz'
    paths_of_experiments.append(path)

for path in paths_of_experiments:
    dict = one = np.load(path, allow_pickle=True)['dict'].item()


nodeOne = dict['avgTrueDiceAction'][:,0]
nodeTwo = dict['avgTrueDiceAction'][:,1]
status = dict['avgTrueDiceAction'][:,2]
priority = dict['avgTrueDiceAction'][:,3]
action = dict['avgTrueDiceAction'][:,4]
segmentation = dict['avgTrueDiceSegmentation'].reshape((10,250,250))

moves = len(nodeOne)
frames = 200
movesPerFrame = int(moves/frames)

img_skips = []
imglist_skips = []
img_constraints = []
imglist_constraints = []
img_merges = []
imglist_merges = []

skips = np.zeros((10 * 250 * 250))
constraints = np.zeros((10 * 250 * 250))
merges = np.zeros((10 * 250 * 250))

for i in range(frames):

    low  = i*movesPerFrame
    high = (i+1)*movesPerFrame

    for j in range(movesPerFrame):

        n = low + j
        one = int(nodeOne[n])
        two = int(nodeTwo[n])
        if action[n] == 1:
            skips[one] = 1
            skips[two] = 1
        if action[n] == 2:
            constraints[one] = 2
            constraints[two] = 2
        if action[n] == 3:
            merges[one] = 3
            merges[two] = 3

    img_skips.append(skips.copy().reshape((10,250,250)))
    img_constraints.append(constraints.copy().reshape((10,250,250)))
    img_merges.append(merges.copy().reshape((10,250,250)))

fig = plt.figure(1, constrained_layout = True)
fig.patch.set_facecolor('black')
fig.set_size_inches(4.8, 4.8)
plt.axis("off")
for i in range(frames):
    imglist_skips.append([plt.imshow(img_skips[i][0]),])
skips_ani = animation.ArtistAnimation(
        fig, imglist_skips, interval=300, repeat_delay=3000, blit=True)
skips_ani.save('videos/skips20.gif')
del fig

fig = plt.figure(2, constrained_layout = True)
fig.patch.set_facecolor('black')
fig.set_size_inches(4.8, 4.8)
plt.axis("off")
for i in range(frames):
    imglist_constraints.append([plt.imshow(img_constraints[i][0]),])
constraints_ani = animation.ArtistAnimation(
        fig, imglist_constraints, interval=300, repeat_delay=3000, blit=True)
constraints_ani.save('videos/constraints20.gif')
del fig

fig = plt.figure(3, constrained_layout = True)
fig.patch.set_facecolor('black')
fig.set_size_inches(4.8, 4.8)
plt.axis("off")
for i in range(frames):
    imglist_merges.append([plt.imshow(img_merges[i][0]),])
    path = 'merge_images20/' + str(i) + '.png'
    plt.imsave(path, img_merges[i][7])
merges_ani = animation.ArtistAnimation(
        fig, imglist_merges, interval=300, repeat_delay=3000, blit=True)
merges_ani.save('videos/merges20.gif')

'''
plt.imshow(img_skips[-1][0])
plt.show()
plt.imshow(img_constraints[-1][0])
plt.show()
plt.imshow(img_merges[-1][0])
plt.show()
plt.imshow(segmentation[0])
plt.show()
'''