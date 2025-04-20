from langchain.tools import BaseTool, tool
from typing import Optional, Union, Any

class CalculatorTool(BaseTool):
    name = "Calculator"
    description = "Useful to perform any mathematical calculations"

    def _run(self, operation: str) -> Union[str, float]:
        """Run the calculator tool."""
        if not isinstance(operation, str):
            return "Error: Input must be a string containing a mathematical expression"
        try:
            # Create a safe dictionary of allowed operations
            safe_dict = {"__builtins__": {}}
            # Add safe mathematical operations
            safe_dict.update({
                k: v for k, v in vars(__builtins__).items() 
                if k in ['abs', 'float', 'int', 'pow', 'round']
            })
            # Evaluate the expression in a safe context
            result = eval(operation, {"__builtins__": None}, safe_dict)
            return str(result)
        except Exception as e:
            return f"Error: Invalid mathematical expression - {str(e)}"

    async def _arun(self, operation: str) -> str:
        """Run the tool asynchronously."""
        raise NotImplementedError("CalculatorTool does not support async")

class CalculatorTools:
    @tool("Make a calculation")
    @staticmethod
    def calculate(operation: str) -> str:
        """Useful to perform any mathematical calculations, 
        like sum, minus, multiplication, division, etc.
        The input to this tool should be a mathematical 
        expression, a couple examples are `200*7` or `5000/2*10`
        """
        try:
            return eval(operation)
        except SyntaxError:
            return "Error: Invalid syntax in mathematical expression"
        except Exception as e:
            return f"Error: {str(e)}"