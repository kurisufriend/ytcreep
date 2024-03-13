import os

# e.g.
channels = [
    ("~/archival/bea", "@beatanichisato", "bea"),
    ("~/archival/schlatt", "@jschlattvault", "jschlattvault"),
    ("~/archival/hehe", "@Sillypoo", "sillypoo"),
    ("~/archival/hehe", "@heheSilly", "hehesilly"),
    ("~/archival/hime/PL", "@@XCHANMUSIC", "xchan"),
    ("~/archival/pengiscool", "@flypenguins1119", "peng")
]
template = "yt-dlp -f --embed-thumbnail --embed-metadata --download-archive $PENISARCHIVE$.txt https://www.youtube.com/$PENISCHANNEL$ -o '%(channel)s/%(title)s.%(ext)s'"

for chan in channels:
    os.chdir(chan[0])
    os.system(template.replace("$PENISARCHIVE$", chan[2]).replace("$PENISCHANNEL$", chan[1]))
    