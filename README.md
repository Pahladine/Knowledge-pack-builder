### How to use

1. Fork this repo to your own GitHub account.  
2. Wait ~10 min; open **Actions ▸ Build knowledge pack ▸ summary**.  
3. Download the **knowledge_slices** artifact.  
4. Upload every `knowledge-pack.tar.zst.*` file to GPT Creator → Knowledge tab.  
   ChatGPT re-assembles slices automatically.

**What happens after you fork**

- GitHub Actions will install Python, grab a sample source (the Rust RFC READ-ME), compress it, slice it into ~7 MB pieces, and bundle them for you.
- You don’t need to run anything locally.

**Next steps**

- Test this stub (you’ll get a tiny sample pack).
- When it works, let me know and we’ll expand `fetch_sources.py` to pull in all the feeds (Discord dumps, Reddit, CVEs, etc.).
