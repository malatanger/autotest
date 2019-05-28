# coding:utf-8
import logging
import time
from config import log_path


class Log(object):

    def __init__(self):
        self.log_path = log_path

    def __mylog(self, level, mesg):
        now = time.strftime('%Y-%m-%d')
        logname = self.log_path + now + '.txt'
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        fh = logging.FileHandler(logname, mode='a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(ch)
        if level == "debug":
            logging.debug(mesg)
        elif level == "info":
            logging.info(mesg)
        elif level == "warning":
            logging.warning(mesg)
        elif level == "error":
            logging.error(mesg)
        logger.removeHandler(ch)
        logger.removeHandler(fh)
        fh.close()

    def info(self, mesg):
        self.__mylog("info", mesg)

    def debug(self, mesg):
        self.__mylog("debug", mesg)

    def warning(self, mesg):
        self.__mylog("warning", mesg)

    def error(self, mesg):
        self.__mylog("error", mesg)

# if __name__ == "__main__":
#     L = Log()
#     L.info("sdfasd")
#     L.error("3334242")
#     L.warning("1123332221")
