# kindstat

Attempt to collect and show reading statistics from Kindle ereader

**Caveats**
- The primary source of data is the fmcache.db which is an sqlite3 DB containing reading sessions and also 'app sessions' which seem to be anytime when the screen is on and other 'records' like every tap on the screen.
- This cache is short.  Probably cleared when sync'd with Amazon.  Therefore you must collect data before syncing with Amazon!

**Note!**
- This is a work in progress!
- I made this for my personal amusement!
- This is not tested with every type of kindle, firmware version, book formats etc.

Using KRDS [KRDS Source mobilereads.com](https://www.mobileread.com/forums/showthread.php?t=322172) to read extra files like .mbp


## Providing test data

I have access to a Kindle Oasis 2 (2017), Kindle Oasis 3 (2019) and a Kindle Paperwhite 3 (2015).  I need test data.  The simplest way to provide data is using the scripts in the [./tools](tools) directory.  Alternatively you can copy files directly off the kindle, I need the system/fmcache/fmcache.db and all files with any of the following extensions (azw3f, azw3r, yjf, yjr, mbs, mbp1, pdt, pds, tas', tal) the filenames must be preserved but the directory structure is not important.  I believe none of these files contain anything secret or sensitive.

What will be revealed?  Book names & types.  Reading progress and speed estimate.  App & Reading sessions (start, end, duration) for the last day or two.
