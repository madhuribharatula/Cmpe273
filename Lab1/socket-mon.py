import psutil
value_Dict = {}
Count_Dict = {}
class  Data():
        def __init__(self,pid,laddr,raddr,status):
                self.pid=pid
                self.laddr=laddr
                self.raddr=raddr
                self.status=status

for c in psutil.net_connections(kind='tcp'):
        if c.raddr:
            laddr = "%s@%s" % (c.laddr)
            raddr = "%s@%s" % (c.raddr)
            pid = "%s" % (c.pid)
            status = "%s" % (c.status)
            data = Data(pid,laddr,raddr,status)
            if pid not in value_Dict:
                    value_Dict[pid] = []
            value_Dict[pid].append(data)
            count=0
            if Count_Dict.has_key(pid):
                    count=Count_Dict[pid]
            Count_Dict[pid] = count+1

print "\"pid\",\"laddr\",\"raddr\",\"status\""

for key, value in sorted(Count_Dict.iteritems(), key=lambda x: x[1],reverse=True):
        datalist = value_Dict[key]
        #print value
        for d in datalist:
                print("\"" + key + "\",\"" + d.laddr + "\",\"" + d.raddr + "\",\"" + d.status + "\"")