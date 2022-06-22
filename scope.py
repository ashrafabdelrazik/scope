import requests
import sys

def main(bbp):
    url = "https://hackerone.com:443/graphql"
    headers = {"content-type": "application/json"}
    json={"operationName": "TeamAssets", "query": "query TeamAssets($handle: String!) {\n  me {\n    membership(team_handle: $handle) {\n      id\n      permissions\n    }\n  }\n  team(handle: $handle) {\n    handle\n    in_scope_assets: structured_scopes(\n      first: 650\n      archived: false\n      eligible_for_submission: true\n    ) {\n      edges {\n        node {\n          asset_type\n          asset_identifier\n\n          eligible_for_bounty\n          labels(first: 100) {\n            edges {\n              node {\n                id\n                name\n              }\n            }\n          }\n        }\n      }\n    }\n  }\n}\n", "variables": {"handle": str(bbp)}}
    r = requests.post(url, headers=headers, json=json)
    for x in r.json()["data"]["team"]["in_scope_assets"]["edges"]:
        if x["node"]["asset_type"] == "URL":
            print(x["node"]["asset_identifier"])
        else:
           continue

if __name__ == "__main__":
    try:
        bbp = sys.argv[1]
        main(bbp)
    except IndexError:
        print("[!] Example: python3 %s att" %sys.argv[0])
