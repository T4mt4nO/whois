import whois

def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        return w
    except:
        return None

# Ejemplo de uso
domain = "google.com"
whois_info = get_whois_info(domain)
print(whois_info)
