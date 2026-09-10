class ContentDefinedChunking:
    """
    FastCDC-inspired Content Defined Chunking (CDC).
    Identifies variable-size chunk boundaries based on rolling byte hash mask.
    Enforces min_size and max_size constraints.
    """
    def __init__(self, min_size=32, target_size=64, max_size=128):
        self.min_size = min_size
        self.target_size = target_size
        self.max_size = max_size
        self.mask = 0x1F

    def chunk_data(self, data_bytes):
        chunks = []
        n = len(data_bytes)
        curr = 0
        while curr < n:
            if n - curr <= self.min_size:
                chunks.append(data_bytes[curr:n])
                break

            start = curr
            curr += self.min_size
            rolling_hash = 0

            while curr < n and (curr - start) < self.max_size:
                byte_val = data_bytes[curr]
                rolling_hash = ((rolling_hash << 1) + byte_val) & 0xFFFFFFFF
                curr += 1
                if (rolling_hash & self.mask) == 0:
                    break

            chunks.append(data_bytes[start:curr])

        return chunks
