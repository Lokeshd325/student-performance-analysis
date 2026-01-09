import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.analysis import load_data, pass_percentage

def test_pass_percentage():
    df = load_data("data/students.csv")
    result = pass_percentage(df)
    assert result > 0