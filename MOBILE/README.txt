Deep Ethical Topological Prompt Engineering™
ACCM Deep Ethics Project mobile navigator
===========================================

Extract this archive and open index.html in your browser. The directory,
search and view controls run from local files. The page links open the
original project website, so reading the originals requires internet
access. Bookmarks and spacing are stored by the browser when available.
Some browsers limit or clear local storage for files opened from disk.

The seven reading clusters follow the public All Pages index. Other
public pages from the navigation and sitemap appear in additional groups.
Some pages belong to several clusters, so counts in the cluster view can
overlap. A–Z and Saved show each address once. The project PDF collection
has its own index, linked from the directory.

Source index
https://deepethics.github.io/ACCM-Deep-Ethics-Project/PAGES/

Live navigator and ZIP
https://deepethics.github.io/ACCM-Deep-Ethics-Project/MOBILE/

Maintenance

Run python3 tools/refresh-catalog.py from this folder to rebuild data.js
from the live public index, navigation and sitemap. The script uses curl
and the Python standard library. Read the report for unmatched links.
Then regenerate the visitor ZIP with:

  zip -9 -r ACCM-Deep-Ethics-Project-Mobile-Navigator.zip \
      index.html style.css app.js data.js README.txt assets tools

Run the packaging command without an old ZIP in the folder to avoid
retaining files removed from the navigator.

The decorative field image was supplied by John Kuhles.
