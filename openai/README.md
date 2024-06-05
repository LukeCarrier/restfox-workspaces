# OpenAI

Lots of long names.

```shell
curl -o openai.yaml https://raw.githubusercontent.com/openai/openai-openapi/master/openapi.yaml
```

At the time of writing you'll need to manually fix issues with the following YAML anchors and aliases:

- `run_temperature_description`
- `run_top_p_description`

Then fix naming issues:

```shell
poetry run openapi <openapi.yaml >openai.fixed.yaml
```
