import datetime
import time
def log_gen(inp=None):
    lg_dt=str(datetime.datetime.now())
    try :
        with (open('log_cache.dat', 'a')) as lg_file:
            lg_file.write("\n"+lg_dt+f"--------> input={inp}")
        return(True)
    except FileExistsError() as e:
        with (open('log_cache.dat', 'w')) as lg_file:
            lg_file.write("\n"+lg_dt+f"--------> input={inp}")
        time.sleep(2)
        return(True)