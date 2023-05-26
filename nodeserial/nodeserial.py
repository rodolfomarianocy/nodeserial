import argparse
from argparse import RawTextHelpFormatter
from .payload import main

def msg():
    return print("""                 _                     _       _ 
                | |                   (_)     | |
 _ __   ___   __| | ___  ___  ___ _ __ _  __ _| |
| '_ \ / _ \ / _` |/ _ \/ __|/ _ \ '__| |/ _` | |
| | | | (_) | (_| |  __/\__ \  __/ |  | | (_| | |
|_| |_|\___/ \__,_|\___||___/\___|_|  |_|\__,_|_|
    """)


def argumentos():

    parser = argparse.ArgumentParser(description=msg(),formatter_class=RawTextHelpFormatter, usage="nodeserial -l <ip> -p <port>")
    parser.add_argument('-l','--lhost', dest='lhost', action='store', type=str, help='Insert an lhost', required=True)
    parser.add_argument('-p','--lport', dest='lport', action='store', type=str, help='Insert an lport', required=True)
    parser.add_argument('-params','--params', dest='params', action='store', type=str, help='Insert an params')
    parser.add_argument('-e','--encode', dest='encode', action='store', type=str, help='Insert an encode', default="")
    args=parser.parse_args()

    main(args.lhost, args.lport, args.params, args.encode)