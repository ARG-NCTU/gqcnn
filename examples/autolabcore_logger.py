from autolab_core import Logger

#Logger
"""
        Build a logger. All logs will be propagated up to the root logger
        if not silenced. If log_file is provided, logs will be written out
        to that file.
        """
logger_time = Logger.get_logger("logger_time")
logger_time.info("Planning took 1 sec")
Logger.add_log_file(logger_time, 'log_time.txt')
logger_time.info("Planning took 1 sec")

logger_content = Logger.get_logger("logger_content")
logger_content.info("The output here is hello")


