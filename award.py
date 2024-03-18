#award

minutes_swimming = int(input("How many minutes used in swimming ? "))
minutes_cycling = int(input("How many minutes used in cycling ? "))
minutes_running = int(input("How many minutes used in running ? "))

total_time = int(minutes_swimming + minutes_cycling + minutes_running)

if (total_time > 0) and (total_time < 100):
   print("Provincial Colours")

elif (total_time > 100) and (total_time < 105):
      print("Provinvial Half Colours" )

elif (total_time > 105) and (total_time < 110):
      print("Provinvial Scroll" )

elif (total_time >= 111):
      print("No award" )