# Prompt Log

## Prompt 1
> ok, please create a markdown file in ./legal_agent and keep track of everything I'm prompting to you (including this prompt). We'll have a design discussion, you'll capture a PRD.md a SPEC.md and a TASKS.md file in the end. We're sctriclty in planning mode, DO NOT CODE till I tell you explicitly and please don't ask me for permission to change or produce code till I explicitly tell you to

## Prompt 2
> OK here's our high level business problem word for word: "AI-powered solution that automatically consolidates a “contract family”—an original contract and its amendments—into a single, unified “Mint Version” that reflects the contract as-amended. By integrating all amendments and surfacing key metadata, the system eliminates the inefficiencies of managing multiple documents. This enables legal and contracts teams to quickly summarize agreements, draft new amendments with full context, and perform accurate analytics across contract portfolios without fragmentation."

## Prompt 3
> We'll create a prototype agent using Google Cloud. We'll use Google ADK and Gemini 2.5 Pro. Our real world contract dataset is in real_contract_families. Oureval questions are in RAG_EVALUATION_QUESTIONS.md. 

## Prompt 4
> What's your suggestion to RAG the agent on these PDFs?

## Prompt 5
> OK, please do a quick check if everything that you're proposing can be set up with gcloud and/or python from an infra and initial setup standpoint

## Prompt 6
> Ok , let's start drafting. Please enumerate all files that need to be created, please also enumerate all steps in tasks.md. Do you need to create an implementation.md file for yourself when executing this or is tasks.md fine? Please also strcture tasks.md in a way that the code base clearly distingueshes infra setup from actually creating the agent. We want to also publish the agent in vertex ai agent engine. capture everything we discussed here.

## Prompt 7
> ok, I copied over every file you produced so far in legal_agent/ . please check all the md files and make sure we're not missing anything that we discussed in this session. I need every detail to be captured. If you can , please also create an architectural diagram with nano banana pro and link it in SPEC.md. I also dont' see that you enumerated every file that needs to be created, and didn't enumerate every step in tasks.md. I really need every subtask to be enumerated too. please keep capturing our convo as instructed previously in both md files, my prompts only and the whole convo

