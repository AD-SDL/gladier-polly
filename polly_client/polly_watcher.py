#!/usr/bin/env python

##Basic Python import's
import argparse

def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', help='dir to be watched', default='.')
    return parser.parse_args()

if __name__ == '__main__':

    args = arg_parse()

    from tools.folder_watch import FileTrigger
    from polly_client import run_poly_flow

    #FileTrigger(args.dir,ClientLogic=run_poly_flow)    
    watcher = FileTrigger(args.dir)
    watcher.run()
    