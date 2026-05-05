import os
import litellm
from dotenv import load_dotenv
from smolagents import CodeAgent, LiteLLMModel
from tools import MathVerificationTool

load_dotenv()

# LiteLLM uses these env vars automatically for Langfuse
# os,enciron["LANGFUSE_PUBLIC_KEY"] = os.getenv("LANGFUSE_PUBLIC_KEY")
# os.environ["LANGFUSE_SECRET_KEY"] = os.getenv("LANGFUSE_SECRET_KEY")
# os.environ["LANGFUSE_HOST"] = os.getenv("LANGFUSE_BASE_URL")

# Enable tracing
# litellm.success_callback = ["langfuse"]
# litellm.failure_callback = ["langfuse"]

model = LiteLLMModel(
    model_id="huggingface/Qwen/Qwen2.5-Coder-32B-Instruct",
    api_key=os.getenv("HF_TOKEN")
)

agent = CodeAgent(
    tools=[MathVerificationTool()],
    model=model,
    additional_authorized_imports=["sympy", "matplotlib.pyplot", "numpy", "pandas"],
    name="MathFirstPrinciplesTutor"
)