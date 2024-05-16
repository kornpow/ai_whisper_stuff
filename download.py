import getpodcast

opt = getpodcast.options(
    date_from="2023-01-01",
    root_dir="/home/skorn/podcasts",
    run=True,
    only_new=True
)

# find feeds here:
# https://castos.com/tools/find-podcast-rss-feed/
podcasts = {
     "WBD": "https://www.whatbitcoindid.com/podcast?format=rss",
     "SLP": "https://anchor.fm/s/7d083a4/podcast/rss",
     "TMP": "https://feeds.megaphone.fm/theminingpod"
}

getpodcast.getpodcast(podcasts, opt)