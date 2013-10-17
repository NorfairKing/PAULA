import os

debug               = False

# Dir settings
paula_dir           = os.getcwd()

# Pid file
pid_file            = '/tmp/paula.pid'

#Std streams
out_file            = '/tmp/paula_out'
err_file            = '/tmp/paula_err'

# Logging config
log_file            = '/tmp/paula_log'
log_format          = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
log_dateFormat      = '%Y-%m-%d %H:%M:%S'
log_maxBytes        = 10000
log_backupCount     = 5

# Seconds between check
check_timer         = 60
