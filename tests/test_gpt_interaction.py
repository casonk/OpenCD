import unittest
from app.gpt_interaction import interact_with_gpt

class TestGPTInteraction(unittest.TestCase):
    
    def test_gpt_response(self):
        prompt = "What is the capital of France?"
        response = interact_with_gpt(prompt)
        self.assertIn("Paris", response)

if __name__ == "__main__":
    unittest.main()
