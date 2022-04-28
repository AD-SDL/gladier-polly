#!/usr/bin/env python

import argparse
def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', help='dir to be watched', default='.')
    return parser.parse_args()

if __name__ == '__main__':

    args = arg_parse()

    from tools.folder_watch import FileTrigger
    from polly_client import *
    
    watcher = FileTrigger(args.dir, pattern='*.json', ClientLogic=run_poly_flow)    #pattern is not working yet
    watcher.run()
