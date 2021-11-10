time=[3,30]
# hour : minute
if time[0]>=12: time[0]-=12
hour_theta=360/12
minute_theta=360/60
print(abs(hour_theta*(time[0] + (time[1]/60))- minute_theta*time[1]))