## GitHub Copilot Chat

- Extension Version: 0.26.3 (prod)
- VS Code: vscode/1.99.2
- OS: Linux
- Remote Name: wsl

## Network

User Settings:
```json
  "github.copilot.advanced.debug.useElectronFetcher": true,
  "github.copilot.advanced.debug.useNodeFetcher": false,
  "github.copilot.advanced.debug.useNodeFetchFetcher": true
```

Connecting to https://api.github.com:
- DNS ipv4 Lookup: 140.82.121.6 (56 ms)
- DNS ipv6 Lookup: Error (50 ms): getaddrinfo ENOTFOUND api.github.com
- Proxy URL: None (5 ms)
- Electron fetch: Unavailable
- Node.js https: timed out after 10 seconds
- Node.js fetch (configured): timed out after 10 seconds
- Helix fetch: timed out after 10 seconds

Connecting to https://api.individual.githubcopilot.com/_ping:
- DNS ipv4 Lookup: 140.82.114.21 (34 ms)
- DNS ipv6 Lookup: Error (27 ms): getaddrinfo ENOTFOUND api.individual.githubcopilot.com
- Proxy URL: None (1 ms)
- Electron fetch: Unavailable
- Node.js https: timed out after 10 seconds
- Node.js fetch (configured): timed out after 10 seconds
- Helix fetch: timed out after 10 seconds

## Documentation

In corporate networks: [Troubleshooting firewall settings for GitHub Copilot](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-firewall-settings-for-github-copilot).