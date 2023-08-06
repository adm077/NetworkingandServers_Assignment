
import requests
from tabulate import tabulate
import time

# List of subdomains to check
subdomains = [
    "https://herovired.com/",
    "https://herovired.com/learning-hub/blogs/",
    "https://herovired.com/success-stories/",
    "https://herovired.com/about-us/",
    "https://vlearnv.herovired.com/",
    "https://herovired.com/contact-us/"
]

def check_subdomain_status(subdomain):
    try:
        response = requests.get(subdomain, timeout=5)
        return "Up" if response.status_code == 200 else "Down"
    except requests.ConnectionError:
        return "Down"

def update_status_table(subdomain_status):
    headers = ["Subdomain", "Status"]
    print(tabulate(subdomain_status, headers=headers))

def main():
    while True:
        subdomain_status = []
        for subdomain in subdomains:
            status = check_subdomain_status(subdomain)
            subdomain_status.append([subdomain, status])
        update_status_table(subdomain_status)
        time.sleep(60)

if __name__ == "__main__":
    main()

