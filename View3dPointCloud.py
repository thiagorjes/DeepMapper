
import open3d as o3d
import matplotlib.pyplot as plt
import deep_mapper as dm
import cv2


if __name__ == "__main__":

    # img = cv2.imread("test_imgs/classroom__rgb_00283.jpg")
    # dm.initialize('nyu')
    # dm.inferenceDepth(img)
    
    color_raw = o3d.io.read_image("test_imgs/classroom__rgb_00283.jpg")
    depth_raw = o3d.io.read_image("/tmp/output2.png")
    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
        color_raw, depth_raw, depth_scale=256000)
    print(rgbd_image)

    plt.subplot(1, 2, 1)
    plt.title('Redwood grayscale image')
    plt.imshow(rgbd_image.color)
    plt.subplot(1, 2, 2)
    plt.title('Redwood depth image')
    plt.imshow(rgbd_image.depth)
    plt.show()

    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
        rgbd_image,
        o3d.camera.PinholeCameraIntrinsic(
            o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault))
    # Flip it, otherwise the pointcloud will be upside down
    pcd.transform([[1, 2, 0, 0], [2, -1.333, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    o3d.visualization.draw_geometries([pcd])
