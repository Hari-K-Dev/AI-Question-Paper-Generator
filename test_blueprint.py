# test_blueprint.py

from agent.interactive_blueprint import build_blueprint

# Simulated input structure from question_loader
chapter_summary = {
    "Ch1": {"MCQ": 5, "VSA": 2},
    "Ch2": {"MCQ": 4, "SA": 3},
}

question_types = ["MCQ", "VSA", "SA"]

blueprint, notes = build_blueprint(chapter_summary, question_types)

print("\n🧾 Final Blueprint:")
print(blueprint)
print("\n🗒️ Notes:")
print(notes)
