from subprocess import check_output, PIPE
import sys
import csv
stat={}
if __name__ == '__main__':
        nc=input("Range of clients (Eg: 10-100): ")
        np=input("Number Of Parallel Clients/Groups you want: ")
        csvfilename=np+".csv"
        startc=int(nc.split("-")[0])
        endc=int(nc.split("-")[1])
        for i in range(startc,endc+startc, startc):
            print("Number of Clients:", i)
            out=check_output("eval bin/test bin/server %s %s | python3 test/calc.py" % (str(i),str(np),), shell=True, stderr=PIPE)
            print(out)
            sys.stdout.flush()
            stat[str(i)]=out
            sys.stdout.flush()
        try:
            flag = str(sys.argv[1])
            sys.stdout.flush()
            if(flag=="-d" or flag=="--dev" ):
                with open(csvfilename, 'w') as f:
                    f.write(("Number of Clients, Time\n"))
                    for key in stat.keys():
                        f.write("%s, %s\n" % (key, stat[key]))
        except:
            print("To generate log file use flag -d or --dev")
            sys.stdout.flush()
