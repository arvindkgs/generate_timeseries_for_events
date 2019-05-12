import argparse
from lib import FileHandler
from lib.ComputeTimeSeries import computeTimeSeries

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Computes and returns a ordered time series of average delivery time and other statistics from given input file, in a specific window/time-frame")
    parser.add_argument('--input-file', default=open('events.txt', 'r'), dest='eventsFile', metavar="INPUT-FILE", type=argparse.FileType('r'),
                        required=True,
                        help='File containing discrete events seperated by new line. An event:- {"timestamp": "2018-12-26 18:11:08.509654","translation_id": "12ab","source_language": "en","target_language": "fr","client_name": "easyjet","event_name": "translation_delivered","nr_words": 30, "duration": 20}')
    parser.add_argument('--window-size', dest='timeFrame', metavar="N",
                        help='Time frame in minutes up to which time series is computed.', default=25, type=int)
    args = parser.parse_args()
    timeUnits = computeTimeSeries(args.timeFrame, FileHandler.read(args.eventsFile))
    FileHandler.write('output.txt', timeUnits)