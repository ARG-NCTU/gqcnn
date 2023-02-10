from autolab_core import CameraIntrinsics

#CameraIntrinsics
"""A set of intrinsic parameters for a camera. This class is used to project
    and deproject points.
    """
if __name__ == "__main__":
    camera_intr = CameraIntrinsics.load('/home/arg/gqcnn/data/calib/phoxi/phoxi.intr')
    print(camera_intr.frame)
    print(camera_intr.height)
    print(camera_intr.width)
    print(camera_intr.proj_matrix)
    print(camera_intr.vec)
    camera_intr_scaled = camera_intr.resize(2)
    print(camera_intr_scaled.proj_matrix)
    CameraIntrinsics.save(camera_intr, 'camera_intr.intr')
