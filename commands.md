prodigy sense2vec.teach skills ../ner-food-ingredients/s2v_old --seeds "communication, problem solving, leadership"

prodigy terms.to-patterns skills --label SKILL --spacy-model blank:en > ./skill_patterns.jsonl

prodigy ner.manual skills blank:en ./corpusSkills.jsonl --label SKILL --patterns skill_patterns.jsonl

prodigy train --ner skills ./tmp_model --eval-split 0.2

prodigy train-curve --ner skills --eval-split 0.2

prodigy ner.correct skills_correct ./tmp_model/model-best ./corpusSkillsSample.jsonl --label SKILL --exclude skills

prodigy train-curve --ner skills_correct --eval-split 0.2

# Export dataset to annotated jsonl 
python -m prodigy db-out skills > ner_skills.jsonl

# Recipe for relation tagging
prodigy rel.manual skills_rel blank:en dataset:skills --label KNOWS,HAS --wrap