import re
import pandas as pd
import netaddr
from bisect import bisect

ips = pd.read_csv("ip2location.csv")
def lookup_region (ipaddr) :
    low = ips["low"].to_list()
   
    regex_ip = re.sub("[a-zA-Z]", "0", str(ipaddr))
   
    net_ip = int(netaddr.IPAddress(regex_ip))
   
    found_idx = bisect(low, net_ip) - 1
   
    ans = ips.at[found_idx, "region"]
   
    return ans


class Filing:
    def __init__(self, html):
        self.dates = [x for x in re.findall(r'\d{4}-\d{2}-\d{2}', html) if x[:2] in ['19','20']]
        self.sic = re.findall(r'SIC=\d+', html)
        self.sic = None if not self.sic else int(self.sic[0].replace('SIC=', ''))
        self.addresses = [] #address 확인해 보기 계속 \n 나오네?
        for addr_html in re.findall(r'<div class="mailer">([\s\S]+?)</div>', html):
            lines = []
            for line in re.findall(r'<span class="mailerAddress">([\s\S]+?)</span>', addr_html):
                if not line.strip() == "":
                    lines.append(line.strip())
            self.addresses.append("\n".join(lines))                                            
        self.addresses = [x for x in self.addresses if x != '']
       
    def state(self):
        if not self.addresses:
            return
        states = []
       
        for addr in self.addresses:
            if re.findall(r'[A-Z]{2} \d{5}', addr) != []:
                states.append(re.findall(r'[A-Z]{2} \d{5}', addr)[0][:2])
        return states[0] if states else None
    