# git-token-scanner-hook
A pre-commit git hook to find tokens and API keys

## Usage 

- Download the repository and add the hook to your project in the .git/hooks/ folder.
- Or via CLI using `
```bash
python3 scan.py <file1> <file2>
```
Once a token is found, an Exception is raised, stopping the current commit process

## Sources

The json of regex to token scan is from https://github.com/dxa4481/truffleHogRegexes
