# 🚀 OptiRoute AI - Intelligent GenAI Router

**An intelligent middleware system that optimizes GenAI costs by routing queries to the most appropriate model based on complexity analysis.**

---

## 🎯 The Problem

Companies waste thousands of dollars sending simple queries (like "Hello" or "What is Python?") to expensive models like GPT-4. Most production systems use a single model for all queries, regardless of complexity.

## 💡 The Solution

**OptiRoute AI** analyzes incoming prompts in real-time and intelligently routes them:
- **Simple queries** → Ultra-fast models (Llama 3.1 8B via Groq)
- **Complex queries** → High-reasoning models (Llama 3.3 70B via Groq)

This demonstrates **cost-of-inference optimization** and **architectural thinking** required for scalable GenAI systems - all while running on free-tier infrastructure.

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
       ├──── Simple ───────► Groq (Llama 3.1 8B) ──► ⚡ Ultra Fast & Free
       │
       └──── Complex ──────► Groq (Llama 3.3 70B) ──► 🧠 Smart & Free
```

---

## 🛠️ Tech Stack

| Layer | Technology | Reason |
|-------|------------|--------|
| **Frontend** | Streamlit | Rapid prototyping, clean UI |
| **Backend Logic** | Python + LangChain | Industry standard for AI orchestration |
| **AI Models** | Llama 3.1 8B + Llama 3.3 70B (Groq) | Zero-cost, production-grade speed |
| **Deployment** | Docker + Docker Compose | Containerization for consistency & portability |
| **Environment** | python-dotenv | Security best practices |

---

## 📁 Project Structure

```
OptiRoute AI/
├── app.py                 # Streamlit dashboard (Frontend)
├── router.py              # Intelligence layer (Core Logic)
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker image configuration
├── docker-compose.yml     # Docker orchestration
├── .dockerignore          # Docker build exclusions
├── .env                   # Environment variables (not committed)
├── .env.example           # API key template
├── .gitignore            # Git exclusions
└── README.md             # This file
```

---

## 🚀 Quick Start

### Prerequisites
- **Option 1 (Docker - Recommended):** Docker Desktop installed
- **Option 2 (Manual):** Python 3.8 or higher
- Groq API key ([Get here](https://console.groq.com/keys) - **100% FREE, No Credit Card**)

### 🐳 Option 1: Docker Deployment (Recommended)

**Fastest way to get started - One command deployment!**

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/optiroute-ai.git
cd optiroute-ai
```

2. **Set up environment variables:**
```bash
cp .env.example .env
# Edit .env and add your GROQ_API_KEY (get it free at console.groq.com)
```

3. **Build and run with Docker Compose:**
```bash
docker-compose up -d
```

4. **Access the application:**
Navigate to `http://localhost:8501`

**Useful Docker Commands:**
```bash
# View logs
docker logs optiroute-ai -f

# Stop the application
docker-compose down

# Restart
docker-compose restart

# Rebuild after code changes
docker-compose up -d --build
```

**Benefits of Docker:**
- ✅ Zero Python dependency conflicts
- ✅ Works identically on Windows, Mac, Linux
- ✅ Production-ready containerization
- ✅ Easy deployment to cloud (AWS, GCP, Azure)

---

### 💻 Option 2: Manual Installation

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
# Edit .env and add your GROQ_API_KEY (get it free at console.groq.com)
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

**Simple Query** (Routes to Llama 3.1 8B - Ultra Fast):
```
"What is Python?"
"Hello, how are you?"
"Define machine learning"
```

**Complex Query** (Routes to Llama 3.3 70B - Smart Reasoning):
```
"Explain the differences between REST and GraphQL APIs"
"Analyze the trade-offs between microservices and monolithic architecture"
"Why is asynchronous programming important for scalability?"
```

---

## 🧠 Routing Logic

The system analyzes prompts using two heuristics:

1. **Word Count Analysis**
   - Simple: ≤ 15 words → Llama 3.1 8B (Ultra Fast)
   - Complex: > 15 words → Llama 3.3 70B (Smart)

2. **Keyword Detection**
   - Contains reasoning keywords ("explain", "analyze", "compare", "why") → Llama 3.3 70B
   - No reasoning keywords → Llama 3.1 8B

---

## 📊 Cost Optimization

### Estimated Savings

| Scenario | Traditional (All GPT-4) | OptiRoute AI (Groq) | Savings |
|----------|------------------------|---------------------|---------||
| 1000 simple queries | $30 | **$0** (Free) | **$30 (100%)** |
| 1000 mixed queries | $30 | **$0** (Free) | **$30 (100%)** |
| 10,000 requests/day | $300/day | **$0** (Free tier) | **$300/day** |

*Groq offers 14,400 free requests per day - perfect for startups and demos!*

---

## 🔮 Future Scaling Strategy

### Phase 1: Current State (MVP)
- Dual-model routing (Both via Groq - 100% free)
- Simple complexity heuristics
- Streamlit dashboard

### Phase 2: Advanced Intelligence (Month 2-3)
- ML-based complexity classifier (Fine-tuned BERT)
- Semantic caching with Redis (avoid duplicate LLM calls)
- PostgreSQL for analytics and usage tracking
- Add GPT-4/Claude for mission-critical queries (hybrid approach)

### Phase 3: Self-Hosted Infrastructure (Month 6+)
**When user base exceeds Groq's free tier (14k+ requests/day):**
- Option A: Groq paid tier (still cheaper than others)
- Option B: Self-hosted Llama 3 on AWS Inferentia or NVIDIA A100s
- Kubernetes orchestration for GPU workloads
- Load balancing across multiple model instances

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
| **Groq (both models)** | <100ms latency + zero cost | Free tier limits (14k/day), but perfect for MVP || **Docker** | Containerization for deployment | Adds overhead, but ensures portability and consistency || **Simple heuristics** | Ship fast, iterate later | Less accurate than ML, but good enough for MVP |
| **No OpenAI** | Avoid costs during development | Can add later for premium features |

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
**Business Impact:** 100% cost reduction in GenAI operations (vs traditional GPT-4-only approach)

---

## 🔗 Links

- [OpenAI Documentation](https://platform.openai.com/docs)
- [Groq Console](https://console.groq.com)
- [LangChain Docs](https://python.langchain.com)
- [Streamlit Docs](https://docs.streamlit.io)

---

**Ready to optimize your GenAI costs? Let's connect!** 🚀
