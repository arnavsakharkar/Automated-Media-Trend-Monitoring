from groq import Groq
from dotenv import load_dotenv
import os

# ==========================================
# Load Environment Variables
# ==========================================

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# ==========================================
# Groq Model
# ==========================================

MODEL_NAME = "openai/gpt-oss-120b"


# ==========================================
# Base Agent
# ==========================================

class BaseAgent:

    def ask_groq(self, prompt):

        response = client.chat.completions.create(

            model=MODEL_NAME,

            messages=[
                {
                    "role": "system",
                    "content": "You are an intelligent AI assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.4

        )

        return response.choices[0].message.content


# ==========================================
# Agent 1
# Trend Collection & Analysis
# ==========================================

class TrendAnalysisAgent(BaseAgent):

    def analyze(self, media_text):

        prompt = f"""

You are Agent 1.

Your task is Media Trend Collection & Analysis.

Analyze the media content below.

Return:

1. Emerging Trends

2. Important Keywords

3. Recurring Themes

4. Noise / Irrelevant Information Removed

5. Trend Summary

Media Content:

{media_text}

"""

        return self.ask_groq(prompt)


# ==========================================
# Agent 2
# Trend Intelligence
# ==========================================

class TrendIntelligenceAgent(BaseAgent):

    def analyze(self, agent1_output):

        prompt = f"""

You are Agent 2.

You received trend analysis from Agent 1.

Perform Trend Intelligence.

Generate:

1. Trend Relevance

2. Momentum

3. Potential Impact

4. Trend Category

5. Why Each Trend Matters

Agent 1 Output:

{agent1_output}

"""

        return self.ask_groq(prompt)


# ==========================================
# Agent 3
# Final Report
# ==========================================

class ReportAgent(BaseAgent):

    def analyze(

        self,

        original_media,

        agent1_output,

        agent2_output

    ):

        prompt = f"""

You are Agent 3.

Create a professional Final Media Trend Monitoring Report.

Use:

Original Media:

{original_media}

--------------------------------

Agent 1 Analysis:

{agent1_output}

--------------------------------

Agent 2 Intelligence:

{agent2_output}

--------------------------------

Generate a report with:

# Executive Summary

# Top Trends

# Key Insights

# Trend Intelligence

# Potential Business Impact

# Recommendations

# Final Conclusion

Format everything in clean Markdown.

"""

        return self.ask_groq(prompt)