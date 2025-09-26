# GPT Slack Bot

Bot Slack używający OpenAI i Flask.

## Jak używać

1. Skonfiguruj zmienne środowiskowe:
   - `OPENAI_API_KEY`
   - `SLACK_BOT_TOKEN`

2. Wdrażaj na Render:
   - Połącz ze swoim repozytorium GitHub
   - Wybierz plik `render.yaml` (lub ustaw ręcznie)
   - Deploy

3. W Slack:
   - Ustaw endpoint do `/slack/events`
   - Dodaj potrzebne uprawnienia: `chat:write`, `channels:history`, itp.
