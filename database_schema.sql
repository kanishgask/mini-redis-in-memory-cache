-- Optional persistence for cache
CREATE TABLE cache_store (
    key VARCHAR(255) PRIMARY KEY,
    value TEXT,
    ttl BIGINT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
