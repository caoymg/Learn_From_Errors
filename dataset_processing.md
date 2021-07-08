# Dataset Processing
**dataset:** MovieLens-100k

**errors:** UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 76620: invalid continuation byte

**solutions:** encoding="latin-1"

**comments:** the movie title might be like "Á köldum klaka", so we should choose latin-1 for Western Europe language. Links to [List of Python standard encodings](https://docs.python.org/3/library/codecs.html#standard-encodings) .



##### train set & test set split strategy:

1. **warm-start** ：based on leave-one-out protocol. ensuring each user in test set have at least one records in train set

2. **user cold-start** : the user in test set should not appear in train set

3. **item cold-start** : the item in test set should not appear in train set

