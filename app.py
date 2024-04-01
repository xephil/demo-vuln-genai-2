from flask import Flask, render_template, request, jsonify
from io import StringIO
import sys
#from langchain.agents import initialize_agent, load_tools
from langchain.agents.tools import Tool
#from langchain_openai import OpenAI
from langchain.agents import create_openai_functions_agent
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import AgentExecutor
from langchain_experimental.tools import PythonREPLTool

#
app = Flask(__name__)

class PythonREPL:
    def __init__(self):
        pass

    def run(self, command: str) -> str:
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        try:
            print(f"Running command: {command}")
            exec(command, globals())
            sys.stdout = old_stdout
            output = mystdout.getvalue()
            print(f"Output: {output}")
        except Exception as e:
            sys.stdout = old_stdout
            output = str(e)
        return output


tools = [PythonREPLTool()]



instructions = """You are an agent designed to write and execute python code to answer questions.
You have access to a python REPL, which you can use to execute python code.
If you get an error, debug your code and try again.
Only use the output of your code to answer the question. 
You might know the answer without running any code, but you should still run the code to get the answer.
If it does not seem like you can write code to answer the question, just return "I don't know" as the answer.
"""
base_prompt = hub.pull("langchain-ai/openai-functions-template")
prompt = base_prompt.partial(instructions=instructions)


agent = create_openai_functions_agent(ChatOpenAI(temperature=0), tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)



# # # # Setup for the agent
# # # llm = OpenAI(temperature=0.0)
# # # python_repl = Tool(
# # #     "PythonREPL",
# # #     PythonREPLTool().run,
# # #     "A Python shell. Use this to execute Python commands. If you expect output, it should be printed out.",
# # # )
# # # tools = [python_repl]

# # # # Initialize the agent with the given tools and language model
# # # agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True, debug=True, max_tokens=400)

@app.route('/')
def home():
    print("Home page")
    return render_template('index.html')

# @app.route('/execute', methods=['POST'])
# def execute_command():
#     print(f"Received query: {request.json}")
#     data = query = request.json['message']
#     print(f"Received query: {query}")
#     command = data.get('command')
    
#     if not command:
#         return jsonify({"error": "No command provided"}), 400

#     # Here you might decide based on the input whether to use the PythonREPL directly or the agent.
#     # This example directly uses the PythonREPL tool. For more complex logic, consider using the agent.
#     output = python_repl.run(command)

#     return jsonify({"output": output})

# Additional endpoint that might use the agent for more complex tasks or inputs
@app.route('/chat', methods=['POST'])
def process_input():
    print(f"Received query: {request.json}")
    query = request.json['message']
    if not query:
        return jsonify({"error": "No query provided"}), 400
    
    # Example of using the agent for processing the input
    # # # response = agent.run(query)  # Ensure your agent's run method can handle such queries appropriately
    response = agent_executor.invoke({"input":query})  # Ensure your agent's run method can handle such queries appropriately
    print(f"Response: {response}")
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
