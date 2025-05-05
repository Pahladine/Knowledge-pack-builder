import tarfile, pathlib, subprocess, tempfile, shutil, requests, zstandard as zstd

OUT = pathlib.Path("knowledge-pack.tar.zst")
SRC_DIR = pathlib.Path("raw_sources"); SRC_DIR.mkdir(exist_ok=True)

# --- example pull: latest Rust RFC index ---
url = "https://raw.githubusercontent.com/rust-lang/rfcs/master/README.md"
SRC_DIR.joinpath("rust_rfcs_README.md").write_bytes(requests.get(url, timeout=30).content)

# TODO: add more fetchers (Discord dumps, Reddit API, CVE feeds …)

with tempfile.NamedTemporaryFile() as tmp:
    with tarfile.open(tmp.name, "w") as tar:
        for p in SRC_DIR.rglob("*"):
            tar.add(p, arcname=p.relative_to(SRC_DIR))
    tmp.flush()
    cctx = zstd.ZstdCompressor(level=19)
    OUT.write_bytes(cctx.compress(tmp.read()))
print("Created", OUT, "size:", OUT.stat().st_size, "bytes")
