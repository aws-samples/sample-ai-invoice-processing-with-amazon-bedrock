---
inclusion: manual
---

# Optional: Builder MCP Server

Builder MCP gives your AI agent access to internal Amazon tools and documentation. It's included in APEX Extension but disabled by default since it requires Builder Toolbox installation.

## What You Get

- **ReadInternalWebsites** - Access wikis, Quip docs, and internal documentation
- **InternalSearch** - Search Amazon's internal knowledge base
- **Taskei** - Read and manage tasks
- **AcronymCentral** - Decode Amazon acronyms
- **Code Review Tools** - Integration with internal code review systems
- **Project Tracking** - Automatic tagging with ProServe job IDs and Salesforce opportunity IDs

## Should You Enable It?

**Yes, if you need:**
- Access to internal Amazon wikis, Quip docs, and knowledge bases during AI workflows
- Automatic project attribution with ProServe job IDs and Salesforce opportunity IDs

**No, if you're:**
- Working on public/open-source projects
- Prefer minimal MCP setup

## Setup (3 Steps)

### 1. Install Builder Toolbox
```bash
# Follow: https://docs.hub.amazon.dev/builder-toolbox/user-guide/getting-started/
```

### 2. Install Builder MCP
```bash
toolbox install mcp-registry && mcp-registry install builder-mcp
```

### 3. Enable in Your IDE

**Kiro** - Edit `.kiro/settings/mcp.json`:
```json
"builder-mcp": {
  "command": "builder-mcp",
  "args": [],
  "disabled": false,  // Change from true
  "autoApprove": []
}
```

**Cline** - Edit `~/.cline/mcp_settings.json` and enable builder-mcp

**Amazon Q CLI** - Edit `.amazonq/mcp.json` and enable builder-mcp

**Cursor** - Edit `.cursor/mcp.json` and enable builder-mcp

## Resources

- [Builder Toolbox Docs](https://docs.hub.amazon.dev/builder-toolbox/user-guide/getting-started/)
- [MCP Guidance](https://docs.hub.amazon.dev/gen-ai-dev/mcp-guidance/#using-model-context-protocol-servers)
- [Builder MCP Registry](https://console.harmony.a2z.com/mcp-registry/server/builder-mcp)
- [Building Effective Artifacts](https://w.amazon.com/bin/view/AWS/Teams/Proserve/Portal/APEX/Blog/BuildingEffectiveArtifacts)
