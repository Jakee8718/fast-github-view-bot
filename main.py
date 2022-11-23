from wrapper import *
import threading
import user_agent
print("+[██╗░░░██╗██╗███████╗░██╗░░░░░░░██╗  ██████╗░░█████╗░████████╗  ██╗░░░██╗██████╗░")
print("+[██║░░░██║██║██╔════╝░██║░░██╗░░██║  ██╔══██╗██╔══██╗╚══██╔══╝  ██║░░░██║╚════██╗")
print("+[╚██╗░██╔╝██║█████╗░░░╚██╗████╗██╔╝  ██████╦╝██║░░██║░░░██║░░░  ╚██╗░██╔╝░░███╔═╝")
print("+[╚██╗░██╔╝██║█████╗░░░╚██╗████╗██╔╝  ██████╦╝██║░░██║░░░██║░░░  ╚██╗░██╔╝░░███╔═╝")
print("+[░╚████╔╝░██║██╔══╝░░░░████╔═████║░  ██╔══██╗██║░░██║░░░██║░░░  ░╚████╔╝░██╔══╝░░")
print("+[░░╚██╔╝░░██║███████╗░░╚██╔╝░╚██╔╝░  ██████╦╝╚█████╔╝░░░██║░░░  ░░╚██╔╝░░███████╗")
print("+[░░░╚═╝░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░  ╚═════╝░░╚════╝░░░░╚═╝░░░  ░░░╚═╝░░░╚══════╝")
print ("+[ Made By nightclubs (github) edited by jakee8718 (github)")
def __get__req():
    try:
        pyreq = Client("camo.githubusercontent.com")
        lol = pyreq.get(
            resource="d57bd52b3b3a7912a23ab6add68fdec121af0f62aea19bf4532b0356c98aad91/68747470733a2f2f677076632e6172747572696f2e6465762f4a616b656538373138",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "User-Agent": user_agent.generate_user_agent(),
            },
        )

        ok = lol.decode()  # ; print(ok)
        if "Profile views" in ok:
            total = ok.split('role="img" aria-label="Profile views: ')[1].split('"')[0]
            print(f"[+] +1 View Sent | Total Views: {total}")
        else:
            print("view failed")
    except Exception:
        pass


while True:
    threading.Thread(target=__get__req).start()
