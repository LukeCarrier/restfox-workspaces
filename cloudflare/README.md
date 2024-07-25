# Cloudflare

Cloudflare tag their resources but don't group them. Fix that:

```shell
poetry run cloudflare <document.json >openai.yaml
```

Strip inconsistent auth away:

```shell
find cloudflare \
    -type f -name '*.json' -not '(' -name '_.json' -or -name 'restfox.json' ')' \
    -exec sh -c 'jq -r \'["X-Auth-Email", "X-Auth-Key"] as $dropHeaders | .headers |= map(select(.name as $headerName | $dropHeaders | all(. != $headerName)))\' "{}" | sponge "{}"' \;
```

And authentication methods:

```shell
find cloudflare \
    -type f -name '*.json' -not '(' -name '_.json' -or -name 'restfox.json' ')' \
    -exec sh -c 'jq -r \'.authentication |= {"type": "No Auth"}\' "{}" | sponge "{}"'
```
