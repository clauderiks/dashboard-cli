# riks
Clauderiks

Hay. Nếu mục tiêu của bạn là Risk AI có khả năng như Codex (đọc code, sửa code, chạy lệnh, dùng tool), mình sẽ thiết kế theo hướng hiện đại và mở rộng được.
Kiến trúc Risk AI
                Risk AI
                   │
     ┌─────────────┴─────────────┐
     │                           │
  Chat Engine               Agent Engine
     │                           │
     │                    Planner
     │                    Memory
     │                    Tool Router
     │                           │
     └─────────────┬─────────────┘
                   │
        Open Source LLM
     (Qwen / DeepSeek / Llama)
                   │
        ┌──────────┼──────────┐
        │          │          │
     Terminal    GitHub     Browser
        │          │          │
      Docker      Git       Search

Công nghệ
Backend
Python + FastAPI
vLLM hoặc Ollama
LangGraph hoặc framework agent tự viết
LLM
Qwen
DeepSeek
Llama
Vector DB
ChromaDB
Qdrant
FAISS
Memory
SQLite
PostgreSQL
Frontend
Next.js
React
Flutter (nếu muốn app)
Cấu trúc dự án
risk-ai/
│
├── backend/
│   ├── api/
│   ├── agents/
│   ├── memory/
│   ├── models/
│   ├── tools/
│   ├── rag/
│   └── main.py
│
├── frontend/
│
├── docker/
│
├── docs/
│
└── config/

Tính năng
Chat như ChatGPT
Đọc toàn bộ project
Viết và sửa code
Thực thi lệnh trong sandbox Docker
Tool calling
GitHub integration
Bộ nhớ dài hạn
RAG để đọc tài liệu
Hỗ trợ nhiều mô hình AI
Các giai đoạn phát triển
v0.1: Chat với LLM.
v0.2: Thêm tool calling (đọc/ghi file, terminal).
v0.3: Agent tự lập kế hoạch và thực hiện nhiều bước.
v0.4: RAG + bộ nhớ dài hạn.
v1.0: IDE assistant kiểu Codex, có thể phân tích và chỉnh sửa cả repository.
Nếu bạn muốn dự án có phong cách riêng, mình cũng có thể giúp thiết kế Risk AI Core, gồm:
RiskAgent (điều phối tác vụ)
RiskCoder (lập trình)
RiskSearch (tìm kiếm)
RiskMemory (ghi nhớ)
RiskPlanner (lập kế hoạch)
RiskTools (quản lý và gọi công cụ)
Cách này sẽ tạo ra một hệ thống có kiến trúc riêng thay vì chỉ sao chép trải nghiệm của Codex.