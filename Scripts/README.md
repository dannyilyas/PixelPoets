# Scripts

This folder contains all the code involved in the training of model,pre-processing of the data and caclulation of evaluation metrics.

-classify_chest_brain_figures.py - Splits images into chest and brain folders for hyper specific classification

-data_exploration_cleaning.py - Performs data exploration such as:keyword analysis and then performs data cleaning by removing punctuation and figure words and saves the cleaned captions into csv format

-evaluation_score.ipynb - Computes Rouge, F1, Bleu and Bert score for a given model on the dataset

-running_imported_model.ipynb - Imports one of the fine-tuned models and generates captions for both fine-tuned and BLIP

-test_model.ipynb - Imports finetuned models and saves predictions to csv format

-training_model.ipynb - Sets up dataloader, Base model, defines and runs the training loop(performs gradient descent) and saves the fully trained model(on latter 1000 images)

-validation.ipynb - Sets up dataloader, Base model, defines and runs the training loop(performs gradient descent) and saves the fully trained model(on initial 1,900 images)
