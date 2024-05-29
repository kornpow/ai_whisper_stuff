import getpodcast

def compressor(*args, **kwargs):
    podcast = kwargs["pod"]
    if podcast != "The Ron Burgundy Podcast":
        return

    if not shutil.which("ffmpeg"):
        getpodcast.message("ffmpeg not available")
        return

    uncompressed = pathlib.Path(kwargs["newfilename"])
    podcast_folder = uncompressed.parent
    compressed = podcast_folder.joinpath(f"__{uncompressed.name}")

    getpodcast.message("Compressing file ...")
    subprocess.run(
        [
            "ffmpeg",
            "-v",
            "quiet",
            "-y",
            "-i",
            str(uncompressed),
            "-filter_complex",
            "compand=attacks=0:points=-80/-900|-45/-15|-27/-9|0/-7|20/-7:gain=5",
            str(compressed),
        ]
    )
    mtime = kwargs["newfilemtime"]
    os.utime(compressed, (mtime, mtime))
    compressed.replace(uncompressed)
    getpodcast.message("Compressing complete")

# opt = getpodcast.options(
#     date_from="2019-07-30", root_dir="./podcast", hooks="validated=compressor"
# )



opt = getpodcast.options(
    date_from="2024-01-01",
    root_dir="/media/podcasts/data/podcasts/",
    run=True,
    only_new=True
)

# find feeds here:
# https://castos.com/tools/find-podcast-rss-feed/
podcasts = {
     "WBD": "https://www.whatbitcoindid.com/podcast?format=rss",
     "SLP": "https://anchor.fm/s/7d083a4/podcast/rss",
     "TMP": "https://feeds.megaphone.fm/theminingpod",
     "TFTC": "https://anchor.fm/s/558f520/podcast/rss",
}

getpodcast.getpodcast(podcasts, opt)