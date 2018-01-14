import xlrd, os
import re
import time
import logging

#logger
logger_name = "logloglog"
logger = logging.getLogger(logger_name)
logger.setLevel(logging.INFO) 
#create file handler
log_path = "./apilog"
fh = logging.FileHandler(log_path)
fh.setLevel(logging.INFO)
       
#create formatter
fmt = "%(asctime) - 15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
datefmt = "%a %d %b %Y %H:%M:%S"
formatter = logging.Formatter(fmt, datefmt)
      
#add handler and formatter to logger
fh.setFormatter(formatter)
logger.addHandler(fh)

def read_log_name():
    filename = './log/log_name'
    with open(filename) as file_object:
        lines = file_object.read().splitlines()
        return lines

def inside_log(logname, device_id):
    api_logname = './log/' + logname

    try:
        with open(api_logname) as file_object:
            line = file_object.readlines()
             
            linenum = 1
            for l in line:
                obj = re.search(device_id, l)
                if obj :
                    logger.info("device_id (%s) , logName(%s), linenum %d", device_id, api_logname, linenum)
                linenum += 1
    except:
        pass

if(__name__ == '__main__'):
    dir_url = os.path.abspath('.')
    url = os.path.join(dir_url, 'un.xls')
    
    data = xlrd.open_workbook(url)
    
    table = data.sheets()[0]
    
    nrows = table.nrows
    ncols = table.ncols
    str1 = ''
    
    for i in range(1, nrows):
        row_data = table.row_values(i)
        device_id = row_data[1]

        ids = read_log_name()
        for name in ids:
            inside_log(name, device_id)
        
        logger.info("===============================================")
        #assert(0)
