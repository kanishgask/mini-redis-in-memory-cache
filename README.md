# ⚡ Mini Redis - In-Memory Cache

> Day 10 – High-Performance Distributed Backend Systems

---

## 📌 Problem Statement

Build a simplified in-memory key-value store similar to Redis:

- Support GET/SET operations
- Support TTL (Time-To-Live)
- Eviction policies (LRU)
- Optional distributed replication

---

# 🎯 Functional Requirements

- SET key value
- GET key
- DELETE key
- TTL per key
- Eviction when memory limit reached

---

# ⚙️ Non-Functional Requirements

- Extremely low latency
- High throughput
- In-memory for speed
- Support millions of keys
- Eviction policies for memory efficiency

---

# 🧠 Core Concepts

✔ Hash Table for fast access  
✔ Doubly Linked List for LRU  
✔ TTL handling (expiration)  
✔ Optional replication  
✔ Distributed caching ideas  

---

# 📊 High-Level Architecture

Client → API → Cache Nodes → Optional Persistent Storage
