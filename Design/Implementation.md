# Legal Contract RAG Agent: Contract Family "Mint Version"

## Goal Description
To build a GCP-backed, AI-powered Retrieval-Augmented Generation (RAG) agent that automatically synthesizes a "contract family" (Master Agreement + Amendments) into a unified answer. The agent must parse complex temporal relationships, accurately resolve clause overrides, and diff documents to extract net-new obligations.

## Proposed Architecture
The implementation uses a **Hybrid Metadata-Filtered Semantic Retrieval Strategy** to ensure cost-efficiency and high accuracy on temporal overrides, fully aligned with current Google Cloud APIs.

**Core Stack:**
- **Parsing:** GCP Document AI (**Layout Parser** for hierarchical context-aware chunks).
- **Metadata Extraction:** Gemini Flash (Deterministically extracts `effective_date` and `amendment_number`).
- **Vector DB:** Vertex AI Vector Search (Indexed with semantic intent + **`restricts`** boolean filtering for `family_id`).
- **Reasoning Engine:** Gemini 2.5 Pro (Resolves conflicts on the retrieved, chronologically-sorted Top-K chunks).
- **Orchestration:** Google Agent Development Kit (ADK).
- **Publishing:** Vertex AI Reasoning Engine (**Python SDK Deployment**).

## Proposed Changes (Task Phasing)
This mirrors our drafted `TASKS.md` for execution tracking:

### Phase 1: Infrastructure Setup (GCP)
- Deploy GCS Buckets (Raw PDFs and JSONs).
- Instantiate Document AI Layout Parser.
- Provision Vertex AI Vector Search (Index & Endpoint).
- Distinct scripts for setup (`setup_infra.sh`, `setup_document_ai.py`, `setup_vector_search.py`).

### Phase 2: Data Pipeline Build
- Reorganize `real_contract_families` data to `./data/`.
- Script PDF -> Document AI ingestion.
- Script LLM-based metadata extraction (Gemini Flash).
- Compute embeddings and upload to Vector Search using `restricts` field for categorical filters.

### Phase 3: Agent Creation (Google ADK)
- Configure `FamilyRetrievalTool` using Vector Search semantic query + `restricts` tags.
- Program context sorting logic (Chronological override sequence for Top-K chunks).
- Parameterize the Gemini 2.5 Pro system prompts.

### Phase 4: Publishing & Evaluation
- Move `RAG_EVALUATION_QUESTIONS.md` dataset to `./eval/`.
- Execute agent against the evaluation dataset.
- Package and publish via `deploy_agent_engine.py` using `ReasoningEngine.create()`.

## Verification Plan
### Automated & Manual Testing
- The primary source of truth for success is achieving accurate responses to the 10 questions outlined in the Evaluation Dataset regarding temporal override tracking and entity diffs.
