from pray_time import PrayTimes
from datetime import date
import argparse
from plyer import notification

prays_ = {
    'Fajr': 'الفجر',
    'Sunrise': 'الشروق',
    'Dhuhr': 'الظهر',
    'Asr': 'العصر',
    'Maghrib': 'المغرب',
    'Isha': 'العشاء',
    'Midnight': 'منتصف الليل'
}

def notify_me(coordinate, calculation_method):
    prayTimes = PrayTimes(calculation_method)
    times = prayTimes.getTimes(date.today(), coordinate, 2)
    masg = ''
    for k, v in prays_.items():
        masg += v + ': ' + times[k.lower()] + '\n'

    masg += ('=' * 41)
    notification.notify(
        title="اوقات الصلاة لليوم",
        message=masg,
        timeout=15
    )

def main():
    parser = argparse.ArgumentParser(description="This script displays prayer times for a given location.", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-n", "--notify", action="store_true", help="Show notification")
    parser.add_argument("-v", "--verbose", action="store_true", help="Increase verbosity")
    parser.add_argument("-lat", "--latitude", type=float, required=True, help="Latitude of the location")
    parser.add_argument("-lon", "--longitude", type=float, required=True, help="Longitude of the location")
    parser.add_argument("-m", "--method", default="ISNA", choices=["MWL", "ISNA", "Egypt", "Makkah", "Karachi", "Tehran"], help="Calculation method for prayer times")
    args = parser.parse_args()

    coordinate = (args.latitude, args.longitude)

    notify_me(coordinate, args.method)

# sample code to run in standalone mode only
if __name__ == "__main__":
    main()
