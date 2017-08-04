#Author:Cairo Li
import optparse
import sys
import os
import subprocess

'''
dirname=os.path.dirname(__file__)
childdir=os.path.join(dirname,"2.txt")
print(childdir)
print(os.path.dirname(__file__))
'''

def main():
    child=os.path.join(os.path.dirname(__file__),"grepword-p-child.py")
    opts,word,args=parse_options()
    filelist=get_files(args,opts.recurse)
    files_per_process=len(filelist)
    start,end=0,files_per_process+(len(filelist)%opts.count)
    number=1

def parse_options():
    parser=optparse.OptionParser(
        usage=(
            "usage:%prog [options] word name1"
            "[name2 [...nameN]\n\n"
            "names are filenames or paths;paths only"
            "make sense with the -r option set") )

    parser.add_option("-p","--process",dest="count",default=7,
                      type="int",
                      help=("the number of child process to use(1..20)"
                            "default %default"))
    parser.add_option("-r","--recurse",dest="recurse",
                      default=False,action="store_true",
                      help="recurse into subdirectories")
    parser.add_option("-d","--debug",dest="debug",default=False,
                      action="store_true")
    opts,args=parser.parse_args()
    if len(args)==0:
        parser.error("a word and at least one path must be specified")
    elif len(args)==1:
        parser.error("at least one path must be specified")
    if(not opts.recurse and
       not any([os.path.isfile(arg) for arg in args])):
        parser.error("at least one file must be specified;or use -r")
    if not(1<=opts.count<=20):
        parser.error("process count must be 1..20")
    return opts,args[0],args[1]

def get_files(args,recurse):
    filelist=[]
    for path in args:
        if os.path.isfile(path):
            filelist.append(path)
        elif recurse:
            for root,dirs,files in os.walk(path):
                for filename in files:
                    filelist.append(os.path.join(root,filename))
    return filelist

main()

#print(os.path.join())