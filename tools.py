from smolagents import Tool
import sympy as sp

class MathVerificationTool(Tool):
    name = "math_verifier"
    description = "Verifies if two mathematical expressions are algebraically equivalent using symbolic logic."
    inputs = {
        "expression_a": {"type": "string", "description": "The target expression (e.g., 'x**2 - 1')"},
        "expression_b": {"type": "string", "description": "The solution to verify (e.g., '(x-1)*(x+1)')"}
    }
    # THIS MUST BE INDENTED INSIDE THE CLASS
    output_type = "string" 

    def forward(self, expression_a: str, expression_b: str) -> str:
        try:
            # sympify converts strings to SymPy symbolic expressions
            expr_a = sp.sympify(expression_a) # Fixed typo: sympify, not simplify
            expr_b = sp.sympify(expression_b)

            # Check difference; if it simplifies to 0, they are equivalent
            if sp.simplify(expr_a - expr_b) == 0:
                return "VERIFICATION SUCCESSFUL: The expressions are algebraically equivalent."
            else:
                return f"VERIFICATION FAILED: {expression_a} is NOT equivalent to {expression_b}."
        except Exception as e:
            return f"Error in symbolic verification: {str(e)}"