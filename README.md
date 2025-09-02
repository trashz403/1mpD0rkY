
# 🔍 1mpD0rkY – Google Dork Generator

A Python tool that helps penetration testers and bug bounty hunters generate **Google Dork queries** for a given target domain.
It prints both the raw queries and clickable Google search URLs so you can directly open them in your browser.

---

## ✨ Features

* Auto-generates a list of **Google dorks** for a given domain.
* Includes both **basic** and **advanced dorks** (for sensitive files, backups, exposed keys, DB dumps, etc.).
* Prints queries in two formats:

  * Plain text queries (for copy-paste).
  * Direct Google search URLs (clickable links).
* Developer credit shown at the start (`@trashz403`).

---

## 🚀 Usage

1. Clone this repo:

   ```bash
   git clone https://github.com/trashz403/1mpD0rkY.git
   cd 1mpD0rkY
   ```

2. Run the script:

   ```bash
   python3 1mpD0rkY.py
   ```

3. Enter the target domain (without `www.`):

   ```
   Enter the site/domain (without 'www.'): example.com
   ```

4. Get results:

   * Raw Google Dork queries
   * Direct Google search URLs

---

## 📌 Example

```
Generated Google dork queries:

site:example.com inurl:".php?Id=" inurl:"search"
site:example.com inurl:"&search="
...
```

```
Generated Google dork clickable URLs:

1. https://www.google.com/search?q=site%3Aexample.com%20inurl%3A%22.php%3FId%3D%22%20inurl%3A%22search%22
2. https://www.google.com/search?q=site%3Aexample.com%20inurl%3A%22%26search%3D%22
...
```

---

## 🤝 Contributing

Want to improve this tool? You can contribute by:

* Adding **new Google Dork templates**.
* Enhancing code (optimization, new features, output formatting, etc.).
* Reporting bugs or suggesting improvements.

To contribute:

1. Fork this repo
2. Add your dork queries in the `dork_templates` list inside `1mpD0rkY.py`
3. Create a pull request with your changes

---

## ⚠️ Disclaimer

This tool is for **educational and security research purposes only**.
Do **NOT** use it against systems without explicit permission.
The author is not responsible for any misuse of this script.

---

## 👤 Author

* **@trashz403**
* GitHub: [https://github.com/trashz403](https://github.com/trashz403)

---

Do you also want me to add a **Preview Screenshot** (example terminal output) section in the README so the repo looks more attractive on GitHub?
