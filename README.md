# FeedbackIQ

**FeedbackIQ** is a real-time feedback intelligence platform that processes user feedback streams, identifies sentiment and emerging issues, and uses RAG and AI agents to investigate and explain customer feedback patterns.

The platform simulates a continuous stream of user feedback through Kafka. PySpark Structured Streaming processes and enriches the incoming data, performs real-time aggregations and anomaly detection, and stores the processed data for analytics. Feedback is also embedded into a vector database, enabling semantic search and RAG-based investigation.

An AI agent combines structured analytics with retrieved feedback, product documentation, release notes, and incident history to investigate issues and generate actionable insights.

## Key Capabilities

* Real-time feedback ingestion using Kafka
* Stream processing with PySpark Structured Streaming
* Data cleaning, validation, deduplication, and enrichment
* Sentiment and feedback classification
* Real-time sentiment and category analytics
* Anomaly and emerging-issue detection
* Semantic search over historical feedback
* RAG-based contextual analysis
* AI agent for feedback investigation and root-cause analysis
* Analytics dashboard for monitoring feedback trends

## Tech Stack

### Data Engineering

* **Apache Kafka** — real-time event streaming
* **PySpark** — distributed stream and batch processing
* **Python** — data processing and application logic
* **Parquet / Data Lake** — analytical data storage

### AI / ML

* **Hugging Face Transformers** — sentiment and NLP models
* **Embeddings** — semantic representation of feedback
* **Qdrant** — vector database
* **RAG** — contextual retrieval and analysis
* **LangChain / LangGraph** — AI agent and orchestration

### Infrastructure

* **Docker / Docker Compose** — local infrastructure
* **PostgreSQL** — structured analytical/application data
* **MinIO** — S3-compatible object storage
* **Ollama** — local LLM inference

### Visualization

* **Streamlit** — feedback intelligence dashboard

## High-Level Architecture

```text
User Feedback
     │
     ▼
   Kafka
     │
     ▼
PySpark Structured Streaming
     │
     ├── Cleaning & Validation
     ├── Deduplication
     ├── Sentiment Analysis
     ├── Classification
     ├── Aggregations
     └── Anomaly Detection
     │
     ├──────────────► Data Lake / PostgreSQL
     │
     └──────────────► Embeddings ──► Qdrant
                                      │
                                      ▼
                              RAG / AI Agent
                                      │
                         ┌────────────┼────────────┐
                         ▼            ▼            ▼
                    Feedback      Product      Incident
                    History        Docs        History
                         │            │            │
                         └────────────┼────────────┘
                                      ▼
                              Investigation
                                      │
                                      ▼
                                Streamlit
                                  Dashboard
```

## Project Goal

The goal of FeedbackIQ is to demonstrate an end-to-end **real-time data engineering + machine learning + RAG + agentic AI** system, where streaming data is transformed into actionable intelligence rather than simply being used as input to a chatbot.
