# Get a URL from the user, clean it, and extract the domain name and TLD (Top-Level Domain).
# Name: Rick Kazman
# Date: Sept. 18, 2026

url = input("Enter a URL: ")

cleaned_url = url.replace("https://", "")
cleaned_url = cleaned_url.replace("/", "")
print("Cleaned URL:", cleaned_url)

parts = cleaned_url.split(".")
print("The parts are: ", parts)

domain_name = parts[1]
TLD = parts[2]
print("Domain name:", domain_name)
print("TLD:", TLD)
