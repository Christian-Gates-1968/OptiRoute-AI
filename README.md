# 🚀 OptiRoute AI - Intelligent GenAI Router

**An intelligent middleware system that optimizes GenAI costs by routing queries to the most appropriate model based on complexity analysis.**

---

## 🎯 The Problem

Companies waste thousands of dollars sending simple queries (like "Hello" or "What is Python?") to expensive models like GPT-4. Most production systems use a single model for all queries, regardless of complexity.

## 💡 The Solution

**OptiRoute AI** analyzes incoming prompts in real-time and intelligently routes them:
- **Simple queries** → Fast, cost-efficient models (Llama 3 via Groq)
- **Complex queries** → High-reasoning models (GPT-4)

This demonstrates **cost-of-inference optimization** and **architectural thinking** required for scalable GenAI systems.

---

## 🏗️ Architecture

```
┌─────────────┐
│   User      │
│   Prompt    │
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│  Complexity         │
│  Analyzer           │
│  - Word count       │
│  - Keyword detection│
└──────┬──────────────┘
       │
       ├──── Simple ───────► Groq (Llama 3) ──► ⚡ Fast & Cheap
       │
       └──── Complex ──────► OpenAI (GPT-4) ──► 🧠 Smart & Deep
```

---

## 🛠️ Tech Stack

| Layer | Technology | Reason |
|-------|------------|--------|
| **Frontend** | Streamlit | Rapid prototyping, clean UI |
| **Backend Logic** | Python + LangChain | Industry standard for AI orchestration |
| **AI Models** | GPT-4 (OpenAI) + Llama 3 (Groq) | High quality + High speed options |
| **Environment** | python-dotenv | Security best practices |

---

## 📁 Project Structure

```
OptiRoute AI/
├── app.py                 # Streamlit dashboard (Frontend)
├── router.py              # Intelligence layer (Core Logic)
├── requirements.txt       # Python dependencies
├── .env.example           # API key template
├── .gitignore            # Git exclusions
└── README.md             # This file
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- OpenAI API key ([Get here](https://platform.openai.com/api-keys))
- Groq API key ([Get here](https://console.groq.com/keys) - **FREE**)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/optiroute-ai.git
cd optiroute-ai
```

2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**
```bash
cp .env.example .env
# Edit .env and add your API keys
```

5. **Run the application:**
```bash
streamlit run app.py
```

6. **Open your browser:**
Navigate to `http://localhost:8501`

---

## 💻 Usage

### Example Queries

**Simple Query** (Routes to Groq/Llama 3):
```
"What is Python?"
"Hello, how are you?"
"Define machine learning"
```

**Complex Query** (Routes to GPT-4):
```
"Explain the differences between REST and GraphQL APIs"
"Analyze the trade-offs between microservices and monolithic architecture"
"Why is asynchronous programming important for scalability?"
```

---

## 🧠 Routing Logic

The system analyzes prompts using two heuristics:

1. **Word Count Analysis**
   - Simple: ≤ 15 words → Groq (Fast)
   - Complex: > 15 words → GPT-4 (Smart)

2. **Keyword Detection**
   - Contains reasoning keywords ("explain", "analyze", "compare", "why") → GPT-4
   - No reasoning keywords → Groq

---

## 📊 Cost Optimization

### Estimated Savings

| Scenario | Traditional (All GPT-4) | OptiRoute AI | Savings |
|----------|------------------------|--------------|---------|
| 1000 simple queries | $30 | $2 | **$28 (93%)** |
| 1000 mixed queries | $30 | $15 | **$15 (50%)** |

*Based on approximate pricing: GPT-4 ($0.03/request), Llama 3 via Groq ($0.002/request)*

---

## 🔮 Future Scaling Strategy

### Phase 1: Current State (MVP)
- API-based routing (OpenAI + Groq)
- Simple complexity heuristics
- Streamlit dashboard

### Phase 2: Advanced Intelligence (Month 2-3)
- ML-based complexity classifier (Fine-tuned BERT)
- Semantic caching with Redis (avoid duplicate LLM calls)
- PostgreSQL for analytics and usage tracking

### Phase 3: Self-Hosted Infrastructure (Month 6+)
**When user base hits 10k+:**
- Deploy self-hosted Llama 3 on AWS Inferentia or NVIDIA A100s
- Kubernetes orchestration for GPU workloads
- Load balancing across multiple model instances
- Cost reduction: API ($0.002/req) → Self-hosted ($0.0005/req)

**Infrastructure Blueprint:**
```yaml
# Kubernetes deployment example
apiVersion: apps/v1
kind: Deployment
metadata:
  name: llama3-inference
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: llama3
        image: vllm/llama3:latest
        resources:
          limits:
            nvidia.com/gpu: 1
```

---

## 🎓 Key Learnings & Trade-offs

### Architecture Decisions

| Decision | Why | Trade-off |
|----------|-----|-----------|
| **LangChain** | Standard abstraction layer for LLMs | Adds dependency, but enables model swapping |
| **Streamlit** | Fastest MVP frontend | Not for production scale, but perfect for demos |
| **Groq (not local Llama)** | <100ms latency vs 2-3s local | API cost vs infrastructure cost |
| **Simple heuristics** | Ship fast, iterate later | Less accurate than ML, but good enough for MVP |

### What I'd Do Differently at Scale
- **Rate Limiting**: Implement per-user quotas with Redis
- **Observability**: Add OpenTelemetry for tracing and monitoring
- **A/B Testing**: Track accuracy metrics (user satisfaction) per routing decision
- **Cost Analytics**: Real-time dashboard showing $ saved per user

---

## 🧪 Testing

Run the test suite:
```bash
# Unit tests
pytest tests/

# Test routing logic
python -c "from router import ModelRouter; r = ModelRouter(); print(r.analyze_complexity('What is Python?'))"
```

---

## 🤝 Contributing

This project demonstrates a **Founding Engineer mindset**:
1. **Velocity over perfection** - Ship fast, iterate based on metrics
2. **Business-aware architecture** - Every decision considers cost and scale
3. **First-principles thinking** - Not just chaining libraries, but understanding trade-offs

---

## 📝 License

MIT License - Feel free to use this for your interviews and projects!

---

## 👨‍💻 About

Built as a demonstration of:
- **AI/ML Engineering**: Multi-model orchestration
- **System Design**: Routing, caching, cost optimization
- **Product Thinking**: Solving real business problems (inference costs)
- **Speed**: Built in <24 hours to demonstrate "high slope" learning ability

**Built by:** A Founding Engineer candidate
**Tech Used for First Time:** Groq LPU API (learned and integrated in 4 hours)
**Business Impact:** Potential 50-90% cost reduction in GenAI operations

---

## 🔗 Links

- [OpenAI Documentation](https://platform.openai.com/docs)
- [Groq Console](https://console.groq.com)
- [LangChain Docs](https://python.langchain.com)
- [Streamlit Docs](https://docs.streamlit.io)

---

**Ready to optimize your GenAI costs? Let's connect!** 🚀
