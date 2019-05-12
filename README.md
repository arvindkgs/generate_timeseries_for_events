Given a **time-frame/window** parameter and **file** containing the events, the tool computes and logs (in a time series of configurable bucket-size) the rolling average delivery time for given events falling in the time frame.

Invoke the python tool as,

`$ python unbabel_cli.py -h`

`usage: unbabel_cli.py [-h] --input-file INPUT-FILE [--window-size N]`

`unbabel_cli.py: error: argument --input-file is required`

Note: Default value for `--window-size` is 10 minutes

Given following input file:  

```
{"timestamp": "2018-12-26 18:11:08.509654","translation_id": "5aa5b2f39f7254a75aa5","source_language": "en","target_language": "fr","client_name": "easyjet","event_name": "translation_delivered","nr_words": 30, "duration": 20}
{"timestamp": "2018-12-26 18:15:19.903159","translation_id": "5aa5b2f39f7254a75aa4","source_language": "en","target_language": "fr","client_name": "easyjet","event_name": "translation_delivered","nr_words": 30, "duration": 31}
{"timestamp": "2018-12-26 18:23:19.903159","translation_id": "5aa5b2f39f7254a75bb33","source_language": "en","target_language": "fr","client_name": "booking","event_name": "translation_delivered","nr_words": 100, "duration": 54}
```
