from client import ContentDefinedChunking

def main():
    print("=== Testing FastCDC Content Defined Chunking ===")
    cdc = ContentDefinedChunking(min_size=16, target_size=32, max_size=64)
    sample_data = b"Antigravity Agentic Skill Distillation Architecture" * 10

    chunks = cdc.chunk_data(sample_data)
    print(f"Total payload: {len(sample_data)} bytes partitioned into {len(chunks)} variable chunks.")
    assert sum(len(c) for c in chunks) == len(sample_data)
    for idx, c in enumerate(chunks[:5]):
        print(f"  Chunk {idx}: len={len(c)} bytes")
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
