import os, subprocess

# e.g.
channels = [
    ("/home/rishi/archival/bea", "@beatanichisato", "bea"),
    ("/home/rishi/archival/schlatt", "@jschlattvault", "jschlattvault"),
    ("/home/rishi/archival/silly", "@Sillypoo", "sillypoo"),
    ("/home/rishi/archival/silly", "@heheSilly", "hehesilly"),
    ("/home/rishi/archival/hime/PL", "@XCHANMUSIC", "xchan"),
    ("/home/rishi/archival/pengiscool", "@flypenguins1119", "peng"),
    ("/home/rishi/archival/josie", "@theprocedural", "theprocedural"),
    ("/home/rishi/archival/miscyt", "@StamperTV_Archive", "stamper"),
    ("/home/rishi/archival/miscyt", "@geuxto", "geuxto"),
    ("/home/rishi/archival/miscyt", "@JebusMatoi", "jebus"),
    ("/home/rishi/archival/miscyt", "@OX_Media", "ox"),
    ("/home/rishi/archival/miscyt", "@versandlukas", "versandlukas"),
    ("/home/rishi/archival/miscyt", "@zhased", "zhased"),
    ("/home/rishi/archival/miscyt", "@readyourbooks5031", "ryb"),
    ("/home/rishi/archival/miscyt", "@jeffstiny3249", "jeffstiny"),
    ("/home/rishi/archival/miscyt", "@CRYSTELLAANN", "some tumblr"),
    ("/home/rishi/archival/miscyt", "@puke.princess", "bassproshops"),
    ("/home/rishi/archival/miscyt", "@plushygirlie", "bassproshops2"),
    ("/home/rishi/archival/miscyt", "@l0de", "l0de")
]
template = "/home/rishi/.local/bin/yt-dlp" + " --write-info-json --write-comments --embed-thumbnail --embed-metadata --download-archive $PENISARCHIVE$.txt https://www.youtube.com/$PENISCHANNEL$ -o '%(channel)s/%(title)s.%(ext)s'"

for chan in channels:
    os.chdir(chan[0])
    os.system(template.replace("$PENISARCHIVE$", chan[2]).replace("$PENISCHANNEL$", chan[1]))
