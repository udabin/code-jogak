import time
import logging
import common  # 사용자 정의 로거 불러오는 모듈

log_level = logging.DEBUG

def timefn2(fn):
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        
        if log_level == logging.DEBUG:
            logger = common.get_runtime_logger()
            time_str = f"@timefn: {fn.__name__} took {t2 - t1:.4f} seconds"
            
            if logger:
                logger.info(time_str)
            else:
                print(time_str)
        
        return result
    return measure_time
