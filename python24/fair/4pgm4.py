#4.Create a class Time with private attributes hour, minute and second. Overload ‘+’ operator to find sum of 2 time.

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def display_time(self):
       
        print(f"{self.hour}h:{self.minute}m:{self.second}s")
	
    def __add__(self, other):
        sum_seconds = self.second + other.second
        sum_minutes = self.minute + other.minute + (sum_seconds // 60)
        sum_hours = self.hour + other.hour + (sum_minutes // 60)

        sum_seconds = sum_seconds % 60
        sum_minutes = sum_minutes % 60

        return Time(sum_hours, sum_minutes, sum_seconds)

h1=int(input("Enter hour1:"))
m1=int(input("Enter minute1:"))
s1=int(input("Enter second1:"))
h2=int(input("\nEnter hour2:"))
m2=int(input("Enter minutes2:"))
s2=int(input("Enter seconds2:"))
t1 = Time(h1,m1,s1);
t2 = Time(h2,m2,s2);


t3 = t1 + t2

print("\nTime 1: ", end="")
t1.display_time()

print("Time 2: ", end="")
t2.display_time()

print("Sum of Time1 and Time2 is ", end="")
t3.display_time()

