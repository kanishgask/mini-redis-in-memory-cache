# 🏗️ Mini Redis Architecture

Client
   ↓
API
   ↓
Cache Node(s)
   ↓
Optional Persistent Storage

---

# Component Explanation

## Cache Node
- In-memory hash table
- TTL expiration
- Eviction policy (LRU)

## TTL Handling
- Background cleaner thread
- Delete expired keys

## Eviction Policy
- LRU (or FIFO simple)
- Memory-aware

## Optional Distributed Setup
- Multiple cache nodes
- Sharding keys via consistent hashing
- Replication for fault tolerance

---

# Scaling Strategy

- Horizontal scaling via sharding
- Replication for HA
- Background expiration thread
- Memory monitoring
