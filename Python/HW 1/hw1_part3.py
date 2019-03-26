
#code calculates amount it must rain daily in Panama to fill up the Gatun Lake

##function returns volume of water needed to fill up a lock given its dimensions
def volume_solid(width,length,depth):
    volume = width * length * depth
    return volume

##function returns the amount of water needed to fill a lock with the volume determined for an entire year
def water_needed_perlock(volume):
    ships_per_day = 35.
    water_needed_perlock = volume * ships_per_day * 365
    return water_needed_perlock


total_volume =  water_needed_perlock(volume_solid(32,320,10)) * 2
daily_rain = int(total_volume) / (30 * 9.) 
mm_rain = daily_rain / 600000.

print "Panama canal statistics:"
print "The total volume of wate rneeded in Gatun lake:", int(total_volume), "m^3"
print "In rainy season, daily rain should be at least:", int(daily_rain), "m^3"
print "This means, it rains about", mm_rain, "millimeters every day during the rainy season"