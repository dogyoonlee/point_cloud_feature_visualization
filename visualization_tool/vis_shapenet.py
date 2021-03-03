import open3d as o3d
import numpy as np
import os


def shapenet():
    '''
        Visualization shapenet
        @ https://github.com/dogyoonlee/point_cloud_feature_visualization
    '''

    # input: B x N x (3 + 3) ; rgb value format : 0~1
    data = np.load(
        '../../feature_vis/2021-3-2-21-25/feature_Decode_Layer_4.npy')
    data = data[0][:][:]

    xyzrgb = data[:, :6]
    # xyzrgb[:, 3:] /= 255
    np.savetxt("shapenet.txt", xyzrgb)
    pcd = o3d.io.read_point_cloud("shapenet.txt", format='xyzrgb')
    # o3d.visualization.
    o3d.visualization.draw_geometries([pcd])


if __name__ == '__main__':
    shapenet()