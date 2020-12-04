# BE AWARE THIS PROGRAM HAS LIMITED TESTING; EXPECT BUGS

# Usage
```sh
 $ python youtube.py [visits] [youtubeLinks.txt] [minWatch] [maxWatch]
 ```

# Help
 - **visits** The amount of visits per video
 - **youtubeLinks** The file that contains the Youtube links; one link per line
 - **minWatch** The minimum watch time in seconds
 - **maxWatch** The maximum watch time in seconds

# Example
 - python youtube.py 300 urls.txt 38 65

# Note
 - Don't forget to have PySocks and Mechanize
```py
pip install pysocks
pip install mechanize
```
