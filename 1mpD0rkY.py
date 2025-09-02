#!/usr/bin/python3


def generate_dork_queries(site):
    dork_templates = [
        'site:{}.com inurl:".php?Id=" inurl:"search"',
        'site:{}.com inurl:".php?Id=" intext:"search"',
        'site:{}.com inurl:"&search="',
        'site:{}.com inurl:"?q="',
        'site:{}.com inurl:"search.php?search="',
        'site:{}.com inurl:"&title="',
        'site:{}.com inurl:".php?words="',
        'site:{}.com inurl:"query.php" intext:"search"',
        'site:{}.com inurl:q= | inurl:s= | inurl:search=',
        'site:{}.com inurl:"url="',
        'site:{}.com inurl:"id="',
        'site:{}.com inurl:"category="',
        'site:{}.com inurl:"cat="',
        'site:{}.com inurl:"query="',
        'site:{}.com inurl:"keyword="',
    ]
    return [dork.format(site) for dork in dork_templates]

def main():
    site = input("Enter the site/domain (without 'www.' or TLD, e.g., 'example'): ")
    print("\nGenerated Google dork queries:\n")
    for query in generate_dork_queries(site):
        print(query)

if __name__ == "__main__":
    main()
