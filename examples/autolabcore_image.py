import argparse
import numpy as np
from autolab_core import (BinaryImage,ColorImage, DepthImage, RgbdImage)

##test code###
#python3  examples/autolabcore_image.py --depth_image data/examples/clutter/phoxi/dex-net_4.0/depth_0.npy --segmask data/examples/clutter/phoxi/dex-net_4.0/segmask_0.png


if __name__ == "__main__":
    # Parse args.
    parser = argparse.ArgumentParser(
        description="Run a testing on an example image")
    parser.add_argument("--segmask",
                    type=str,
                    default=None,
                    help="path to an optional segmask to use")
    parser.add_argument(
        "--depth_image",
        type=str,
        default=None,
        help="path to a test depth image stored as a .npy file")

    args = parser.parse_args()
    segmask_filename = args.segmask
    depth_im_filename = args.depth_image


#BinaryImage
"""A binary image in which individual pixels are either black or white (0 or BINARY_IM_MAX_VAL)."""
"""Parameters
        ----------
        data : :obj:`numpy.ndarray`
            An array of data with which to make the image. The first dimension
            of the data should index rows, the second columns, and the third
            individual pixel elements (only one channel, all uint8).
            The data array will be thresholded and will end up only containing
            elements that are BINARY_IM_MAX_VAL or 0.
        threshold : int
            A threshold value. Any value in the data array greater than
            threshold will be set to BINARY_IM_MAX_VAL, and all others will be
            set to 0.
        frame : :obj:`str`
            A string representing the frame of reference in which this image
            lies.
"""
segmask = BinaryImage.open(segmask_filename)
print("@@@@@@@@@@@@@@@@@@@binary_open@@@@@@@@@@@@@@@@@@@")
print(segmask.data)

segmask_rize = segmask.resize(5)
print("@@@@@@@@@@@@@@@@@@@binary_resize@@@@@@@@@@@@@@@@@@@")
print(segmask_rize .data)

segmask_prune_contours = segmask.prune_contours(area_thresh=1000.0, dist_thresh=20, preserve_topology=True)
print("@@@@@@@@@@@@@@@@@@@segmask_prune_contours @@@@@@@@@@@@@@@@@@@")
print(segmask_prune_contours.data)


#DepthImage
"""A depth image in which individual pixels have a single floating-point depth channel."""
"""       Parameters
        ----------
        data : :obj:`numpy.ndarray`
            An array of data with which to make the image. The first dimension
            of the data should index rows, the second columns, and the third
            individual pixel elements (depths as floating point numbers).
        frame : :obj:`str`
            A string representing the frame of reference in which this image
            lies.
"""
depth_data = np.load(depth_im_filename)
frame = 'phoxi'

depth_im = DepthImage(depth_data, frame=frame)
print("@@@@@@@@@@@@@@@@@@@depth_im@@@@@@@@@@@@@@@@@@@")
print(depth_im.data)

valid_px_mask = depth_im.invalid_pixel_mask().inverse()
print("@@@@@@@@@@@@@@@@@@@valid_px_mask@@@@@@@@@@@@@@@@@@@")
print(valid_px_mask .data)

segmask = segmask.mask_binary(valid_px_mask)
print("@@@@@@@@@@@@@@@@@@@mask_binary@@@@@@@@@@@@@@@@@@@")
print(segmask.data)

combine_with_depth = depth_im.combine_with(depth_im)
print("@@@@@@@@@@@@@@@@@@@combine_with_depth@@@@@@@@@@@@@@@@@@@")
print(combine_with_depth.data)

depth_im_threshold = depth_im.threshold(0.0,100.0)
print("@@@@@@@@@@@@@@@@@@@depth_im_threshold@@@@@@@@@@@@@@@@@@@")
print(depth_im_threshold.data)

depth_im_to_binary = depth_im.to_binary(0.0)
print("@@@@@@@@@@@@@@@@@@@depth_im_to_binary@@@@@@@@@@@@@@@@@@@")
print(depth_im_to_binary.data)

depth_im_to_color= depth_im.to_color(False)
print("@@@@@@@@@@@@@@@@@@@depth_im_to_color@@@@@@@@@@@@@@@@@@@")
print(depth_im_to_color.data)


#ColorImage
"""An RGB color image."""
"""Parameters
        ----------
        data : :obj:`numpy.ndarray`
            An array of data with which to make the image. The first dimension
            of the data should index rows, the second columns, and the third
            individual pixel elements (i.e. R,G,B values). Alternatively, the
            image may have a single channel, in which case it is interpreted as
            greyscale.
        frame : :obj:`str`
            A string representing the frame of reference in which this image
            lies.
        encoding : :obj:`str`
            Either rgb8 or bgr8, depending on the channel storage mode
"""
color_im = ColorImage(np.zeros([depth_im.height, depth_im.width,3]).astype(np.uint8),frame=frame)
print("@@@@@@@@@@@@@@@@@@@color_im @@@@@@@@@@@@@@@@@@@")
print(color_im.data)

color_resize = color_im.resize(5)
print("@@@@@@@@@@@@@@@@@@@color_resize @@@@@@@@@@@@@@@@@@@")
print(color_resize.data)



#RgbdImage
"""An image containing a red, green, blue, and depth channel."""
"""       Parameters
        ----------
        data : :obj:`numpy.ndarray`
            An array of data with which to make the image. The first dimension
            of the data should index rows, the second columns, and the third
            individual pixel elements (four channels, all float).
            The first three channels should be the red, greed, and blue
            channels which must be in the range (0, BINARY_IM_MAX_VAL).
            The fourth channel should be the depth channel.
        frame : :obj:`str`
            A string representing the frame of reference in which this image
            lies.
        Raises
        ------
"""
rgbd_im = RgbdImage.from_color_and_depth(color_im, depth_im)
print("@@@@@@@@@@@@@@@@@@@rgbd_im@@@@@@@@@@@@@@@@@@@")
print (rgbd_im.data)

rgbd_color = rgbd_im.color
print("@@@@@@@@@@@@@@@@@@@rgbd_color@@@@@@@@@@@@@@@@@@@")
print(rgbd_color.data)

rgbd_depth = rgbd_im.depth
print("@@@@@@@@@@@@@@@@@@@rgbd_depth@@@@@@@@@@@@@@@@@@")
print(rgbd_depth.data)

rgbd_resize = rgbd_im.resize(10)
print("@@@@@@@@@@@@@@@@@@@rgbd_resize@@@@@@@@@@@@@@@@@@@")
print(rgbd_resize.data)

rgbd_crop = rgbd_im.crop(5,5)
print("@@@@@@@@@@@@@@@@@@@rgbd_crop@@@@@@@@@@@@@@@@@@@")
print(rgbd_crop.data)

