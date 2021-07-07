# Dataset Processing
**dataset:** MovieLens-100k

**errors:** UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 76620: invalid continuation byte

**solutions:** encoding="latin-1"

**comments:** the movie title might be like "Á köldum klaka", so we should choose latin-1 for Western Europe language. Links to [List of Python standard encodings](https://docs.python.org/3/library/codecs.html#standard-encodings) .

