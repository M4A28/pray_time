
from pray_time import *
import argparse

coordinate = (30.53, 31.65)
prays_ = {
            'Fajr': 'الفجر',
            'Sunrise': 'الشروق',
            'Dhuhr': 'الظهر',
            'Asr': 'العصر',
            'Maghrib': 'المغرب',
            'Isha': 'العشاء',
            'Midnight': 'منتصف الليل'

    }

def notify_me():
    prayTimes = PrayTimes('Egypt')
    times = prayTimes.getTimes(date.today(), coordinate, 2)
    masg = ''
    for k, v  in prays_.items():
        masg += v + ': ' + times[k.lower()] + '\n'
        
    masg += ('=' * 41)
    notification.notify(
            title = "اوقات الصلاة لليوم",
            message = masg,
            timeout = 15
        )

def main():
    
    # this for egypt cairo only 
    
    parser = argparse.ArgumentParser(description="this how to use praytime script ", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-n", "--notify", action="store_true", help="show notification")
    parser.add_argument("-v", "--verbose", action="store_true", help="increase verbosity")
    parser.add_argument("-f", "--fajer", help="show fajer pryrime")
    parser.add_argument("-s", "--sunrise", action="store_true", help="show sunrise time")
    parser.add_argument("-d", "--dhuhr", action="store_true", help="show dhuhr pryrime")
    parser.add_argument("-a", "--aser", action="store_true", help="show aser pryrime")
    parser.add_argument("-m", "--maghrib", action="store_true", help="show maghrib pryrime")
    parser.add_argument("-i", "--isha", action="store_true", help="show isha pryrime")
    args = parser.parse_args()
    config = vars(args)

    notify_me()



# sample code to run in standalone mode only
if __name__ == "__main__":
    main()
