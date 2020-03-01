# TODO: Create a thread that mines monero 
# TODO: Figure out how to make a Python library that you can use pip to install on your fopd python virtual environment
# TODO: Use demo3 to run the thread
# TODO: Make a test strap that can run this thread.

def start(app_state, args, barrier):

    logger.setLevel(args['log_level'])
    logger.info('starting crypto-miner thread')

    while not app_state['stop']:

      sleep(1)

   logger.info('exiting climate controller thread')

