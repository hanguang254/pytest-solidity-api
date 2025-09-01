'''
@Project ：pytest-API-Project 
@File ：Logger.py
@Author ：le
@Date ：2022/8/24 9:47 
'''
import logging
import os
import sys
import time


def creater_file(suffix=""):
    # 获取项目根目录（Logger.py 在 common 下，不管在哪执行都能定位到 根目录下）
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_dir = os.path.join(project_root, 'logout')

    if not os.path.exists(log_dir):
        os.mkdir(log_dir)

    # 时间戳
    now_time = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))

    # 拼接日志文件名
    filename = f"{now_time}_{suffix}.log" if suffix else f"{now_time}.log"
    log_file = os.path.join(log_dir, filename)

    return log_file



class Log():

    def __init__(self,name,level='DEBUG', suffix=""):
        #日志器名字
        self.__name = name
        #log的绝对路径
        self.__path = creater_file(suffix)
        #日志输入级别 默认DEBUG调试级别
        self.__level = level
        #创建日志器 传入名字
        self.__logger = logging.getLogger(self.__name)
        #输出日志级别 传入级别
        self.__logger.setLevel(self.__level)
        """
        日志等级有
        INFO：记录一切事件信息
        WARING ：记录警告
        ERROR：记录错误信息
        
        """

    def __ini_handler(self):
        # 初始化handler处理器
        self.__logger.handlers.clear()

        stream_handler = logging.StreamHandler()

        #输出到log文件中
        file_handler = logging.FileHandler(self.__path,encoding='utf-8')

        return stream_handler,file_handler


    def set_handler(self,stream_handler,file_handler,level='DEBUG'):
        """设置logger收集器"""
        #日志输出级别
        stream_handler.setLevel(level)
        #文件输出级别
        file_handler.setLevel(level)
        #将记录添加到收集器
        self.__logger.addHandler(stream_handler)
        self.__logger.addHandler(file_handler)


    def set_formatter(self,stream_handler,file_handler):
        """日志输出格式"""
        formatter = logging.Formatter('%(asctime)s-%(name)s-[line:%(lineno)d]-%(levelname)s'
                                      '-[日志信息]:%(message)s',datefmt='%a %d %b %Y %H:%M:%S')

        # 屏幕显示格式记录到收集器中
        stream_handler.setFormatter(formatter)
        # 文件收集格式记录到收集器中
        file_handler.setFormatter(formatter)

    def close_handler(self,stream_handler,file_handler):

        stream_handler.close()
        file_handler.close()

    def Logger(self):
        """构造收集器"""
        # 调用handler方法赋值给sh ，fh
        stream_handler,file_handler = self.__ini_handler()
        #调用日志级别
        self.set_handler(stream_handler,file_handler)
        #输出日志格式
        self.set_formatter(stream_handler,file_handler)

        #关闭日志
        self.close_handler(stream_handler,file_handler)

        return self.__logger
"""
使用方法：
file = os.path.basename(__file__)   #获取当前文件名字
file=os.path.basename(sys.argv[0])  #获取当前文件名字
log = Log(file)
logger = log.Logger()
logger.info('222222222222222222222')
"""


if __name__ == '__main__':
    file = os.path.basename(__file__)
    # file=os.path.basename(sys.argv[0])
    log = Log(file)
    logger = log.Logger()
    logger.info('222222222222222222222')
    logger.error('error test')
    logger.debug("调试信息")
    logger.info("普通信息")
    logger.warning("这是个警告")
    logger.error("出错了！")
    logger.critical("严重错误，程序可能无法继续！")