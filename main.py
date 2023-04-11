from pySmartDL import SmartDL

downloads = [
    {"url": "https://safebooru.org//samples/4140/sample_469f2c388c37b36726fd4a1648fa73f5812b84a6.jpg?4326142",
     "dest": "C:/Users/Lord/Pictures"},

    {"url": "https://safebooru.org//images/4113/c58b00f066857cdb7bd793e48f04b08974c12232.jpg?4298214",
     "dest": "C:/Users/Lord/Pictures"},

    {"url": "https://safebooru.org//samples/4128/sample_567deac4d172153cf057f2c8b9319d8452dcde01.jpg?4314211",
     "dest": "C:/Users/Lord/Pictures"}
]

# Create SmartDL objects for each download
sm_downloads = []
for download in downloads:
    sm_download = SmartDL(download["url"], download["dest"])
    sm_download.progress_bar = True
    sm_downloads.append(sm_download)

# Start the downloads
for sm_download in sm_downloads:
    sm_download.start()

# Check if all downloads were successful
for sm_download in sm_downloads:
    if sm_download.isSuccessful():
        print(f"{sm_download.get_dest()} downloaded successfully!")
    else:
        print(f"{sm_download.get_dest()} download failed with an error: {sm_download.get_errors()}")
