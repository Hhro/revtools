import subprocess

def download_apk(apk_id, gmail, pw):
    subprocess.run(
        "gplaycli -v -d {apk_id} -m {gmail} -pw {pw}"
        .format(
            apk_id=apk_id, 
            gmail=gmail, 
            pw=pw)
        .split()
    )

def decompile_apk(apk, dest_dir=None):
    args = ["jadx"]

    if dest_dir != None:
        args += ["-d", dest_dir]
    args += [apk]

    subprocess.run(args)