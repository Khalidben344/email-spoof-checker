import dns.resolver

def check_spoof_protection(domain):
    try:
        print(f"🔍 Checking SPF for {domain}...")
        spf = dns.resolver.resolve(domain, 'TXT')
        for record in spf:
            if "v=spf1" in record.to_text():
                print(f"✅ SPF found: {record.to_text()}")
                break
        else:
            print("❌ No SPF record found.")

    except Exception as e:
        print("⚠️ Error checking SPF:", e)

    try:
        print(f"\n🔍 Checking DMARC for {domain}...")
        dmarc = dns.resolver.resolve(f"_dmarc.{domain}", 'TXT')
        for record in dmarc:
            print(f"✅ DMARC record: {record.to_text()}")
            break
    except:
        print("❌ No DMARC record found.")

# 👇 Ask for domain
domain = input("🌐 Enter a domain to check (e.g. gmail.com): ")
check_spoof_protection(domain)

input("\n🖱️ Press Enter to exit...")
