@asynchronous
def module_init():
    if not get("enabled",True,"daemon"):
        return
    while True:
        busdir = os.environ["HOME"]
        if os.path.exists("/{}/pardus-greeter".format(busdir)):
            os.unlink("/{}/pardus-greeter".format(busdir))
        os.mkfifo("/{}/pardus-greeter".format(busdir))
        f = open("/{}/pardus-greeter".format(busdir),"r")
        for line in f.read().split("\n"):
            if line.startswith("username:"):
                lightdm.username = line[9:]
            if line.startswith("password:"):
                lightdm.password = line[9:]
            if line.startswith("session:"):
                lightdm.session = line[8:]
        lightdm.login()
