import sys, pathlib
CHUNK = int(sys.argv[2])  # e.g. 7340032 ≈ 7 MB
src = pathlib.Path(sys.argv[1])
with src.open("rb") as f:
    i = 1
    while True:
        chunk = f.read(CHUNK)
        if not chunk:
            break
        part = src.with_suffix(src.suffix + f".{i:03d}")
        part.write_bytes(chunk)
        i += 1
print("Split into", i-1, "chunks.")
