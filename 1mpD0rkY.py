#!/usr/bin/python3
import urllib.parse

def generate_dork_queries(site):
    dork_templates = [
        # Original ones
        'site:{} inurl:".php?Id=" inurl:"search"',
        'site:{} inurl:".php?Id=" intext:"search"',
        'site:{} inurl:"&search="',
        'site:{} inurl:"?q="',
        'site:{} inurl:"search.php?search="',
        'site:{} inurl:"&title="',
        'site:{} inurl:".php?words="',
        'site:{} inurl:"query.php" intext:"search"',
        'site:{} inurl:q= | inurl:s= | inurl:search=',
        'site:{} inurl:"url="',
        'site:{} inurl:"id="',
        'site:{} inurl:"category="',
        'site:{} inurl:"cat="',
        'site:{} inurl:"query="',
        'site:{} inurl:"keyword="',

        # New advanced ones
        'site:{} (ext:env | ext:log | ext:bak | ext:sql | ext:zip | ext:conf | ext:ini) '
        '(intext:"db_password" | intext:"password" | intext:"authorization" | intext:"api_key" | intext:"private key") -stackoverflow -github',

        'site:{} (ext:pem | ext:key) ("PRIVATE KEY" | "BEGIN RSA PRIVATE KEY" | "BEGIN OPENSSH PRIVATE KEY") '
        '-stackoverflow -github',

        'site:{} (ext:sql | ext:bak | ext:zip | ext:tar | ext:gz | ext:rar) '
        '("dump" | "backup" | "password" | "credentials") -stackoverflow -github',

        'site:{} intitle:index.of (env | .git | .svn | backup | db.sql | .bak | config | secrets) '
        '-stackoverflow -github',

        'site:{} ("Warning: mysql_fetch_assoc()" | "Warning: pg_connect()" | "Notice: Undefined index" | "System.Data.SqlClient.SqlException") '
        '-stackoverflow -github',

        'site:{} (filetype:doc | filetype:docx | filetype:xls | filetype:xlsx | filetype:ppt | filetype:pptx) '
        '("password" | "credentials" | "db user" | "db pass" | "secret key") -stackoverflow -github',

        'site:{} intitle:"index of" ".git"',

        'site:{} filetype:sql "INSERT INTO" "VALUES"',

        'site:{} filetype:env "APP_KEY="',

        'site:{} intitle:"index of" ".svn"',
    ]
    return [dork.format(site) for dork in dork_templates]


def main():
    # Print developer info
    print("\n")
    print("\033[96m@trashz403\033[0m")  # cyan
    print("\033[91mGitHub:\033[0m https://github.com/trashz403\n\n")  # red


    site = input("Enter the site/domain (without 'www.'): ")
    queries = generate_dork_queries(site)

    # First print queries normally
    print("\n\n\nGenerated Google dork queries:\n")
    for q in queries:
        print(q)

    # Then print URLs
    print("\n\n\nGenerated Google dork clickable URLs:\n")
    for idx, q in enumerate(queries, 1):
        encoded = urllib.parse.quote(q)
        url = f"https://www.google.com/search?q={encoded}"
        print(f"{idx}. {url}")


if __name__ == "__main__":
    main()
