import datetime

from _utilities import internet_up, tweet


TOTAL_DOWNTIME = 0


def _wait_for_internet_up():
    while not internet_up():
        sleep(1)


def _monitor_internet(start_time):
    while True:
        if not internet_up():
            begin_internet_down = datetime.datetime.now()
            _wait_for_internet_up()
            end_internet_down = datetime.datetime.now()
            time_down = end_internet_down - begin_internet_down
            TOTAL_DOWNTIME += time_down.total_seconds()
            time_since_start = end_internet_down - start_time
            message = "*beep boop*\nInternet down from {} to {}\nDown {:0.1f}% since {}".format(
                    begin_internet_down,
                    end_internet_down,
                    float(TOTAL_DOWNTIME) / float((end_internet_downtime - start_time).total_seconds()) * 100,
                    start_time)
            tweet(message)


def main():
    start_time = datetime.datetime.now()
    while True:
        try:
            _monitor_internet(start_time)
        except:
            pass


if __name__ == "__main__":
    main()
