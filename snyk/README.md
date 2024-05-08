# Snyk

Snyk's OpenAPI specification seems to configure both bearer authentication and manually add an `Authorization` header. Disable the bearer authentication method after importing a new OpenAPI specification document as follows:

```shell
find snyk/Snyk\ API\ REST/ \
    -name '*.json' -a -not '(' -name '_.json' -o -name 'restfox.json' ')' \
    -exec sh -c 'jq -r \'(.authentication.disabled = true)\' "{}" | sponge "{}"' \;
```
