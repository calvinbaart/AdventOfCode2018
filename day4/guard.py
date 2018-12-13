import math
import re
from dateutil.parser import parse

class Guard:
    def __init__(self, id: int):
        self.id = id
        self.sleepStart = None
        self.sleepRanges = []
        self.totalSleepTime = 0
        self.asleepMinutes = {}

    def sleep(self, date):
        self.sleepStart = date

    def wakeup(self, date):
        if self.sleepStart is None:
            return

        sleepRange = date - self.sleepStart
        self.sleepRanges.append(sleepRange)
        self.totalSleepTime = sum(
            [int(x.total_seconds() / 60) for x in self.sleepRanges])

        for x in range(0, int(sleepRange.total_seconds() / 60)):
            hour = self.sleepStart.hour
            minute = self.sleepStart.minute + x

            hour = hour + math.floor(minute / 60)
            minute = minute % 60

            key = f"{hour}:{minute}"
            if key in self.asleepMinutes:
                self.asleepMinutes[key] = self.asleepMinutes[key] + 1
            else:
                self.asleepMinutes[key] = 1

    def regularSleepMinute(self):
        if len(self.asleepMinutes) is 0:
            return (0, 0, self.id)
    
        base = max(self.asleepMinutes.items(), key=lambda x: x[1])
        key = int(base[0].split(":")[1])
        return (key, base[1], self.id)

    def __repr__(self):
        return f"Guard({self.id}): {self.totalSleepTime}"


def process(entry: str):
    split = entry.split("]")
    date = parse(split[0][1:])
    entry = split[1][1:]
    action = 0
    guard = -1

    if entry.startswith("wakes up"):
        action = 1
    elif entry.startswith("falls asleep"):
        action = 2
    else:
        regex = r"Guard\s*#(\d*)"
        matches = re.findall(regex, entry, re.MULTILINE)

        guard = int(matches[0])

    return (date, action, guard)
