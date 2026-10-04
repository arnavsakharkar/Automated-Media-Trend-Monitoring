import gradio as gr
from agents import (
    TrendAnalysisAgent,
    TrendIntelligenceAgent,
    ReportAgent
)

# ==========================================
# AI WORKFLOW
# ==========================================

def monitor_trends(industry, goal, keywords, media_text):

    if not media_text.strip():
        return (
            "⚠️ Please enter media/news content.",
            "",
            ""
        )

    complete_input = f"""
Industry:
{industry}

Monitoring Goal:
{goal}

Keywords:
{keywords}

Media Content:
{media_text}
"""

    try:

        # Initialize AI Agents
        agent1 = TrendAnalysisAgent()
        agent2 = TrendIntelligenceAgent()
        agent3 = ReportAgent()

        # ----------------------------
        # Agent 1
        # ----------------------------
        agent1_output = agent1.analyze(
            complete_input
        )

        # ----------------------------
        # Agent 2
        # ----------------------------
        agent2_output = agent2.analyze(
            agent1_output
        )

        # ----------------------------
        # Agent 3
        # ----------------------------
        final_report = agent3.analyze(
            complete_input,
            agent1_output,
            agent2_output
        )

        return (
            agent1_output,
            agent2_output,
            final_report
        )

    except Exception as e:

        return (
            f"❌ Error: {str(e)}",
            "",
            ""
        )


# ==========================================
# LOAD CSS
# ==========================================

with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()


# ==========================================
# GRADIO DASHBOARD
# ==========================================

with gr.Blocks(
    title="Automated Media Trend Monitoring",
    css=css,
    theme=gr.themes.Soft()
) as demo:

    gr.HTML("""
    <div class="main-title">
        📊 Automated Media Trend Monitoring
    </div>

    <div class="subtitle">
        Agentic AI Project using 3 Sequential AI Agents powered by Groq
    </div>
    """)

    gr.HTML("""
    <div class="workflow">

        📥 <b>Media Input</b>

        <br><br>

        ⬇️

        <br><br>

        🤖 <b>Agent 1</b><br>
        Trend Collection & Analysis
                <br><br>

        ⬇️

        <br><br>

        🤖 <b>Agent 2</b><br>
        Trend Intelligence & Impact Analysis

        <br><br>

        ⬇️

        <br><br>

        🤖 <b>Agent 3</b><br>
        Report & Recommendations

        <br><br>

        ⬇️

        <br><br>

        📈 <b>Final Trend Report</b>

    </div>
    """)

    gr.Markdown("## 📥 Input Media Information")

    with gr.Row():

        industry = gr.Textbox(
            label="🏭 Industry",
            value="Artificial Intelligence",
            placeholder="Enter Industry"
        )

        goal = gr.Textbox(
            label="🎯 Monitoring Goal",
            value="Identify emerging AI technology trends receiving increasing media attention.",
            placeholder="Monitoring Goal"
        )

    keywords = gr.Textbox(
        label="🏷️ Keywords",
        value="AI Agents, Automation, Multi-Agent Systems, Generative AI",
        placeholder="Keywords separated by commas"
    )

    media = gr.Textbox(
        label="📰 Media / News Content",
        lines=12,
        placeholder="""
Article 1:
Several technology companies are increasingly adopting autonomous AI agents to automate repetitive business workflows.

Article 2:
AI agent startups are receiving increased attention from investors.

Article 3:
Developers are discussing multi-agent systems.

Article 4:
Businesses are exploring AI automation.
"""
    )

    analyze_btn = gr.Button(
        "🔍 Monitor Media Trends",
        variant="primary",
        size="lg"
    )

    gr.HTML("""
    <div class="section-title">
        🤖 AI Agent Outputs
    </div>
    """)

    with gr.Row():

        agent1_box = gr.Markdown(
            label="🤖 Agent 1 - Trend Analysis"
        )

        agent2_box = gr.Markdown(
            label="🤖 Agent 2 - Trend Intelligence"
        )

    gr.Markdown("---")

    final_box = gr.Markdown(
        label="📊 Final Automated Trend Report"
    )
    analyze_btn.click(
        fn=monitor_trends,
        inputs=[
            industry,
            goal,
            keywords,
            media
        ],
        outputs=[
            agent1_box,
            agent2_box,
            final_box
        ]
    )

    gr.Markdown("---")

    gr.HTML("""
    <center>

    <h3>💡 About This Project</h3>

    <p>
    This Agentic AI application automatically monitors media content using
    three AI agents powered by the Groq LLM.
    </p>

    </center>
    """)

    gr.HTML("""
<div style="
    background:#f8fafc;
    color:#1e293b;
    padding:20px;
    border-radius:12px;
    border:2px solid #2563eb;
    margin-top:10px;
">

<h3 style="color:#1d4ed8;">⚙️ Workflow</h3>

<ul style="font-size:17px; line-height:2; color:#334155;">

<li>📥 User enters media/news articles</li>

<li>🤖 Agent 1 extracts trends, keywords and themes</li>

<li>🤖 Agent 2 evaluates relevance, momentum and impact</li>

<li>🤖 Agent 3 generates the final trend report and recommendations</li>

</ul>

</div>
""")

    gr.HTML("""
    <div style="
        margin-top:20px;
        text-align:center;
        color:#64748b;
        font-size:15px;
    ">

    <b>Technology Stack</b><br>

    Python • Gradio • Groq API • Multi-Agent AI • dotenv

    </div>
    """)

    gr.HTML("""
    <div style="
        margin-top:15px;
        text-align:center;
        color:#2563eb;
        font-weight:bold;
        font-size:16px;
    ">

    🎓 Flexi Credit Course Project
    <br>
    Automated Media Trend Monitoring using Agentic AI

    </div>
    """)


if __name__ == "__main__":
    import os

port = int(os.environ.get("PORT", 7860))

demo.launch(
    server_name="0.0.0.0",
    server_port=port,
    share=False,
    show_error=True
)