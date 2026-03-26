# Product Requirements Document (PRD): Contract Family "Mint Version" Agent

## 1. Business Problem
Legal and contracts teams manually manage "contract families"—an original Master Agreement distributed across multiple Amendments. This fragmentation causes massive inefficiencies in summarizing agreements, drafting new amendments, and performing portfolio analytics because humans must manually cross-reference outdated clauses with new ones.

## 2. Product Vision
An AI-powered solution that automatically consolidates a contract family into a single, unified source of truth. The product supports two distinct workflows:
1. **Interactive Q&A RAG Agent (Online):** A fast, chat-based agent that uses deterministic metadata filtering paired with semantic search to quickly and cost-effectively answer questions (e.g., "What is our current payment term?") by finding the relevant chunks across the contract family and resolving conflicts chronologically.
2. **"Mint Version" Generation (Offline Batch Process):** An asynchronous pipeline that ingests a Master Agreement and its Amendments, evaluates all modifications, and generates a brand-new, unified document (the "Mint Version") reflecting the contract as-amended.

## 3. Core Capabilities
* **Targeted Semantic Retrieval**: Efficiently finding relevant clauses using Vector Search paired with strict `family_id` metadata filtering.
* **Temporal Tracking**: Tracing values (fees, dates, limits) chronologically from the Master agreement to the final Amendment within the retrieved chunks.
* **Conflict Resolution**: Accurately identifying when a newer clause explicitly overrides an older clause, and prioritizing the newer text using Gemini 2.5 Pro.
* **Net-New Analysis**: Diffing documents to find entirely new obligations added over time.

## 4. Evaluation Criteria
The prototype must pass the complex 10-question evaluation dataset located in `eval/RAG_EVALUATION_QUESTIONS.md`. These questions specifically stress-test temporal evolution, clause overrides, entity addition/removal, and date extensions.
