time_sec1=int(input("the the time in sec:"))

time_day=time_sec1//(24*3600)
time_hour=(time_sec1%(24*3600))//3600
time_min=((time_sec1%(24*3600))%3600)//60
time_sec=((time_sec1%(24*3600))%3600)%60

print("the given time is",time_day,"days",time_hour,"hours",time_min,"mins",time_sec,'sec')