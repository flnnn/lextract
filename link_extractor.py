import argparse
import requests
from bs4 import BeautifulSoup

def banner():
    text = " _            _               _   \n"
    text += "| |   _____ _| |_ _ _ __ _ __| |_ \n"
    text += "| |__/ -_) \ /  _| '_/ _` / _|  _|\n"
    text += "|____\___/_\_\\\__|_| \\__,_\__|\__|\n"
    text += "\tsrc & href extractor\n"
    print("\033[34;1m" + text + "\033[m")


def link_extractor(response_text: str):
    soup = BeautifulSoup(response_text, 'html.parser')
    tags = soup.find_all(["a", "script", "img"])
    for tag in tags:
        print(tag)


def request_handler(url: str):
    try:
        response = requests.get(url)
    except Exception as e:
        print(f"[!] can't connect to host...")
        exit(1)
    else:
        status = response.status_code

        if status == 200:
            link_extractor(response.text)
        else:
            print(f"[-] something went wrong - {status}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extracts links from src and href atributes in html tags.",
        usage="%(prog)s --url http://example.com"
    )
    parser.add_argument("--url", "-u", required=True, help="url for the webpage.")
    args = parser.parse_args()

    banner()

    request_handler(args.url)
