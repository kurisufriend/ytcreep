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
    ("/home/rishi/archival/miscyt", "@geuxto", "geuxto")
]
template = subprocess.check_output(["which", "yt-dlp"]).decode("ascii").strip() + " --embed-thumbnail --embed-metadata --download-archive $PENISARCHIVE$.txt https://www.youtube.com/$PENISCHANNEL$ -o '%(channel)s/%(title)s.%(ext)s'"

for chan in channels:
    os.chdir(chan[0])
    os.system(template.replace("$PENISARCHIVE$", chan[2]).replace("$PENISCHANNEL$", chan[1]))
