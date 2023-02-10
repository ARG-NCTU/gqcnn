from autolab_core import (YamlConfig, Logger, CameraIntrinsics,
                          BinaryImage, ColorImage, DepthImage, RgbdImage)

#YamlConfig
"""Class to load a configuration file and parse it into a dictionary.
    Attributes
    ----------
    config : :obj:`dictionary`
        A dictionary that contains the contents of the configuration.
    """
config = YamlConfig("/home/arg/gqcnn/examples/../cfg/examples/gqcnn_pj.yaml")

#Logger
"""
        Build a logger. All logs will be propagated up to the root logger
        if not silenced. If log_file is provided, logs will be written out
        to that file. If global_log_file is true, log_file will be handed
        the root logger, otherwise it will only be used by this particular
        logger.
        Parameters
        ----------
        name :obj:`str`
            The name of the logger to be built.
        log_level : `int`
            The log level. See the python logging module documentation
            for possible enum values.
        log_file :obj:`str`
            The path to the log file to log to.
        global_log_file :obj:`bool`
            Whether or not to use the given log_file for this particular
            logger or for the root logger.
        silence :obj:`bool`
            Whether or not to silence this logger. If it is silenced, the
            only way to get output from this logger is through a
            non-global log file.
        Returns
        -------
        :obj:`logging.Logger`
            A custom logger.
        """
logger = Logger.get_logger("examples/policy.py")
logger.info("Planning took 1 sec")

#CameraIntrinsics
"""A set of intrinsic parameters for a camera. This class is used to project
    and deproject points.
    """
camera_intr = CameraIntrinsics.load(camera_intr_filename)
