# Agent Implementation Tasks (Granular)

## Phase 1: Infrastructure Setup (GCP)
- [ ] Create GCS bucket `gs://legal-agent-contracts` for raw PDFs.
- [ ] Create GCS bucket `gs://legal-agent-parsed-json` for Document AI output storage.
- [ ] Enable the Document AI API.
- [ ] Create a Document Processor of type **"Layout Parser"** (to preserve hierarchical context-aware chunks).
- [ ] Save `PROCESSOR_ID` and `LOCATION` to environment config.
- [ ] Enable the Vertex AI API.
- [ ] Create a Service Account for index creation and querying.
- [ ] Implement `infra/setup_infra.sh` to automate bucket creation and API enablement.
- [ ] Implement `infra/setup_document_ai.py` creating the Layout Parser processor
- [ ] Implement `infra/setup_vector_search.py` (Python SDK) to create the vector index.
- [ ] Execute index creation and wait for Index Endpoint deployment (long-running).

## Phase 2: Data Pipeline Build
- [ ] Move `real_contract_families` data to `./data/real_contract_families/`.
- [ ] Implement `data_ingestion/upload_to_gcs.py` to sync local files to GCS.
- [ ] Implement `data_ingestion/process_with_doc_ai.py` using `google-cloud-documentai` for Layout Parsing.
- [ ] Implement `data_ingestion/llm_metadata_extractor.py` using Gemini Flash structured output to extract `effective_date`, `document_type`, and `amendment_number`.
- [ ] Implement `data_ingestion/parse_doc_ai_json.py` to extract context-aware text blocks and attach the LLM-extracted metadata.
- [ ] Implement `data_ingestion/generate_embeddings.py` using Vertex TextEmbedding. Ensure Datapoints strictly structure `family_id` within the **`restricts`** field (e.g., `{'namespace': 'family_id', 'allow': [...]}`).
- [ ] Batch upload semantic chunks with `restricts` to the vector search index.

## Phase 3: Agent Creation (Google ADK)
- [ ] Initialize standard Python Workspace for Google ADK.
- [ ] Define main dependencies in `requirements.txt`.
- [ ] Implement `agent/family_retrieval_tool.py` using GCP `MatchingEngineIndexEndpoint` to query by semantic intent, ensuring the **`restricts`** parameter is passed to filter by `family_id`.
- [ ] Implement `agent/context_grouper.py` to take retrieved Top-K chunks and sort them chronologically by `effective_date`.
- [ ] Implement `agent/prompts.py` containing the system instruction prompt for Gemini 2.5 Pro.
- [ ] Instruct Gemini on zero-shot reasoning regarding date overrides and limit updates using the chronologically ordered chunks.
- [ ] Implement `agent/agent_main.py` tying the ADK loop to Gemini 2.5 Pro.

## Phase 4: Evaluation & Vertex AI Publishing
- [ ] Move `RAG_EVALUATION_QUESTIONS.md` into `./eval/`.
- [ ] Implement `eval/run_eval.py` to run loop over all 10 questions.
- [ ] Generate standard response output for human grading.
- [ ] Validate results, tweak prompt instructions for precision (e.g., date formats).
- [ ] Implement `infra/deploy_agent_engine.py` incorporating the Vertex AI Python SDK. Define the Agent app class locally.
- [ ] Deploy the app by calling `vertexai.preview.reasoning_engines.ReasoningEngine.create(app, requirements=["google-adk", ...])`.
