from sys import exit
from definitions import ReplitData

def main():
    replit  = ReplitData()
    replit.init()

    err     = replit.login()
    if err != None:
        exit(f"[!] Failed to Login: {err}")

    print("\n[i] Access\n")
    guides  = replit.guides_data()
    replit.get_guides(guides)

    replit.close()


if __name__ == "__main__":
    main()
