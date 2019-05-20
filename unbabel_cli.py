import argparse
from lib import FileHandler
from lib.ComputeTimeSeries import computeTimeSeries

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Computes and returns a ordered time series of average delivery time and other statistics from given input file, in a specific window/time-frame")
    parser.add_argument('--input-file', default='events.txt', dest='eventsFile', metavar="INPUT-FILE",
                        type=str,
                        required=True,
                        help='(Required) File containing discrete events seperated by new line.')
    parser.add_argument('--window-size', dest='timeFrame', metavar="N",
                        help='(Optional) Time frame in minutes up to which time series is computed. Defaults to 10 minutes',
                        default=10, type=int)
    parser.add_argument('--time-slot', default=1, dest='timeSlot', metavar="T", type=int,
                        help="(Optional) Time slot duration in minutes. Defaults to 1 min")
    args = parser.parse_args()
    timeUnits = computeTimeSeries(args.timeFrame, FileHandler.read(open(args.eventsFile)), args.timeSlot)
    FileHandler.write('output.txt', timeUnits)
