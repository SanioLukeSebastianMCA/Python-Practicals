class Time:
    def __init__(self, h, m, s):
        self._h = h
        self._m = m
        self._s = s

    def __add__(self, x):
        h_sum = self._h + x._h
        m_sum = self._m + x._m
        s_sum = self._s + x._s
        if s_sum >= 60:
            s_sum = s_sum - 60
            m_sum = m_sum + 1
        if m_sum >= 60:
            m_sum = m_sum - 60
            h_sum = h_sum + 1
        print(h_sum, ":", m_sum, ":", s_sum)


print("Time 01")
h1 = int(input("Enter the hour in time 01 : "))
m1 = int(input("Enter the minute in time 01 : "))
s1 = int(input("Enter the second in time 01 : "))
obj1 = Time(h1, m1, s1)

print("\nTime 02")
h2 = int(input("Enter the hour in time 02 : "))
m2 = int(input("Enter the minute in time 02 : "))
s2 = int(input("Enter the second in time 02 : "))
obj2 = Time(h2, m2, s2)

print("\nThe summation of both times is : ")
obj1 + obj2
