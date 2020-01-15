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