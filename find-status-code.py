import requests

live_site = "/home/karthithehacker/Hunting/dataset/live.txt"
output_file = "/home/karthithehacker/Hunting/recon/status-code.txt"

def get_status_code(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code
    except requests.ConnectionError:
        pass
    except requests.Timeout:
        pass
    except Exception as e:
        pass
    return None

with open(live_site, 'r') as infile, open(output_file, 'a') as outfile:
    for line in infile:
        subdomain = line.strip()
        live_url = f"{subdomain}"
        status_code = get_status_code(live_url)
        if status_code is not None:
            outfile.write(f"{live_url} -> Status Code: {status_code}\n")
            print(f"{live_url} -> Status Code: {status_code}")
