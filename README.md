# 🧠 Multi-Agent RAG Customer Support System using Ollama

## 🚀 What is this project?

This project implements a **multi-agent Retrieval-Augmented Generation (RAG)** system for customer support, powered by **Ollama**. It uses [LangChain](https://www.langchain.com/), [LangGraph](https://github.com/langchain-ai/langgraph), and a modular agent-based architecture to intelligently route queries about orders, returns, deliveries, and product info to specialized assistants.

![ytb logo](./images/ytb.png)  
📺 [Watch Demo Video](https://drive.google.com/file/d/1bHIurW52So11GKodWY5po4Pijg8xCruJ/view?usp=drivesdk)

---

## 🧠 Powered by Ollama

We use **Ollama** to run open-source LLMs like `llama2`, `mistral`, or `gemma` locally, enabling:
- Local inference
- Data privacy
- Low-latency responses
- Offline-friendly deployment

---

## 🗺️ Architecture Overview

The system is built as a **LangGraph state machine** where agents and tool nodes pass control based on conversation state and intent.

### Agents

- `Primary Assistant`: Entry point that routes queries to other agents.
- `Order Agent`: Places/tracks orders.
- `Returns Agent`: Manages returns/refunds.
- `Delivery Agent`: Answers logistics/delivery questions.
- `Product Agent`: Provides product info and suggestions.

### Core Features

- Multi-agent routing via LangGraph
- Vector search via Qdrant
- Memory/state via Redis
- Safe vs. sensitive tool use
- Integrated observability via LangSmith

![System Graph](./graphs/multi-agent-rag-system-graph.png)

---

## ☁️ Suggested AWS Architecture

![AWS Architecture](./images/multi_agent_rag_system_architecture_aws.png)

| Layer            | Components                                                                 |
|------------------|-----------------------------------------------------------------------------|
| **Data Layer**   | S3 (raw/clean/gold), Athena, Redshift, Qdrant (Vectors), ElastiCache (Redis) |
| **Processing**   | Airflow on EKS, EC2 embedding jobs, SageMaker/Bedrock (optional)            |
| **Chat Service** | EKS (LLM chat API), API Gateway, Ollama backend                             |
| **CI/CD**        | CodePipeline, CodeBuild, Docker (ECR)                                       |
| **Monitoring**   | CloudWatch, Grafana, Secrets Manager                                        |

---

## 🔍 Observability with LangSmith

LangSmith tracks:
- Agent tool usage
- Vector search results
- Generated responses
- Model confidence
- Error traces

![LangSmith](./images/langsmith.gif)

---

## 🧪 Requirements

- Python 3.12+
- [Poetry](https://python-poetry.org/docs/#installation)
- Docker & Docker Compose
- [Ollama](https://ollama.com/)
- LangSmith API key (optional)

---

## 🛠️ Setup Guide

### 1. Clone the repository
```bash
git clone https://github.com/Vivek17020/SupportHive.git
cd SupportHive
```

### 2. Setup environment
```bash
cp .dev.env .env
```

Update `.env` file with:
```env
OLLAMA_MODEL=llama2
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_key # Optional
```

### 3. Install dependencies
```bash
poetry install
```

### 4. Generate vector embeddings
```bash
poetry run python vectorizer/app/main.py
```

### 5. Start Qdrant vector database
```bash
docker compose up qdrant -d
```

### 6. Run customer support system
```bash
poetry run python ./customer_support_chat/app/main.py
```

> Access Qdrant UI at: [http://localhost:6333/dashboard#](http://localhost:6333/dashboard#)

---

## 🧾 Project Structure

```text
├── vectorizer/                  # Embedding generation pipeline
├── customer_support_chat/       # Main multi-agent chat system
├── graphs/                      # LangGraph system graphs
├── images/                      # Architecture and demo visuals
├── .env                         # Environment configuration
├── docker-compose.yml           # Services: Qdrant, Ollama (optional)
├── README.md
```

---

## 📊 Data Sources

- **Travel DB (template)**: LangGraph Travel Benchmark
- ![travel_db_schema](https://github.com/user-attachments/assets/95f26921-c3b5-49ae-84c0-f6c1b4252e71)

- **Qdrant**:Stores embeddings for vector search
-  ![qdrant_schema](https://github.com/user-attachments/assets/0b427aef-ccb3-404d-bc60-1666f20e6a2a)
- **Redis**: Maintains chat memory and conversation history
- **Local documents**: (Can include product catalogs, FAQs, order info, etc.)

---

📂 Custom Dataset Justification

For this project, we decided to work with a custom travel-focused dataset instead of the synthetic one provided by the hackathon organizers. The reason? Realism and richness. Our dataset mirrors a real-world travel and airline system — it includes detailed flight schedules, airport data, bookings, seat assignments, car rentals, hotel reservations, and even trip recommendations.

This allowed us to build a much more robust, interactive, and intelligent customer support system. Our multi-agent framework powered by Ollama, LangGraph, and LangChain can now handle deeper queries like:

- Booking or modifying travel itineraries
- Checking seat availability or flight delays
- Managing hotel or car rental services
- Giving smart travel recommendations based on history or preferences

By using a dataset that simulates actual travel operations, we’re able to demonstrate the full potential of our system in realistic customer service scenarios — something that wouldn't be possible with a synthetic dataset. It’s all about grounding the intelligence in context that matters.

## 💡 Enhancements / Next Steps

### 🔍 Tool Upgrades
- ✅ **Adaptive RAG**: Smarter query refinement for vector tools
- 🔄 **Corrective RAG**: Retry if poor grounding from vectors
- 🧠 **Self-RAG**: Rerank outputs based on grounding score

### 🧠 Agent Memory
- Redis-based memory per customer session
- Agents remember recent intents, issues, preferences

### 🤖 LangGraph Optimization
- Richer conditional logic for agent handoffs
- Fallback flows (retry failed tool calls with alternate agents)

---

## 🛠️ Tech Stack

- 🧠 **Ollama** — local LLM runtime
- 🔗 **LangGraph & LangChain** — multi-agent orchestration
- 🔍 **Qdrant** — vector search engine
- 🐍 **Python + Poetry**
- 🐳 **Docker + Docker Compose**
- 📈 **Grafana, CloudWatch** — observability
- 🔐 **Secrets Manager** — secure API key storage

---



## 📎 Reference Links

- [LangGraph Adaptive RAG](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag/)
- [Corrective RAG Paper](https://arxiv.org/abs/2401.15884)
- [LangGraph Self-RAG Tutorial](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/)
- [Ollama Docs](https://ollama.com/)
