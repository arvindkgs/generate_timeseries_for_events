# The **_WHAT_**:

Given a **time-frame/window** parameter and **file** containing the events, the tool computes and logs (in a time series of configurable bucket-size) the rolling average delivery time for given events falling in the time frame.

Invoke the python tool as,

```
$ python unbabel_cli.py -h

usage: unbabel_cli.py [-h] --input-file INPUT-FILE [--window-size N]
                      [--time-slot T]

Computes and returns a ordered time series of average delivery time and other
statistics from given input file, in a specific window/time-frame

optional arguments:
  -h, --help            show this help message and exit
  --input-file INPUT-FILE
                        (Required) Path to file containing discrete events seperated
                        by new line.
  --window-size N       (Optional) Time frame in minutes up to which time
                        series is computed. Defaults to 10 minutes
  --time-slot T         (Optional) Time slot duration in minutes. Defaults to
                        1 min

```

Passing following input file to the tool:  

```
{"timestamp": "2018-12-26 18:11:08.509654","translation_id": "5aa5b2f39f7254a75aa5","source_language": "en","target_language": "fr","client_name": "easyjet","event_name": "translation_delivered","nr_words": 30, "duration": 20}
{"timestamp": "2018-12-26 18:15:19.903159","translation_id": "5aa5b2f39f7254a75aa4","source_language": "en","target_language": "fr","client_name": "easyjet","event_name": "translation_delivered","nr_words": 30, "duration": 31}
{"timestamp": "2018-12-26 18:23:19.903159","translation_id": "5aa5b2f39f7254a75bb33","source_language": "en","target_language": "fr","client_name": "booking","event_name": "translation_delivered","nr_words": 100, "duration": 54}
```

The tool generates a 'output.txt' log containing time-series ordered chronologically from the first event timestamp(T = '2018-12-26 18:11:08.509654') upto the given time-frame(10+T minutes = '2018-12-26 18:22:00'), as

 ```
{ "date": "2018-12-26 18:11:00", "average_delivery_time": 0, "words":0 }
{ "date": "2018-12-26 18:12:00", "average_delivery_time": 20.0, "words":0 }
{ "date": "2018-12-26 18:13:00", "average_delivery_time": 20.0, "words":1 }
{ "date": "2018-12-26 18:14:00", "average_delivery_time": 20.0, "words":0 }
{ "date": "2018-12-26 18:15:00", "average_delivery_time": 20.0, "words":1 }
{ "date": "2018-12-26 18:16:00", "average_delivery_time": 25.5, "words":0 }
{ "date": "2018-12-26 18:17:00", "average_delivery_time": 25.5, "words":1 }
{ "date": "2018-12-26 18:18:00", "average_delivery_time": 25.5, "words":0 }
{ "date": "2018-12-26 18:19:00", "average_delivery_time": 25.5, "words":1 }
{ "date": "2018-12-26 18:20:00", "average_delivery_time": 25.5, "words":0 }
{ "date": "2018-12-26 18:21:00", "average_delivery_time": 25.5, "words":1 }
{ "date": "2018-12-26 18:22:00", "average_delivery_time": 25.5, "words":0 }

```

# The _**HOW**_:

Computation of 'average_delivery_time' in i<sup>th</sup> time slot in time series,
* Average delivery time = avg(list(durations of all events that fall in i<sup>th</sup> slot))
    * Consider the 6<sup>th</sup> entry in output : `{ "date": "2018-12-26 18:16:00", "average_delivery_time": 25.5 }`
    * 1<sup>st</sup> Event, and 2<sup>nd</sup> are still running in the time slot `from : 2018-12-26 18:15:00, to : 2018-12-26 18:15:99`.
    * So, Average Delivery Time = Avg(20 (Duration of 1<sup>st</sup> Event) , 25 (Duration of 2<sup>nd</sup> Event) )  = 25.5 
* Number of words, in a time slot, as
    * wordsPerMin per event = (words of event)/(duration of event)
    * This is accumulated per event in given time slot 

# **_Algorithm_**
 
There are two ways to solve the problem.
1. Loop through all one minute time slots in time frame, inner-loop through all events and compute avg delivery time and words
2. Order the events chronologically, maintain time slot information and loop through all events, and for each event loop through the pertinent time slots updating the time slot information if event execution is within the time frame. 

Both approaches takes O(n<sup>2</sup>), while the second is O(n) if there are no overlapping events (best case scenario). So went with second approach.

# Enhancements
1. Added computation of words per time slot.
2. Currently the time slots are fixed at one minute, however, this can be configured by setting the `--time-slot ` optional argument.    
