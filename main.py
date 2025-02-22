import scripts.preprocess_data
import scripts.train_model
import scripts.evaluate_model

if __name__ == "__main__":
    print("Running Sentiment Analysis Pipeline...")
    scripts.preprocess_data.run()
    scripts.train_model.run()
    scripts.evaluate_model.run()
