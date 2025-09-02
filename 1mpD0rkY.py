#!/usr/bin/python3


def generate_dork_queries(site):
    dork_templates = [
        # Original ones
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

        # Newly added ones
        'site:*.com (ext:env | ext:log | ext:bak | ext:sql | ext:zip | ext:conf | ext:ini) '
        '(intext:"db_password" | intext:"password" | intext:"authorization" | intext:"api_key" | intext:"private key") -stackoverflow -github',

        'site:*.com (ext:pem | ext:key) ("PRIVATE KEY" | "BEGIN RSA PRIVATE KEY" | "BEGIN OPENSSH PRIVATE KEY") '
        '-stackoverflow -github',

        'site:*.com (ext:sql | ext:bak | ext:zip | ext:tar | ext:gz | ext:rar) '
        '("dump" | "backup" | "password" | "credentials") -stackoverflow -github',

        'site:*.com intitle:index.of (env | .git | .svn | backup | db.sql | .bak | config | secrets) '
        '-stackoverflow -github',

        'site:*.in ("Warning: mysql_fetch_assoc()" | "Warning: pg_connect()" | "Notice: Undefined index" | "System.Data.SqlClient.SqlException") '
        '-stackoverflow -github',

        'site:*.com (filetype:doc | filetype:docx | filetype:xls | filetype:xlsx | filetype:ppt | filetype:pptx) '
        '("password" | "credentials" | "db user" | "db pass" | "secret key") -stackoverflow -github',

        'site:*.com intitle:"index of" ".git"',

        'site:*.com filetype:sql "INSERT INTO" "VALUES"',

        'site:*.com filetype:env "APP_KEY="',

        'site:*.com intitle:"index of" ".svn"',
    ]
    return [dork.format(site) if '{}' in dork else dork for dork in dork_templates]


def main():
    site = input("Enter the site/domain (without 'www.' or TLD, e.g., 'example'): ")
    print("\nGenerated Google dork queries:\n")
    for query in generate_dork_queries(site):
        print(query)


if __name__ == "__main__":
    main()
