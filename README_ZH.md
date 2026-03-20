## 🚀 5W2H Skill for PM: Requirement Definition & Alignment

One-click to activate your "Senior AI Product Partner." > A powerful framework designed for Product Managers to transform vague ideas into structured, dev-ready requirements. It automatically identifies user roles and generates high-fidelity alignment specs for cross-functional teams.

## 🌟 Core Value Proposition
Transforming "fuzzy thoughts" into reviewable, actionable product outputs:

- Structured Distillation: Leverages the 5W2H framework for guided inquiry.

- Psychological Enhancement: Advanced analysis of user personas and "Moments of Truth" in the Who/When phases.

- Multi-Role Alignment: Automatically generates tailored communication synopses for RD / UI/UX / QA.

## 👥 Target Audience
- Role A (Pro PM / Requirement Owner): Has a clear vision, draft PRD, or feature list.
  
- Role B (Business / Sales / Marketing): Has vague ideas/pain points but doesn't know where to start.
  
- Role C (Designer / Engineer / Tester): Needs to digest long PRDs without getting lost in the noise.

## ⚙️ Workflow Logic
The skill operates on three intelligent layers: Input Filtering -> Logic Distillation -> Role-Based Dispatching.
graph TD
    A[Raw Ideas / Scrappy Notes / Long PRD] --> B{5W2H Logic Engine}
    
    subgraph B [5W2H Analysis]
        B1[Why: Business Goals & Product Stage]
        B2[Who: Personas & Competitive Heuristics]
        B3[What: Feature List & Prototype Logic]
        B4[Where/When: Entry Points & Triggers]
        B5[How: Business Rules & State Machines]
        B6[How Much: Roadmap & Edge Risks]
    end

    B --> C{Role Dispatcher}

    C --> D[🎨 Designer View]
    D1[Output: Information Hierarchy/Priority/Flow]

    C --> E[💻 Developer View]
    E1[Output: API Contracts/State Matrix/Complexity]

    C --> F[🔍 Tester View]
    F1[Output: Acceptance Criteria/Edge Cases/Risk]
    
## 📖 How to Use

Scenario A: Cursor / IDE Integration (Recommended 🌟)Deeply integrated for seamless documentation and coding.

- Setup: Place the .cursorrules file in your project’s root directory.

- Usage: Drop your PDF/Doc into the project (e.g., /docs). In the chat, type: @filename + instructions.

- Highlight: Zero-config required. AI automatically activates the 5W2H engine.

Scenario B: Web-based LLM (ChatGPT / Claude / Doubao)The "Plug-and-Play" solution for any browser.
- Setup: Copy the content of prompts/5W2H-Prompt.md.

- Usage: Paste the prompt first, then upload your document or describe your idea.

- Highlight: Best for quick brainstorming and formatting long documents.

Scenario C: Custom Agent / Enterprise AI Platform. Standardize your team's output.

- Setup: Paste the 5W2H Prompt into the "System Instructions" or "Persona" of your AI Agent.

- Usage: Team members upload raw documents to get standardized analysis instantly.
  
## 🤝 Cross-Functional Alignment Standards

⚙️ Engineering (RD),"Logic loops, state consistency, idempotency, concurrency, & performance."

🎨 Design (UI/UX),"Cognitive load, 3-second understandability, & controllable/reversible/traceable flows."

🔍 Quality (QA),"Acceptance Criteria (AC), Given-When-Then scenarios, & extreme edge-case coverage."

## 📁 Directory StructurePlaintext.
├── .cursorrules           # [Engine] Real-time logic for Cursor/IDE
├── README.md              # [Docs] This documentation
├── configs/
│   └── .cursorrules       # [Template] Backup of the skill config
├── examples/
│   └── AI4S-Case.md       # [Case Study] Scientific Assistant Demo
└── prompts/
    └── 5W2H-Prompt.md     # [Portable] Prompt for Web-based AI
