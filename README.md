__Human Activity Recognition with Machine Learning__
Smartphone audio data and wristband accelerometer data

This project centers on a dataset focused on at-home tasks ranging from passively
watching TV for entertainment to actively mopping to clean the floor. Accelerometer data was
captured by a wearable device wristband, and environmental sound was captured by a smartphone. Our project’s feature extraction was driven by hand-engineered features such as magnitude mean, magnitude root-mean-squared, and x root-mean-squared. We implemented classical
ML models including XGBoost, Random Forest, and Naive Bayes and evaluated performance
using both standard 80/20 train-test splits and Leave-One-Subject-Out (LOSO) validation. Our
final tuned XGBoost model achieved 81.8% accuracy and 81.3% macro F1 under a standard
80/20 split, but performance dropped to 62.5% accuracy and 60.9% macro F1 under LOSO
evaluation. This gap shows that random train-test splitting can overestimate real-world wearable HAR performance because windows from the same users may appear in both training
and testing. Our window-size analysis showed that very short windows were less stable, while
longer windows generally improved classification performance. The selected 3-second window
was a reasonable trade-off between accuracy, stability, and number of training samples. Activities such as sweeping and mopping were often confused because they share repeated arm
movements, while eating chips was harder to classify because a short window may capture either a rest period or a quick hand-to-mouth motion.
Overall, the results show that accelerometer-based HAR can recognize several home activities, but cross-user generalization remains challenging with only three participants and wrist
accelerometer data alone. Future work could improve performance by adding audio features,
increasing the number of participants, testing deep sequence models such as CNNs or LSTMs,
and using longer temporal context to better capture activities with repeated or irregular motion.
