def add_racer(racers, times, new_name, new_time):
    racers.append(new_name)
    times.append(new_time)

def disqualify_racer(racers, times, name):
    if name in racers:
        i = racers.index(name)
        racers.pop(i)
        times.pop(i)
        return True
    return False

def get_fastest_laps(racers, times, n):
    r = list(racers)
    t = list(times)
    result = []
    for i in range(n):
        if not t:
            break
        m = 0
        for i in range(1, len(t)):
            if t[i] < t[m]:
                m = i
        result.append(r[m])
        r.pop(m)
        t.pop(m)
    return result

def manage_race_results(racers, times, new_data, dq_name, count):
    r = list(racers)
    t = list(times)
    add_racer(r, t, new_data[0], new_data[1])
    disqualify_racer(r, t, dq_name)
    fastest = get_fastest_laps(r, t, count)
    return r, fastest


racers = ["Axel", "Blaze", "Cruz", "Dash", "Echo"]
times = [95.42, 94.88, 96.10, 95.90, 94.99]
new_racer = ["Fang", 94.50]
disq = "Dash"
count = 3

final_racers, fastest = manage_race_results(racers, times, new_racer, disq, count)

print("Final racers:", final_racers)
print("Fastest list:", fastest)
