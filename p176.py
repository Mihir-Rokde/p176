import matplotlib.pyplot as plt
import speedtest
import time
lds=[]
lus=[]
for i in range(5):
    st=speedtest.Speedtest()
    ds=round(st.download()/1000000,2)
    lds.append(ds)
    us=round(st.upload()/1000000,2)
    lus.append(us)
    time.sleep(60)
    print(lds)
    print(lus)
x=[1,2,3,4,5]
plt.plot(x,lds,label="download speed")
plt.title("speed")
plt.plot(x,lus,label="upload speed")
plt.legend()
plt.show()
