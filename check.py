import subprocess
import requests
import json
import os
import time
import socket

with open('config.json') as config_file:
    data = json.load(config_file)

def render(output):
    output = """{}""".format(output)
    output = output.replace("\\n","\n").replace("\\t","\t").replace("b'","")[:-1]
    return output

class Check:
    def __init__(self,msg):
        self.msg = msg
        self.list_func = data['list_func']
    def msg_for_bot(self):
        first_key = self.msg.split(" ")[0]
        if first_key in self.list_func:

            if first_key == "check":
                output1 = render(subprocess.check_output('free -m',shell=True))
                output2 = render(subprocess.check_output('df -h',shell=True))
                return output1+output2

            elif first_key[:7] == "caulenh" and len(self.msg.split(" ")) == 2:
                second_key = self.msg.split(" ")[1]
                cmd =  'zcat '+ data['path'][first_key] + '*' + ' | grep ' + second_key
                output = render(subprocess.check_output(cmd,shell=True))
                return output

            elif first_key == 'ping' and len(self.msg.split(" ")) == 2:
                response = os.system("ping -c 3 " + self.msg.split(" ")[1])
                if response == 0:
                    output = 'OK'
                else:
                    output = 'Not OK'
                return output

            elif first_key == 'telnet' and len(self.msg.split(" ")) == 3:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(3)
                try:
                        s.connect((self.msg.split(" ")[1], int(self.msg.split(" ")[2])))
                        s.shutdown(socket.SHUT_RDWR)
                        output = 'OK'
                except:
                        output = 'Not OK'
                finally:
                        s.close()
                return output
            else:
                return False
        else:
            return False