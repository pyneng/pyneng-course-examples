import json
data = {
    "login": "natenka",
    "url": "https://api.github.com/users/natenka",
    "html_url": "https://github.com/natenka",
    "starred_url": "https://api.github.com/users/natenka/starred{/owner}{/repo}",
    "type": "User",
    "site_admin": False,
    "name": "Наташа Самойленко",
    "company": None,
    "blog": "https://natenka.io/",
    "public_repos": 34,
    "public_gists": 3,
    "followers": 676,
    "following": 34,
    "created_at": "2015-11-14T20:32:44Z",
    "updated_at": "2022-10-26T11:07:11Z",
}

with open("json_files/result_ex05.json", "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
