# Instagram RSS URL Generator

## Description
A Python script that creates custom RSS feed URLs from Instagram account handles. The script uses a publicly available instance of [RSS-Bridge](https://github.com/RSS-Bridge/rss-bridge) to create the RSS feed and then generates a unique URL to reference for RSS feed subscriptions.

## Getting Started

### Dependencies
* [RSS-Bridge](https://github.com/RSS-Bridge/rss-bridge)
* Python v3.1.3+

### Installation
Clone this project & use the Command Line/Terminal to run:

```
python3 install -r requirements.txt 
```

### Run the Script
This script only needs the ***handle*** for the targeted Instagram account and not the full URL (i.e. type "easystreetrecords" rather than "https://www.instagram.com/easystreetrecords", no quotation marks or brackets).

#### Instagram URL Validation
Run this command to verify that the script is reading the correct data from the targeted Instagram account:

```
python3 feed_rss.py [Instagram handle] --validate
```

#### Generate an RSS URL

```
python3 feed_rss.py [Instagram handle]
```

Example command:
```
python3 feed_rss.py easystreetrecords
```

Example URL produced:
```
https://rss-bridge.org/bridge01/?action=display&bridge=Instagram&context=Username&u=easystreetrecords&format=Atom
```