import os
import sys
import logging 

logging_str = "[%(asctime)s:%(levelname)s:%(module)s:%(message)s]" #logging string
#whenever we will log information, this information will be stored, time,label,module,message

log_dir = "logs" #a directory for storing the logs.
log_filepath = os.path.join(log_dir,"running_log.log")
os.makedirs(log_dir,exist_ok = True)

logging.basicConfig(
    level = logging.INFO,
    format= logging_str,
    handlers= [
        logging.FileHandler(log_filepath), #for showing in file.
        logging.StreamHandler(sys.stdout) #for showing in terminal.
    ]

)

logger = logging.getLogger("TextSummarisationLogger")